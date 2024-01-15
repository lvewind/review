# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_demon_parade_table.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGroupBox,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Dialog_demon_parade_table(object):
    def setupUi(self, Dialog_demon_parade_table):
        if not Dialog_demon_parade_table.objectName():
            Dialog_demon_parade_table.setObjectName(u"Dialog_demon_parade_table")
        Dialog_demon_parade_table.resize(830, 401)
        self.groupBox_job_list_10 = QGroupBox(Dialog_demon_parade_table)
        self.groupBox_job_list_10.setObjectName(u"groupBox_job_list_10")
        self.groupBox_job_list_10.setGeometry(QRect(10, 10, 811, 381))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(9)
        self.groupBox_job_list_10.setFont(font)
        self.tableWidget_demon_parade_list = QTableWidget(self.groupBox_job_list_10)
        if (self.tableWidget_demon_parade_list.columnCount() < 2):
            self.tableWidget_demon_parade_list.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_demon_parade_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_demon_parade_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_demon_parade_list.setObjectName(u"tableWidget_demon_parade_list")
        self.tableWidget_demon_parade_list.setGeometry(QRect(0, 20, 231, 361))
        self.tableWidget_demon_parade_list.setFont(font)
        self.tableWidget_demon_parade_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_demon_parade_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_demon_parade_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_demon_parade_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_demon_parade_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_demon_parade_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_demon_parade_list.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_demon_parade_list.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_demon_parade_list.horizontalHeader().setHighlightSections(False)
        self.tableWidget_demon_parade_list.verticalHeader().setVisible(False)
        self.tableWidget_demon_parade_list.verticalHeader().setMinimumSectionSize(18)
        self.tableWidget_demon_parade_list.verticalHeader().setDefaultSectionSize(18)

        self.retranslateUi(Dialog_demon_parade_table)

        QMetaObject.connectSlotsByName(Dialog_demon_parade_table)
    # setupUi

    def retranslateUi(self, Dialog_demon_parade_table):
        Dialog_demon_parade_table.setWindowTitle(QCoreApplication.translate("Dialog_demon_parade_table", u"\u767e\u9b3c\u591c\u884c", None))
        self.groupBox_job_list_10.setTitle(QCoreApplication.translate("Dialog_demon_parade_table", u"\u767e\u9b3c\u591c\u884c\u9884\u8bbe\u5217\u8868", None))
        ___qtablewidgetitem = self.tableWidget_demon_parade_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_demon_parade_table", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_demon_parade_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_demon_parade_table", u"\u540d\u79f0", None));
    # retranslateUi

