from tkinter import messagebox
from tkinter import Toplevel
from tkinter.ttk import Label, Entry, Button

from config import *


class DialogChangAddress(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.grab_set()
        self.deiconify()
        self.config(background="yellow", border=4, padx=5, pady=10)
        self.title = "Выбор адреса устройства"
        self.geometry("180x100")
        self.resizable(False, False)

        self.lbl_change_address = Label(text="Введите новый адрес устройства")
        self.lbl_change_address.config()
        self.lbl_change_address.grid(column=0, row=1)
        self.etr_slave = Entry(self)
        self.etr_slave.grid(column=0, row=2)
        self.btn_change = Button(self, text="Изменить", command=self.change)
        self.btn_change.config(btn_conf)
        self.btn_change.grid(column=3, row=1)
        self.btn_close = Button(self, text="Отмена", command=self.close)
        self.btn_close.config(btn_conf)
        self.btn_close.grid(column=3, row=2)
    def close(self):
        self.destroy()

    def change(self):
        "Обработка события и отправка данных"
        address = self.etr_slave.get()


def msg_err_address():
    messagebox.showerror(
        title="error",
        message="Не верно введен адрес устройства"
    )




