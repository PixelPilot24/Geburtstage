import json
import math
from tkinter import *
from datetime import datetime


class Delete:
    """
    In dieser Klasse werden die Geburtstagsdaten gelöscht.
    """
    def __init__(self):
        """
        Initialisiert die GUI für die Löschung der Daten.
        """
        self.root = Tk()
        self.root.title("Geburtstage löschen")
        self.new_dates = {}  # Liste der Geburtstagsdaten
        self.cache_dates = []  # Liste für die Namen

    @staticmethod
    def calculate_age(birthday_date: str) -> int:
        """
        Berechnung des Alters das angezeigt werden soll.
        :param birthday_date: Das zu berechnende Geburtstagsdatum.
        :return: Die Ausgabe zeigt das aktuelle Alter an.
        """
        date = datetime.strptime(birthday_date, "%Y-%m-%d")

        return math.floor((datetime.today() - date).days / 365.2422)

    @staticmethod
    def format_date(date: str) -> str:
        """
        Umformatierung des Datums von YYYY-MM-DD zu DD.MM.YYYY
        :param date: Das zu umformatierende Datum.
        :return: Die Ausgabe ist das geänderte Datum.
        """
        new_date = date[8:10] + "." + date[5:7] + "." + date[0:4]

        return str(new_date)

    def remove_birthday(self, index: int, frame: Frame):
        """
        Die Löschung des Geburtstages und des Namen.
        :param index: Gibt den Index an, an welcher Stelle sich der Key in der Liste befindet.
        :param frame: Die Zeile mit den Daten und dem Knopf die gelöscht werden sollen.
        """
        name = self.cache_dates[index]
        self.new_dates.pop(name)
        frame.pack_forget()
        file = open("geburtstage.json", "w")
        json.dump(self.new_dates, file)

    def create_list(self, dates: dict):
        """
        Erstellung eine Liste mit den Daten und der Löschtaste in der GUI.
        :param dates: Die Liste mit den Namen und den Geburtstagen.
        """
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
