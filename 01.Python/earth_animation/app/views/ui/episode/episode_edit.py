# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'place_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Dialog_place_edit(object):
    def setupUi(self, Dialog_place_edit):
        if not Dialog_place_edit.objectName():
            Dialog_place_edit.setObjectName(u"Dialog_place_edit")
        Dialog_place_edit.setWindowModality(Qt.ApplicationModal)
        Dialog_place_edit.resize(640, 640)
        Dialog_place_edit.setMinimumSize(QSize(640, 640))
        Dialog_place_edit.setMaximumSize(QSize(640, 640))
        self.groupBox_5 = QGroupBox(Dialog_place_edit)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 10, 621, 541))
        self.textEdit_content = QTextEdit(self.groupBox_5)
        self.textEdit_content.setObjectName(u"textEdit_content")
        self.textEdit_content.setGeometry(QRect(10, 70, 611, 471))
        self.textEdit_content.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(11)
        self.textEdit_content.setFont(font)
        self.lineEdit_name = QLineEdit(self.groupBox_5)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(10, 30, 431, 31))
        self.lineEdit_name.setAlignment(Qt.AlignCenter)
        self.checkBox_show_subtitles = QCheckBox(self.groupBox_5)
        self.checkBox_show_subtitles.setObjectName(u"checkBox_show_subtitles")
        self.checkBox_show_subtitles.setGeometry(QRect(480, 30, 121, 31))
        self.pushButton_save_place = QPushButton(Dialog_place_edit)
        self.pushButton_save_place.setObjectName(u"pushButton_save_place")
        self.pushButton_save_place.setGeometry(QRect(270, 570, 121, 31))
        QWidget.setTabOrder(self.lineEdit_name, self.textEdit_content)
        QWidget.setTabOrder(self.textEdit_content, self.pushButton_save_place)

        self.retranslateUi(Dialog_place_edit)

        QMetaObject.connectSlotsByName(Dialog_place_edit)
    # setupUi

    def retranslateUi(self, Dialog_place_edit):
        Dialog_place_edit.setWindowTitle(QCoreApplication.translate("Dialog_place_edit", u"Dialog", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog_place_edit", u"\u6587\u6848\u5185\u5bb9", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("Dialog_place_edit", u"\u540d\u79f0", None))
        self.checkBox_show_subtitles.setText(QCoreApplication.translate("Dialog_place_edit", u"\u64ad\u653e\u65f6\u663e\u793a\u5b57\u5e55", None))
        self.pushButton_save_place.setText(QCoreApplication.translate("Dialog_place_edit", u"\u4fdd\u5b58", None))
    # retranslateUi

