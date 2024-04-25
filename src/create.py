import baseWindow as createDW

from tkinter import *
from tkinter import messagebox
from validator import DataValidator
from json_handler import JsonHandler as Json


class CreateBirthday:
    """
    Eine Klasse zum Erstellen von Geburtstagen.
    """
    def __init__(self, inner_frame: Frame, name="", day="", month="", year=""):
        """
        Erstellt ein neues Fenster mit dem passenden Titel und erstellt die nötigen Widgets.
        :param inner_frame: Das Frame vom Hauptfenster um das neue Widget erstellen zu lassen.
        :param name: Wenn ein Geburtstag erstellt wird, ist der String ist leer. Ansonsten steht dort, beim Bearbeiten, der zu bearbeitende Name.
        :param day: Wenn ein Geburtstag erstellt wird, ist der String ist leer. Ansonsten steht dort, beim Bearbeiten, der zu bearbeitende Tag.
        :param month: Wenn ein Geburtstag erstellt wird, ist der String ist leer. Ansonsten steht dort, beim Bearbeiten, der zu bearbeitende Monat.
        :param year: Wenn ein Geburtstag erstellt wird, ist der String ist leer. Ansonsten steht dort, beim Bearbeiten, der zu bearbeitende Jahr.
        """
        self.__inner_frame = inner_frame
        self.__name = name
        self.__root = Tk()

        if name != "":
            self.__root.title("Geburtstag bearbeiten")
        else:
            self.__root.title("Geburtstag erstellen")

        self.__root.geometry("300x220")

        self.__name_entry = Entry(master=self.__root)
        self.__day_entry = Entry(master=self.__root)
        self.__month_entry = Entry(master=self.__root)
        self.__year_entry = Entry(master=self.__root)

        self.__name_entry.insert(0, name)
        self.__day_entry.insert(0, day)
        self.__month_entry.insert(0, month)
        self.__year_entry.insert(0, year)

        self.__create_widgets()
        self.__root.focus_force()

    def __create_widgets(self):
        x_pos_label = 20
        x_pos_entry = x_pos_label * 2 + 50

        Label(master=self.__root, text="Name").place(x=x_pos_label, y=20)
        Label(master=self.__root, text="Tag").place(x=x_pos_label, y=50)
        Label(master=self.__root, text="Monat").place(x=x_pos_label, y=80)
        Label(master=self.__root, text="Jahr").place(x=x_pos_label, y=110)
        date_label = Label(master=self.__root, text="Datumsformat: DD.MM.YYYY")
        date_label.place(relx=0.5, y=140, anchor=CENTER)

        self.__name_entry.place(x=x_pos_entry, y=20)
        self.__day_entry.place(x=x_pos_entry, y=50)
        self.__month_entry.place(x=x_pos_entry, y=80)
        self.__year_entry.place(x=x_pos_entry, y=110)

        # Überprüft beim Verlassen des Feldes ob dieser die richtige Länge und ob dieser eine Zahl ist.
        self.__day_entry.bind("<FocusOut>",
                              lambda event, e=self.__day_entry: DataValidator.check_input(event, e))
        self.__month_entry.bind("<FocusOut>",
                                lambda event, e=self.__month_entry: DataValidator.check_input(event, e))
        self.__year_entry.bind("<FocusOut>",
                               lambda event, e=self.__year_entry: DataValidator.check_input(event, e, 3))

        # Überprüft beim Schreiben, ob der Text die richtige Länge und ob dieser eine Zahl ist.
        self.__day_entry.bind("<Key>", lambda event, e=self.__day_entry: DataValidator.check_input(event, e))
        self.__month_entry.bind("<Key>", lambda event, e=self.__month_entry: DataValidator.check_input(event, e))
        self.__year_entry.bind("<Key>",
                               lambda event, e=self.__year_entry: DataValidator.check_input(event, e, 3))

        save_button = Button(master=self.__root, text="Speichern", command=self.__birthday_save)
        save_button.place(relx=0.5, y=170, anchor=CENTER)

    def __birthday_save(self):
        """
        Es wird zuerst überprüft, ob ein Name eingegeben wurde oder nicht. Falls nicht, dann wird eine Meldung mit dem
        passenden Text ausgegeben. Wenn der Name gegeben ist, dann wird überprüft, ob der Tag, Monat, Jahr gültig sind.
        Falls nicht, dann wird eine Meldung angezeigt. Falls alles richtig ist, dann werden die Daten gespeichert.
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
                dates = Json().json_data

                if self.__name != name and self.__name != "":
                    dates.pop(self.__name)

                birthday = f"{year}-{month}-{day}"
                dates[name] = birthday
                Json().save_in_json(dates)

                messagebox.showinfo("Speichern", "Daten wurden gespeichert")
                createDW.create_widgets(dates, self.__inner_frame)
                self.__root.destroy()

    def run(self):
        self.__root.mainloop()
