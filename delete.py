from tkinter import *


class Delete:
    @staticmethod
    def create_window(dates):
        root = Tk()
        root.title("Geburtstage löschen")
        pad = 5

        for i in range(5):
            frame = Frame(root, relief=RIDGE, borderwidth=2, padx=pad, pady=pad)
            text_label = Label(frame, text="Name und Datum")
            delete_button = Button(frame, text="löschen")
            text_label.pack(side="left")
            delete_button.pack(side="right")
            frame.pack(padx=10, pady=10)

        mainloop()
