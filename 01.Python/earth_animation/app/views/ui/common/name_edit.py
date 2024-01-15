# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'name_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_name_edit(object):
    def setupUi(self, Dialog_name_edit):
        if not Dialog_name_edit.objectName():
            Dialog_name_edit.setObjectName(u"Dialog_name_edit")
        Dialog_name_edit.setWindowModality(Qt.ApplicationModal)
        Dialog_name_edit.resize(320, 240)
        self.lineEdit = QLineEdit(Dialog_name_edit)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 60, 231, 41))
        self.pushButton = QPushButton(Dialog_name_edit)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 150, 101, 31))
        self.label = QLabel(Dialog_name_edit)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 51, 21))

        self.retranslateUi(Dialog_name_edit)

        QMetaObject.connectSlotsByName(Dialog_name_edit)
    # setupUi

    def retranslateUi(self, Dialog_name_edit):
        Dialog_name_edit.setWindowTitle(QCoreApplication.translate("Dialog_name_edit", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_name_edit", u"\u4fdd\u5b58", None))
        self.label.setText(QCoreApplication.translate("Dialog_name_edit", u"\u8f93\u5165\u540d\u79f0", None))
    # retranslateUi

