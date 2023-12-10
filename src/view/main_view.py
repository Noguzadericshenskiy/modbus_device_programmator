from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)


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
        self.tabWidget_main.setGeometry(QRect(0, 0, 641, 471))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_main.sizePolicy().hasHeightForWidth())
        self.tabWidget_main.setSizePolicy(sizePolicy)
        self.tabWidget_main.setTabShape(QTabWidget.Triangular)
        self.base_tab = QWidget()
        self.base_tab.setObjectName(u"base_tab")
        self.pushButtonbase = QPushButton(self.base_tab)
        self.pushButtonbase.setObjectName(u"pushButtonbase")
        self.pushButtonbase.setGeometry(QRect(420, 40, 161, 151))
        self.labelbase = QLabel(self.base_tab)
        self.labelbase.setObjectName(u"labelbase")
        self.labelbase.setGeometry(QRect(50, 70, 291, 101))
        font = QFont()
        font.setPointSize(36)
        self.labelbase.setFont(font)
        self.tabWidget_main.addTab(self.base_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.labelscan = QLabel(self.tab_2)
        self.labelscan.setObjectName(u"labelscan")
        self.labelscan.setGeometry(QRect(30, 260, 301, 161))
        self.labelscan.setFont(font)
        self.pushButtonscan = QPushButton(self.tab_2)
        self.pushButtonscan.setObjectName(u"pushButtonscan")
        self.pushButtonscan.setGeometry(QRect(380, 260, 231, 181))
        self.tabWidget_main.addTab(self.tab_2, "")
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

        self.tabWidget_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonbase.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.labelbase.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.base_tab), QCoreApplication.translate("MainWindow", u"Base", None))
        self.labelscan.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButtonscan.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Scan", None))
    # retranslateUi

