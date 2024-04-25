from tkinter import *
from tkinter import messagebox
from validator import DataValidator as Validator
from json_handler import JsonHandler as Json
from create import CreateBirthday as Create
from search import SearchBirthday as Search


class BaseGUI:
    """
    Eine Klasse die das Hauptfenster der Anwendung erstellt.
    """
    def __init__(self):
        self.__dates = Json().json_data
        self.__root = Tk()
        self.__canvas = Canvas(master=self.__root, scrollregion=(0, 0, 700, 700))
        self.__inner_frame = Frame(master=self.__canvas)
        self.__search_frame = Frame(master=self.__inner_frame)
        self.__widget_frame = Frame(master=self.__inner_frame)
        self.__setup_window()

    def __setup_window(self):
        """
        Erstellt das Hauptfenster mit den Widgets und Funktionen
        """
        self.__root.title("Geburtstage Liste")
        self.__root.focus_force()
        self.__canvas.bind_all("<MouseWheel>", self.__on_mouse_wheel)
        self.__canvas.create_window((0, 0), window=self.__inner_frame, anchor=NW)
        Search(self.__search_frame, self.__widget_frame)
        create_widgets(self.__dates, self.__widget_frame)
        self.__search_frame.pack(anchor=NW)
        self.__widget_frame.pack()
        self.__canvas.update_idletasks()
        self.__resize_window()
        self.__create_scrollbar()
        self.__create_menubar()

    def __on_mouse_wheel(self, event: Event):
        """
        Ermöglicht das Scrollen im Hauptfenster
        :param event:
        """
        self.__canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def __create_scrollbar(self):
        """
        Erstellt die horizontale und vertikale Scrollleiste für den Canvas
        """
        self.__canvas.config(scrollregion=self.__canvas.bbox(ALL))
        scrollbar_x = Scrollbar(master=self.__root, orient=HORIZONTAL)
        scrollbar_y = Scrollbar(master=self.__root, orient=VERTICAL)

        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        scrollbar_x.config(command=self.__canvas.xview)
        scrollbar_y.config(command=self.__canvas.yview)

        self.__canvas.config(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        self.__canvas.pack(fill=BOTH, expand=True)

    def __resize_window(self):
        width = self.__inner_frame.winfo_reqwidth() + 21

        self.__root.geometry(f"{width}x{width}")

    def __create_menubar(self):
        """
        Erstellt das Menü mit Optionen für die Anwendung.
        """
        menubar = Menu(self.__root)
        option_menu = Menu(master=menubar, tearoff=0)
        option_menu.add_command(label="Neu", command=lambda: Create(self.__widget_frame).run())
        option_menu.add_separator()
        option_menu.add_command(label="Schließen", command=lambda: exit())
        menubar.add_cascade(label="Optionen", menu=option_menu)

        self.__root.config(menu=menubar)

    def run(self):
        self.__root.mainloop()


def create_widgets(dates: dict, widget_frame: Frame):
    """
    Löscht zuerst alle vorhandenen Widgets und erstellt, anhand der übergebenen Daten, eine neue Anzeige mit den Widgets.
    :param dates: Daten von dem jeweiligen Namen und Geburtstag.
    :param widget_frame: Frame von den Widgets.
    """
    for widget in widget_frame.winfo_children():
        widget.destroy()
    index = 0
    pad = 5

    for name, date in dates.items():
        row = index // 6
        column = index - (row * 6)
        frame = Frame(master=widget_frame, relief=RIDGE, borderwidth=2, padx=pad, pady=pad)
        BirthdayLabel(frame, name, date, pad, widget_frame)
        frame.grid(row=row, column=column, padx=pad, pady=pad)
        index += 1


class BirthdayLabel:
    """
    In dieser Klasse wird das Label erstellt.
    """
    def __init__(self, frame: Frame, name: str, date: str, pad: int, inner_frame: Frame):
        self.__inner_frame = inner_frame
        self.__frame = frame
        self.__name = name
        self.__date = date
        self.__pad = pad
        self.__create_label()

    def __create_label(self):
        """
        Erstellt das passende Label mit dem Bearbeitungsmenü.
        """
        pad = self.__pad
        dates_text = self.__text_label_str()

        text_label = Label(master=self.__frame, text=dates_text, padx=pad, pady=pad)
        text_label.pack()
        self.__add_menu(text_label)

    def __text_label_str(self) -> str:
        """
        Erstellt den passenden Text für das Textlabel.
        :return: Es wird der formatierte Text ausgegeben.
        """
        date = self.__date
        validator = Validator()
        age = validator.calculate_age(date)
        new_date = f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

        return f"{self.__name}\n{age} Jahre\n{new_date}"

    def __add_menu(self, text_label: Label):
        """
        Das Menü wird erstellt, mit dem man den Geburtstag bearbeiten oder löschen kann.
        :param text_label: Das richtige Label wird mitgegeben,
        damit nicht das falsche Label bearbeitet oder gelöscht wird.
        """
        menu = Menu(master=text_label, tearoff=0)
        menu.add_command(label="Bearbeiten", command=lambda: self.__edit_birthday())
        menu.add_command(label="Löschen", command=self.__remove_birthday)

        text_label.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

    def __edit_birthday(self):
        """
        Es wird das Fenster vom Erstellen des Geburtstages, mit den zu bearbeitenden Parametern, geöffnet.
        """
        split_date = self.__date.split("-")
        day, month, year = split_date[2], split_date[1], split_date[0]

        Create(self.__inner_frame, self.__name, day, month, year).run()

    def __remove_birthday(self):
        """
        Es wird abgefragt, ob der Geburtstag gelöscht werden soll, wenn ja, dann wird dieser gelöscht und gespeichert.
        """
        name = self.__name
        delete_option = messagebox.askyesno(
            "Löschen", f"Sollen die Daten von {name} wirklich gelöscht werden?")

        if delete_option:
            self.__dates = Json().json_data
            self.__dates.pop(name)
            Json().save_in_json(self.__dates)
            create_widgets(self.__dates, self.__inner_frame)
