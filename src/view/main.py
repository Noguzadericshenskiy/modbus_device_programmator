# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win_v_2_3.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(650, 447)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tab_widget_main = QTabWidget(self.centralwidget)
        self.tab_widget_main.setObjectName(u"tab_widget_main")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget_main.sizePolicy().hasHeightForWidth())
        self.tab_widget_main.setSizePolicy(sizePolicy)
        self.tab_widget_main.setStyleSheet(u"QTabWidget {\n"
"	border-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 1px solid rgb(0, 83, 122);\n"
"	border-top: 1px solid rgb(0, 83, 122);\n"
"	border-right: 1px solid rgb(0, 50, 74);	\n"
"	border-bottom: 1px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"")
        self.tab_widget_main.setTabShape(QTabWidget.Triangular)
        self.tab_base = QWidget()
        self.tab_base.setObjectName(u"tab_base")
        self.gridLayout_2 = QGridLayout(self.tab_base)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.base_central_left_frame = QFrame(self.tab_base)
        self.base_central_left_frame.setObjectName(u"base_central_left_frame")
        self.base_central_left_frame.setFrameShape(QFrame.StyledPanel)
        self.base_central_left_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.base_central_left_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 0)
        self.combobox_bits = QComboBox(self.base_central_left_frame)
        self.combobox_bits.setObjectName(u"combobox_bits")
        self.combobox_bits.setMinimumSize(QSize(70, 0))
        font = QFont()
        font.setPointSize(10)
        self.combobox_bits.setFont(font)
        self.combobox_bits.setCursor(QCursor(Qt.PointingHandCursor))
        self.combobox_bits.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")

        self.gridLayout_4.addWidget(self.combobox_bits, 4, 1, 1, 1)

        self.btn_address = QPushButton(self.base_central_left_frame)
        self.btn_address.setObjectName(u"btn_address")
        self.btn_address.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_address.sizePolicy().hasHeightForWidth())
        self.btn_address.setSizePolicy(sizePolicy1)
        self.btn_address.setMinimumSize(QSize(200, 0))
        self.btn_address.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setKerning(True)
        self.btn_address.setFont(font1)
        self.btn_address.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_address.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_address, 0, 2, 1, 1)

        self.combobox_speed = QComboBox(self.base_central_left_frame)
        self.combobox_speed.setObjectName(u"combobox_speed")
        self.combobox_speed.setMinimumSize(QSize(70, 0))
        self.combobox_speed.setFont(font)
        self.combobox_speed.setCursor(QCursor(Qt.PointingHandCursor))
        self.combobox_speed.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")

        self.gridLayout_4.addWidget(self.combobox_speed, 1, 1, 1, 1)

        self.btn_speed = QPushButton(self.base_central_left_frame)
        self.btn_speed.setObjectName(u"btn_speed")
        sizePolicy1.setHeightForWidth(self.btn_speed.sizePolicy().hasHeightForWidth())
        self.btn_speed.setSizePolicy(sizePolicy1)
        self.btn_speed.setMinimumSize(QSize(200, 0))
        self.btn_speed.setMaximumSize(QSize(200, 16777215))
        self.btn_speed.setFont(font)
        self.btn_speed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_speed.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_speed, 1, 2, 1, 1)

        self.combobox_parity = QComboBox(self.base_central_left_frame)
        self.combobox_parity.setObjectName(u"combobox_parity")
        self.combobox_parity.setMinimumSize(QSize(70, 0))
        self.combobox_parity.setFont(font)
        self.combobox_parity.setCursor(QCursor(Qt.PointingHandCursor))
        self.combobox_parity.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")

        self.gridLayout_4.addWidget(self.combobox_parity, 3, 1, 1, 1)

        self.btn_stop_bit = QPushButton(self.base_central_left_frame)
        self.btn_stop_bit.setObjectName(u"btn_stop_bit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(200)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_stop_bit.sizePolicy().hasHeightForWidth())
        self.btn_stop_bit.setSizePolicy(sizePolicy2)
        self.btn_stop_bit.setMinimumSize(QSize(200, 0))
        self.btn_stop_bit.setFont(font)
        self.btn_stop_bit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop_bit.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_stop_bit, 4, 2, 1, 1)

        self.lbl_stop_bit = QLabel(self.base_central_left_frame)
        self.lbl_stop_bit.setObjectName(u"lbl_stop_bit")
        self.lbl_stop_bit.setMinimumSize(QSize(100, 20))
        self.lbl_stop_bit.setMaximumSize(QSize(0, 0))
        self.lbl_stop_bit.setFont(font)

        self.gridLayout_4.addWidget(self.lbl_stop_bit, 4, 0, 1, 1)

        self.btn_parity = QPushButton(self.base_central_left_frame)
        self.btn_parity.setObjectName(u"btn_parity")
        self.btn_parity.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_parity.sizePolicy().hasHeightForWidth())
        self.btn_parity.setSizePolicy(sizePolicy3)
        self.btn_parity.setMinimumSize(QSize(200, 0))
        self.btn_parity.setMaximumSize(QSize(200, 16777215))
        self.btn_parity.setFont(font)
        self.btn_parity.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_parity.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_parity, 3, 2, 1, 1)

        self.lbl_slave = QLabel(self.base_central_left_frame)
        self.lbl_slave.setObjectName(u"lbl_slave")
        self.lbl_slave.setMinimumSize(QSize(100, 20))
        self.lbl_slave.setMaximumSize(QSize(43, 16777215))
        self.lbl_slave.setFont(font)

        self.gridLayout_4.addWidget(self.lbl_slave, 0, 0, 1, 1)

        self.etr_address = QLineEdit(self.base_central_left_frame)
        self.etr_address.setObjectName(u"etr_address")
        self.etr_address.setMinimumSize(QSize(70, 0))
        self.etr_address.setFont(font)
        self.etr_address.setContextMenuPolicy(Qt.NoContextMenu)
        self.etr_address.setStyleSheet(u"QLineEdit {\n"
"border: 1px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")

        self.gridLayout_4.addWidget(self.etr_address, 0, 1, 1, 1)

        self.lbl_speed = QLabel(self.base_central_left_frame)
        self.lbl_speed.setObjectName(u"lbl_speed")
        self.lbl_speed.setMinimumSize(QSize(100, 20))
        self.lbl_speed.setMaximumSize(QSize(43, 16777215))
        self.lbl_speed.setFont(font)

        self.gridLayout_4.addWidget(self.lbl_speed, 1, 0, 1, 1)

        self.lbl_parity = QLabel(self.base_central_left_frame)
        self.lbl_parity.setObjectName(u"lbl_parity")
        self.lbl_parity.setMinimumSize(QSize(100, 20))
        self.lbl_parity.setMaximumSize(QSize(0, 0))
        self.lbl_parity.setFont(font)
        self.lbl_parity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lbl_parity, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.base_central_left_frame, 1, 0, 1, 1)

        self.base_central_right_frame = QFrame(self.tab_base)
        self.base_central_right_frame.setObjectName(u"base_central_right_frame")
        self.base_central_right_frame.setFrameShape(QFrame.StyledPanel)
        self.base_central_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.base_central_right_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.btn_set_param_sigma = QPushButton(self.base_central_right_frame)
        self.btn_set_param_sigma.setObjectName(u"btn_set_param_sigma")
        self.btn_set_param_sigma.setMinimumSize(QSize(200, 50))
        self.btn_set_param_sigma.setFont(font)
        self.btn_set_param_sigma.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_set_param_sigma.setContextMenuPolicy(Qt.NoContextMenu)
        self.btn_set_param_sigma.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_set_param_sigma)

        self.btn_connect = QPushButton(self.base_central_right_frame)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMinimumSize(QSize(200, 50))
        self.btn_connect.setFont(font)
        self.btn_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connect.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(125, 125, 93);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(152, 152, 114);\n"
