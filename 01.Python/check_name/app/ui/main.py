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
        MainWindow.resize(401, 320)
        MainWindow.setMinimumSize(QSize(401, 320))
        MainWindow.setMaximumSize(QSize(491, 725))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 361, 71))
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
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 180, 361, 61))
        self.groupBox_3.setFont(font)
        self.lineEdit_output_excel = QLineEdit(self.groupBox_3)
        self.lineEdit_output_excel.setObjectName(u"lineEdit_output_excel")
        self.lineEdit_output_excel.setGeometry(QRect(10, 20, 341, 31))
        self.lineEdit_output_excel.setFont(font)
        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(130, 260, 131, 31))
        self.pushButton_start.setFont(font)
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 100, 361, 71))
        self.groupBox_4.setFont(font)
        self.pushButton_select_file = QPushButton(self.groupBox_4)
        self.pushButton_select_file.setObjectName(u"pushButton_select_file")
        self.pushButton_select_file.setGeometry(QRect(280, 30, 75, 31))
        self.pushButton_select_file.setFont(font)
        self.lineEdit_input_file = QLineEdit(self.groupBox_4)
        self.lineEdit_input_file.setObjectName(u"lineEdit_input_file")
        self.lineEdit_input_file.setGeometry(QRect(10, 30, 271, 31))
        self.lineEdit_input_file.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9759\u8001\u677f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u540d\u5355EXCEL", None))
        self.pushButton_select_excel.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u8f93\u51fa\u540d\u5355EXCEL\uff0c\u7559\u7a7a\u5219\u4e0e\u4f5c\u4e1a\u6587\u4ef6\u5939\u76f8\u540c", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6838\u5bf9", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4f5c\u4e1a\u6587\u4ef6\u5939", None))
        self.pushButton_select_file.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
    # retranslateUi

