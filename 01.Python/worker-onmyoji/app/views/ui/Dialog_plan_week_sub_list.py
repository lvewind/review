# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_plan_week_sub_list.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGroupBox, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog_plan_week_sub_list(object):
    def setupUi(self, Dialog_plan_week_sub_list):
        if not Dialog_plan_week_sub_list.objectName():
            Dialog_plan_week_sub_list.setObjectName(u"Dialog_plan_week_sub_list")
        Dialog_plan_week_sub_list.setWindowModality(Qt.ApplicationModal)
        Dialog_plan_week_sub_list.resize(320, 240)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Dialog_plan_week_sub_list.setFont(font)
        self.buttonBox = QDialogButtonBox(Dialog_plan_week_sub_list)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 190, 161, 32))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(9)
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox_2 = QGroupBox(Dialog_plan_week_sub_list)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 30, 281, 71))
        self.groupBox_2.setFont(font1)
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 29, 51, 23))
        self.pushButton.setFont(font1)
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(20, 30, 201, 21))
        self.lineEdit.setFont(font1)
        self.lineEdit.setReadOnly(True)
        self.groupBox_3 = QGroupBox(Dialog_plan_week_sub_list)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 110, 281, 71))
        self.groupBox_3.setFont(font1)
        self.comboBox = QComboBox(self.groupBox_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 30, 241, 22))
        self.comboBox.setFont(font1)
        self.comboBox.setCurrentText(u"")

        self.retranslateUi(Dialog_plan_week_sub_list)
        self.buttonBox.accepted.connect(Dialog_plan_week_sub_list.accept)
        self.buttonBox.rejected.connect(Dialog_plan_week_sub_list.reject)

        QMetaObject.connectSlotsByName(Dialog_plan_week_sub_list)
    # setupUi

    def retranslateUi(self, Dialog_plan_week_sub_list):
        Dialog_plan_week_sub_list.setWindowTitle(QCoreApplication.translate("Dialog_plan_week_sub_list", u"\u65b0\u589e\u5468\u8ba1\u5212\u5b50\u5217\u8868", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_plan_week_sub_list", u"\u8bf7\u9009\u62e9\u8981\u6267\u884c\u7684\u65e5\u8ba1\u5212", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_plan_week_sub_list", u"\u9009\u62e9", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog_plan_week_sub_list", u"\u8bf7\u9009\u62e9\u8981\u6267\u884c\u7684\u65e5\u671f", None))
    # retranslateUi

