# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'media_move.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHeaderView,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Dialog_media_move(object):
    def setupUi(self, Dialog_media_move):
        if not Dialog_media_move.objectName():
            Dialog_media_move.setObjectName(u"Dialog_media_move")
        Dialog_media_move.setWindowModality(Qt.ApplicationModal)
        Dialog_media_move.resize(480, 640)
        self.tableWidget_media_move = QTableWidget(Dialog_media_move)
        self.tableWidget_media_move.setObjectName(u"tableWidget_media_move")
        self.tableWidget_media_move.setGeometry(QRect(10, 20, 461, 541))
        self.tableWidget_media_move.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_media_move.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_media_move.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_media_move.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_media_move.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_media_move.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_media_move.verticalHeader().setVisible(False)
        self.tableWidget_media_move.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_media_move.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_media_move.verticalHeader().setHighlightSections(False)
        self.pushButton = QPushButton(Dialog_media_move)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 590, 111, 31))

        self.retranslateUi(Dialog_media_move)

        QMetaObject.connectSlotsByName(Dialog_media_move)
    # setupUi

    def retranslateUi(self, Dialog_media_move):
        Dialog_media_move.setWindowTitle(QCoreApplication.translate("Dialog_media_move", u"\u5c06\u5a92\u4f53\u79fb\u52a8\u5230\u9009\u4e2d\u5b57\u5e55", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_media_move", u"\u4fdd\u5b58", None))
    # retranslateUi