"	border-top: 2px solid rgb(152, 152, 114);\n"
"	border-right: 2px solid rgb(84, 84, 84);	\n"
"	border-bottom: 2px solid rgb(84, 84, 84);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(148, 148, 110);\n"
"	border-left: 2px solid rgb(152, 152, 114);\n"
"	border-top: 2px solid rgb(152, 152, 114);\n"
"	border-right: 2px solid rgb(84, 84, 84);	\n"
"	border-bottom: 2px solid rgb(84, 84, 84);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(112, 112, 83);\n"
"	border-left: 2px solid rgb(84, 84, 84);\n"
"	border-top: 2px solid rgb(84, 84, 84);\n"
"	border-right: 2px solid rgb(152, 152, 114);	\n"
"	border-bottom: 2px solid rgb(152, 152, 114);\n"
"}\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_connect)


        self.gridLayout_2.addWidget(self.base_central_right_frame, 1, 1, 1, 1)

        self.base_body_frame = QFrame(self.tab_base)
        self.base_body_frame.setObjectName(u"base_body_frame")
        self.base_body_frame.setFrameShape(QFrame.StyledPanel)
        self.base_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.base_body_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 20, 10, 5)
        self.tableWidget = QTableWidget(self.base_body_frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 200))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"	background-color: rgb(0, 0, 127);\n"
