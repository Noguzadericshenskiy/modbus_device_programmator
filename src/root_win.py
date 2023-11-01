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
from src.utils import get_device, get_ports_info, get_port, check_slave
from src.pop_up_window import msg_err_address, DialogChangAddress

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
        self.lbl_stop_bit = Label(self, text="Parity")
        self.lbl_stop_bit.config(lbl_conf)
        self.lbl_stop_bit.grid(column=0, row=5)
        self.lbl_parity = Label(self, text="Stop bit/s")
        self.lbl_parity.config(lbl_conf)
        self.lbl_parity.grid(column=0, row=6)
        self.combobox_port = Combobox(self, values=get_ports_info(), state="readonly")
        self.combobox_port.config(combobox_conf_long)
        self.combobox_port.grid(column=1, row=1, sticky="w", padx=10)
        self.combobox_type = Combobox(self, values=LIST_NAMES_DEVICES, state="readonly")
        self.combobox_type.config(combobox_conf_long)
        self.combobox_type.grid(column=1, row=2, sticky="w", padx=10)
        self.etr_address = Entry(self)
        self.etr_address.grid(column=1, row=3, sticky="w", padx=10)
        self.combobox_speed = Combobox(self, values=SPEEDS, state="readonly")
        self.combobox_speed.config(combobox_conf_sm)
        self.combobox_speed.grid(column=1, row=4, sticky="w", padx=10)
        self.combobox_parity = Combobox(self, values=PARITY, state="readonly")
        self.combobox_parity.config(combobox_conf_sm)
        self.combobox_parity.grid(column=1, row=5, sticky="w", padx=10)
        self.combobox_bits = Combobox(self, values=BITS, state="readonly")
        self.combobox_bits.config(combobox_conf_sm)
        self.combobox_bits.grid(column=1, row=6, sticky="w", padx=10)

        self.btn_connect_def = Button(self, text='Получить параметры по умолчанию', command=self.get_info_dev)
        self.btn_connect_def.config(btn_conf)
        self.btn_connect_def.grid(column=5, row=1,)
        self.btn_connect = Button(self, text="Прочитать параметры", command=self.get_info_dev)
        self.btn_connect.config(btn_conf)
        self.btn_connect.grid(column=5, row=2,
                              # columnspan=2
                              )
        self.btn_connect_sigma = Button(self, text="Прочитать с пар. Сигма", command=self.get_info_dev)
        self.btn_connect_sigma.config(btn_conf)
        self.btn_connect_sigma.grid(column=5, row=3,
                              # columnspan=2
                              )
        self.btn_set_param_sigma = Button(self, text="Установить парамеры SIGMA", )
        self.btn_set_param_sigma.config(btn_conf)
        self.btn_set_param_sigma.grid(column=5, row=4,)

        self.btn_disconnect = Button(self, text="Изменить адрес устройства", command=self.set_address)
        self.btn_disconnect.config(btn_conf)
        self.btn_disconnect.grid(column=5, row=5)

        self.btn_write = Button(self, text="Кнопка 2",
                                )
        self.btn_write.config(btn_conf)
        self.btn_write.grid(column=5, row=6)

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

    def set_address(self):
        # new_address = 0
        # slave: str = self.etr_address.get()
        # dev = self.get_conn_params()
        print("Вызов DialogChangAddress")
        new_addrees_viget = DialogChangAddress(self)
        print(new_addrees_viget)


    def get_info_dev(self):
        "Получить информацию об устройстве"
        slave: str = self.etr_address.get()
        dev = self.get_conn_params()

        if slave != "":
            if check_slave(slave):
                self.table_output(dev.get_info(int(slave)))
            else:
                msg_err_address()
                print("вывод окна с ошибкой")
        else:
            self.table_output(dev.get_info())

    def get_conn_params(self):
        "Получить информацию для соединения"
        port = get_port(self.combobox_port.get())
        name = self.combobox_type.get()

        speed = self.combobox_speed.get()
        parity = self.combobox_parity.get()
        bits = self.combobox_bits.get()
        if speed != "" and parity != "" and bits != "":
            return get_device(name=name, port=port, baudrate=int(speed), parity=parity, stopbits=int(bits))
        elif speed != "" and parity != "":
            return get_device(name=name, port=port, baudrate=int(speed), parity=parity)
        elif parity != "" and bits != "":
            return get_device(name=name, port=port, parity=parity, stopbits=int(bits))
        elif speed != "" and bits != "":
            return get_device(name=name, port=port, baudrate=int(speed), stopbits=int(bits))
        elif speed != "":
            return get_device(name=name, port=port, baudrate=int(speed))
        elif parity != "":
            return get_device(name=name, port=port, parity=parity)
        elif bits != "":
            return get_device(name=name, port=port, stopbits=int(bits))
        else:
            return get_device(name=name, port=port)

    # def disconnect(self):
    #     self.lbl_status.config(text="Отключено")


    # def set_sigma(self):
    #     port = get_port(self.combobox_port.get())
    #     device = ip535_07ea_rs.SignalingDeviceIP53_507EA_RS(port=port)

    # def out_params_device(self, params: list) -> None:
        # for i_param in params:


if __name__ == "__main__":
    app = Root()
    app.mainloop()

# par = {'ID устройства': 21, 'Адрес устройства': 2, 'Скорость интерфейса': 4, 'Статус шлейфа 1': 'Короткое замыкание', 'Статус шлейфа 2': 'Короткое замыкание', 'Статус шлейфа 3': 'Короткое замыкание', 'Статус источника 1': 'Норма', 'Статус источника 2': 'Неисправность', 'Длинна кабеля (ТРЕВОГА) 1': [65535], 'Длинна кабеля (ТРЕВОГА) 2': [65535], 'Длинна кабеля (ТРЕВОГА) 3': [65535], 'Тест 11 адрес': [0]}
