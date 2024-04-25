from tkinter import *
from tkinter import messagebox
from validator import DataValidator as Validator
from json_handler import JsonHandler as Json
from create import CreateBirthday as Create


class BaseGUI:
    def __init__(self):
        self.__dates = Json().json_data
        self.__root = Tk()
        self.__canvas = Canvas(master=self.__root, scrollregion=(0, 0, 700, 700))
        self.__inner_frame = Frame(master=self.__canvas)
        self.__setup_window()

    def __setup_window(self):
        self.__root.title("Geburtstage Liste")
        self.__root.focus_force()
        self.__canvas.bind_all("<MouseWheel>", self.__on_mouse_wheel)
        self.__canvas.create_window((0, 0), window=self.__inner_frame, anchor=NW)
        create_widgets(self.__dates, self.__inner_frame)
        self.__canvas.update_idletasks()
        self.__resize_window()
        self.__create_scrollbar()
        self.__create_menubar()

    def __on_mouse_wheel(self, event: Event):
        self.__canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def __create_widgets(self):
        index = 0
        pad = 5

        for name, date in self.__dates.items():
            row = index // 6
            column = index - (row * 6)
            frame = Frame(master=self.__inner_frame, relief=RIDGE, borderwidth=2, padx=pad, pady=pad)
            BirthdayLabel(frame, name, date, pad, self.__inner_frame)
            frame.grid(row=row, column=column, padx=pad, pady=pad)
            index += 1

        self.__canvas.update_idletasks()
        self.__resize_window()
        self.__create_scrollbar()
        self.__create_menubar()

    def __create_scrollbar(self):
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
        if len(self.__dates) < 3:
            width = 200
        else:
            width = self.__inner_frame.winfo_reqwidth() + 21

        self.__root.geometry(f"{width}x{width}")

    def __create_menubar(self):
        menubar = Menu(self.__root)
        option_menu = Menu(master=menubar, tearoff=0)
        option_menu.add_command(label="Neu", command=lambda: Create(self.__root, self.__inner_frame).run())
        option_menu.add_separator()
        option_menu.add_command(label="Schließen", command=lambda: exit())
        menubar.add_cascade(label="Optionen", menu=option_menu)

        self.__root.config(menu=menubar)

    def run(self):
        self.__root.mainloop()


def create_widgets(dates: dict, inner_frame: Frame):
    for widget in inner_frame.winfo_children():
        widget.destroy()
    index = 0
    pad = 5

    for name, date in dates.items():
        row = index // 6
        column = index - (row * 6)
        frame = Frame(master=inner_frame, relief=RIDGE, borderwidth=2, padx=pad, pady=pad)
        BirthdayLabel(frame, name, date, pad, inner_frame)
        frame.grid(row=row, column=column, padx=pad, pady=pad)
        index += 1


class BirthdayLabel:
    def __init__(self, frame: Frame, name: str, date: str, pad: int, inner_frame: Frame):
        self.__inner_frame = inner_frame
        self.__frame = frame
        self.__name = name
        self.__date = date
        self.__pad = pad
        self.__create_label()

    def __create_label(self):
        pad = self.__pad
        dates_text = self.__text_label_str()

        text_label = Label(master=self.__frame, text=dates_text, padx=pad, pady=pad)
        text_label.pack()  # side=LEFT
        self.__add_menu(text_label)

    def __text_label_str(self) -> str:
        date = self.__date
        validator = Validator()
        age = validator.calculate_age(date)
        new_date = f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

        return f"{self.__name}\n{age} Jahre\n{new_date}"

    def __add_menu(self, text_label: Label):
        menu = Menu(master=text_label, tearoff=0)
        menu.add_command(label="Bearbeiten", command=lambda: self.__edit_birthday(text_label))
        menu.add_command(label="Löschen", command=self.__remove_birthday)

        text_label.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

    def __edit_birthday(self, text_label: Label):
        name = self.__name
        date = self.__date
        split_date = date.split("-")
        day, month, year = split_date[2], split_date[1], split_date[0]
        validator = Validator()

        text_label.pack_forget()

        entry_frame = Frame(master=self.__frame)
        name_entry = Entry(master=entry_frame)
        day_entry = Entry(master=entry_frame, width=4, justify=CENTER)
        month_entry = Entry(master=entry_frame, width=4, justify=CENTER)
        year_entry = Entry(master=entry_frame, width=6, justify=CENTER)
        save_button = Button(master=entry_frame, text="Speichern", anchor=CENTER)

        name_entry.insert(0, name)
        day_entry.insert(0, day)
        month_entry.insert(0, month)
        year_entry.insert(0, year)

        save_button.config(command=lambda: self.__save_change(
            name_entry.get(), [day_entry.get(), month_entry.get(), year_entry.get()], entry_frame))

        day_entry.bind("<Key>", lambda event, e=day_entry: validator.check_input(event, e))
        month_entry.bind("<Key>", lambda event, e=month_entry: validator.check_input(event, e))
        year_entry.bind("<Key>", lambda event, e=year_entry: validator.check_input(event, e, 3))

        name_entry.pack()
        day_entry.pack()
        month_entry.pack()
        year_entry.pack()
        save_button.pack()
        entry_frame.pack()

    def __save_change(self, name: str, date: list, entry_frame: Frame):
        validator = Validator()
        day, month, year = date[0], date[1], date[2]
        new_date = f"{year}-{month}-{day}"

        if (validator.check_day(day) != ""
                and validator.check_month(month) != ""
                and validator.check_year(year) != ""):
            entry_frame.pack_forget()
            self.__dates = Json().json_data
            self.__dates[name] = new_date
            self.__name = name
            self.__date = new_date
            self.__create_label()
            Json().save_in_json(self.__dates)

    def __remove_birthday(self):
        name = self.__name
        delete_option = messagebox.askyesno(
            "Löschen", f"Sollen die Daten von {name} wirklich gelöscht werden?")

        if delete_option:
            self.__dates = Json().json_data
            self.__dates.pop(name)
            Json().save_in_json(self.__dates)
            create_widgets(self.__dates, self.__inner_frame)