"	color: rgb(85, 255, 0);\n"
"	font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"\n"
"}\n"
"")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(250)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.gridLayout_2.addWidget(self.base_body_frame, 2, 0, 1, 2)

        self.base_header_frame = QFrame(self.tab_base)
        self.base_header_frame.setObjectName(u"base_header_frame")
        self.base_header_frame.setFrameShape(QFrame.StyledPanel)
        self.base_header_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.base_header_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 5)
        self.lbl_type = QLabel(self.base_header_frame)
        self.lbl_type.setObjectName(u"lbl_type")
        self.lbl_type.setMinimumSize(QSize(100, 20))
        self.lbl_type.setMaximumSize(QSize(43, 16777215))
        self.lbl_type.setFont(font)

        self.gridLayout_3.addWidget(self.lbl_type, 2, 0, 1, 1)

        self.lbl_port = QLabel(self.base_header_frame)
        self.lbl_port.setObjectName(u"lbl_port")
        self.lbl_port.setMinimumSize(QSize(100, 20))
        self.lbl_port.setMaximumSize(QSize(71, 16777215))
        self.lbl_port.setFont(font)

        self.gridLayout_3.addWidget(self.lbl_port, 0, 0, 1, 1)

        self.combobox_type = QComboBox(self.base_header_frame)
        self.combobox_type.setObjectName(u"combobox_type")
        self.combobox_type.setFont(font)
        self.combobox_type.setCursor(QCursor(Qt.PointingHandCursor))
        self.combobox_type.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")

        self.gridLayout_3.addWidget(self.combobox_type, 2, 1, 1, 1)

        self.combobox_port = QComboBox(self.base_header_frame)
        self.combobox_port.setObjectName(u"combobox_port")
        self.combobox_port.setFont(font)
        self.combobox_port.setCursor(QCursor(Qt.PointingHandCursor))
        self.combobox_port.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")

        self.gridLayout_3.addWidget(self.combobox_port, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.base_header_frame, 0, 0, 1, 2)

        self.tab_widget_main.addTab(self.tab_base, "")
        self.tab_scan = QWidget()
        self.tab_scan.setObjectName(u"tab_scan")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_scan)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_5 = QFrame(self.tab_scan)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(10, 10, 10, 10)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.groupBox_parity = QGroupBox(self.frame_7)
        self.groupBox_parity.setObjectName(u"groupBox_parity")
        self.groupBox_parity.setMinimumSize(QSize(0, 90))
        self.check_box_none_3 = QCheckBox(self.groupBox_parity)
        self.check_box_none_3.setObjectName(u"check_box_none_3")
        self.check_box_none_3.setGeometry(QRect(10, 20, 62, 17))
        self.check_box_none_3.setChecked(True)
        self.check_box_none_3.setAutoRepeat(False)
        self.check_box_none_3.setAutoExclusive(False)
        self.check_box_none_3.setTristate(False)
        self.check_box_even_3 = QCheckBox(self.groupBox_parity)
        self.check_box_even_3.setObjectName(u"check_box_even_3")
        self.check_box_even_3.setGeometry(QRect(10, 40, 62, 17))
        self.check_box_odd_3 = QCheckBox(self.groupBox_parity)
        self.check_box_odd_3.setObjectName(u"check_box_odd_3")
        self.check_box_odd_3.setGeometry(QRect(10, 60, 62, 17))

        self.gridLayout_5.addWidget(self.groupBox_parity, 1, 0, 1, 1)

        self.group_box_slave = QGroupBox(self.frame_7)
        self.group_box_slave.setObjectName(u"group_box_slave")
        self.group_box_slave.setMinimumSize(QSize(220, 60))
        font2 = QFont()
        font2.setBold(True)
        self.group_box_slave.setFont(font2)
        self.horizontalLayout_2 = QHBoxLayout(self.group_box_slave)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_from_3 = QLabel(self.group_box_slave)
        self.lbl_from_3.setObjectName(u"lbl_from_3")
        font3 = QFont()
        font3.setBold(False)
        self.lbl_from_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.lbl_from_3)

        self.etr_slave_from_3 = QLineEdit(self.group_box_slave)
        self.etr_slave_from_3.setObjectName(u"etr_slave_from_3")
        self.etr_slave_from_3.setFont(font3)
        self.etr_slave_from_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.etr_slave_from_3.setStyleSheet(u"QLineEdit {\n"
"border: 1px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.etr_slave_from_3)

        self.lbl_to_3 = QLabel(self.group_box_slave)
        self.lbl_to_3.setObjectName(u"lbl_to_3")
        self.lbl_to_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.lbl_to_3)

        self.etr_slave_to_3 = QLineEdit(self.group_box_slave)
        self.etr_slave_to_3.setObjectName(u"etr_slave_to_3")
        self.etr_slave_to_3.setFont(font3)
        self.etr_slave_to_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.etr_slave_to_3.setStyleSheet(u"QLineEdit {\n"
"border: 1px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.etr_slave_to_3)


        self.gridLayout_5.addWidget(self.group_box_slave, 0, 0, 1, 2)

        self.groupBox_speeds = QGroupBox(self.frame_7)
        self.groupBox_speeds.setObjectName(u"groupBox_speeds")
        self.groupBox_speeds.setMinimumSize(QSize(95, 230))
        self.checkBox_1202 = QCheckBox(self.groupBox_speeds)
        self.checkBox_1202.setObjectName(u"checkBox_1202")
        self.checkBox_1202.setGeometry(QRect(10, 20, 62, 17))
        self.checkBox_2402 = QCheckBox(self.groupBox_speeds)
        self.checkBox_2402.setObjectName(u"checkBox_2402")
        self.checkBox_2402.setGeometry(QRect(10, 40, 62, 17))
        self.checkBox_4802 = QCheckBox(self.groupBox_speeds)
        self.checkBox_4802.setObjectName(u"checkBox_4802")
        self.checkBox_4802.setGeometry(QRect(10, 60, 62, 17))
        self.checkBox_9602 = QCheckBox(self.groupBox_speeds)
        self.checkBox_9602.setObjectName(u"checkBox_9602")
        self.checkBox_9602.setGeometry(QRect(10, 80, 62, 17))
        self.checkBox_9602.setChecked(True)
        self.checkBox_14402 = QCheckBox(self.groupBox_speeds)
        self.checkBox_14402.setObjectName(u"checkBox_14402")
        self.checkBox_14402.setGeometry(QRect(10, 100, 62, 17))
        self.checkBox_19202 = QCheckBox(self.groupBox_speeds)
        self.checkBox_19202.setObjectName(u"checkBox_19202")
        self.checkBox_19202.setGeometry(QRect(10, 120, 62, 17))
        self.checkBox_28802 = QCheckBox(self.groupBox_speeds)
        self.checkBox_28802.setObjectName(u"checkBox_28802")
        self.checkBox_28802.setGeometry(QRect(10, 140, 62, 17))
        self.checkBox_38402 = QCheckBox(self.groupBox_speeds)
        self.checkBox_38402.setObjectName(u"checkBox_38402")
        self.checkBox_38402.setGeometry(QRect(10, 160, 62, 17))
        self.checkBox_57602 = QCheckBox(self.groupBox_speeds)
        self.checkBox_57602.setObjectName(u"checkBox_57602")
        self.checkBox_57602.setGeometry(QRect(10, 180, 62, 17))
        self.checkBox_115202 = QCheckBox(self.groupBox_speeds)
        self.checkBox_115202.setObjectName(u"checkBox_115202")
        self.checkBox_115202.setGeometry(QRect(10, 200, 62, 17))

        self.gridLayout_5.addWidget(self.groupBox_speeds, 0, 2, 4, 1)

        self.groupBox_s_bits = QGroupBox(self.frame_7)
        self.groupBox_s_bits.setObjectName(u"groupBox_s_bits")
        self.groupBox_s_bits.setMinimumSize(QSize(80, 0))
        self.check_box_sb1_3 = QCheckBox(self.groupBox_s_bits)
        self.check_box_sb1_3.setObjectName(u"check_box_sb1_3")
        self.check_box_sb1_3.setGeometry(QRect(10, 20, 62, 17))
        self.check_box_sb1_3.setChecked(True)
        self.check_box_sb2_3 = QCheckBox(self.groupBox_s_bits)
        self.check_box_sb2_3.setObjectName(u"check_box_sb2_3")
        self.check_box_sb2_3.setGeometry(QRect(10, 40, 62, 17))

        self.gridLayout_5.addWidget(self.groupBox_s_bits, 1, 1, 1, 1)

        self.pushButton_stop_scan = QPushButton(self.frame_7)
        self.pushButton_stop_scan.setObjectName(u"pushButton_stop_scan")
        sizePolicy1.setHeightForWidth(self.pushButton_stop_scan.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_scan.setSizePolicy(sizePolicy1)
        self.pushButton_stop_scan.setMinimumSize(QSize(81, 81))
        font4 = QFont()
        font4.setFamilies([u"Georgia"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.pushButton_stop_scan.setFont(font4)
        self.pushButton_stop_scan.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(240, 85, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 108, 35);\n"
"	border-top: 2px solid rgb(255, 108, 35);\n"
"	border-right: 2px solid rgb(255, 108, 35);	\n"
"	border-bottom: 2px solid rgb(255, 108, 35);\n"
"	font: 75 10pt \"Georgia\";\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(230, 85, 0);\n"
"	border-left: 2px solid rgb(230, 85, 0);\n"
"	border-top: 2px solid rgb(230, 85, 0);\n"
"	border-right: 2px solid rgb(230, 85, 0);	\n"
"	border-bottom: 2px solid rgb(230, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(250, 85, 0);\n"
"	border-left: 2px solid rgb(180, 60, 0);\n"
"	border-top: 2px solid rgb(180, 60, 0);\n"
"	border-right: 2px solid rgb(180, 60, 0);	\n"
"	border-bottom: 2px solid rgb(180, 60, 0);\n"
"}")

        self.gridLayout_5.addWidget(self.pushButton_stop_scan, 2, 1, 1, 1)

        self.pushButton_scan = QPushButton(self.frame_7)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        sizePolicy1.setHeightForWidth(self.pushButton_scan.sizePolicy().hasHeightForWidth())
        self.pushButton_scan.setSizePolicy(sizePolicy1)
        self.pushButton_scan.setMinimumSize(QSize(121, 81))
        font5 = QFont()
        font5.setFamilies([u"Georgia"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setStrikeOut(False)
        self.pushButton_scan.setFont(font5)
        self.pushButton_scan.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 180, 0);\n"
"	border-top: 2px solid rgb(0, 180, 0);\n"
"	border-right: 2px solid rgb(0, 180, 0);	\n"
"	border-bottom: 2px solid rgb(0, 180, 0);\n"
"	font: 75 10pt \"Georgia\";\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 160, 0);\n"
"	border-left: 2px solid rgb(0, 160, 0);\n"
"	border-top: 2px solid rgb(0, 160, 0);\n"
"	border-right: 2px solid rgb(0, 160, 0);	\n"
"	border-bottom: 2px solid rgb(0, 160, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 180, 0);\n"
"	border-left: 2px solid rgb(0, 130, 0);\n"
"	border-top: 2px solid rgb(0, 130, 0);\n"
"	border-right: 2px solid rgb(0, 130, 0);	\n"
"	border-bottom: 2px solid rgb(0, 130, 0);\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_scan, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_7, 1, 0, 3, 1)

        self.scan_mb_top_frame = QFrame(self.frame_5)
        self.scan_mb_top_frame.setObjectName(u"scan_mb_top_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scan_mb_top_frame.sizePolicy().hasHeightForWidth())
        self.scan_mb_top_frame.setSizePolicy(sizePolicy5)
        self.scan_mb_top_frame.setFrameShape(QFrame.StyledPanel)
        self.scan_mb_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.scan_mb_top_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.com_port = QLabel(self.scan_mb_top_frame)
        self.com_port.setObjectName(u"com_port")
        self.com_port.setMinimumSize(QSize(100, 0))
        self.com_port.setFont(font2)
        self.com_port.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout.addWidget(self.com_port)

        self.comboBox_com_port = QComboBox(self.scan_mb_top_frame)
        self.comboBox_com_port.setObjectName(u"comboBox_com_port")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.comboBox_com_port.sizePolicy().hasHeightForWidth())
        self.comboBox_com_port.setSizePolicy(sizePolicy6)
        self.comboBox_com_port.setContextMenuPolicy(Qt.NoContextMenu)
        self.comboBox_com_port.setStyleSheet(u"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);")

        self.horizontalLayout.addWidget(self.comboBox_com_port)


        self.gridLayout_6.addWidget(self.scan_mb_top_frame, 0, 0, 1, 4)

        self.progressBar_ = QProgressBar(self.frame_5)
        self.progressBar_.setObjectName(u"progressBar_")
        font6 = QFont()
        font6.setPointSize(8)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setKerning(True)
        self.progressBar_.setFont(font6)
        self.progressBar_.setStyleSheet(u"QProgressBar {\n"
"	color:rgb(0, 0, 0);\n"
"	background-color: rgb(0, 61, 89);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	\n"
"}\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(0, 255, 0);\n"
"		\n"
"}\n"
"\n"
"\n"
"")
        self.progressBar_.setValue(0)

        self.gridLayout_6.addWidget(self.progressBar_, 4, 3, 1, 1)

        self.table_devices = QTableWidget(self.frame_5)
        if (self.table_devices.columnCount() < 2):
            self.table_devices.setColumnCount(2)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setBackground(QColor(0, 85, 127));
        __qtablewidgetitem4.setForeground(brush);
        self.table_devices.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignHCenter|Qt.AlignBottom);
        __qtablewidgetitem5.setBackground(QColor(0, 85, 127));
        __qtablewidgetitem5.setForeground(brush);
        self.table_devices.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.table_devices.setObjectName(u"table_devices")
        self.table_devices.setEnabled(True)
        sizePolicy.setHeightForWidth(self.table_devices.sizePolicy().hasHeightForWidth())
        self.table_devices.setSizePolicy(sizePolicy)
        self.table_devices.setMinimumSize(QSize(200, 0))
        palette = QPalette()
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.table_devices.setPalette(palette)
        self.table_devices.setContextMenuPolicy(Qt.NoContextMenu)
        self.table_devices.setStyleSheet(u"QTableWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 8pt \"Terminal\";\n"
"}\n"
"")
        self.table_devices.setFrameShape(QFrame.StyledPanel)
        self.table_devices.setColumnCount(2)
        self.table_devices.horizontalHeader().setVisible(False)
        self.table_devices.horizontalHeader().setCascadingSectionResizes(True)
        self.table_devices.horizontalHeader().setMinimumSectionSize(90)
        self.table_devices.horizontalHeader().setDefaultSectionSize(90)
        self.table_devices.horizontalHeader().setHighlightSections(True)
        self.table_devices.horizontalHeader().setStretchLastSection(True)
        self.table_devices.verticalHeader().setVisible(False)
        self.table_devices.verticalHeader().setDefaultSectionSize(23)
        self.table_devices.verticalHeader().setProperty("showSortIndicator", False)

        self.gridLayout_6.addWidget(self.table_devices, 1, 3, 3, 1)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.tab_widget_main.addTab(self.tab_scan, "")
        self.tab_dcon_scan = QWidget()
        self.tab_dcon_scan.setObjectName(u"tab_dcon_scan")
        self.frame = QFrame(self.tab_dcon_scan)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 240, 621, 231))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox_device_dcon = QGroupBox(self.frame)
        self.groupBox_device_dcon.setObjectName(u"groupBox_device_dcon")
        self.groupBox_device_dcon.setGeometry(QRect(20, 10, 601, 191))
        self.label_command_dcon = QLabel(self.groupBox_device_dcon)
        self.label_command_dcon.setObjectName(u"label_command_dcon")
        self.label_command_dcon.setGeometry(QRect(10, 20, 43, 13))
        self.lineEdit_command_dcon = QLineEdit(self.groupBox_device_dcon)
        self.lineEdit_command_dcon.setObjectName(u"lineEdit_command_dcon")
        self.lineEdit_command_dcon.setGeometry(QRect(60, 20, 113, 20))
        self.lineEdit_command_dcon.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_command_dcon.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Terminal\";")
        self.btn_send_command_dcon = QPushButton(self.groupBox_device_dcon)
        self.btn_send_command_dcon.setObjectName(u"btn_send_command_dcon")
        self.btn_send_command_dcon.setGeometry(QRect(190, 20, 181, 20))
        self.btn_send_command_dcon.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.btn_change_protocol_dcon = QPushButton(self.groupBox_device_dcon)
        self.btn_change_protocol_dcon.setObjectName(u"btn_change_protocol_dcon")
        self.btn_change_protocol_dcon.setGeometry(QRect(400, 20, 191, 20))
        self.btn_change_protocol_dcon.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.table_info_dev_dcon = QTableWidget(self.groupBox_device_dcon)
        self.table_info_dev_dcon.setObjectName(u"table_info_dev_dcon")
        self.table_info_dev_dcon.setGeometry(QRect(10, 70, 251, 101))
        self.table_info_dev_dcon.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_info_dcon = QLabel(self.groupBox_device_dcon)
        self.label_info_dcon.setObjectName(u"label_info_dcon")
        self.label_info_dcon.setGeometry(QRect(10, 50, 43, 13))
        self.frame_3 = QFrame(self.tab_dcon_scan)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 641, 231))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(490, 20, 151, 201))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_devices_dcon = QLabel(self.frame_2)
        self.label_devices_dcon.setObjectName(u"label_devices_dcon")

        self.verticalLayout.addWidget(self.label_devices_dcon)

        self.table_devices_dcon = QTableWidget(self.frame_2)
        self.table_devices_dcon.setObjectName(u"table_devices_dcon")
        self.table_devices_dcon.setContextMenuPolicy(Qt.NoContextMenu)
        self.table_devices_dcon.setStyleSheet(u"background-color: rgb(0, 0, 79);\n"
"color: rgb(0, 255, 0);")

        self.verticalLayout.addWidget(self.table_devices_dcon)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 10, 471, 211))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.groupBox_parameters_dcon = QGroupBox(self.frame_4)
        self.groupBox_parameters_dcon.setObjectName(u"groupBox_parameters_dcon")
        self.groupBox_parameters_dcon.setGeometry(QRect(20, 10, 431, 191))
        self.groupBox_parameters_dcon.setStyleSheet(u"")
        self.comboBox_com_port_dcon = QComboBox(self.groupBox_parameters_dcon)
        self.comboBox_com_port_dcon.setObjectName(u"comboBox_com_port_dcon")
        self.comboBox_com_port_dcon.setGeometry(QRect(80, 20, 331, 22))
        self.comboBox_com_port_dcon.setContextMenuPolicy(Qt.NoContextMenu)
        self.comboBox_com_port_dcon.setStyleSheet(u"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);")
        self.label = QLabel(self.groupBox_parameters_dcon)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 43, 13))
        self.groupBox_address_dcon = QGroupBox(self.groupBox_parameters_dcon)
        self.groupBox_address_dcon.setObjectName(u"groupBox_address_dcon")
        self.groupBox_address_dcon.setGeometry(QRect(160, 50, 231, 51))
        self.lineEdit_to_dcon = QLineEdit(self.groupBox_address_dcon)
        self.lineEdit_to_dcon.setObjectName(u"lineEdit_to_dcon")
        self.lineEdit_to_dcon.setGeometry(QRect(150, 20, 61, 20))
        self.lineEdit_to_dcon.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_to_dcon.setStyleSheet(u"QLineEdit {\n"
"border: 1px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}")
        self.lineEdit_from_dcon = QLineEdit(self.groupBox_address_dcon)
        self.lineEdit_from_dcon.setObjectName(u"lineEdit_from_dcon")
        self.lineEdit_from_dcon.setGeometry(QRect(40, 20, 61, 19))
        self.lineEdit_from_dcon.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_from_dcon.setStyleSheet(u"QLineEdit {\n"
"border: 1px solid rgb(255, 255, 255);\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}")
        self.label_from_dcon = QLabel(self.groupBox_address_dcon)
        self.label_from_dcon.setObjectName(u"label_from_dcon")
        self.label_from_dcon.setGeometry(QRect(10, 20, 21, 16))
        self.label_to_dcon = QLabel(self.groupBox_address_dcon)
        self.label_to_dcon.setObjectName(u"label_to_dcon")
        self.label_to_dcon.setGeometry(QRect(120, 20, 21, 16))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_parameters_dcon)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 60, 135, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_speed_dcon = QLabel(self.gridLayoutWidget_2)
        self.label_speed_dcon.setObjectName(u"label_speed_dcon")

        self.gridLayout.addWidget(self.label_speed_dcon, 0, 0, 1, 1)

        self.label_s_bits_dcon = QLabel(self.gridLayoutWidget_2)
        self.label_s_bits_dcon.setObjectName(u"label_s_bits_dcon")

        self.gridLayout.addWidget(self.label_s_bits_dcon, 2, 0, 1, 1)

        self.label_parity_dcon = QLabel(self.gridLayoutWidget_2)
        self.label_parity_dcon.setObjectName(u"label_parity_dcon")

        self.gridLayout.addWidget(self.label_parity_dcon, 1, 0, 1, 1)

        self.comboBox_speed_dcon = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_speed_dcon.setObjectName(u"comboBox_speed_dcon")
        self.comboBox_speed_dcon.setContextMenuPolicy(Qt.NoContextMenu)
        self.comboBox_speed_dcon.setStyleSheet(u"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);")

        self.gridLayout.addWidget(self.comboBox_speed_dcon, 0, 1, 1, 1)

        self.comboBox_parity_dcon = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_parity_dcon.setObjectName(u"comboBox_parity_dcon")
        self.comboBox_parity_dcon.setContextMenuPolicy(Qt.NoContextMenu)
        self.comboBox_parity_dcon.setStyleSheet(u"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);")

        self.gridLayout.addWidget(self.comboBox_parity_dcon, 1, 1, 1, 1)

        self.comboBox_s_bit_dcon = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_s_bit_dcon.setObjectName(u"comboBox_s_bit_dcon")
        self.comboBox_s_bit_dcon.setContextMenuPolicy(Qt.NoContextMenu)
        self.comboBox_s_bit_dcon.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}")

        self.gridLayout.addWidget(self.comboBox_s_bit_dcon, 2, 1, 1, 1)

        self.btn_start_dcon = QPushButton(self.groupBox_parameters_dcon)
        self.btn_start_dcon.setObjectName(u"btn_start_dcon")
        self.btn_start_dcon.setGeometry(QRect(180, 110, 91, 41))
        sizePolicy6.setHeightForWidth(self.btn_start_dcon.sizePolicy().hasHeightForWidth())
        self.btn_start_dcon.setSizePolicy(sizePolicy6)
        self.btn_start_dcon.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 180, 0);\n"
