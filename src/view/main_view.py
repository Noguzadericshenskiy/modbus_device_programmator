from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.main_menu = QMenuBar(MainWindow)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setGeometry(QRect(0, 0, 640, 21))
        self.menuBase = QMenu(self.main_menu)
        self.menuBase.setObjectName(u"menuBase")
        self.menuScaner = QMenu(self.main_menu)
        self.menuScaner.setObjectName(u"menuScaner")
        MainWindow.setMenuBar(self.main_menu)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.main_menu.addAction(self.menuBase.menuAction())
        self.main_menu.addAction(self.menuScaner.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBase.setTitle(QCoreApplication.translate("MainWindow", u"Base", None))
        self.menuScaner.setTitle(QCoreApplication.translate("MainWindow", u"Scaner", None))
    # retranslateUi

