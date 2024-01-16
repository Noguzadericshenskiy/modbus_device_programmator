import sys

from serial import SerialException
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTableWidgetItem,
)
from pymodbus.exceptions import ConnectionException

from config import (
    LIST_NAMES_DEVICES,
    BITS,
    PARITY,
    SPEEDS,
    BAUDRATE_SIGMA,
    PARITY_SIGMA,
    S_BITS_SIGMA
)
from view.main_view import Ui_MainWindow
from utils import (
    get_device,
    get_ports_info,
    get_port,
    get_value_baudrate_dev,
    get_value_parity_dev,
    get_value_stop_bits_dev,
    nls_change_protocol_mb,
    nls_change_protocol_dcon,
    send_decon_command,
    device_dcon,
    device_mb,
)
from src.dialogues import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_killed = False

        self.com_ports(get_ports_info())
        self.com_ports_scan()
        self.output_devices(LIST_NAMES_DEVICES)
        self.output_s_bitts(BITS)
        self.output_speeds(SPEEDS)
        self.output_parity(PARITY)
        self.com_ports_dcon()
        self.output_speeds_dcon(SPEEDS)
        self.output_parity_dcon(PARITY)
        self.output_s_bits_dcon(BITS)
        self.ui.btn_connect.clicked.connect(self.get_info_dev)
        self.ui.btn_speed.clicked.connect(self.changing_speed)
        self.ui.btn_address.clicked.connect(self.changing_address)
        self.ui.btn_parity.clicked.connect(self.changing_parity)
        self.ui.btn_stop_bit.clicked.connect(self.changing_stop_bit)
        self.ui.btn_set_param_sigma.clicked.connect(self.set_params_sigma)

        self.ui.btn_start_scan.clicked.connect(self.btn_scan_click)
        self.ui.btn_stop_scan.clicked.connect(self.stop_scan)

        self.ui.btn_chenge_protocol_on_dcon.clicked.connect(self.change_protokol_nls_dcon)
        self.ui.btn_change_protocol_on_modbus.clicked.connect(self.change_protokol_nls_mb)
        self.ui.btn_send_command_dcon.clicked.connect(self.send_command_dcon)
        self.ui.etr_command_dcon.returnPressed.connect(self.send_command_dcon)

    def com_ports(self, value):
        for i in value:
            self.ui.combobox_port.addItem(i[0] + " " + i[1])

    def output_devices(self, value):
        for dev in value:
            self.ui.combobox_type.addItem(dev)

    def output_speeds(self, speeds):
        for speed in speeds:
            self.ui.combobox_speed.addItem(str(speed))
        self.ui.combobox_speed.setCurrentText("9600")

    def output_parity(self, parity_list):
        for parity in parity_list:
            self.ui.combobox_parity.addItem(parity)

    def output_s_bitts(self, s_bits_list):
        for s_bit in s_bits_list:
            self.ui.combobox_bits.addItem(s_bit)

    def get_conn_params(self):
        "Получить информацию для соединения"
        port: str = get_port(self.ui.combobox_port.currentText())
        name: str = self.ui.combobox_type.currentText()
        speed: int = int(self.ui.combobox_speed.currentText())
        parity: str = self.ui.combobox_parity.currentText()
        bits: int = int(self.ui.combobox_bits.currentText())
        return get_device(name=name, port=port, baudrate=speed, parity=parity, stopbits=bits)

    def get_info_dev(self):
        "Получить информацию об устройстве"
        self.ui.tableWidget.clear()
        slave: int = self.ui. spinBox_address.value()
        dev = self.get_conn_params()
        try:
            self.table_output(dev.get_info(slave))

        except (AttributeError, TypeError):
            QMessageBox.critical(self, "Error connect",
                                 "Не удалось подключиться к устройству, проверьте настройки подключения")
        except ValueError:
            QMessageBox.critical(self, "Error incorrect params",
                                 "Не верные данные для подключения")
        except ConnectionException:
            QMessageBox.critical(self, "Error incorrect params",
                                 "Не верные данные для подключения")
        except IndexError:
            QMessageBox.critical(self, "Error incorrect param",
                                 "Не верно выбрано устройство для подключения или его параметры")
        finally:
            dev.close()

    def table_output(self, list_params: tuple) -> None:
        self.ui.tableWidget.setRowCount(len(list_params))
        for i_row in range(len(list_params)):
            self.ui.tableWidget.setItem(
                i_row, 0, QTableWidgetItem(list_params[i_row][0]))
            self.ui.tableWidget.setItem(
                i_row, 1, QTableWidgetItem(str(list_params[i_row][1])))

    def set_params_sigma(self):
        "Меняем значения по умолчанию на сигму"
        port: str = get_port(self.ui.combobox_port.currentText())
        name: str = self.ui.combobox_type.currentText()
        new_slave, flag = dialog_address(self)
        try:
            if flag:
                dev = get_device(name, port)
                dev.set_slave(new_slave, dev.SLAVE)
            self.ui.spinBox_address.setValue(new_slave)
            dev = get_device(name, port)
            baudrate: int = get_value_baudrate_dev(dev, BAUDRATE_SIGMA)
            dev.set_baudrate(baudrate, new_slave)
            dev = get_device(name, port, baudrate=BAUDRATE_SIGMA)
            parity = get_value_parity_dev(dev, PARITY_SIGMA)
            dev.set_parity(parity, slave=new_slave)
            dev = get_device(name, port, baudrate=BAUDRATE_SIGMA, parity=PARITY_SIGMA)
            stop_bits = get_value_stop_bits_dev(dev, S_BITS_SIGMA)
            dev.set_stop_bit(stop_bits, slave=new_slave)
            dev = get_device(
                name, port, baudrate=BAUDRATE_SIGMA, parity=PARITY_SIGMA, stopbits=stop_bits)
            self.table_output(dev.get_info(new_slave))

        except (ValueError, AttributeError):
            err_connect(self)

    def changing_stop_bit(self):
        dev = self.get_conn_params()
        stop_bits = [str(i_s_bits[1]) for i_s_bits in dev.STOP_BITS]
        slave: int = self.ui.spinBox_address.value()
        value, flag = dialog_s_bits(self, stop_bits)
        try:
            if flag:
                dev.set_stop_bit(get_value_stop_bits_dev(dev, value), slave)
                self.ui.combobox_bits.setCurrentText(value)
                dev = self.get_conn_params()
                self.table_output(dev.get_info(slave))

        except (ValueError, AttributeError):
            err_connect(self)

    def changing_parity(self):
        dev = self.get_conn_params()
        slave = self.ui.spinBox_address.value()
        parity_dev = [str(i_par[1]) for i_par in dev.VERIFICATION_BITS]
        value, flag = dialog_parity(self, parity_dev)
        try:
            if flag:
                dev.set_parity(get_value_parity_dev(dev, value), slave)
                self.ui.combobox_parity.setCurrentText(value)
                dev = self.get_conn_params()
                self.table_output(dev.get_info(slave))

        except (ValueError, AttributeError):
            err_connect(self)

    def changing_speed(self):
        dev = self.get_conn_params()
        speeds_dev = [str(i_spd[1]) for i_spd in dev.SPEEDS_DEVICE]
        value, flag = dialog_speed(self, speeds_dev)
        try:
            if flag:
                dev.set_baudrate(get_value_baudrate_dev(dev, int(value)), self.ui.spinBox_address.value())
                self.ui.combobox_speed.setCurrentText(value)
                dev = self.get_conn_params()
                self.table_output(dev.get_info(self.ui.spinBox_address.value()))

        except (ValueError, AttributeError):
            err_connect(self)

    def changing_address(self):
        dev = self.get_conn_params()
        value, flag = dialog_address(self)
        try:
            if flag:
                dev.set_slave(value, self.ui.spinBox_address.value())
                self.ui.spinBox_address.setValue(value)
                dev = self.get_conn_params()
                self.table_output(dev.get_info(value))

        except (ValueError, AttributeError):
            err_connect(self)

