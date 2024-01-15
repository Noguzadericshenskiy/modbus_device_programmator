from PySide6.QtWidgets import (
    QMessageBox,
    QInputDialog,
)


def err_port(parent):
    QMessageBox.critical(parent,
        "Error COM port",
        "Не верно указан порт для подключения!",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )

def err_connect(parent):
    QMessageBox.critical(parent,
        "Error connect",
        "Не верно указаны параметры для подключения!",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )


def err_address_scan(parent):
    QMessageBox.critical(
        parent,
        "Error!",
        "Адрес начала сканирования должен быть\n"
        "меньше или равен конечному адресу\n",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )

def err_params(parent):
    QMessageBox.critical(parent,
        "Error parameters",
        "Не верно указаны параметры!",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )


def info_restart_device(parent):
    QMessageBox.information(
        parent,
        "Перезагрузите устройство",
        "Для применения настроек перезагрузите \nустройство, отключив питание.",
        buttons=QMessageBox.Ok
    )


def dialog_address(parent) -> tuple[int, bool]:
    value, ok = QInputDialog.getInt(
        parent,
        "Изменение адреса устройства",
        "Введите новаый адрес.\nАдрес, должен быть числом от 1 до 247 включительно.",
        minValue=1,
        maxValue=247,
    )
    return value, ok


def dialog_speed(parent, speeds) -> tuple[str, bool]:
    value, ok = QInputDialog.getItem(
        parent,
        "Изменение скорости",
        "Выберите скорость из списка:",
        speeds,
        0,
        False
    )
    return value, ok


def dialog_parity(parent, parity: list) -> tuple[str, bool]:
    value, ok = QInputDialog.getItem(
        parent,
        "Изменение проверки четности",
        "Выберите проверку четности",
        parity,
        0,
        False
    )
    return value, ok


def dialog_s_bits(parent, s_bits: list)-> tuple[str, bool]:
    value, ok = QInputDialog.getItem(
        parent,
        "Изменение стоп бит",
        "Выберите количество стоп бит",
        s_bits,
        0,
        False
    )
    return value, ok
