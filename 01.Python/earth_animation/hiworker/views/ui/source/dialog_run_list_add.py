# -*- coding: utf-8 -*-

# Form implementation generated from reading view file 'dialog_run_list_add.view'
#
# Created by: PySide6 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_run_list_add(object):
    def setupUi(self, Dialog_run_list_add):
        Dialog_run_list_add.setObjectName("Dialog_run_list_add")
        Dialog_run_list_add.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_run_list_add.resize(320, 240)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog_run_list_add.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_run_list_add)
        self.buttonBox.setGeometry(QtCore.QRect(80, 190, 161, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(Dialog_run_list_add)
        self.label_3.setGeometry(QtCore.QRect(90, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.spinBoxadd_new_count = QtWidgets.QSpinBox(Dialog_run_list_add)
        self.spinBoxadd_new_count.setGeometry(QtCore.QRect(91, 100, 141, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.spinBoxadd_new_count.setFont(font)
        self.spinBoxadd_new_count.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxadd_new_count.setMinimum(1)
        self.spinBoxadd_new_count.setObjectName("spinBoxadd_new_count")

        self.retranslateUi(Dialog_run_list_add)
        self.buttonBox.accepted.connect(Dialog_run_list_add.accept)
        self.buttonBox.rejected.connect(Dialog_run_list_add.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_run_list_add)

    def retranslateUi(self, Dialog_run_list_add):
        _translate = QtCore.QCoreApplication.translate
        Dialog_run_list_add.setWindowTitle(_translate("Dialog_run_list_add", "新增运行列表项"))
        self.label_3.setText(_translate("Dialog_run_list_add", "请输入增加的运行列表数量"))
