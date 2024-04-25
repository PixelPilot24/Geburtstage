import baseWindow as createDW

from tkinter import *
from json_handler import JsonHandler as Json


class SearchBirthday:
    """
    Eine Klasse zum Suchen von Geburtstagen und Anzeigen der Suchergebnisse.
    """
    def __init__(self, search_frame: Frame, widget_frame: Frame):
        """
        :param search_frame: Das Frame, in dem die Suchleiste platziert wird.
        :param widget_frame: Das Frame, in dem die Suchergebnisse angezeigt werde.
        """
        self.__search_frame = search_frame
        self.__widget_frame = widget_frame
        self.__search_entry = Entry()
        self.__entry_var = StringVar()

        self.__create_searchbar()

    def __create_searchbar(self):
        """
        Erstellt eine Suchleiste mit einem Eingabefeld und einem Löschen Button. Dahinter ist ein Infotext.
        """
        frame = Frame(master=self.__search_frame)
        Label(master=frame, text="Suche").pack(side=LEFT)
        self.__search_entry = Entry(master=frame, textvariable=self.__entry_var)
        search_clear = Button(master=frame, text="\u2715", command=lambda: self.__clear_search())
        self.__search_entry.bind("<KeyRelease>", lambda event: self.__check_input())
        info_text = Label(master=frame, text="\u2139 Mit Rechtsklick kann bearbeitet oder gelöscht werden",
                          fg="grey")

        self.__search_entry.pack(side=LEFT)
        search_clear.pack(side=LEFT)
        info_text.pack(side=LEFT)
        frame.pack()

    def __clear_search(self):
        """
        Löscht den Inhalt des Eingabefeldes und zeigt alle Geburtstage wieder an.
        """
        self.__search_entry.delete(0, END)
        dates = Json().json_data
        createDW.create_widgets(dates, self.__widget_frame)

    def __check_input(self):
        """
        Überprüft die Eingabe und zeigt die passenden Ergebnisse an.
        """
        search_text = self.__entry_var.get().lower()

        dates = Json().json_data
        search_results = {}

        for name, date in dates.items():
            if search_text in name.lower():
                search_results[name] = date

        createDW.create_widgets(search_results, self.__widget_frame)
