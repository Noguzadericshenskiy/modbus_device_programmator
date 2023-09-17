import re

from tkinter import Tk, Frame, messagebox, Listbox, StringVar, Label
from tkinter.ttk import Button, Entry

# from tkinter.ttk import filedialog as fd
from md_prog.views import config


class RootWin(Tk):
    def __int__(self):
        super().__init__()
        self.title("Программатор устройств Modbus")
        self.geometry("500x300")
        self.resizable(False, False)
        # self.minsize(1024, 800)
        # self.maxsize(1920, 1080)
        # self.bold_font = "bold"
        self.configure(bd="red")
        ButtonFrame()

    def quit_app(self):
        self.quit()


class ButtonFrame(Frame):
    """Up frame, with parameters and buttons"""
    def __init__(self):
        super().__init__()

        choices = ["dev 1", "dev 2", "dev 3"]
        choices_var = StringVar(value=choices)

        self.configure(bd=config.main_window_color,
                       width=1000,
                       height=100, )

        self.type_device_lbl = Label(self, text='Тип',)
        self.type_device = Listbox(self, listvariable=choices_var)


        self.type_device.bind("<<ListboxSelect>>", self.on_select)
        self.connect_btn = Button(
            self,
            text="Подключить",
            # compound=self.connect_device
        )
        self.disconnect_btn = Button(
            self,
            text="Отключить",
        )
        self.status_devise_lbl = Label(self, text='Статус', )
        self.status_devise = "ВАТАФАКА"
        self.address = Entry(self)
        self.write_btn = Button(
            self,
            text="Записать",
        )

    @staticmethod
    def validation(address):
        result = re.match("[1-9]", address) is not None
        if not result and len(address) > 1:
            messagebox.showerror(config.error_enter_address)
#ToDo: Проверить ввод

    def on_select(self):
        type = "Type-1"
#ToDo: дописать запись параметра или будем передавать все сразу?


class InfoFrame(Frame):
    def __init__(self):
        super().__init__()



class DownFrame(Frame):
    ...


if __name__ == "__main__":
    app = RootWin()
    app.mainloop()



