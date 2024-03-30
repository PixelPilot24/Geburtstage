import json
import math
from tkinter import *
from datetime import datetime


class Delete:
    def __init__(self):
        self.root = Tk()
        self.root.title("Geburtstage löschen")
        self.new_dates = {}
        self.cache_dates = []

    @staticmethod
    def calculate_age(birthday_date) -> int:
        date = datetime.strptime(birthday_date, "%Y-%m-%d")

        return math.floor((datetime.today() - date).days / 365.2422)

    @staticmethod
    def format_date(date) -> str:
        new_date = date[8:10] + "." + date[5:7] + "." + date[0:4]

        return str(new_date)

    def remove_birthday(self, index, frame):
        name = self.cache_dates[index]
        self.new_dates.pop(name)
        frame.pack_forget()
        file = open("geburtstage.json", "w")
        json.dump(self.new_dates, file)

    def create_list(self, dates):
        self.cache_dates = list(dates.keys())
        self.new_dates = dates
        pad = 5
        dates_key = list(self.new_dates.keys())
        dates_values = list(self.new_dates.values())

        for i in range(len(dates_key)):
            age = self.calculate_age(dates_values[i])
            date = self.format_date(dates_values[i])
            dates_text = str(dates_key[i]) + "(" + str(age) + "): " + date
            frame = Frame(self.root, relief=RIDGE, borderwidth=2, padx=pad, pady=pad)
            text_label = Label(frame, text=dates_text, padx=pad)
            delete_button = Button(frame, text="löschen", padx=pad)
            text_label.pack(side="left")
            delete_button.pack(side="right")
            frame.pack(padx=10, pady=10)
            delete_button.config(command=lambda b=frame, index=i: self.remove_birthday(index, b))

        mainloop()
