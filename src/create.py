import createDataWindow as createDW

from tkinter import *
from tkinter import messagebox
from validator import DataValidator
from json_handler import JsonHandler as Json


class CreateBirthday:
    """
    Diese Klasse ermöglicht es über eine GUI die Geburtstage zu speichern.
    """

    def __init__(self, root: Tk, inner_frame: Frame):
        self.__inner_frame = inner_frame
        self.__top_level = Toplevel(master=root)
        self.__top_level.title("Geburtstage speichern")
        self.__top_level.geometry("300x220")

        self.__name_entry = Entry(master=self.__top_level)
        self.__day_entry = Entry(master=self.__top_level)
        self.__month_entry = Entry(master=self.__top_level)
        self.__year_entry = Entry(master=self.__top_level)

        self.__create_widgets()
        self.__top_level.focus_force()

    def __create_widgets(self):
        x_pos_label = 20
        x_pos_entry = x_pos_label * 2 + 50

        Label(master=self.__top_level, text="Name").place(x=x_pos_label, y=20)
        Label(master=self.__top_level, text="Tag").place(x=x_pos_label, y=50)
        Label(master=self.__top_level, text="Monat").place(x=x_pos_label, y=80)
        Label(master=self.__top_level, text="Jahr").place(x=x_pos_label, y=110)
        date_label = Label(master=self.__top_level, text="Datumsformat: DD.MM.YYYY")
        date_label.place(relx=0.5, y=140, anchor=CENTER)

        self.__name_entry.place(x=x_pos_entry, y=20)
        self.__day_entry.place(x=x_pos_entry, y=50)
        self.__month_entry.place(x=x_pos_entry, y=80)
        self.__year_entry.place(x=x_pos_entry, y=110)

        self.__day_entry.bind("<FocusOut>",
                              lambda event, e=self.__day_entry: DataValidator.check_input(event, e))
        self.__month_entry.bind("<FocusOut>",
                                lambda event, e=self.__month_entry: DataValidator.check_input(event, e))
        self.__year_entry.bind("<FocusOut>",
                               lambda event, e=self.__year_entry: DataValidator.check_input(event, e, 3))

        self.__day_entry.bind("<Key>", lambda event, e=self.__day_entry: DataValidator.check_input(event, e))
        self.__month_entry.bind("<Key>", lambda event, e=self.__month_entry: DataValidator.check_input(event, e))
        self.__year_entry.bind("<Key>",
                               lambda event, e=self.__year_entry: DataValidator.check_input(event, e, 3))

        save_button = Button(master=self.__top_level, text="Speichern", command=self.__birthday_save)
        save_button.place(relx=0.5, y=170, anchor=CENTER)

    def __birthday_save(self):
        """
        Speichert den Namen und den Geburtstag in einer JSON Datei.
        """
        name = self.__name_entry.get()
        day = self.__day_entry.get()
        month = self.__month_entry.get()
        year = self.__year_entry.get()

        day = DataValidator.check_int_len(day)
        month = DataValidator.check_int_len(month)

        if len(name) == 0:
            messagebox.showinfo("Name", "Es muss ein Name eingegeben werden")
        else:
            if (DataValidator.check_day(day) != "" and
                    DataValidator.check_month(month) != "" and
                    DataValidator.check_year(year) != ""):
                # Wenn alle Daten Zahlen sind und in der richtigen Spanne sind, dann werden diese gespeichert
                birthday = year + "-" + month + "-" + day
                dates = Json().json_data
                dates[name] = birthday
                Json().save_in_json(dates)

                messagebox.showinfo("Speichern", "Daten wurden gespeichert")
                createDW.create_widgets(dates, self.__inner_frame)
                self.__top_level.destroy()

    def run(self):
        self.__top_level.mainloop()
