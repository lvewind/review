# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindowLogin(object):
    def setupUi(self, MainWindowLogin):
        if not MainWindowLogin.objectName():
            MainWindowLogin.setObjectName(u"MainWindowLogin")
        MainWindowLogin.resize(360, 240)
        MainWindowLogin.setMinimumSize(QSize(360, 240))
        MainWindowLogin.setMaximumSize(QSize(360, 240))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        MainWindowLogin.setFont(font)
        self.centralwidget = QWidget(MainWindowLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 341, 201))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 30, 211, 20))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 31, 16))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 31, 16))
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 70, 211, 20))
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 120, 75, 23))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(70, 70, 211, 20))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 30, 31, 16))
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 120, 75, 23))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 70, 31, 16))
        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(70, 30, 211, 20))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lineEdit_11 = QLineEdit(self.tab_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(70, 70, 211, 20))
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 30, 31, 16))
        self.pushButton_5 = QPushButton(self.tab_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(130, 120, 75, 23))
        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 70, 31, 16))
        self.lineEdit_12 = QLineEdit(self.tab_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(70, 30, 211, 20))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.lineEdit_13 = QLineEdit(self.tab_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(70, 30, 211, 20))
        self.label_13 = QLabel(self.tab_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 30, 41, 16))
        self.pushButton_6 = QPushButton(self.tab_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(130, 120, 75, 23))
        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 70, 31, 16))
        self.lineEdit_14 = QLineEdit(self.tab_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(70, 70, 211, 20))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label_5 = QLabel(self.tab_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 70, 91, 21))
        self.label_5.setTextFormat(Qt.AutoText)
        self.tabWidget.addTab(self.tab_5, "")
        MainWindowLogin.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowLogin)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowLogin.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowLogin)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindowLogin)
    # setupUi

    def retranslateUi(self, MainWindowLogin):
        MainWindowLogin.setWindowTitle(QCoreApplication.translate("MainWindowLogin", u"HiWorker", None))
        self.label.setText(QCoreApplication.translate("MainWindowLogin", u"\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("MainWindowLogin", u"\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindowLogin", u"\u767b\u5f55", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindowLogin", u"\u767b\u5f55", None))
        self.lineEdit_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindowLogin", u"\u8d26\u53f7", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindowLogin", u"\u6ce8\u518c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindowLogin", u"\u5bc6\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindowLogin", u"\u6ce8\u518c", None))
        self.lineEdit_11.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindowLogin", u"\u8d26\u53f7", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindowLogin", u"\u786e\u8ba4", None))
        self.label_12.setText(QCoreApplication.translate("MainWindowLogin", u"\u5361\u5bc6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindowLogin", u"\u5145\u503c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindowLogin", u"\u5151\u6362\u7801", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindowLogin", u"\u5151\u6362", None))
        self.label_14.setText(QCoreApplication.translate("MainWindowLogin", u"\u5361\u5bc6", None))
        self.lineEdit_14.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindowLogin", u"\u5361\u5bc6", None))
        self.label_5.setText(QCoreApplication.translate("MainWindowLogin", u"onmyoji.cloud", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindowLogin", u"\u6587\u6863", None))
    # retranslateUi

