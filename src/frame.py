from tkinter import (
    Tk,
    Button,
    filedialog,
    Frame,
    StringVar,
    Listbox,
    LabelFrame,
    CENTER,
    END
)
from tkinter.ttk import (
    Combobox,
    Entry,
    Label,
    Progressbar,
    Treeview)

from devices import devices_def
from utils import *
from src.config import *


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
        UpFrame()
        CenterFrameLeft()
        CenterFrameRight()
        DownFrame()


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
        self.grid(column=0, row=1, columnspan=2, sticky="ew")

        self.lbl_port = Label(self, text="Укажите номер COM порта",)
        self.lbl_port.config(lbl_conf)
        self.lbl_port.grid(column=0, row=1)

        self.port_etr = Entry(self,)
        self.port_etr.grid(column=1, row=1, sticky="w", padx=10)

        self.lbl_type = Label(self, text='Тип',)
        self.lbl_type.config(lbl_conf)
        self.lbl_type.grid(column=0, row=2)
        self.combobox_type = Combobox(
            self,
            width=50,
            height=10,
            values=self.combobox_type(),
            state="readonly"
        )
        self.combobox_type.grid(column=1, row=2, sticky="w", padx=10)

        self.lbl_address = Label(self, text="Введите адрес", )
        self.lbl_address.config(lbl_conf)
        self.lbl_address.grid(column=0, row=3)

        self.etr_address = Entry(self)
        self.etr_address.grid(column=1, row=3, sticky="w", padx=10)
        # self.combobox_type.bind("<<ComboboxSelected>>", self.selected_type)

        self.btn_connect = Button(self, text="Подключить", command=self.check_connect, )
        self.btn_connect.config(btn_conf)
        self.btn_connect.grid(column=5, row=1, columnspan=2)

        self.btn_disconnect = Button(self, text="Отключить", command=self.disconnect,)
        self.btn_disconnect.config(btn_conf)
        self.btn_disconnect.grid(column=5, row=2)

        self.lbl_status_devise = Label(self, text='Статус',)
        self.lbl_status_devise.config(lbl_conf)
        self.lbl_status_devise.grid(column=0, row=4)

        self.lbl_status = Label(self, text="подключено",)
        self.lbl_status.config(lbl_conf)
        self.lbl_status.grid(column=1, row=4)

        self.btn_write = Button(self, text="Записать", command=self.write_params,)
        self.btn_write.config(btn_conf)
        self.btn_write.grid(column=5, row=3)

    def combobox_type(self):
        list_dev = []
        for i_dev in devices_def:
            list_dev.append(i_dev["name"])
        return list_dev

    def check_connect(self):
        ...

    def disconnect(self):
        ...

    def write_params(self):
        ...


class CenterFrameLeft(LabelFrame):
    def __init__(self):
        super().__init__()
        self.configure(
            background="#b3c5f5",
            border=5,
            height=250,
            width=500,
            relief="raised",
            text='Содержание регистров устройства',
            font=14
        )
        self.grid(column=0, row=2, sticky="nw")
        self.view_table()

    def view_table(self):
        self.table = Treeview(
            self,
            show="headings",
            selectmode="browse",
            columns=HEADS_TABLE,
            displaycolumns=COLUMNS_TABLE)

        self.table.column("Параметр", width=0)
        self.table.column("Значение", width=100)

        for header in HEADS_TABLE:
            self.table.heading(header, text=header, anchor=CENTER)

        self.table.pack(side='left')

        self.table.tag_configure("oddrow", background='white')
        self.table.tag_configure("evenrow", background='lightblue')
        count = 0
        self.table.column('Параметр',

                          width=390)
        self.table.column('Значение',

                          width=100)

        for row_info in self.get_info():
            if count % 2 == 0:
                # row = tuple_additional(heading_tab)
                self.table.insert('', END, values=row_info, tags=('evenrow',))
            else:
                # row = tuple_additional(heading_tab)
                self.table.insert('', END, values=row_info, tags=('oddrow',))
            count += 1

    @staticmethod
    def get_info():
        list_params = [("Параметр 1", 1), ("Параметр 2", 0)]
        return list_params


class CenterFrameRight(LabelFrame):
    def __init__(self):
        super().__init__()
        self.configure(
            background="#b3c5f5",
            border=5,
            height=250,
            width=500,
            relief="raised",
            text='Содержание регистров устройства после записи',
            font=14
        )
        self.grid(column=1, row=2, sticky="nw")


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
        self.grid(column=0, row=3, columnspan=2)


if __name__ == "__main__":
    app = Root()
    app.mainloop()