"	border-top: 2px solid rgb(0, 180, 0);\n"
"	border-right: 2px solid rgb(0, 180, 0);	\n"
"	border-bottom: 2px solid rgb(0, 180, 0);\n"
"	font: 75 10pt \"Georgia\";\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 160, 0);\n"
"	border-left: 2px solid rgb(0, 160, 0);\n"
"	border-top: 2px solid rgb(0, 160, 0);\n"
"	border-right: 2px solid rgb(0, 160, 0);	\n"
"	border-bottom: 2px solid rgb(0, 160, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 180, 0);\n"
"	border-left: 2px solid rgb(0, 130, 0);\n"
"	border-top: 2px solid rgb(0, 130, 0);\n"
"	border-right: 2px solid rgb(0, 130, 0);	\n"
"	border-bottom: 2px solid rgb(0, 130, 0);\n"
"}\n"
"")
        self.btn_stop_dcon = QPushButton(self.groupBox_parameters_dcon)
        self.btn_stop_dcon.setObjectName(u"btn_stop_dcon")
        self.btn_stop_dcon.setGeometry(QRect(280, 110, 91, 41))
        self.btn_stop_dcon.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(240, 85, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 108, 35);\n"
"	border-top: 2px solid rgb(255, 108, 35);\n"
"	border-right: 2px solid rgb(255, 108, 35);	\n"
"	border-bottom: 2px solid rgb(255, 108, 35);\n"
"	font: 75 10pt \"Georgia\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(230, 85, 0);\n"
"	border-left: 2px solid rgb(230, 85, 0);\n"
"	border-top: 2px solid rgb(230, 85, 0);\n"
"	border-right: 2px solid rgb(230, 85, 0);	\n"
"	border-bottom: 2px solid rgb(230, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(250, 85, 0);\n"
"	border-left: 2px solid rgb(180, 60, 0);\n"
"	border-top: 2px solid rgb(180, 60, 0);\n"
"	border-right: 2px solid rgb(180, 60, 0);	\n"
"	border-bottom: 2px solid rgb(180, 60, 0);\n"
"}")
        self.tab_widget_main.addTab(self.tab_dcon_scan, "")

        self.verticalLayout_4.addWidget(self.tab_widget_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_widget_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.combobox_bits.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u043e\u043f \u0431\u0438\u0442</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_address.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0430\u0434\u0440\u0435\u0441 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
#if QT_CONFIG(tooltip)
        self.combobox_speed.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_speed.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.combobox_parity.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0440\u043e\u0432\u0435\u043a\u0440\u043a\u0430 \u043d\u0430 \u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_stop_bit.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c Stop bits", None))
        self.lbl_stop_bit.setText(QCoreApplication.translate("MainWindow", u"Stop bits", None))
        self.btn_parity.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443 \u043d\u0430 \u0447\u0451\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.lbl_slave.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u0443\u0441\u0442\u0440-\u0432\u0430", None))
#if QT_CONFIG(tooltip)
        self.etr_address.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0410\u0434\u0440\u0435\u0441 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_speed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.lbl_parity.setText(QCoreApplication.translate("MainWindow", u"Parity", None))
#if QT_CONFIG(tooltip)
        self.btn_set_param_sigma.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0418\u0437\u043c\u0435\u043d\u0438\u0442 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430 \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435:</p><p>\u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c - 9600, \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0447\u0435\u0442\u043d\u043e\u0441\u0442\u0438 - N, \u0421\u0442\u043e\u043f \u0431\u0438\u0442 - 1.</p><p>\u0412\u043e \u0432\u0441\u043f\u043b\u044b\u0432\u0430\u044e\u0449\u0435\u043c \u043e\u043a\u043d\u0435 \u043d\u0443\u0436\u043d\u043e \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 </p><p>\u0444\u0434\u0440\u0435\u0441 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430.</p><p>\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e, \u0442\u043e\u043b\u044c\u043a\u043e \u043d\u0430 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0435"
                        " </p><p>\u0441 \u0437\u0430\u0432\u043e\u0434\u0441\u043a\u0438\u043c\u0438 \u043f\u0430\u0440\u043c\u0435\u0442\u0440\u0430\u043c\u0438.</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_set_param_sigma.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b Sigma", None))
