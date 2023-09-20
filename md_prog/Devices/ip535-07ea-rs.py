#ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный
# ИП535-07еа-RS

class SignalingDevice:
    """
    ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный ИП535-07еа-RS
    (протокол Modbus RTU)
    Руководство по эксплуатации
    4371-006-43082497-04-04 РЭ, 2021 г.
    """
    id: int = 1
    protocol_version: int = 2
    device_version: int = 3
    po_version: str = 3
    serial_number: str
    status_device: str
    configuration: str