# scan modbus ==========================================================
    def com_ports_scan(self):
        for i in get_ports_info():
            self.ui.comboBox_com_port.addItem(i[0] + " " + i[1])

    def get_value_checkBox(self):
        "Получить значения всех чекбоксов"
        speeds = []
        s_bits = []
        parity = []

        if self.ui.checkBox_1202.isChecked():
            speeds.append(1200)
        if self.ui.checkBox_2402.isChecked():
            speeds.append(2400)
        if self.ui.checkBox_4802.isChecked():
            speeds.append(4800)
        if self.ui.checkBox_9602.isChecked():
            speeds.append(9600)
        if self.ui.checkBox_14402.isChecked():
            speeds.append(14400)
        if self.ui.checkBox_19202.isChecked():
            speeds.append(19200)
        if self.ui.checkBox_28802.isChecked():
            speeds.append(28800)
        if self.ui.checkBox_38402.isChecked():
            speeds.append(38400)
        if self.ui.checkBox_57602.isChecked():
            speeds.append(57600)
        if self.ui.checkBox_115202.isChecked():
            speeds.append(115200)
        if self.ui.check_box_none_3.isChecked():
            parity.append("N")
        if self.ui.check_box_even_3.isChecked():
            parity.append("E")
        if self.ui.check_box_odd_3.isChecked():
            parity.append("O")
        if self.ui.check_box_sb1_3.isChecked():
            s_bits.append(1)
        if self.ui.check_box_sb2_3.isChecked():
            s_bits.append(2)

        if len(speeds) == 0 or len(s_bits) == 0 or len(parity) == 0:
            raise ValueError
        return speeds, s_bits, parity

    def btn_scan_click(self):
        self.is_killed = False

        try:
            com_port = get_port(self.ui.comboBox_com_port.currentText())
            speeds, s_bits, parity = self.get_value_checkBox()
            slave_from: int = self.ui.spinBox_from_scan.value()
            slave_to: int = self.ui.spinBox_to_scan.value()

            if slave_from <= slave_to:
                self.scan(com_port, speeds, s_bits, parity, slave_from, slave_to)
            else:
                err_address_scan(self)

        except (SerialException, ConnectionException):
            err_port(self)
        except ValueError:
            err_params(self)

    def scan(self, port: str, speeds: list[int], s_bits: list, parity: list, address_from: int, address_to: int):
        count_iter = len(speeds) * len(s_bits) * len(parity) * (address_to - address_from)
        self.ui.progressBar_.setMaximum(count_iter)
        self.ui.table_devices.clear()
        self.ui.table_devices.setRowCount(0)
        self.ui.btn_start_scan.setText("Ожидайте")
        count = 0

        if self.ui.radioButton_madbus.isChecked():
            flag_protokol = True
        else:
            flag_protokol = False

        for i_bits in s_bits:
            for i_parity in parity:
                for i_baudrate in speeds:
                    for i_slave in range(address_from, address_to+1):
                        if self.is_killed:
                            break

                        count += 1
                        self.ui.progressBar_.setValue(count)
                        if not flag_protokol:
                            ans = device_dcon(port, i_slave, i_baudrate, i_parity, i_bits)
                            if ans:
                                self.out_info_scan(i_slave, i_baudrate, i_parity, i_bits)
                        else:
                            ans = device_mb(port, i_slave, i_baudrate, i_parity, i_bits)
                            if ans:
                                self.out_info_scan(i_slave, i_baudrate, i_parity, i_bits)

                        QApplication.processEvents()
        self.ui.btn_start_scan.setText("Start")

    def out_info_scan(self, slave, baudrate, parity, bits):
        count = self.ui.table_devices.rowCount()
        self.ui.table_devices.setRowCount(count + 1)
        self.ui.table_devices.setItem(count, 0, QTableWidgetItem(f'{slave} ({baudrate} {parity} {bits})'))
        self.ui.table_devices.executeDelayedItemsLayout()

    def stop_scan(self):
        self.ui.btn_start_scan.setText("Start")
        self.is_killed = True

