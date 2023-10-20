#ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный
# ИП535-07еа-RS
import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb


class SignalingDeviceIP53_507EA_RS(Client_mb):
    """
    ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный ИП535-07еа-RS
    (протокол Modbus RTU)
    Руководство по эксплуатации
    4371-006-43082497-04-04 РЭ, 2021 г.
    """
    SPEEDS_DEVICE = (
        (1, 1200),
        (2, 2400),
        (3, 4800),
        (4, 9600),
        (5, 14400),
        (6, 19200),
        (7, 28800),
        (8, 38400),
        (9, 57600),
        (10, 115200)
    )
    VERIFICATION_BITS = ((1, "N"), (2, "E"), (3, "O"))
    STATUS = (
        (1, "Загрузка"),
        (2, "Тест"),
        (3, "Норма"),
        (4, "Требование квитирования"),
        (5, "Сработал"),
        (6, "Неисправность")
    )
    NAME = "ИП535-07еа-RS"
    SPEED_DEFAULT = SPEEDS_DEVICE[5][1]
    AV_VERIFICATION_BIT = VERIFICATION_BITS[1][1]
    NUMS_STOP_BIT = 1
    SLAVE = 1

    def __init__(
            self,
            port,
            baudrate=SPEED_DEFAULT,
            parity=AV_VERIFICATION_BIT,
            stopbits=NUMS_STOP_BIT
    ):
          Client_mb.__init__(
            self,
            port=port,
            baudrate=baudrate,
            stopbits=stopbits,
            parity=parity,
            framer=pymodbus.framer.ModbusRtuFramer,
            timeout=0.05
        )

    def conn_dev(self):
        self.get_info()

    def discon(self):
        ...


    def get_info(self, slave=SLAVE) -> dict:
        params = dict()
        params["Адрес устройства"] = self.read_holding_registers(address=0, slave=slave).registers
        params["Скорость интерфейса"] = self.SPEEDS_DEVICE[
            self.read_holding_registers(address=1, slave=slave).registers[0] - 1]
        params["Проверочный бит"] = self.VERIFICATION_BITS[
            self.read_holding_registers(address=2, slave=slave).registers[0] - 1]
        params["Количество стоп битов"] = self.read_holding_registers(address=3, slave=slave).registers[0]
        params["Идентификатор устройства"] = self.read_holding_registers(address=4, slave=slave).registers[0]
        params["Версия устройства"] = self.read_holding_registers(address=6, slave=slave).registers[0]
        params["Версия ПО устройства"] = self.read_holding_registers(address=7, slave=slave).registers[0]
        params["Серийный номер"] = self.read_holding_registers(address=8, slave=slave).registers[0]
        params["Состояние устройства"] = self.STATUS[
            self.read_holding_registers(address=10, slave=slave).registers[0] - 1]
        self.close()
        return params

    def set_params_sigma(self, new_slave):
        self.write_registers(slave=self.SPEED_DEFAULT, address=0, values=new_slave)

    def set_slave(self, slave, new_slave):
        self.write_registers(slave=slave, address=0, values=new_slave)

    def clear_status(self):
        self.write_registers(address=12, values=4, slave=1)
        self.close()
        # self.get_info()






