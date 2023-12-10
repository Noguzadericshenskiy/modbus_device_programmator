from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidgetItem, QMessageBox
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ConnectionException
from PySide6.QtCore import QCoreApplication
from src.view.main_view import Ui_MainWindow
import time


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonbase.clicked.connect(self.btn_etr)
        self.ui.labelbase.setText("fdfdfdfdfdfdf")

    def btn_etr(self):
        for i in range(10):
            self.ui.labelbase.setText("fffff")

            time.sleep(1)
            self.ui.labelbase.setText(str(i))
            print(i)



if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    # sys.exit(app.exec())
    app.exec()