# dcon scan ==========================================================
    def com_ports_dcon(self):
        for i in get_ports_info():
            self.ui.comboBox_com_port_dcon.addItem(i[0] + " " + i[1])

    def output_speeds_dcon(self, speeds):
        for speed in speeds:
            self.ui.comboBox_speed_dcon.addItem(str(speed))
        self.ui.comboBox_speed_dcon.setCurrentText("9600")

    def output_parity_dcon(self, parity_list):
        for parity in parity_list:
            self.ui.comboBox_parity_dcon.addItem(parity)

    def output_s_bits_dcon(self, s_bits_list):
        for s_bit in s_bits_list:
            self.ui.comboBox_s_bit_dcon.addItem(s_bit)

    def get_params_dcon(self):
        address: int = self.ui.spinBox_address_dcon.value()
        port: str = get_port(self.ui.comboBox_com_port_dcon.currentText())
        speed: int = int(self.ui.comboBox_speed_dcon.currentText())
        parity: str = self.ui.comboBox_parity_dcon.currentText()
        s_bits: int = int(self.ui.comboBox_s_bit_dcon.currentText())
        return address, port, speed, parity, s_bits

    def change_protokol_nls_dcon(self):
        address, port, speed, parity, s_bits = self.get_params_dcon()
        try:
            nls_change_protocol_dcon(address, port, speed, parity, s_bits)
            info_restart_device(self)

        except ConnectionException:
            err_port(self)
        except ValueError:
            err_connect(self)

    def change_protokol_nls_mb(self):
        address, port, speed, parity, s_bits = self.get_params_dcon()
        count = self.ui.table_out_info_dcon.rowCount()
        try:
            answer = nls_change_protocol_mb(address, port, speed, parity, s_bits)
            self.ui.table_out_info_dcon.setRowCount(count + 1)
            self.ui.table_out_info_dcon.setItem(count, 0, QTableWidgetItem(answer))
            self.ui.table_out_info_dcon.executeDelayedItemsLayout()
            info_restart_device(self)

        except SerialException:
            err_port(self)
        except ValueError:
            err_connect(self)

    def send_command_dcon(self) -> None:
        command: bytes = (self.ui.etr_command_dcon.text() + "\r").encode("ASCII")
        address, port, speed, parity, s_bits = self.get_params_dcon()
        count = self.ui.table_out_info_dcon.rowCount()
        try:
            answer = send_decon_command(command, address, port, speed, parity, s_bits)
            self.ui.table_out_info_dcon.setRowCount(count + 1)
            self.ui.table_out_info_dcon.setItem(count, 0, QTableWidgetItem("-> " + command.decode("ASCII")))
            count = self.ui.table_out_info_dcon.rowCount()
            self.ui.table_out_info_dcon.executeDelayedItemsLayout()
            self.ui.table_out_info_dcon.setRowCount(count + 1)
            self.ui.table_out_info_dcon.setItem(count, 0, QTableWidgetItem("<- " + answer))
            self.ui.table_out_info_dcon.executeDelayedItemsLayout()

        except SerialException:
            err_port(self)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    # app.exec()
