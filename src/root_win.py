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

# from devices import (
#     ip535_07ea_rs,
#     ip535_07ea_rs_START,
#     ip329_330_1_1,
#     mip_i_ex,
# )
from src.config import *
from src.utils import get_device, get_port_info, get_port


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
        self.grid(column=0, row=1, sticky="ew")

        self.lbl_port = Label(self, text="COM порт",)
        self.lbl_port.config(lbl_conf)
        self.lbl_port.grid(column=0, row=1)
        self.lbl_type = Label(self, text="Устройство",)
        self.lbl_type.config(lbl_conf)
        self.lbl_type.grid(column=0, row=2)
        self.lbl_address = Label(self, text="Адрес устр-ва", )
        self.lbl_address.config(lbl_conf)
        self.lbl_address.grid(column=0, row=3)
        self.lbl_speed = Label(self, text="Скорость")
        self.lbl_speed.config(lbl_conf)
        self.lbl_speed.grid(column=0, row=4)
        self.lbl_stop_bit = Label(self, text="Stop bit/s")
        self.lbl_stop_bit.config(lbl_conf)
        self.lbl_stop_bit.grid(column=0, row=5)
        self.lbl_parity = Label(self, text="Parity")
        self.lbl_parity.config(lbl_conf)
        self.lbl_parity.grid(column=0, row=6)

        self.combobox_port = Combobox(
            self,
            width=50,
            height=10,
            values=get_port_info(),
            state="readonly",
        )
        self.combobox_port.grid(column=1, row=1, sticky="w", padx=10)
        self.combobox_type = Combobox(
            self,
            width=50,
            height=10,
            values=LIST_NAMES_DEVICES,
            state="readonly"
        )
        self.combobox_type.grid(column=1, row=2, sticky="w", padx=10)

        self.etr_address = Entry(self)
        self.etr_address.grid(column=1, row=3, sticky="w", padx=10)

        self.combobox_speed = Combobox(
            self,
            width=20,
            height=10,
            values=("1","2")
        )


        self.btn_connect = Button(self, text="Прочитать параметры", )
        self.btn_connect.config(btn_conf)
        self.btn_connect.grid(column=5, row=1,
                              # columnspan=2
                              )

        self.btn_set_def_param = Button(self, text="Установить параметры SIGMA", )
        # self.btn_set_def_param.grid(column=5, row=2,  )

        self.btn_disconnect = Button(self, text="Кнопка 1", )
        self.btn_disconnect.config(btn_conf)
        self.btn_disconnect.grid(column=5, row=2)

        self.btn_write = Button(self, text="Кнопка 2",
                                )
        self.btn_write.config(btn_conf)
        self.btn_write.grid(column=5, row=3)

        self.table = Treeview(
            show="headings",
            selectmode="browse",
            columns=HEADS_TABLE,
            displaycolumns=COLUMNS_TABLE,
        )
        self.table.grid(column=0, row=5, sticky="ew")

    def table_output(self, list_params: tuple) -> None:
        for header in HEADS_TABLE:
            self.table.heading(header, text=header, anchor=CENTER)

        self.table.tag_configure("oddrow", background='white')
        self.table.tag_configure("evenrow", background='lightblue')
        count = 0
        self.table.column('Параметр', width=390)
        self.table.column('Значение', width=100)

        for row_info in list_params:
            if count % 2 == 0:
                self.table.insert('', END, values=row_info, tags=('evenrow',))
            else:
                self.table.insert('', END, values=row_info, tags=('oddrow',))
            count += 1

    def get_conn_params_def(self):
        device = get_device(self.combobox_type.get())
        speed = device.SPEEDS_DEVICE


    def get_speed_dev(self):
        device = get_device(self.combobox_type.get())

        speed = self.combobox_type.get()
        return speed

    # def disconnect(self):
    #     self.lbl_status.config(text="Отключено")



    def get_params(self) -> list:
        "Получает параметры устройства"
        port = get_port(self.combobox_port.get())

        slave = self.etr_address.get()


        # if self.combobox_type.get() == "ИП535-07еа-RS":
        #     device = ip535_07ea_rs.SignalingDeviceIP53_507EA_RS(port=port)
        # if self.combobox_type.get() == "ИП535-07еа-RS-ПУСК":
        #     device = ip535_07ea_rs_START.SignalingDeviceStart(port=port)
        #     print("Пуск")
        # if self.combobox_type.get() == "ИП329/330-1-1":
        #     device = ip329_330_1_1.FireDetektorFlameIP329_330_re(port=port)
        # if self.combobox_type.get() == "МИП-И-Ех":
        #     device = mip_i_ex.InterfaceFirefighterModule(port=port)



        # if slave:
        #     params_dev = device.get_info(slave=int(slave))
        # else:
        #     params_dev = device.get_info()

        return []


    # def set_sigma(self):
    #     port = get_port(self.combobox_port.get())
    #     device = ip535_07ea_rs.SignalingDeviceIP53_507EA_RS(port=port)

    # def out_params_device(self, params: list) -> None:
        # for i_param in params:
        ...


if __name__ == "__main__":
    app = Root()
    app.mainloop()

# par = {'ID устройства': 21, 'Адрес устройства': 2, 'Скорость интерфейса': 4, 'Статус шлейфа 1': 'Короткое замыкание', 'Статус шлейфа 2': 'Короткое замыкание', 'Статус шлейфа 3': 'Короткое замыкание', 'Статус источника 1': 'Норма', 'Статус источника 2': 'Неисправность', 'Длинна кабеля (ТРЕВОГА) 1': [65535], 'Длинна кабеля (ТРЕВОГА) 2': [65535], 'Длинна кабеля (ТРЕВОГА) 3': [65535], 'Тест 11 адрес': [0]}
