import tkinter as tk
from tkinter import Tk, Frame, messagebox, Listbox, StringVar, Label
from tkinter import ttk
from tkinter.ttk import Combobox, Button, Entry

from md_prog.views import config


class RootWin(Tk):
    def __init__(self):
        super().__init__()
        self.title("Программатор устройств Modbus")
        self.geometry("1000x800")
        self.resizable(False, False)
        self.configure(background=config.main_window_color)
        self.lbl_type = Label(
            self,
            bg=config.button_color,
            fg=config.text_color,
            text='Тип',
            justify='right',
            pady=5)
        self.lbl_type.pack()


        self.combobox_type = Combobox(
            self,
            values=self.combobox_type(),
            state="readonly"
        )
        # self.combobox_type.bind("<<ComboboxSelected>>", self.selected_type)
        self.combobox_type.pack()
        self.btn_connect = Button(
            self,
            text="Подключить",
            command=self.get_selected_type,
        )
        self.btn_connect.pack()

    # def selected_type(self, event):
    #     value = self.combobox_type.get()
    #     index = self.combobox_type.current()
    #     print(value, index)

        self.btn_disconnect = Button(
            self,
            text="Отключить",
            command=self.disconnect
        )
        self.btn_disconnect.pack()
        self.lbl_status_devise = Label(self, text='Статус',)
        self.lbl_status_devise.pack()
        self.lbl_status = Label(self, text="подключено, ожидание")
        self.lbl_status.pack()
        self.lbl_address = Label(self, text="Адрес")
        self.lbl_address.pack()
        self.etr_address = Entry(self)
        self.etr_address.pack()
        self.btn_write = Button(self, text="Записать", command=self.write,)
        self.btn_write.pack()
    # ToDo сюда добавить поле вывода с информацией
        self.etr_save_info = Button(self, )


    def get_selected_type(self):
        value = self.combobox_type.get()
        print(value)

    @staticmethod
    def combobox_type():
        items = ("Tupe 1", "Tupe 2", "Type 3", "Type 4")
        return items

    def quit_app(self):
        self.quit()

    def disconnect(self):
        print("Отключить")

    def write(self):
        value = self.etr_address.get()
        print(value)


if __name__ == "__main__":
    app = RootWin()
    app.mainloop()
