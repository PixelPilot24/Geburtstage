import json
from tkinter import *


class CreateBirthday:
    dates = {}
    days = [i for i in range(1, 32)]
    months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
              "November", "Dezember"]

    def __init__(self):
        root = Tk()
        root.title("Geburtstage speichern")
        root.geometry("270x270")

        self.clicked_day = StringVar()
        self.clicked_month = StringVar()
        self.clicked_day.set("1")
        self.clicked_month.set("Januar")

        Label(root, text="Name:").pack()
        self.entry_name = Entry(root)
        self.entry_name.pack()

        Label(root, text="Tag:").pack()
        OptionMenu(root, self.clicked_day, *self.days).pack()

        Label(root, text="Monat:").pack()
        OptionMenu(root, self.clicked_month, *self.months).pack()

        Label(root, text="Jahr:").pack()
        self.entry_year = Entry(root)
        self.entry_year.pack()

        Button(root, text="Speichern", command=self.birthday_save).pack()
        self.error_text_label = Label(root, text="", fg="red")
        self.error_text_label.pack()

        root.mainloop()

    def error_text(self, text):
        self.error_text_label.config(text=text)

    def check_year(self, year) -> str:
        if len(year) == 0:
            self.error_text("Das Jahr darf nicht leer sein")
            return ""
        else:
            try:
                self.error_text("")
                year = int(year)

                if 999 > year or year > 9999:
                    self.error_text("Das Jahr muss 4 Zeichen haben")
                    return ""
                else:
                    return str(year)
            except ValueError:
                self.error_text("Das Jahr muss eine Zahl sein")
                return ""

    @staticmethod
    def check_int_len(num) -> str:
        if len(str(num)) == 1:
            return "0" + str(num)
        else:
            return str(num)

    def birthday_save(self):
        name = self.entry_name.get()
        day = self.clicked_day.get()
        month_str = self.clicked_month.get()
        month = self.months.index(month_str) + 1
        year = self.entry_year.get()

        day = self.check_int_len(day)
        month = self.check_int_len(month)

        self.error_text_label.config(text="")

        year = self.check_year(year)

        if len(name) == 0:
            self.error_text("Es muss ein Name eingegeben werden")

        if len(year) == 4 and not len(name) == 0:
            birthday = year + "-" + month + "-" + day
            self.dates[name] = birthday
            with open("geburtstage.json", "w") as file:
                json.dump(self.dates, file)
            self.error_text_label.config(text="Daten gespeichert", fg="green")
