from tkinter import Tk, Button, filedialog, Frame, StringVar, Listbox, LabelFrame
from tkinter.ttk import Combobox, Entry, Label, Progressbar

from devices import devices_def
from src import config


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Программатор устройств Modbus")
        self.configure(
            background="#171212",
            border=8,
            height=1000,
            width=800,
            relief="groove",
        )
        self.resizable(False, False)
        frame_up = UpFrame()
        freme_center = CenterFrame()
        frame_down = DownFrame()


class UpFrame(Frame):
    def __init__(self):
        super().__init__()
        self.configure(
            background="#fc5e03",
            border=5,
            height=200,
            width=1000,
            relief="raised",
        )
        self.grid(column=0, row=1)


class CenterFrame(Frame):
    def __init__(self):
        super().__init__()
        self.configure(
            background="#b3c5f5",
            border=5,
            height=250,
            width=1000,
            relief="sunken",
        )
        self.grid(column=0, row=2, sticky="nsew")
        self.lbl_status_devise_in = Label(self, text='Содержание регистров устройства',)
        self.lbl_status_devise_in.config(background="#043bc7", font=14, )
        self.lbl_status_devise_in.grid(column=1, row=1, padx=10, pady=10)
        self.lbl_status_devise_out = Label(self, text='Содержание регистров устройства после записи', )
        # self.lbl_status_devise_out.config(config.lbl_conf)
        self.lbl_status_devise_out.grid(column=2, row=1)


class DownFrame(Frame):
    def __init__(self):
        super().__init__()
        self.configure(
            background="#fc5e03",
            border=5,
            height=100,
            width=1000,
            relief="raised",
        )
        self.grid(column=0, row=3)


if __name__ == "__main__":
    app = Root()
    app.mainloop()
