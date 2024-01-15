# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 160)
        MainWindow.setMinimumSize(QSize(401, 160))
        MainWindow.setMaximumSize(QSize(540, 240))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 40, 361, 71))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        self.groupBox.setFont(font)
        self.lineEdit_input_excel = QLineEdit(self.groupBox)
        self.lineEdit_input_excel.setObjectName(u"lineEdit_input_excel")
        self.lineEdit_input_excel.setGeometry(QRect(10, 30, 271, 31))
        self.lineEdit_input_excel.setFont(font)
        self.pushButton_select_excel = QPushButton(self.groupBox)
        self.pushButton_select_excel.setObjectName(u"pushButton_select_excel")
        self.pushButton_select_excel.setGeometry(QRect(280, 30, 75, 31))
        self.pushButton_select_excel.setFont(font)
        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(400, 50, 131, 61))
        self.pushButton_start.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6021\u5b9d-\u77f3\u677f\u8003\u52e4\u7edf\u8ba1", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u540d\u5355EXCEL", None))
        self.pushButton_select_excel.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6838\u5bf9", None))
    # retranslateUi

