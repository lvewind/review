# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'media_three_kml_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_media_three_kml_edit(object):
    def setupUi(self, Dialog_media_three_kml_edit):
        if not Dialog_media_three_kml_edit.objectName():
            Dialog_media_three_kml_edit.setObjectName(u"Dialog_media_three_kml_edit")
        Dialog_media_three_kml_edit.setWindowModality(Qt.ApplicationModal)
        Dialog_media_three_kml_edit.resize(480, 540)
        self.pushButton = QPushButton(Dialog_media_three_kml_edit)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 460, 121, 41))
        self.groupBox_three = QGroupBox(Dialog_media_three_kml_edit)
        self.groupBox_three.setObjectName(u"groupBox_three")
        self.groupBox_three.setGeometry(QRect(10, 20, 461, 111))
        self.pushButton_media_three = QPushButton(self.groupBox_three)
        self.pushButton_media_three.setObjectName(u"pushButton_media_three")
        self.pushButton_media_three.setGeometry(QRect(390, 30, 71, 61))
        self.plainTextEdit_media_path_three = QPlainTextEdit(self.groupBox_three)
        self.plainTextEdit_media_path_three.setObjectName(u"plainTextEdit_media_path_three")
        self.plainTextEdit_media_path_three.setGeometry(QRect(0, 30, 391, 61))

        self.retranslateUi(Dialog_media_three_kml_edit)

        QMetaObject.connectSlotsByName(Dialog_media_three_kml_edit)
    # setupUi

    def retranslateUi(self, Dialog_media_three_kml_edit):
        Dialog_media_three_kml_edit.setWindowTitle(QCoreApplication.translate("Dialog_media_three_kml_edit", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_media_three_kml_edit", u"\u4fdd\u5b58", None))
        self.groupBox_three.setTitle(QCoreApplication.translate("Dialog_media_three_kml_edit", u"KML\u8bbe\u7f6e", None))
        self.pushButton_media_three.setText(QCoreApplication.translate("Dialog_media_three_kml_edit", u"\u6d4f\u89c8\u6587\u4ef6", None))
        self.plainTextEdit_media_path_three.setPlaceholderText(QCoreApplication.translate("Dialog_media_three_kml_edit", u"KML\u6587\u4ef6\u8def\u5f84", None))
    # retranslateUi

