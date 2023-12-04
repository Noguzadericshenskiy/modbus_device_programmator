import sys
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidgetItem
from src.ui_scan import Ui_form_scan
from src.utils import get_ports_info, get_port
from pymodbus.client import ModbusSerialClient
from src.ui_dialogs_win import CustomDialog
from loguru import logger


class Scan(QMainWindow):
    def __init__(self, parent=None):
        super(Scan, self).__init__(parent)
        self.slave_from: int = 0
        self.slave_to: int = 0
        self.ui = Ui_form_scan()
        self.ui.setupUi(self)
        self.com_ports()
        self.ui.pushButton_scan.clicked.connect(self.btn_scan_click)
        self.ui.table_devices.setColumnCount(4)
        self.ui.table_devices.setHorizontalHeaderLabels(["Speed", "slave", "S/bits", "parity"])

    def com_ports(self):
        for i in get_ports_info():
            self.ui.comboBox_com_port.addItem(i[0] + " " + i[1])

    def get_value_checkBox(self):
        "Получить значения всех чекбоксов"
        speeds = []
        s_bits = []
        parity = []

        if self.ui.checkBox_1200.isChecked():
            speeds.append(1200)
        if self.ui.checkBox_2400.isChecked():
            speeds.append(2400)
        if self.ui.checkBox_4800.isChecked():
            speeds.append(4800)
        if self.ui.checkBox_9600.isChecked():
            speeds.append(9600)
        if self.ui.checkBox_14400.isChecked():
            speeds.append(14400)
        if self.ui.checkBox_19200.isChecked():
            speeds.append(19200)
        if self.ui.checkBox_28800.isChecked():
            speeds.append(28800)
        if self.ui.checkBox_38400.isChecked():
            speeds.append(38400)
        if self.ui.checkBox_57600.isChecked():
            speeds.append(57600)
        if self.ui.checkBox_115200.isChecked():
            speeds.append(115200)
        if self.ui.check_box_none.isChecked():
            parity.append("N")
        if self.ui.check_box_even.isChecked():
            parity.append("E")
        if self.ui.check_box_odd.isChecked():
            parity.append("O")
        if self.ui.check_box_sb1.isChecked():
            s_bits.append(1)
        # if self.ui.check_box_sb15.isChecked():
        #     s_bits.append(1.5)
        if self.ui.check_box_sb2.isChecked():
            s_bits.append(2)
        return speeds, s_bits, parity

    def btn_scan_click(self):
        # com_port = get_port(self.ui.comboBox_com_port.currentText())
        # speeds, s_bits, parity = self.get_value_checkBox()
        # slave_from = int(self.ui.etr_slave_from.text())
        # slave_to = int(self.ui.etr_slave_to.text())
        # devices = scan(com_port, speeds, s_bits, parity, slave_from, slave_to)
        # self.output_info(devices)
        self.check_enter()
    #
    # def get_text_slave_from(self, text):
    #     try:
    #         self.slave_from = int(text)
    #     except ValueError:
    #         form = DialogWin()
    #         form.show()
    # def get_text_slave_to(self, text):
    #     try:
    #         self.slave_to = int(text)
    #     except ValueError:
    #         DialogWin()

    def output_info(self, devices_list_info):
        self.ui.table_devices.setRowCount(len(devices_list_info))

        for i_row in range(len(devices_list_info)):
            self.ui.table_devices.setItem(
                i_row, 0, QTableWidgetItem(str(devices_list_info[i_row][0])))
            self.ui.table_devices.setItem(
                i_row, 1, QTableWidgetItem(str(devices_list_info[i_row][1])))
            self.ui.table_devices.setItem(
                i_row, 2, QTableWidgetItem(str(devices_list_info[i_row][2])))
            self.ui.table_devices.setItem(
                i_row, 3, QTableWidgetItem(str(devices_list_info[i_row][3])))

    def check_enter(self):
        fix = CustomDialog()
        fix.show()


def scan(port: str, speeds: list[int], s_bits: list, parity: list, address_from: int, address_to: int):
    device_list = []
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
                    if not client.read_holding_registers(address=0, slave=i_slave).isError():
                        device = (i_baudrate, i_slave, i_bits, i_parity)
                        device_list.append(device)
                    client.close()
    return device_list


if __name__ == "__main__":
    app = QApplication()
    window = Scan()
    window.show()
    # sys.exit(app.exec())
    app.exec()