from tkinter import messagebox
from tkinter import Toplevel
from tkinter.ttk import Label, Entry, Button

from config import *


class DialogChangAddress(Toplevel):
    def __init__(self, master, conn, new_address):
        super().__init__(master)
        self.new_address = new_address
        self.grab_set()
        self.deiconify()
        self.config(bg="yellow", border=4, padx=5, pady=10)
        self.title = "Выбор адреса устройства"
        self.geometry("300x200")
        # self.resizable(False, False)

        self.lbl_change_address = Label(self, text="Введите новый адрес устройства")
        self.lbl_change_address.config(background="red", border=4, justify="center", width=20, padding=2)
        self.lbl_change_address.grid(column=0, row=1)
        self.etr_slave = Entry(self,
            # textvariable=self.new_address.get()
        )
        self.etr_slave.grid(column=1, row=1)
        self.btn_change = Button(self, text="Изменить", command=self.change_button)
        self.btn_change.config(width=10, padding=10)
        self.btn_change.grid(column=0, row=3)
        self.btn_close = Button(self, text="Отмена", command=self.close)
        self.btn_close.config(width=10, padding=10)
        self.btn_close.grid(column=1, row=3)

    def close(self):
        self.destroy()

    def change_button(self):
        "Обработка события и отправка данных"

        self.new_address.set(self.etr_slave.get())

        self.close()


def msg_err_address():
    messagebox.showerror(
        title="error",
        message="Не верно введен адрес устройства"
    )





