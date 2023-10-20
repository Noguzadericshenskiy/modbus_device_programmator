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

from devices import (
    ip535_07ea_rs,
    ip535_07ea_rs_START,
    ip329_330_1_1,
    mip_i_ex,
)
from src.config import *
from src.utils import get_port_info, get_port

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


class UpFrame(Frame):

    conn = None
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

        self.combobox_port = Combobox(
            self,
            width=50,
            height=10,
            values=get_port_info(),
            state="readonly",
        )
        self.combobox_port.grid(column=1, row=1, sticky="w", padx=10)

        # self.port_etr = Entry(self,)
        # self.port_etr.grid(column=1, row=1, sticky="w", padx=10)

        self.lbl_type = Label(self, text='Тип',)
        self.lbl_type.config(lbl_conf)
        self.lbl_type.grid(column=0, row=2)
        self.combobox_type = Combobox(
            self,
            width=50,
            height=10,
            values=self.get_list_devices(),
            state="readonly"
        )
        self.combobox_type.grid(column=1, row=2, sticky="w", padx=10)

        self.lbl_address = Label(self, text="Введите адрес", )
        self.lbl_address.config(lbl_conf)
        self.lbl_address.grid(column=0, row=3)

        self.etr_address = Entry(self)
        self.etr_address.grid(column=1, row=3, sticky="w", padx=10)

        self.btn_connect = Button(self, text="Прочитать параметры", command=self.read_params,)
        self.btn_connect.config(btn_conf)
        self.btn_connect.grid(column=5, row=1, columnspan=2)

        self.btn_set_def_param = Button(self, text="Установить параметры SIGMA", command=self.set_sigma)

        self.btn_disconnect = Button(self, text="Отключить", command=self.disconnect,)
        self.btn_disconnect.config(btn_conf)
        self.btn_disconnect.grid(column=5, row=2)

        self.lbl_status_devise = Label(self, text='Статус',)
        self.lbl_status_devise.config(lbl_conf)
        self.lbl_status_devise.grid(column=0, row=4)

        self.lbl_status = Label(self, text="Выполните подключение",)
        self.lbl_status.config(lbl_conf)
        self.lbl_status.grid(column=1, row=4)

        self.btn_write = Button(self, text="Записать",
                                # command=self.write_params,
                                )
        self.btn_write.config(btn_conf)
        self.btn_write.grid(column=5, row=3)

        self.table = Treeview(
            show="headings",
            selectmode="browse",
            columns=HEADS_TABLE,
            displaycolumns=COLUMNS_TABLE,
        )
        self.table.grid(column=0, row=5, columnspan=5)

    def table_wiev(self, list_params):

        self.table.column("Параметр", width=0)
        self.table.column("Значение", width=150)
        for header in HEADS_TABLE:
            self.table.heading(header, text=header, anchor=CENTER)

        # self.table.pack(side='left')

        self.table.tag_configure("oddrow", background='white')
        self.table.tag_configure("evenrow", background='lightblue')
        count = 0
        self.table.column('Параметр', width=390)
        self.table.column('Значение', width=100)

        for row_info in list_params:
            if count % 2 == 0:
                # row = tuple_additional(heading_tab)
                self.table.insert('', END, values=row_info, tags=('evenrow',))
            else:
                # row = tuple_additional(heading_tab)
                self.table.insert('', END, values=row_info, tags=('oddrow',))
            count += 1


    def disconnect(self):
        self.lbl_status.config(text="Отключено")

    def read_params(self):
        params = self.get_params()
        self.table_wiev(params)

    def get_list_devices(self) -> list:
        list_devices = [
            ip535_07ea_rs.SignalingDeviceIP53_507EA_RS.NAME,
            ip535_07ea_rs_START.SignalingDeviceStart.NAME,
            ip329_330_1_1.FireDetektorFlameIP329_330_re.NAME,
            mip_i_ex.InterfaceFirefighterModule.NAME,
            ]
        return list_devices

    def get_params(self):
        "Получает параметры устройства"
        params_dev = []
        port = get_port(self.combobox_port.get())

        if self.combobox_type.get() == "ИП535-07еа-RS":
            device = ip535_07ea_rs.SignalingDeviceIP53_507EA_RS(port=port)
            params_dev = device.get_info(slave=1)
            print(params_dev)
        if self.combobox_type.get() == "ИП535-07еа-RS-ПУСК":
            device = ip535_07ea_rs_START.SignalingDeviceStart(port=port)
            print("Пуск")
        if self.combobox_type.get() == "ИП329/330-1-1":
            device = ip329_330_1_1.FireDetektorFlameIP329_330_re(port=port)
            params_dev = device.get_info()
            print(params_dev)
        if self.combobox_type.get() == "МИП-И-Ех":
            device = mip_i_ex.InterfaceFirefighterModule(port=port)
            params_dev = device.get_info(slave=2)
            print(params_dev)

        return params_dev


    def set_sigma(self):
        port = get_port(self.combobox_port.get())
        device = ip535_07ea_rs.SignalingDeviceIP53_507EA_RS(port=port)

    # def out_params_device(self, params: list) -> None:
        # for i_param in params:
        ...


if __name__ == "__main__":
    app = Root()
    app.mainloop()

# par = {'ID устройства': 21, 'Адрес устройства': 2, 'Скорость интерфейса': 4, 'Статус шлейфа 1': 'Короткое замыкание', 'Статус шлейфа 2': 'Короткое замыкание', 'Статус шлейфа 3': 'Короткое замыкание', 'Статус источника 1': 'Норма', 'Статус источника 2': 'Неисправность', 'Длинна кабеля (ТРЕВОГА) 1': [65535], 'Длинна кабеля (ТРЕВОГА) 2': [65535], 'Длинна кабеля (ТРЕВОГА) 3': [65535], 'Тест 11 адрес': [0]}
