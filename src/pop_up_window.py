from tkinter import messagebox
from tkinter import Toplevel
from tkinter.ttk import Label, Entry, Button, Combobox

from config import *


class BaseDialogWin(Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.grab_set()
        self.deiconify()
        self.config(bg="yellow", border=4, padx=5, pady=10)
        self.geometry("300x200")
        self.lbl_parameter_enter = Label(self,)
        self.lbl_parameter_enter.config(background="red", border=4, justify="center", width=20, padding=2)
        self.lbl_parameter_enter.grid(column=0, row=1)
        self.btn_change = Button(self, text="OK", command=self.ok_button)
        self.btn_change.config(width=10, padding=10)
        self.btn_change.grid(column=0, row=3)
        self.btn_close = Button(self, text="Отмена", command=self.close)
        self.btn_close.config(width=10, padding=10)
        self.btn_close.grid(column=1, row=3)

    def close(self):
        self.destroy()

    def ok_button(self):
        ...


class DialogEnterNewSlave(BaseDialogWin):
    """Диалоговое окно ввода адреса устройства"""
    def __init__(self, master, new_address):
        super().__init__(master)
        self.title = "Выбор адреса устройства"
        self.new_address = new_address
        self.lbl_parameter_enter.config(text="Введите Адрес устройства")
        self.etr_slave = Entry(self, )
        self.etr_slave.grid(column=1, row=1)
        self.btn_change = Button(command=self.ok_button)

    def ok_button(self):
        "Обработка события и установка данных"
        self.new_address.set(self.etr_slave.get())
        self.close()


class DialogEnterNewBaudrate(BaseDialogWin):
    """Диалоговое окно ввода скорости работы интерфейса"""
    def __init__(self, master, new_baudrate, speeds):
        super().__init__(master)
        self.title = "Выбор скорости устройства"
        self.lbl_parameter_enter.config(text="Выберите скорость устройства")
        self.new_baudrate = new_baudrate
        self.speeds = speeds
        self.combobox_speeds = Combobox(self, values=self.speeds, state="readonly")
        self.combobox_speeds.config(combobox_conf_sm)
        self.combobox_speeds.grid(column=1, row=1)

    def ok_button(self):
        "Обработка события и установка данных"
        self.new_baudrate.set(self.combobox_speeds.get())
        self.close()


class DialogEnterNewParity(BaseDialogWin):
    """Диалоговое окно ввода выбора значения проверки на четность"""
    def __init__(self, master, new_parity, parity_dev):
        super().__init__(master)
        self.new_parity = new_parity
        self.parity_dev = parity_dev
        self.title = "Выбор проверки на четность"
        self.lbl_parameter_enter.config(text="Выберите проверку на четность ")
        self.combobox_parity = Combobox(self, values=self.parity_dev, state="readonly")
        self.combobox_parity.config(combobox_conf_sm)
        self.combobox_parity.grid(column=1, row=1)

    def ok_button(self):
        "Обработка события и установка данных"
        self.new_parity.set(self.combobox_parity.get())
        self.close()


class DialogEnterNewStopBit(BaseDialogWin):
    """Диалоговое окно выбора стоп бита"""
    def __init__(self, master, new_bits, bits):
        super().__init__(master)
        self.new_bits = new_bits
        self.bits = bits
        self.title = "Выбор стоп бита"
        self.lbl_parameter_enter.config(text="Выберите стоп-бит")
        self.combobox_s_bits = Combobox(self, values=self.bits, state="readonly")
        self.combobox_s_bits.config(combobox_conf_sm)
        self.combobox_s_bits.grid(column=1, row=1)

    def ok_button(self):
        """Обработка события и установка данных"""
        self.new_bits.set(self.combobox_s_bits.get())
        self.close()


def msg_err_address():
    messagebox.showerror(
        title="error",
        message="Не верно введен адрес устройства"
    )


def msg_err_no_connect():
    messagebox.showerror(
        title="error connect",
        message="не удалось подключится к устройству"
    )

def msg_err_incorect_params():
    messagebox.showerror(
        title="incorrect params",
        message="Не верные данные для подключения"
    )

