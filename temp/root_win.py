import time
import tkinter

from tkinter import (
    Tk,
    Button,
    Frame,
    StringVar,
    CENTER,
    END,
    IntVar,
    Menu,
)
from tkinter.ttk import (
    Combobox,
    Entry,
    Label,
    Treeview)
from src.config import *
from src.utils import (
    get_device,
    get_ports_info,
    get_port,
    check_slave,
    get_value_baudrate_dev,
    get_value_parity_dev,
    get_value_stop_bits_dev,
)
from temp.pop_up_window import (
    msg_err_address,
    msg_err_no_connect,
    msg_err_incorect_params,
    DialogEnterNewSlave,
    DialogEnterNewBaudrate,
    DialogEnterNewParity,
    DialogEnterNewStopBit,
)
# from src.scan_frame import Scan
# from PySide6.QtWidgets import QApplication


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Программатор устройств Modbus")
        self.configure(
            background="#171212",
            border=8,
            height=600,
            width=800,
            relief="groove",
        )
        self.resizable(False, False)
        self.option_add("*tearOff", tkinter.FALSE)

        main_menu = Menu()
        main_menu.configure(bg="#008080")
        main_menu.add_cascade(label="Lite", command=self.start_up_frame)
        main_menu.add_cascade(label="Advance")
        main_menu.add_cascade(label="Scan", command=self.start_scan)
        main_menu.configure(bg="#A1ABAA", )
        self.config(menu=main_menu)

    def start_up_frame(self):
        UpFrame()

    def start_scan(self):
        ...


