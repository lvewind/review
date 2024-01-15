# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_account.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHeaderView,
    QMainWindow, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindowAccount(object):
    def setupUi(self, MainWindowAccount):
        if not MainWindowAccount.objectName():
            MainWindowAccount.setObjectName(u"MainWindowAccount")
        MainWindowAccount.resize(880, 436)
        MainWindowAccount.setMinimumSize(QSize(880, 436))
        MainWindowAccount.setMaximumSize(QSize(880, 436))
        self.centralwidget = QWidget(MainWindowAccount)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_play_list_8 = QGroupBox(self.centralwidget)
        self.groupBox_play_list_8.setObjectName(u"groupBox_play_list_8")
        self.groupBox_play_list_8.setGeometry(QRect(10, 10, 851, 401))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(9)
        self.groupBox_play_list_8.setFont(font)
        self.tableWidget_account = QTableWidget(self.groupBox_play_list_8)
        self.tableWidget_account.setObjectName(u"tableWidget_account")
        self.tableWidget_account.setGeometry(QRect(0, 20, 841, 381))
        self.tableWidget_account.setFont(font)
        self.tableWidget_account.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_account.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_account.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_account.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_account.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_account.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_account.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_account.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_account.horizontalHeader().setHighlightSections(False)
        self.tableWidget_account.verticalHeader().setVisible(False)
        self.tableWidget_account.verticalHeader().setMinimumSectionSize(18)
        self.tableWidget_account.verticalHeader().setDefaultSectionSize(18)
        MainWindowAccount.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowAccount)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowAccount.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowAccount)

        QMetaObject.connectSlotsByName(MainWindowAccount)
    # setupUi

    def retranslateUi(self, MainWindowAccount):
        MainWindowAccount.setWindowTitle(QCoreApplication.translate("MainWindowAccount", u"\u8d26\u53f7", None))
        self.groupBox_play_list_8.setTitle(QCoreApplication.translate("MainWindowAccount", u"\u8d26\u53f7\u5217\u8868", None))
    # retranslateUi

