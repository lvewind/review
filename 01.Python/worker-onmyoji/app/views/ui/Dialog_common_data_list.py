# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_common_data_list.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QHeaderView, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Dialog_common_data_list(object):
    def setupUi(self, Dialog_common_data_list):
        if not Dialog_common_data_list.objectName():
            Dialog_common_data_list.setObjectName(u"Dialog_common_data_list")
        Dialog_common_data_list.setWindowModality(Qt.ApplicationModal)
        Dialog_common_data_list.resize(320, 420)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Dialog_common_data_list.setFont(font)
        self.buttonBox = QDialogButtonBox(Dialog_common_data_list)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(90, 370, 161, 32))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(8)
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tableWidget_data_list = QTableWidget(Dialog_common_data_list)
        if (self.tableWidget_data_list.columnCount() < 2):
            self.tableWidget_data_list.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_data_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_data_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_data_list.setObjectName(u"tableWidget_data_list")
        self.tableWidget_data_list.setGeometry(QRect(10, 10, 301, 351))
        self.tableWidget_data_list.setFont(font1)
        self.tableWidget_data_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_data_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_data_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_data_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_data_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_data_list.horizontalHeader().setHighlightSections(False)
        self.tableWidget_data_list.verticalHeader().setVisible(False)
        self.tableWidget_data_list.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_data_list.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_data_list.verticalHeader().setHighlightSections(False)

        self.retranslateUi(Dialog_common_data_list)
        self.buttonBox.accepted.connect(Dialog_common_data_list.accept)
        self.buttonBox.rejected.connect(Dialog_common_data_list.reject)

        QMetaObject.connectSlotsByName(Dialog_common_data_list)
    # setupUi

    def retranslateUi(self, Dialog_common_data_list):
        Dialog_common_data_list.setWindowTitle(QCoreApplication.translate("Dialog_common_data_list", u"\u8bbe\u7f6e\u8ba1\u5212", None))
        ___qtablewidgetitem = self.tableWidget_data_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_common_data_list", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_data_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_common_data_list", u"\u540d\u79f0", None));
    # retranslateUi