class UpFrame(Frame):
    def __init__(self):
        super().__init__()
        self.new_slave = IntVar()
        self.new_baudrate = IntVar()
        self.new_parity = StringVar()
        self.new_bits = StringVar()
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
        self.lbl_slave = Label(self, text="Адрес устр-ва", )
        self.lbl_slave.config(lbl_conf)
        self.lbl_slave.grid(column=0, row=3)
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

        self.btn_connect = Button(self, text="Прочитать параметры", command=self.get_info_dev)
        self.btn_connect.config(btn_conf)
        self.btn_connect.grid(column=5, row=1,)

        self.btn_set_param_sigma = Button(self, text="Установить парамеры SIGMA", command=self.set_params_sigma)
        self.btn_set_param_sigma.config(btn_conf)
        self.btn_set_param_sigma.grid(column=5, row=2,)

        self.btn_address = Button(self, text="Изменить адрес устройства", command=self.set_address)
        self.btn_address.config(btn_conf)
        self.btn_address.grid(column=5, row=3)

        self.btn_speed = Button(self, text='Установить скорость', command=self.set_speed_dev)
        self.btn_speed.config(btn_conf)
        self.btn_speed.grid(column=5, row=4,)

        self.btn_parity = Button(self, text="Изменение проверки на четность", command=self.set_parity)
        self.btn_parity.config(btn_conf)
        self.btn_parity.grid(column=5, row=5)

        self.btn_stop_bit = Button(self, text="Изменение стоп-бита", command=self.set_stop_bit)
        self.btn_stop_bit.config(btn_conf)
        self.btn_stop_bit.grid(column=5, row=6)

        self.btn_connect_sigma = Button(self, text="----------",)
        self.btn_connect_sigma.config(btn_conf)
        self.btn_connect_sigma.grid(column=5, row=7,)

        self.table = Treeview(
            show="headings",
            selectmode="browse",
            columns=HEADS_TABLE,
            displaycolumns=COLUMNS_TABLE,
        )
        self.table.grid(column=0, row=5, sticky="ew")

    def table_output(self, list_params: tuple) -> None:
        self.table.delete(*self.table.get_children())
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

    def diag_info(self):
        """В разработке, олжна выводить диагностическую информацию в этом или другом фрейме"""
        dev = self.get_conn_params()
        dev.get_diagnostic_info()


    def set_stop_bit(self):
        dev = self.get_conn_params()
        stop_bis = [str(i_s_bits[1]) for i_s_bits in dev.STOP_BITS]
        self.wait_window(DialogEnterNewStopBit(self, self.new_bits, stop_bis))
        dev.set_stop_bit(get_value_stop_bits_dev(dev, self.new_bits.get()), int(self.etr_address.get()))
        self.combobox_bits.set(self.new_bits.get())
        dev = self.get_conn_params()
        self.table_output(dev.get_info(int(self.etr_address.get())))

    def set_parity(self):
        dev = self.get_conn_params()
        parity_dev = [str(i_par[1]) for i_par in dev.VERIFICATION_BITS]
        self.wait_window(DialogEnterNewParity(self, self.new_parity, parity_dev))
        dev.set_parity(get_value_parity_dev(dev, self.new_parity.get()), int(self.etr_address.get()))
        self.combobox_parity.set(self.new_parity.get())
        dev = self.get_conn_params()
        self.table_output(dev.get_info(int(self.etr_address.get())))

    def set_speed_dev(self):
        dev = self.get_conn_params()
        speeds_dev = [str(i_spd[1]) for i_spd in dev.SPEEDS_DEVICE]
        win_change_baudrate = DialogEnterNewBaudrate(self, self.new_baudrate, speeds_dev)
        self.wait_window(win_change_baudrate)
        dev.set_baudrate(get_value_baudrate_dev(dev, self.new_baudrate.get()), int(self.etr_address.get()))
        self.combobox_speed.set(self.new_baudrate.get())
        dev = self.get_conn_params()
        self.table_output(dev.get_info(int(self.etr_address.get())))

    def set_address(self):
        dev = self.get_conn_params()
        win_change_address = DialogEnterNewSlave(self, self.new_slave)
        self.wait_window(win_change_address)
        dev.set_slave(self.new_slave.get(), int(self.etr_address.get()))
        dev = self.get_conn_params()
        self.table_output(dev.get_info(self.new_slave.get()))

    def set_params_sigma(self):
        "Меняем значения по умолчанию на сигму"
        port = get_port(self.combobox_port.get())
        name = self.combobox_type.get()
        win_new_slave = DialogEnterNewSlave(self, self.new_slave)
        self.wait_window(win_new_slave)
        new_slave = self.new_slave.get()
        if check_slave(str(new_slave)) != True:
            msg_err_address()
        dev = get_device(name, port)
        dev.set_slave(new_slave=new_slave, slave=dev.SLAVE)
        time.sleep(0.2)
        dev = get_device(name, port)
        baudrate = get_value_baudrate_dev(dev, BAUDRATE_SIGMA)
        dev.set_baudrate(baudrate, slave=new_slave)
        time.sleep(0.2)
        dev = get_device(name, port, baudrate=BAUDRATE_SIGMA)
        parity = get_value_parity_dev(dev, PARITY_SIGMA)
        dev.set_parity(parity, slave=new_slave)
        time.sleep(0.2)
        dev = get_device(name, port, baudrate=BAUDRATE_SIGMA, parity=PARITY_SIGMA)
        stop_bits = get_value_stop_bits_dev(dev, S_BITS_SIGMA)
        dev.set_stop_bit(stop_bits, slave=new_slave)
        time.sleep(0.2)
        dev = get_device(
            name, port, baudrate=BAUDRATE_SIGMA, parity=PARITY_SIGMA, stopbits=stop_bits)
        self.table_output(dev.get_info(new_slave))

    def get_info_dev(self):
        "Получить информацию об устройстве"
        slave: str = self.etr_address.get()
        dev = self.get_conn_params()
        try:
            if slave != "":
                if check_slave(slave):
                    self.table_output(dev.get_info(int(slave)))
                else:
                    msg_err_address()
                    print("вывод окна с ошибкой")
            else:
                self.table_output(dev.get_info())
        except AttributeError:
            msg_err_no_connect()
        except ValueError:
            msg_err_incorect_params()

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


if __name__ == "__main__":
    app = Root()
    app.mainloop()
