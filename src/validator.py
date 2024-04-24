import json
import math
from datetime import datetime
from tkinter import messagebox
from tkinter import *


class DataValidator:
    @staticmethod
    def check_input(event: Event, text_entry: Entry, length=1):
        text = text_entry.get()

        if event.char.isdigit():
            if len(text) > length:
                text_entry.delete(length, END)
        elif (event.keysym == "Tab"
              or event.keysym == "BackSpace"
              or event.keysym == "Left"
              or event.keysym == "Right"):
            return "continue"
        else:
            return "break"

    @staticmethod
    def check_int_len(num) -> str:
        """
        Überprüft die Länge von der Nummer. Falls die Nummer nur eine Stelle hat, dann wird davor eine 0 hinzugefügt.
        :param num: Die zu überprüfende Nummer.
        :return: Die Ausgabe ist ein String der immer 2 Stellen hat.
        """
        if len(str(num)) == 1:
            return "0" + str(num)
        else:
            return str(num)

    @staticmethod
    def check_year(year: str) -> str:
        """
        Überprüft, ob das Jahr gültig ist. Falls nicht, wird ein entsprechender Fehlertext angezeigt.
        :param year: Das eingegebene Jahr.
        :return: Das gültige Jahr oder ein leerer String, wenn das Jahr ungültig ist.
        """
        if len(year) == 0:
            messagebox.showinfo("Jahr", "Das Jahr darf nicht leer sein")
            return ""
        else:
            try:
                year = int(year)

                if 999 > year or year > 9999:
                    messagebox.showinfo("Jahr", "Das Jahr muss 4 Zeichen haben")
                    return ""
                else:
                    return str(year)
            except ValueError:
                messagebox.showinfo("Jahr", "Das Jahr muss eine Zahl sein")
                return ""

    @staticmethod
    def check_month(month: str) -> str:
        if len(month) == 0:
            messagebox.showinfo("Monat", "Der Monat darf nicht leer sein")
            return ""
        else:
            try:
                month = int(month)

                if 1 > month or month > 12:
                    messagebox.showinfo("Monat", "Der Monat muss zwischen 1 und 12 liegen")
                    return ""
                else:
                    return str(month)
            except ValueError:
                messagebox.showinfo("Monat", "Der Monat muss eine Zahl sein")
                return ""

    @staticmethod
    def check_day(day: str) -> str:
        if len(day) == 0:
            messagebox.showinfo("Tag", "Der Tag darf nicht leer sein")
            return ""
        else:
            try:
                day = int(day)

                if 1 > day or day > 31:
                    messagebox.showinfo("Tag", "Der Tag muss zwischen 1 und 31 liegen")
                    return ""
                else:
                    return str(day)
            except ValueError:
                messagebox.showinfo("Tag", "Der Tag muss eine Zahl sein")
                return ""

    @staticmethod
    def calculate_age(birthday_date: str) -> int:
        """
        Berechnung des Alters das angezeigt werden soll.
        :param birthday_date: Das zu berechnende Geburtstagsdatum.
        :return: Die Ausgabe zeigt das aktuelle Alter an.
        """
        date = datetime.strptime(birthday_date, "%Y-%m-%d")

        return math.floor((datetime.today() - date).days / 365.2422)

