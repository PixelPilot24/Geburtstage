import json
from tkinter import *
from tkinter import ttk
from delete import Delete


class CreateBirthday:
    """
    Diese Klasse ermöglicht es über eine GUI die Geburtstage zu speichern.
    """
    dates = {}  # Eine Klassenvariable um die gespeicherten Geburtstage zu speichern
    days = [str(i) for i in range(1, 32)]   # Liste aller möglichen Tage
    months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
              "November", "Dezember"]   # Liste aller möglichen Monate

    def __init__(self):
        """
        Initialisiert die GUI für die Eingabe von Geburtstagen.
        """
        # Erstellung eines Fensters
        root = Tk()
        root.title("Geburtstage speichern")
        root.geometry("300x220")

        # Erstellung der GUI Elemente und ihre Platzierung
        self.clicked_day = StringVar()
        self.clicked_month = StringVar()
        self.clicked_day.set("1")
        self.clicked_month.set("Januar")

        x_pos_1 = 20
        x_pos_2 = x_pos_1 * 2 + 50

        Label(root, text="Name:").place(x=x_pos_1, y=20)
        self.entry_name = Entry(root)
        self.entry_name.place(x=x_pos_2, y=20)

        Label(root, text="Tag:").place(x=x_pos_1, y=50)
        ttk.Combobox(root, textvariable=self.clicked_day, values=self.days, state="readonly").place(x=x_pos_2, y=50)

        Label(root, text="Monat:").place(x=x_pos_1, y=80)
        ttk.Combobox(root, textvariable=self.clicked_month, values=self.months, state="readonly").place(x=x_pos_2, y=80)

        Label(root, text="Jahr:").place(x=x_pos_1, y=110)
        self.entry_year = Entry(root)
        self.entry_year.place(x=x_pos_2, y=110)

        Button(root, text="Speichern", command=self.birthday_save, width=10, height=2).place(x=95, y=150)
        self.error_text_label = Label(root, text="", fg="red")
        self.error_text_label.pack(side="bottom")

        # Menüleiste
        menubar = Menu(root)
        option_menu = Menu(menubar, tearoff=0)
        option_menu.add_command(label="Geburtstage löschen", command=self.birthdays_list)
        option_menu.add_separator()
        option_menu.add_command(label="Schließen", command=self.close_program)
        menubar.add_cascade(label="Optionen", menu=option_menu)

        root.config(menu=menubar)

        root.mainloop()

    def birthdays_list(self):
        """
        Öffnet das Fenster wo die Geburtstage angezeigt und gelöscht werden können.
        """
        Delete.create_list(Delete(), self.dates)

    @staticmethod
    def close_program():
        """
        Schließt das Programm.
        """
        exit()

    def error_text(self, text):
        """
        Zeigt einen Fehlertext unten im Fenster an.
        :param text: Der anzuzeigende Text.
        """
        self.error_text_label.config(text=text)

    def check_year(self, year: str) -> str:
        """
        Überprüft, ob das Jahr gültig ist. Falls nicht, wird ein entsprechender Fehlertext angezeigt.
        :param year: Das eingegebene Jahr.
        :return: Das gültige Jahr oder ein leerer String, wenn das Jahr ungültig ist.
        """
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
        """
        Überprüft die Länge von der Nummer. Falls die Nummer nur eine Stelle hat, dann wird davor eine 0 hinzugefügt.
        :param num: Die zu überprüfende Nummer.
        :return: Die Ausgabe ist ein String der immer 2 Stellen hat.
        """
        if len(str(num)) == 1:
            return "0" + str(num)
        else:
            return str(num)

    def birthday_save(self):
        """
        Speichert den Namen und den Geburtstag in einer JSON Datei.
        """
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
