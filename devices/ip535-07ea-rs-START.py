#ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный
# ИП535-07еа-RS-“ПУСК”:

class SignalingDeviceStart:
    """
    ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный ИП535-07еа-RS-“ПУСК”:
    (протокол Modbus RTU)
    Руководство по эксплуатации
    4371-006-43082497-04-04 РЭ, 2021 г.
    """
    id: int = 1
    name: str = "ИП535-07еа-RS-“ПУСК”"
    protocol_version: int = 2
    device_version: int = 1
    po_version: str = 3
    serial_number: str
    status_device: str
    configuration: str