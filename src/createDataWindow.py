import validator

from tkinter import *
from tkinter import messagebox


class CreateDataWindow:
    def __init__(self, dates: dict):
        self.root = None
        self.canvas = Canvas()
        self.inner_frame = Frame()
        self._new_dates = dates
        self._cache_dates = list(dates.keys())
        self.validator = validator.DataValidator()

    def __initial_window(self):
        self.root = Tk()
        self.root.title("Geburtstage Liste")
        self.root.geometry("600x150")
        self.root.focus_force()

    def __on_mouse_wheel(self, event: Event):
        self.canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

    def _text_label_str(self, name: str, date: str) -> str:
        age = self.validator.calculate_age(date)
        new_date = date[8:10] + "." + date[5:7] + "." + date[0:4]

        return f"{name}\n{age} Jahre\n{new_date}"

    def _add_menu(self, name: str, date: str, frame: Frame, label: Label, index: int):
        data_handler = DataHandler(self._new_dates)
        menu = Menu(master=label, tearoff=0)

        menu.add_command(label="Bearbeiten", command=lambda:
                         data_handler.edit_data(name, date, frame, label, index, self.root))
        menu.add_command(label="Löschen", command=lambda: data_handler.remove_birthday(index, frame, self.root))

        label.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

    def __create_widgets(self):
        pad = 5
        dates_keys = list(self._new_dates.keys())
        dates_values = list(self._new_dates.values())

        for index in range(len(dates_keys)):
            value = dates_values[index]
            name = dates_keys[index]
            dates_text = self._text_label_str(name, value)

            frame = Frame(master=self.inner_frame, relief=RIDGE, borderwidth=2, padx=pad, pady=pad)
            text_label = Label(master=frame, text=dates_text, padx=pad)

            text_label.pack(side=LEFT)
            self._add_menu(name, value, frame, text_label, index)
            frame.pack(side=LEFT, padx=10, pady=10, anchor=W)

    def create_window(self):
        self.__initial_window()

        self.canvas = Canvas(master=self.root, scrollregion=(0, 0, 700, 700))
        self.canvas.bind_all("<MouseWheel>", self.__on_mouse_wheel)

        self.inner_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor=NW)

        self.__create_widgets()

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        scrollbar = Scrollbar(master=self.root, orient=HORIZONTAL)
        scrollbar.pack(side=BOTTOM, fill=X)
        scrollbar.config(command=self.canvas.xview)
        self.canvas.config(xscrollcommand=scrollbar.set)
        self.canvas.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.root.mainloop()


class DataHandler(CreateDataWindow):
    """
    In dieser Klasse werden die Geburtstagsdaten gelöscht.
    """

    def remove_birthday(self, index: int, frame: Frame, root: Tk):
        """
        Die Löschung des Geburtstages und des Namen.
        :param root:
        :param index: Gibt den Index an, an welcher Stelle sich der Key in der Liste befindet.
        :param frame: Die Zeile mit den Daten und dem Knopf die gelöscht werden sollen.
        """
        name = self._cache_dates[index]
        delete_option = messagebox.askyesno(
            "Löschen", f"Sollen die Daten von {name} wirklich gelöscht werden?"
        )

        if delete_option:
            self._new_dates.pop(name)
            frame.pack_forget()
            self.validator.save_in_json(self._new_dates)

        root.focus_force()

    def __save_change(self, day: str, month: str, year: str, name: str, old_name: str, index: int,
                      frame: Frame, entry_frame: Frame, root: Tk):
        date = f"{year}-{month}-{day}"
        vali = validator.DataValidator()

        if (vali.check_day(day) != "" and
                vali.check_month(month) != "" and
                vali.check_year(year) != ""):
            entry_frame.pack_forget()
            if name == old_name:
                self._new_dates[old_name] = date
            else:
                self._new_dates.pop(old_name)
                self._new_dates[name] = date

            dates_text = self._text_label_str(name, date)
            text_label = Label(master=frame, text=dates_text, padx=5)

            text_label.pack(side=LEFT)
            self._add_menu(name, date, frame, text_label, index)

            self.inner_frame.update_idletasks()

            self.validator.save_in_json(self._new_dates)

        root.focus_force()

    def edit_data(self, name: str, date: str, frame: Frame, text_label: Label, index: int, root: Tk):
        split_date = date.split("-")
        day = split_date[2]
        month = split_date[1]
        year = split_date[0]
        vali = validator.DataValidator()

        text_label.pack_forget()

        entry_frame = Frame(master=frame)
        name_entry = Entry(master=entry_frame)
        day_entry = Entry(master=entry_frame, width=4, justify=CENTER)
        month_entry = Entry(master=entry_frame, width=4, justify=CENTER)
        year_entry = Entry(master=entry_frame, width=6, justify=CENTER)
        save_button = Button(master=entry_frame, text="Speichern", anchor=CENTER)

        save_button.config(command=lambda n=name, e=entry_frame: self.__save_change(
            day_entry.get(), month_entry.get(), year_entry.get(), name_entry.get(), n, index, frame, e, root))

        name_entry.insert(0, name)
        day_entry.insert(0, day)
        month_entry.insert(0, month)
        year_entry.insert(0, year)

        day_entry.bind("<Key>", lambda event, e=day_entry: vali.check_input(event, e))
        month_entry.bind("<Key>", lambda event, e=month_entry: vali.check_input(event, e))
        year_entry.bind("<Key>", lambda event, e=year_entry: vali.check_input(event, e, 3))

        name_entry.pack()
        day_entry.pack()
        month_entry.pack()
        year_entry.pack()
        save_button.pack()
        entry_frame.pack()

        self.inner_frame.update_idletasks()
