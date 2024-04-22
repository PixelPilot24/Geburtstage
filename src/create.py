import check
import createDataWindow

from tkinter import *
from tkinter import messagebox
from check import CheckData


class CreateBirthday:
    """
    Diese Klasse ermöglicht es über eine GUI die Geburtstage zu speichern.
    """
    dates = {}  # Eine Klassenvariable um die gespeicherten Geburtstage zu speichern

    def __init__(self):
        self.root = Tk()
        self.root.title("Geburtstage speichern")
        self.root.geometry("300x220")

        self.name_entry = Entry(master=self.root)
        self.day_entry = Entry(master=self.root)
        self.month_entry = Entry(master=self.root)
        self.year_entry = Entry(master=self.root)

        self.create_widgets()
        self.create_menubar()

        self.root.mainloop()

    def create_widgets(self):
        x_pos_label = 20
        x_pos_entry = x_pos_label * 2 + 50

        Label(master=self.root, text="Name").place(x=x_pos_label, y=20)
        Label(master=self.root, text="Tag").place(x=x_pos_label, y=50)
        Label(master=self.root, text="Monat").place(x=x_pos_label, y=80)
        Label(master=self.root, text="Jahr").place(x=x_pos_label, y=110)
        date_label = Label(master=self.root, text="Datumsformat: DD.MM.YYYY")
        date_label.place(relx=0.5, y=140, anchor=CENTER)

        self.name_entry.place(x=x_pos_entry, y=20)
        self.day_entry.place(x=x_pos_entry, y=50)
        self.month_entry.place(x=x_pos_entry, y=80)
        self.year_entry.place(x=x_pos_entry, y=110)

        save_button = Button(master=self.root, text="Speichern", command=self.birthday_save)
        save_button.place(relx=0.5, y=170, anchor=CENTER)

    def create_menubar(self):
        menubar = Menu(self.root)
        option_menu = Menu(master=menubar, tearoff=0)
        option_menu.add_command(label="Geburtstage",
                                command=lambda: createDataWindow.CreateDataWindow(self.dates).create_window())
        option_menu.add_separator()
        option_menu.add_command(label="Schließen", command=lambda: exit())
        menubar.add_cascade(label="Optionen", menu=option_menu)

        self.root.config(menu=menubar)
# todo: nach dem speichern sollen die Entry Felder wieder leer sein

    def birthday_save(self):
        """
        Speichert den Namen und den Geburtstag in einer JSON Datei.
        """
        name = self.name_entry.get()
        day = self.day_entry.get()
        month = self.month_entry.get()
        year = self.year_entry.get()

        day = CheckData.check_int_len(day)
        month = CheckData.check_int_len(month)

        if len(name) == 0:
            messagebox.showinfo("Name", "Es muss ein Name eingegeben werden")
        else:
            if (CheckData.check_day(day) != "" and
                    CheckData.check_month(month) != "" and
                    CheckData.check_year(year) != ""):
                # Wenn alle Daten Zahlen sind und in der richtigen Spanne sind, dann werden diese gespeichert
                birthday = year + "-" + month + "-" + day
                self.dates[name] = birthday
                check.save_in_json(self.dates)

                messagebox.showinfo("Speichern", "Daten wurden gespeichert")
                self.name_entry.delete(0, len(name))
                self.day_entry.delete(0, len(day))
                self.month_entry.delete(0, len(month))
                self.year_entry.delete(0, 4)
