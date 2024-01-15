# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_plan_list.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGroupBox, QLineEdit, QSizePolicy,
    QTimeEdit, QWidget)

class Ui_Dialog_plan_list_add(object):
    def setupUi(self, Dialog_plan_list_add):
        if not Dialog_plan_list_add.objectName():
            Dialog_plan_list_add.setObjectName(u"Dialog_plan_list_add")
        Dialog_plan_list_add.setWindowModality(Qt.ApplicationModal)
        Dialog_plan_list_add.resize(320, 320)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Dialog_plan_list_add.setFont(font)
        self.buttonBox = QDialogButtonBox(Dialog_plan_list_add)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 260, 161, 32))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(9)
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox_list_item_name = QGroupBox(Dialog_plan_list_add)
        self.groupBox_list_item_name.setObjectName(u"groupBox_list_item_name")
        self.groupBox_list_item_name.setGeometry(QRect(20, 30, 281, 81))
        self.groupBox_list_item_name.setFont(font1)
        self.lineEdit_new_list_name = QLineEdit(self.groupBox_list_item_name)
        self.lineEdit_new_list_name.setObjectName(u"lineEdit_new_list_name")
        self.lineEdit_new_list_name.setGeometry(QRect(20, 30, 241, 31))
        self.lineEdit_new_list_name.setFont(font1)
        self.checkBox_close_env = QCheckBox(Dialog_plan_list_add)
        self.checkBox_close_env.setObjectName(u"checkBox_close_env")
        self.checkBox_close_env.setGeometry(QRect(90, 210, 141, 21))
        self.groupBox = QGroupBox(Dialog_plan_list_add)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 120, 281, 71))
        self.timeEdit_timing_start = QTimeEdit(self.groupBox)
        self.timeEdit_timing_start.setObjectName(u"timeEdit_timing_start")
        self.timeEdit_timing_start.setGeometry(QRect(20, 20, 241, 31))
        self.timeEdit_timing_start.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog_plan_list_add)
        self.buttonBox.accepted.connect(Dialog_plan_list_add.accept)
        self.buttonBox.rejected.connect(Dialog_plan_list_add.reject)

        QMetaObject.connectSlotsByName(Dialog_plan_list_add)
    # setupUi

    def retranslateUi(self, Dialog_plan_list_add):
        Dialog_plan_list_add.setWindowTitle(QCoreApplication.translate("Dialog_plan_list_add", u"\u65b0\u589e\u8ba1\u5212\u5217\u8868\u9879", None))
        self.groupBox_list_item_name.setTitle(QCoreApplication.translate("Dialog_plan_list_add", u"\u8bf7\u8f93\u5165\u65b0\u589e\u7684\u8ba1\u5212\u540d\u79f0", None))
        self.checkBox_close_env.setText(QCoreApplication.translate("Dialog_plan_list_add", u"\u5b8c\u6210\u8ba1\u5212\u5173\u95ed\u8fd0\u884c\u73af\u5883", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_plan_list_add", u"\u5b9a\u65f6\u5f00\u542f", None))
        self.timeEdit_timing_start.setDisplayFormat(QCoreApplication.translate("Dialog_plan_list_add", u"HH:mm:ss", None))
    # retranslateUi

