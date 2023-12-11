from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(677, 521)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.tabWidget_main = QTabWidget(self.centralwidget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        self.tabWidget_main.setGeometry(QRect(0, 0, 681, 501))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_main.sizePolicy().hasHeightForWidth())
        self.tabWidget_main.setSizePolicy(sizePolicy)
        self.tabWidget_main.setTabShape(QTabWidget.Triangular)
        self.tab_base = QWidget()
        self.tab_base.setObjectName(u"tab_base")
        self.frame_base = QFrame(self.tab_base)
        self.frame_base.setObjectName(u"frame_base")
        self.frame_base.setGeometry(QRect(0, 0, 791, 531))
        self.frame_base.setFrameShape(QFrame.StyledPanel)
        self.frame_base.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_base)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 210, 601, 231))
        self.btn_set_param_sigma = QPushButton(self.frame_base)
        self.btn_set_param_sigma.setObjectName(u"btn_set_param_sigma")
        self.btn_set_param_sigma.setGeometry(QRect(420, 80, 191, 51))
        font = QFont()
        font.setPointSize(10)
        self.btn_set_param_sigma.setFont(font)
        self.etr_address = QLineEdit(self.frame_base)
        self.etr_address.setObjectName(u"etr_address")
        self.etr_address.setGeometry(QRect(120, 80, 81, 20))
        self.etr_address.setFont(font)
        self.lbl_port = QLabel(self.frame_base)
        self.lbl_port.setObjectName(u"lbl_port")
        self.lbl_port.setGeometry(QRect(20, 20, 70, 21))
        self.lbl_port.setMinimumSize(QSize(60, 20))
        self.lbl_port.setMaximumSize(QSize(71, 16777215))
        self.lbl_port.setFont(font)
        self.combobox_bits = QComboBox(self.frame_base)
        self.combobox_bits.setObjectName(u"combobox_bits")
        self.combobox_bits.setGeometry(QRect(120, 170, 81, 22))
        self.combobox_bits.setFont(font)
        self.lbl_parity = QLabel(self.frame_base)
        self.lbl_parity.setObjectName(u"lbl_parity")
        self.lbl_parity.setGeometry(QRect(20, 140, 70, 20))
        self.lbl_parity.setMinimumSize(QSize(70, 20))
        self.lbl_parity.setMaximumSize(QSize(0, 0))
        self.lbl_parity.setFont(font)
        self.btn_address = QPushButton(self.frame_base)
        self.btn_address.setObjectName(u"btn_address")
        self.btn_address.setGeometry(QRect(240, 80, 171, 21))
        self.btn_address.setFont(font)
        self.btn_parity = QPushButton(self.frame_base)
        self.btn_parity.setObjectName(u"btn_parity")
        self.btn_parity.setGeometry(QRect(240, 140, 171, 21))
        self.btn_parity.setFont(font)
        self.lbl_stop_bit = QLabel(self.frame_base)
        self.lbl_stop_bit.setObjectName(u"lbl_stop_bit")
        self.lbl_stop_bit.setGeometry(QRect(20, 170, 70, 20))
        self.lbl_stop_bit.setMinimumSize(QSize(70, 20))
        self.lbl_stop_bit.setMaximumSize(QSize(0, 0))
        self.lbl_stop_bit.setFont(font)
        self.combobox_type = QComboBox(self.frame_base)
        self.combobox_type.setObjectName(u"combobox_type")
        self.combobox_type.setGeometry(QRect(120, 50, 291, 22))
        self.combobox_type.setFont(font)
        self.combobox_port = QComboBox(self.frame_base)
        self.combobox_port.setObjectName(u"combobox_port")
        self.combobox_port.setGeometry(QRect(120, 20, 291, 22))
        self.combobox_port.setFont(font)
        self.combobox_speed = QComboBox(self.frame_base)
        self.combobox_speed.setObjectName(u"combobox_speed")
        self.combobox_speed.setGeometry(QRect(120, 110, 81, 22))
        self.combobox_speed.setFont(font)
        self.btn_connect = QPushButton(self.frame_base)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setGeometry(QRect(420, 140, 191, 51))
        self.btn_connect.setFont(font)
        self.btn_stop_bit = QPushButton(self.frame_base)
        self.btn_stop_bit.setObjectName(u"btn_stop_bit")
        self.btn_stop_bit.setGeometry(QRect(240, 170, 171, 21))
        self.btn_stop_bit.setFont(font)
        self.lbl_speed = QLabel(self.frame_base)
        self.lbl_speed.setObjectName(u"lbl_speed")
        self.lbl_speed.setGeometry(QRect(20, 100, 70, 34))
        self.lbl_speed.setMinimumSize(QSize(70, 20))
        self.lbl_speed.setMaximumSize(QSize(43, 16777215))
        self.lbl_speed.setFont(font)
        self.lbl_slave = QLabel(self.frame_base)
        self.lbl_slave.setObjectName(u"lbl_slave")
        self.lbl_slave.setGeometry(QRect(20, 70, 70, 34))
        self.lbl_slave.setMinimumSize(QSize(70, 20))
        self.lbl_slave.setMaximumSize(QSize(43, 16777215))
        self.lbl_slave.setFont(font)
        self.combobox_parity = QComboBox(self.frame_base)
        self.combobox_parity.setObjectName(u"combobox_parity")
        self.combobox_parity.setGeometry(QRect(120, 140, 81, 22))
        self.combobox_parity.setFont(font)
        self.lbl_type = QLabel(self.frame_base)
        self.lbl_type.setObjectName(u"lbl_type")
        self.lbl_type.setGeometry(QRect(20, 40, 70, 34))
        self.lbl_type.setMinimumSize(QSize(70, 20))
        self.lbl_type.setMaximumSize(QSize(43, 16777215))
        self.lbl_type.setFont(font)
        self.btn_speed = QPushButton(self.frame_base)
        self.btn_speed.setObjectName(u"btn_speed")
        self.btn_speed.setGeometry(QRect(240, 110, 171, 21))
        self.btn_speed.setFont(font)
        self.tabWidget_main.addTab(self.tab_base, "")
        self.tab_scan = QWidget()
        self.tab_scan.setObjectName(u"tab_scan")
        self.frame_scan = QFrame(self.tab_scan)
        self.frame_scan.setObjectName(u"frame_scan")
        self.frame_scan.setGeometry(QRect(0, 0, 681, 461))
        self.frame_scan.setFrameShape(QFrame.StyledPanel)
        self.frame_scan.setFrameShadow(QFrame.Raised)
        self.progressBar_ = QProgressBar(self.frame_scan)
        self.progressBar_.setObjectName(u"progressBar_")
        self.progressBar_.setGeometry(QRect(340, 250, 171, 23))
        self.progressBar_.setValue(0)
        self.groupBox_speeds = QGroupBox(self.frame_scan)
        self.groupBox_speeds.setObjectName(u"groupBox_speeds")
        self.groupBox_speeds.setGeometry(QRect(230, 40, 91, 231))
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
        self.table_devices = QTableWidget(self.frame_scan)
        if (self.table_devices.columnCount() < 2):
            self.table_devices.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 170, 0));
        self.table_devices.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignHCenter|Qt.AlignBottom);
        __qtablewidgetitem1.setBackground(QColor(255, 170, 0));
        self.table_devices.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_devices.setObjectName(u"table_devices")
        self.table_devices.setGeometry(QRect(340, 50, 171, 181))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.table_devices.setPalette(palette)
        self.table_devices.setColumnCount(2)
        self.table_devices.horizontalHeader().setDefaultSectionSize(42)
        self.comboBox_com_port = QComboBox(self.frame_scan)
        self.comboBox_com_port.setObjectName(u"comboBox_com_port")
        self.comboBox_com_port.setGeometry(QRect(80, 10, 431, 22))
        self.groupBox_parity = QGroupBox(self.frame_scan)
        self.groupBox_parity.setObjectName(u"groupBox_parity")
        self.groupBox_parity.setGeometry(QRect(30, 100, 81, 80))
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
        self.group_box_slave = QGroupBox(self.frame_scan)
        self.group_box_slave.setObjectName(u"group_box_slave")
        self.group_box_slave.setGeometry(QRect(10, 40, 211, 51))
        font1 = QFont()
        font1.setBold(True)
        self.group_box_slave.setFont(font1)
        self.etr_slave_to_3 = QLineEdit(self.group_box_slave)
        self.etr_slave_to_3.setObjectName(u"etr_slave_to_3")
        self.etr_slave_to_3.setGeometry(QRect(160, 20, 41, 20))
        font2 = QFont()
        font2.setBold(False)
        self.etr_slave_to_3.setFont(font2)
        self.lbl_from_3 = QLabel(self.group_box_slave)
        self.lbl_from_3.setObjectName(u"lbl_from_3")
        self.lbl_from_3.setGeometry(QRect(10, 20, 43, 13))
        self.lbl_from_3.setFont(font2)
        self.lbl_to_3 = QLabel(self.group_box_slave)
        self.lbl_to_3.setObjectName(u"lbl_to_3")
        self.lbl_to_3.setGeometry(QRect(130, 20, 21, 16))
        self.lbl_to_3.setFont(font2)
        self.etr_slave_from_3 = QLineEdit(self.group_box_slave)
        self.etr_slave_from_3.setObjectName(u"etr_slave_from_3")
        self.etr_slave_from_3.setGeometry(QRect(40, 20, 41, 20))
        self.etr_slave_from_3.setFont(font2)
        self.pushButton_scan = QPushButton(self.frame_scan)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setGeometry(QRect(10, 190, 131, 81))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        self.pushButton_scan.setFont(font3)
        self.groupBox_s_bits = QGroupBox(self.frame_scan)
        self.groupBox_s_bits.setObjectName(u"groupBox_s_bits")
        self.groupBox_s_bits.setGeometry(QRect(130, 100, 81, 80))
        self.check_box_sb1_3 = QCheckBox(self.groupBox_s_bits)
        self.check_box_sb1_3.setObjectName(u"check_box_sb1_3")
        self.check_box_sb1_3.setGeometry(QRect(10, 20, 62, 17))
        self.check_box_sb1_3.setChecked(True)
        self.check_box_sb15_3 = QCheckBox(self.groupBox_s_bits)
        self.check_box_sb15_3.setObjectName(u"check_box_sb15_3")
        self.check_box_sb15_3.setGeometry(QRect(10, 40, 62, 17))
        self.check_box_sb2_3 = QCheckBox(self.groupBox_s_bits)
        self.check_box_sb2_3.setObjectName(u"check_box_sb2_3")
        self.check_box_sb2_3.setGeometry(QRect(10, 60, 62, 17))
        self.com_port = QLabel(self.frame_scan)
        self.com_port.setObjectName(u"com_port")
        self.com_port.setGeometry(QRect(10, 10, 51, 16))
        self.com_port.setFont(font1)
        self.pushButton_stop_scan = QPushButton(self.frame_scan)
        self.pushButton_stop_scan.setObjectName(u"pushButton_stop_scan")
        self.pushButton_stop_scan.setGeometry(QRect(150, 190, 71, 81))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.pushButton_stop_scan.setFont(font4)
        self.tabWidget_main.addTab(self.tab_scan, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 677, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(False)
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_set_param_sigma.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b Sigma", None))
        self.lbl_port.setText(QCoreApplication.translate("MainWindow", u"COM Port", None))
        self.lbl_parity.setText(QCoreApplication.translate("MainWindow", u"Parity", None))
        self.btn_address.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0430\u0434\u0440\u0435\u0441 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.btn_parity.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443 \u043d\u0430 \u0447\u0451\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.lbl_stop_bit.setText(QCoreApplication.translate("MainWindow", u"Stop bits", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.btn_stop_bit.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c Stop bits", None))
        self.lbl_speed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.lbl_slave.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u0443\u0441\u0442\u0440-\u0432\u0430", None))
        self.lbl_type.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
        self.btn_speed.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_base), QCoreApplication.translate("MainWindow", u"Base", None))
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
        ___qtablewidgetitem = self.table_devices.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Slave", None));
        ___qtablewidgetitem1 = self.table_devices.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"speed, s/bits, parity", None));
        self.groupBox_parity.setTitle(QCoreApplication.translate("MainWindow", u"Parity", None))
        self.check_box_none_3.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.check_box_even_3.setText(QCoreApplication.translate("MainWindow", u"Even", None))
        self.check_box_odd_3.setText(QCoreApplication.translate("MainWindow", u"Odd", None))
        self.group_box_slave.setTitle(QCoreApplication.translate("MainWindow", u"Slave", None))
        self.etr_slave_to_3.setInputMask("")
        self.etr_slave_to_3.setText("")
        self.lbl_from_3.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.lbl_to_3.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.etr_slave_from_3.setInputMask("")
        self.etr_slave_from_3.setText("")
        self.pushButton_scan.setText(QCoreApplication.translate("MainWindow", u"Start Scan", None))
        self.groupBox_s_bits.setTitle(QCoreApplication.translate("MainWindow", u"Stop Bits", None))
        self.check_box_sb1_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.check_box_sb15_3.setText(QCoreApplication.translate("MainWindow", u"1,5", None))
        self.check_box_sb2_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.com_port.setText(QCoreApplication.translate("MainWindow", u"COM Port", None))
        self.pushButton_stop_scan.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_scan), QCoreApplication.translate("MainWindow", u"Scan", None))
    # retranslateUi

