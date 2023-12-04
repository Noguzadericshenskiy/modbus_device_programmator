import sys
from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QDialogButtonBox, QLabel


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Кривой ввод данных!")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