#if QT_CONFIG(tooltip)
        self.btn_connect.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e\u0431 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0435</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u04461", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u04302", None));
        self.lbl_type.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
        self.lbl_port.setText(QCoreApplication.translate("MainWindow", u"COM Port", None))
#if QT_CONFIG(tooltip)
        self.combobox_type.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e \u0434\u043b\u044f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.combobox_port.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u041e\u041c \u043f\u043e\u0440\u0442 \u0434\u043b\u044f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0443</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_base), QCoreApplication.translate("MainWindow", u"Base", None))
        self.groupBox_parity.setTitle(QCoreApplication.translate("MainWindow", u"Parity", None))
        self.check_box_none_3.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.check_box_even_3.setText(QCoreApplication.translate("MainWindow", u"Even", None))
        self.check_box_odd_3.setText(QCoreApplication.translate("MainWindow", u"Odd", None))
        self.group_box_slave.setTitle(QCoreApplication.translate("MainWindow", u"Slave", None))
        self.lbl_from_3.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.etr_slave_from_3.setInputMask("")
        self.etr_slave_from_3.setText("")
        self.lbl_to_3.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.etr_slave_to_3.setInputMask("")
        self.etr_slave_to_3.setText("")
        self.groupBox_speeds.setTitle(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.checkBox_1202.setText(QCoreApplication.translate("MainWindow", u"1200", None))
        self.checkBox_2402.setText(QCoreApplication.translate("MainWindow", u"2400", None))
        self.checkBox_4802.setText(QCoreApplication.translate("MainWindow", u"4800", None))
        self.checkBox_9602.setText(QCoreApplication.translate("MainWindow", u"9600", None))
        self.checkBox_14402.setText(QCoreApplication.translate("MainWindow", u"14400", None))
        self.checkBox_19202.setText(QCoreApplication.translate("MainWindow", u"19200", None))
        self.checkBox_28802.setText(QCoreApplication.translate("MainWindow", u"28800", None))
        self.checkBox_38402.setText(QCoreApplication.translate("MainWindow", u"38400", None))
        self.checkBox_57602.setText(QCoreApplication.translate("MainWindow", u"57600", None))
        self.checkBox_115202.setText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.groupBox_s_bits.setTitle(QCoreApplication.translate("MainWindow", u"Stop Bits", None))
        self.check_box_sb1_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.check_box_sb2_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_stop_scan.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_scan.setText(QCoreApplication.translate("MainWindow", u"Start Scan", None))
        self.com_port.setText(QCoreApplication.translate("MainWindow", u"COM Port", None))
        ___qtablewidgetitem4 = self.table_devices.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Slave", None));
        ___qtablewidgetitem5 = self.table_devices.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"speed, s/bits, parity", None));
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_scan), QCoreApplication.translate("MainWindow", u"ModBus Scan", None))
        self.groupBox_device_dcon.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
        self.label_command_dcon.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0430", None))
        self.btn_send_command_dcon.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u043c\u0430\u043d\u0434\u0443 \u043d\u0430 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
        self.btn_change_protocol_dcon.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u043d\u0430 MODBUS", None))
        self.label_info_dcon.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0434", None))
        self.label_devices_dcon.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.groupBox_parameters_dcon.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f DCON", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"COM Port", None))
        self.groupBox_address_dcon.setTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.label_from_dcon.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442", None))
        self.label_to_dcon.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e", None))
        self.label_speed_dcon.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.label_s_bits_dcon.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f \u0431\u0438\u0442\u044b", None))
        self.label_parity_dcon.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0438\u0442\u0435\u0442", None))
        self.btn_start_dcon.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.btn_stop_dcon.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_dcon_scan), QCoreApplication.translate("MainWindow", u"DCON Scan", None))
    # retranslateUi

