from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QTableWidgetItem,
    QMessageBox,
    QDialogButtonBox,
    QInputDialog,
    QComboBox,
)
from pymodbus.exceptions import ConnectionException

from src.view.base_view import Ui_form_base
from src.config import LIST_NAMES_DEVICES, BITS, PARITY, SPEEDS, BAUDRATE_SIGMA, PARITY_SIGMA, S_BITS_SIGMA
from src.utils import (
    get_device,
    get_ports_info,
    get_port,
    check_slave,
    get_value_baudrate_dev,
    get_value_parity_dev,
    get_value_stop_bits_dev,
)


class Basic(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowTitle("Программатор устройств Modbus")
        self.ui = Ui_form_base()
        self.ui.setupUi(self)
        self.com_ports(get_ports_info())
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
        self.ui.tableWidget.setColumnWidth(0, 250)
        self.ui.tableWidget.setColumnWidth(1, 120)


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
            # time.sleep(0.2)
        dev = get_device(name, port)
        baudrate: int = get_value_baudrate_dev(dev, BAUDRATE_SIGMA)
        dev.set_baudrate(baudrate, new_slave)
        # time.sleep(0.2)
        dev = get_device(name, port, baudrate=BAUDRATE_SIGMA)
        parity = get_value_parity_dev(dev, PARITY_SIGMA)
        dev.set_parity(parity, slave=new_slave)
        # time.sleep(0.2)
        dev = get_device(name, port, baudrate=BAUDRATE_SIGMA, parity=PARITY_SIGMA)
        stop_bits = get_value_stop_bits_dev(dev, S_BITS_SIGMA)
        dev.set_stop_bit(stop_bits, slave=new_slave)
         # time.sleep(0.2)
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
            # self.ui.etr_address.setText(int(value))


if __name__ == "__main__":
    app = QApplication()
    window = Basic()
    window.show()
    # sys.exit(app.exec())
    app.exec()
