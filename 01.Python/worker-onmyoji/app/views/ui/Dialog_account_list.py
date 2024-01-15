# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_account_list.ui'
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
    QDialogButtonBox, QGroupBox, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_DialogAccount(object):
    def setupUi(self, DialogAccount):
        if not DialogAccount.objectName():
            DialogAccount.setObjectName(u"DialogAccount")
        DialogAccount.setWindowModality(Qt.ApplicationModal)
        DialogAccount.resize(321, 472)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        DialogAccount.setFont(font)
        self.buttonBox = QDialogButtonBox(DialogAccount)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 430, 161, 32))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(9)
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(DialogAccount)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 90, 281, 51))
        self.groupBox.setFont(font1)
        self.radioButton_iOS = QRadioButton(self.groupBox)
        self.radioButton_iOS.setObjectName(u"radioButton_iOS")
        self.radioButton_iOS.setGeometry(QRect(180, 30, 51, 16))
        self.radioButton_iOS.setFont(font1)
        self.radioButton_android = QRadioButton(self.groupBox)
        self.radioButton_android.setObjectName(u"radioButton_android")
        self.radioButton_android.setGeometry(QRect(60, 30, 81, 16))
        self.radioButton_android.setFont(font1)
        self.radioButton_android.setChecked(True)
        self.groupBox_2 = QGroupBox(DialogAccount)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 150, 281, 61))
        self.groupBox_2.setFont(font1)
        self.lineEdit_regional = QLineEdit(self.groupBox_2)
        self.lineEdit_regional.setObjectName(u"lineEdit_regional")
        self.lineEdit_regional.setEnabled(True)
        self.lineEdit_regional.setGeometry(QRect(20, 31, 201, 21))
        self.lineEdit_regional.setFont(font1)
        self.lineEdit_regional.setAlignment(Qt.AlignCenter)
        self.lineEdit_regional.setReadOnly(True)
        self.pushButton_regional = QPushButton(self.groupBox_2)
        self.pushButton_regional.setObjectName(u"pushButton_regional")
        self.pushButton_regional.setGeometry(QRect(220, 30, 51, 23))
        self.pushButton_regional.setFont(font1)
        self.groupBox_3 = QGroupBox(DialogAccount)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 20, 281, 61))
        self.groupBox_3.setFont(font1)
        self.lineEdit_new_list_name = QLineEdit(self.groupBox_3)
        self.lineEdit_new_list_name.setObjectName(u"lineEdit_new_list_name")
        self.lineEdit_new_list_name.setGeometry(QRect(20, 30, 241, 24))
        self.lineEdit_new_list_name.setFont(font1)
        self.groupBox_4 = QGroupBox(DialogAccount)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 290, 281, 61))
        self.pushButton_teamup_img = QPushButton(self.groupBox_4)
        self.pushButton_teamup_img.setObjectName(u"pushButton_teamup_img")
        self.pushButton_teamup_img.setGeometry(QRect(220, 29, 51, 23))
        self.pushButton_teamup_img.setFont(font1)
        self.lineEdit_teamup_img = QLineEdit(self.groupBox_4)
        self.lineEdit_teamup_img.setObjectName(u"lineEdit_teamup_img")
        self.lineEdit_teamup_img.setEnabled(True)
        self.lineEdit_teamup_img.setGeometry(QRect(20, 30, 201, 21))
        self.lineEdit_teamup_img.setFont(font1)
        self.lineEdit_teamup_img.setAlignment(Qt.AlignCenter)
        self.lineEdit_teamup_img.setReadOnly(True)
        self.groupBox_5 = QGroupBox(DialogAccount)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 360, 281, 61))
        self.pushButton_login_img = QPushButton(self.groupBox_5)
        self.pushButton_login_img.setObjectName(u"pushButton_login_img")
        self.pushButton_login_img.setGeometry(QRect(220, 29, 51, 23))
        self.pushButton_login_img.setFont(font1)
        self.lineEdit_login_img = QLineEdit(self.groupBox_5)
        self.lineEdit_login_img.setObjectName(u"lineEdit_login_img")
        self.lineEdit_login_img.setEnabled(True)
        self.lineEdit_login_img.setGeometry(QRect(20, 30, 201, 21))
        self.lineEdit_login_img.setFont(font1)
        self.lineEdit_login_img.setAlignment(Qt.AlignCenter)
        self.lineEdit_login_img.setReadOnly(True)
        self.groupBox_6 = QGroupBox(DialogAccount)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 220, 281, 61))
        self.checkBox_remember_password = QCheckBox(self.groupBox_6)
        self.checkBox_remember_password.setObjectName(u"checkBox_remember_password")
        self.checkBox_remember_password.setGeometry(QRect(20, 30, 71, 16))
        self.checkBox_change_role = QCheckBox(self.groupBox_6)
        self.checkBox_change_role.setObjectName(u"checkBox_change_role")
        self.checkBox_change_role.setGeometry(QRect(130, 30, 101, 16))

        self.retranslateUi(DialogAccount)
        self.buttonBox.accepted.connect(DialogAccount.accept)
        self.buttonBox.rejected.connect(DialogAccount.reject)

        QMetaObject.connectSlotsByName(DialogAccount)
    # setupUi

    def retranslateUi(self, DialogAccount):
        DialogAccount.setWindowTitle(QCoreApplication.translate("DialogAccount", u"\u65b0\u589e\u6e38\u620f\u5e10\u6237", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogAccount", u"\u9009\u62e9\u8d26\u53f7\u5e73\u53f0", None))
        self.radioButton_iOS.setText(QCoreApplication.translate("DialogAccount", u"iOS", None))
        self.radioButton_android.setText(QCoreApplication.translate("DialogAccount", u"Android", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DialogAccount", u"\u89d2\u8272\u670d\u52a1\u5668", None))
        self.pushButton_regional.setText(QCoreApplication.translate("DialogAccount", u"\u9009\u62e9", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DialogAccount", u"\u8bf7\u8f93\u5165\u8d26\u6237\u540d\u79f0", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("DialogAccount", u"\u7ec4\u961f\u56fe\u7247", None))
        self.pushButton_teamup_img.setText(QCoreApplication.translate("DialogAccount", u"\u9009\u62e9", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("DialogAccount", u"\u767b\u5f55\u56fe\u7247", None))
        self.pushButton_login_img.setText(QCoreApplication.translate("DialogAccount", u"\u9009\u62e9", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("DialogAccount", u"\u767b\u5f55\u8bbe\u7f6e", None))
        self.checkBox_remember_password.setText(QCoreApplication.translate("DialogAccount", u"\u514d\u5bc6\u767b\u5f55", None))
        self.checkBox_change_role.setText(QCoreApplication.translate("DialogAccount", u"\u767b\u5f55\u91cd\u9009\u89d2\u8272", None))
    # retranslateUi

