# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_run_list_set_teamup.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QRadioButton, QSizePolicy, QWidget)

class Ui_Dialog_run_list_set_teamup(object):
    def setupUi(self, Dialog_run_list_set_teamup):
        if not Dialog_run_list_set_teamup.objectName():
            Dialog_run_list_set_teamup.setObjectName(u"Dialog_run_list_set_teamup")
        Dialog_run_list_set_teamup.setWindowModality(Qt.ApplicationModal)
        Dialog_run_list_set_teamup.resize(320, 240)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Dialog_run_list_set_teamup.setFont(font)
        self.buttonBox = QDialogButtonBox(Dialog_run_list_set_teamup)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 190, 161, 32))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(9)
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(Dialog_run_list_set_teamup)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 281, 61))
        self.groupBox.setFont(font1)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(60, 30, 51, 16))
        self.radioButton.setFont(font1)
        self.radioButton.setChecked(True)
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(160, 30, 51, 16))
        self.radioButton_2.setFont(font1)
        self.radioButton_2.setChecked(False)
        self.groupBox_2 = QGroupBox(Dialog_run_list_set_teamup)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 100, 281, 61))
        self.groupBox_2.setFont(font1)
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(60, 30, 51, 16))
        self.radioButton_3.setFont(font1)
        self.radioButton_3.setChecked(True)
        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(160, 30, 51, 16))
        self.radioButton_4.setFont(font1)
        self.radioButton_4.setChecked(False)

        self.retranslateUi(Dialog_run_list_set_teamup)
        self.buttonBox.accepted.connect(Dialog_run_list_set_teamup.accept)
        self.buttonBox.rejected.connect(Dialog_run_list_set_teamup.reject)

        QMetaObject.connectSlotsByName(Dialog_run_list_set_teamup)
    # setupUi

    def retranslateUi(self, Dialog_run_list_set_teamup):
        Dialog_run_list_set_teamup.setWindowTitle(QCoreApplication.translate("Dialog_run_list_set_teamup", u"\u8bbe\u7f6e\u961f\u4f0d\u6a21\u5f0f", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_run_list_set_teamup", u"\u961f\u4f0d\u7c7b\u578b", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog_run_list_set_teamup", u"\u5355\u4eba", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog_run_list_set_teamup", u"\u53cc\u4eba", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_run_list_set_teamup", u"\u961f\u4f0d\u4f4d\u7f6e", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog_run_list_set_teamup", u"\u961f\u957f", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog_run_list_set_teamup", u"\u961f\u53cb", None))
    # retranslateUi

