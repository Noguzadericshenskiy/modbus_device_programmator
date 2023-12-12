import sys
import threading
from PySide6 import QtCore
from PySide6.QtGui import QValidator
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTableWidgetItem,
    QMessageBox,
    QInputDialog,
)
from pymodbus.client import ModbusSerialClient
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
from view.main1 import Ui_MainWindow
from utils import (
    get_device,
    get_ports_info,
    get_port,
    check_slave,
    get_value_baudrate_dev,
    get_value_parity_dev,
    get_value_stop_bits_dev,
)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.slave_from: int = 0
        self.slave_to: int = 0
        self.is_killed = False

        self.com_ports(get_ports_info())
        self.com_ports_scan()
        self.output_devices(LIST_NAMES_DEVICES)
        self.output_s_bitts(BITS)
        self.output_speeds(SPEEDS)
        self.otput_parity(PARITY)
        self.ui.btn_connect.clicked.connect(self.get_info_dev)
        self.ui.btn_speed.clicked.connect(self.set_speed_dev)
        self.ui.btn_address.clicked.connect(self.set_address)
        self.ui.btn_parity.clicked.connect(self.set_parity)
        self.ui.btn_stop_bit.clicked.connect(self.set_stop_bit)
        self.ui.btn_set_param_sigma.clicked.connect(self.set_params_sigma)


        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Параметр", "Значение"])
        self.ui.tableWidget.setColumnWidth(0, 300)
        self.ui.tableWidget.setColumnWidth(1, 280)
        self.ui.progressBar_.setValue(0)
        self.ui.table_devices.setColumnWidth(0, 40)
        self.ui.table_devices.setColumnWidth(1, 110)
        self.ui.pushButton_scan.clicked.connect(self.btn_scan_click)
        # self.ui.pushButton_scan.clicked.connect(self.stop_scan)
        self.ui.pushButton_stop_scan.clicked.connect(self.stop_scan)
        self.ui.etr_slave_from_3.insert("1")
        self.ui.etr_slave_to_3.insert("10")

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

    def otput_parity(self, parity_list):
        for parity in parity_list:
            self.ui.combobox_parity.addItem(parity)

    def output_s_bitts(self, s_bits_list):
        for s_bit in s_bits_list:
            self.ui.combobox_bits.addItem(s_bit)

    def get_conn_params(self):
        "Получить информацию для соединения"
        port: str = get_port(self.ui.combobox_port.currentText())
        name: str = self.ui.combobox_type.currentText()
        speed: str = self.ui.combobox_speed.currentText()
        parity: str = self.ui.combobox_parity.currentText()
        bits: str = self.ui.combobox_bits.currentText()
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

    def get_info_dev(self):
        "Получить информацию об устройстве"
        slave: str = self.ui.etr_address.text()
        dev = self.get_conn_params()
        try:
            if slave != "":
                if check_slave(slave):
                    self.table_output(dev.get_info(int(slave)))
                    dev.close()
                else:
                    QMessageBox.critical(
                        self,
                        "Кривой ввод",
                        "Не верно введен адрес устройства"
                    )
            else:
                self.table_output(dev.get_info())

        except AttributeError:
            dev.close()
            QMessageBox.critical(self, "Error connect",
                                 "Не удалось подключиться к устройству, проверьте настройки подключения")
        except ValueError:
            dev.close()
            QMessageBox.critical(self, "Error incorrect params2",
                                 "Не верные данные для подключения")
        except ConnectionException:
            dev.close()
            QMessageBox.critical(self, "Error incorrect params3",
                                 "Не верные данные для подключения")
        except IndexError:
            dev.close()
            QMessageBox.critical(self, "Error incorrect param4",
                                 "Не верно выбрано устройство для подклюения или его параметры")

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
        new_slave, ok = QInputDialog.getInt(
            self,
            "Изменение адреса устройства",
            "Введите ноый адрес.\nАдрес должен быть числом от 1 до 255 включительно.",
            minValue=1,
            maxValue=255,
        )
        if new_slave and ok:
            dev = get_device(name, port)
            dev.set_slave(new_slave, dev.SLAVE)
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

    def set_stop_bit(self):
        dev = self.get_conn_params()
        stop_bis = [str(i_s_bits[1]) for i_s_bits in dev.STOP_BITS]
        slave = int(self.ui.etr_address.text())
        value, ok = QInputDialog.getItem(
            self,
            "Изменение стоп бит",
            "Выберите число стоп бит",
            stop_bis,
            0,
            False
        )
        if ok and value:
            dev.set_stop_bit(get_value_stop_bits_dev(dev, value), slave)
            self.ui.combobox_bits.setCurrentText(value)
            dev = self.get_conn_params()
            self.table_output(dev.get_info(slave))

    def set_parity(self):
        dev = self.get_conn_params()
        slave = int(self.ui.etr_address.text())
        parity_dev = [str(i_par[1]) for i_par in dev.VERIFICATION_BITS]
        value, ok = QInputDialog.getItem(
            self,
            "Изменение проверки четности",
            "Выберите проверку четности",
            parity_dev,
            0,
            False
        )
        if ok and value:
            dev.set_parity(get_value_parity_dev(dev, value), slave)
            self.ui.combobox_parity.setCurrentText(value)
            dev = self.get_conn_params()
            self.table_output(dev.get_info(slave))

    def set_speed_dev(self, sp):
        dev = self.get_conn_params()
        speeds_dev = [str(i_spd[1]) for i_spd in dev.SPEEDS_DEVICE]
        value, ok = QInputDialog.getItem(
            self,
            "Изменение скорости",
            "Выберите скорость из списка:",
            speeds_dev,
            0,
            False
        )
        if ok and value:
            dev.set_baudrate(get_value_baudrate_dev(dev, int(value)), int(self.ui.etr_address.text()))
            self.ui.combobox_speed.setCurrentText(value)
            dev = self.get_conn_params()
            self.table_output(dev.get_info(int(self.ui.etr_address.text())))

    def set_address(self):
        dev = self.get_conn_params()
        value, ok = QInputDialog.getInt(
            self,
            "Изменение адреса устройства",
            "Введите ноый адрес.\nАдрес должен быть числом от 1 до 255 включительно.",
            minValue=1,
            maxValue=255,

        )
        if ok:
            dev.set_slave(int(value), int(self.ui.etr_address.text()))
            dev = self.get_conn_params()
            self.table_output(dev.get_info(int(value)))

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
        return speeds, s_bits, parity

    def btn_scan_click(self):
        self.is_killed = False

        try:
            com_port = get_port(self.ui.comboBox_com_port.currentText())
            speeds, s_bits, parity = self.get_value_checkBox()
            slave_from: str = self.ui.etr_slave_from_3.text()
            slave_to: str = self.ui.etr_slave_to_3.text()

            if self.check_enter(slave_from, slave_to):
                self.scan(com_port, speeds, s_bits, parity, int(slave_from), int(slave_to))
            else:
                QMessageBox.critical(
                    self,
                    "Кривой ввод!",
                    "Лошадь копытом вводит лучше! \nАдрес может быть только числом от 1 до 255",
                    buttons=QMessageBox.Discard,
                    defaultButton=QMessageBox.Discard,
                )
        except (ConnectionException, FileNotFoundError):
            QMessageBox.critical(
                self,
                "Кривой ввод!",
                "А порт лошадь будет указывать? \nНеобходимо выбрать СОМ порт!",
                buttons=QMessageBox.Discard,
                defaultButton=QMessageBox.Discard,
            )

    def check_enter(self, data1: str, data2: str):
        if data1.isdigit() and data2.isdigit():
            d1 = int(data1)
            d2 = int(data2)
            if (0 < d1 <= 255) and (0 < d2 <= 255) and (d1 <= d2):
                return True
        return False

    def scan(self, port: str, speeds: list[int], s_bits: list, parity: list, address_from: int, address_to: int):
        count_iter = len(speeds) * len(s_bits) * len(parity) * (address_to - address_from)
        self.ui.progressBar_.setMaximum(count_iter)
        self.ui.table_devices.clear()
        self.ui.pushButton_scan.setText("и шо мы ждем? ")
        self.ui.pushButton_scan.setStyleSheet('pushButton_scan {background-color: #A3C1DA; color: red;}')
        count = 0
        count_table = 0

        for i_bits in s_bits:
            for i_parity in parity:
                for i_baudrate in speeds:
                    for i_slave in range(address_from, address_to+1):
                        client = ModbusSerialClient(
                            port=port,
                            baudrate=i_baudrate,
                            parity=i_parity,
                            stopbits=i_bits,
                            timeout=0.02
                        )
                        count += 1
                        self.ui.progressBar_.setValue(count)
                        if self.is_killed:
                            break
                        if not client.read_holding_registers(address=0, slave=i_slave).isError():
                            self.ui.table_devices.setRowCount(count_table + 1)
                            self.ui.table_devices.setItem(
                                count_table,
                                0,
                                QTableWidgetItem(str(i_slave)))
                            self.ui.table_devices.setItem(
                                count_table,
                                1,
                                QTableWidgetItem(f'{i_baudrate} {i_bits} {i_parity} '))
                            self.ui.table_devices.executeDelayedItemsLayout()
                            count_table += 1

                        client.close()
                        QApplication.processEvents()
        self.ui.pushButton_scan.setText("Start")

    def stop_scan(self):
        self.ui.pushButton_scan.setText("Start")
        self.is_killed = True


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    # app.exec()
