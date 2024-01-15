# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_plan.ui'
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

class Ui_MainWindowPlan(object):
    def setupUi(self, MainWindowPlan):
        if not MainWindowPlan.objectName():
            MainWindowPlan.setObjectName(u"MainWindowPlan")
        MainWindowPlan.resize(880, 436)
        MainWindowPlan.setMinimumSize(QSize(880, 436))
        MainWindowPlan.setMaximumSize(QSize(880, 436))
        self.centralwidget = QWidget(MainWindowPlan)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_play_list_6 = QGroupBox(self.centralwidget)
        self.groupBox_play_list_6.setObjectName(u"groupBox_play_list_6")
        self.groupBox_play_list_6.setGeometry(QRect(10, 10, 421, 401))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(9)
        self.groupBox_play_list_6.setFont(font)
        self.tableWidget_plan = QTableWidget(self.groupBox_play_list_6)
        self.tableWidget_plan.setObjectName(u"tableWidget_plan")
        self.tableWidget_plan.setGeometry(QRect(0, 20, 421, 381))
        self.tableWidget_plan.setFont(font)
        self.tableWidget_plan.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_plan.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_plan.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_plan.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_plan.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_plan.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_plan.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_plan.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_plan.horizontalHeader().setHighlightSections(False)
        self.tableWidget_plan.verticalHeader().setVisible(False)
        self.tableWidget_plan.verticalHeader().setMinimumSectionSize(18)
        self.tableWidget_plan.verticalHeader().setDefaultSectionSize(18)
        self.groupBox_sub_play_list_6 = QGroupBox(self.centralwidget)
        self.groupBox_sub_play_list_6.setObjectName(u"groupBox_sub_play_list_6")
        self.groupBox_sub_play_list_6.setGeometry(QRect(450, 10, 421, 401))
        self.groupBox_sub_play_list_6.setFont(font)
        self.groupBox_sub_play_list_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tableWidget_plan_sub = QTableWidget(self.groupBox_sub_play_list_6)
        self.tableWidget_plan_sub.setObjectName(u"tableWidget_plan_sub")
        self.tableWidget_plan_sub.setGeometry(QRect(0, 20, 421, 381))
        self.tableWidget_plan_sub.setFont(font)
        self.tableWidget_plan_sub.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_plan_sub.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_plan_sub.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_plan_sub.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_plan_sub.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_plan_sub.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_plan_sub.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_plan_sub.horizontalHeader().setHighlightSections(False)
        self.tableWidget_plan_sub.verticalHeader().setVisible(False)
        self.tableWidget_plan_sub.verticalHeader().setMinimumSectionSize(18)
        self.tableWidget_plan_sub.verticalHeader().setDefaultSectionSize(18)
        MainWindowPlan.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowPlan)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowPlan.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowPlan)

        QMetaObject.connectSlotsByName(MainWindowPlan)
    # setupUi

    def retranslateUi(self, MainWindowPlan):
        MainWindowPlan.setWindowTitle(QCoreApplication.translate("MainWindowPlan", u"\u8ba1\u5212", None))
        self.groupBox_play_list_6.setTitle(QCoreApplication.translate("MainWindowPlan", u"\u8ba1\u5212\u5217\u8868", None))
        self.groupBox_sub_play_list_6.setTitle(QCoreApplication.translate("MainWindowPlan", u"\u8ba1\u5212\u5305\u542b\u7684\u4ea7\u54c1", None))
    # retranslateUi

