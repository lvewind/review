# -*- coding: utf-8 -*-

# Form implementation generated from reading view file 'dialog_info.view'
#
# Created by: PySide6 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_info(object):
    def setupUi(self, Dialog_info):
        Dialog_info.setObjectName("Dialog_info")
        Dialog_info.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_info.resize(320, 240)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        Dialog_info.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_info)
        self.buttonBox.setGeometry(QtCore.QRect(80, 180, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_info = QtWidgets.QLabel(Dialog_info)
        self.label_info.setGeometry(QtCore.QRect(20, 80, 271, 31))
        self.label_info.setText("")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")

        self.retranslateUi(Dialog_info)
        self.buttonBox.accepted.connect(Dialog_info.accept)
        self.buttonBox.rejected.connect(Dialog_info.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_info)

    def retranslateUi(self, Dialog_info):
        _translate = QtCore.QCoreApplication.translate
        Dialog_info.setWindowTitle(_translate("Dialog_info", "提示"))
