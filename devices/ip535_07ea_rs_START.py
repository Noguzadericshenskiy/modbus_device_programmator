#ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный
# ИП535-07еа-RS-“ПУСК”:
import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb


class SignalingDeviceStart(Client_mb):
    """
    ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный ИП535-07еа-RS-“ПУСК”:
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
    NAME = "ИП535-07еа-RS-ПУСК"
    SPEED_DEFAULT = SPEEDS_DEVICE[6][1]
    AV_VERIFICATION_BIT = VERIFICATION_BITS[1][1]
    NUMS_STOP_BIT = 1