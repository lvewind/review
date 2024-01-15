# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_run_list.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindowRunList(object):
    def setupUi(self, MainWindowRunList):
        if not MainWindowRunList.objectName():
            MainWindowRunList.setObjectName(u"MainWindowRunList")
        MainWindowRunList.resize(1000, 460)
        MainWindowRunList.setMinimumSize(QSize(1000, 460))
        MainWindowRunList.setMaximumSize(QSize(1000, 460))
        self.centralwidget = QWidget(MainWindowRunList)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget_run_count = QTableWidget(self.centralwidget)
        self.tableWidget_run_count.setObjectName(u"tableWidget_run_count")
        self.tableWidget_run_count.setGeometry(QRect(910, 10, 82, 401))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(8)
        self.tableWidget_run_count.setFont(font)
        self.tableWidget_run_count.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_run_count.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_run_count.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_run_count.horizontalHeader().setVisible(True)
        self.tableWidget_run_count.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_run_count.horizontalHeader().setDefaultSectionSize(40)
        self.tableWidget_run_count.horizontalHeader().setHighlightSections(False)
        self.tableWidget_run_count.verticalHeader().setVisible(False)
        self.tableWidget_run_count.verticalHeader().setMinimumSectionSize(16)
        self.tableWidget_run_count.verticalHeader().setDefaultSectionSize(16)
        self.tableWidget_run_list = QTableWidget(self.centralwidget)
        self.tableWidget_run_list.setObjectName(u"tableWidget_run_list")
        self.tableWidget_run_list.setGeometry(QRect(10, 10, 901, 401))
        self.tableWidget_run_list.setMinimumSize(QSize(0, 0))
        self.tableWidget_run_list.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.tableWidget_run_list.setFont(font1)
        self.tableWidget_run_list.setTabletTracking(False)
        self.tableWidget_run_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_run_list.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_run_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_run_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_run_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_run_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_run_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_run_list.setGridStyle(Qt.SolidLine)
        self.tableWidget_run_list.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_run_list.horizontalHeader().setDefaultSectionSize(45)
        self.tableWidget_run_list.horizontalHeader().setHighlightSections(False)
        self.tableWidget_run_list.verticalHeader().setVisible(False)
        self.tableWidget_run_list.verticalHeader().setMinimumSectionSize(18)
        self.tableWidget_run_list.verticalHeader().setDefaultSectionSize(18)
        self.tableWidget_run_list.verticalHeader().setHighlightSections(True)
        MainWindowRunList.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowRunList)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        MainWindowRunList.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowRunList)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowRunList.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowRunList)

        QMetaObject.connectSlotsByName(MainWindowRunList)
    # setupUi

    def retranslateUi(self, MainWindowRunList):
        MainWindowRunList.setWindowTitle(QCoreApplication.translate("MainWindowRunList", u"\u8fd0\u884c\u5217\u8868", None))
    # retranslateUi

