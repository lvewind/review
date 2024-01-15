# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_fonts.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_set_fonts(object):
    def setupUi(self, Dialog_set_fonts):
        if not Dialog_set_fonts.objectName():
            Dialog_set_fonts.setObjectName(u"Dialog_set_fonts")
        Dialog_set_fonts.setWindowModality(Qt.ApplicationModal)
        Dialog_set_fonts.resize(320, 240)
        Dialog_set_fonts.setMinimumSize(QSize(320, 240))
        Dialog_set_fonts.setMaximumSize(QSize(320, 240))
        self.comboBox_font_size = QComboBox(Dialog_set_fonts)
        self.comboBox_font_size.setObjectName(u"comboBox_font_size")
        self.comboBox_font_size.setGeometry(QRect(70, 90, 121, 31))
        self.comboBox_font = QComboBox(Dialog_set_fonts)
        self.comboBox_font.setObjectName(u"comboBox_font")
        self.comboBox_font.setGeometry(QRect(70, 40, 121, 31))
        self.label_11 = QLabel(Dialog_set_fonts)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 90, 31, 31))
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(Dialog_set_fonts)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 40, 31, 31))
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton = QPushButton(Dialog_set_fonts)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 190, 81, 31))
        self.comboBox_font_color = QComboBox(Dialog_set_fonts)
        self.comboBox_font_color.setObjectName(u"comboBox_font_color")
        self.comboBox_font_color.setGeometry(QRect(70, 140, 121, 31))
        self.label_12 = QLabel(Dialog_set_fonts)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 140, 31, 31))
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.checkBox_font = QCheckBox(Dialog_set_fonts)
        self.checkBox_font.setObjectName(u"checkBox_font")
        self.checkBox_font.setGeometry(QRect(210, 39, 71, 31))
        self.checkBox_font_size = QCheckBox(Dialog_set_fonts)
        self.checkBox_font_size.setObjectName(u"checkBox_font_size")
        self.checkBox_font_size.setGeometry(QRect(210, 89, 71, 31))
        self.checkBox_font_color = QCheckBox(Dialog_set_fonts)
        self.checkBox_font_color.setObjectName(u"checkBox_font_color")
        self.checkBox_font_color.setGeometry(QRect(210, 139, 71, 31))

        self.retranslateUi(Dialog_set_fonts)

        QMetaObject.connectSlotsByName(Dialog_set_fonts)
    # setupUi

    def retranslateUi(self, Dialog_set_fonts):
        Dialog_set_fonts.setWindowTitle(QCoreApplication.translate("Dialog_set_fonts", u"\u8bbe\u7f6e\u5b57\u4f53", None))
        self.label_11.setText(QCoreApplication.translate("Dialog_set_fonts", u"\u5b57\u53f7", None))
        self.label_10.setText(QCoreApplication.translate("Dialog_set_fonts", u"\u5b57\u4f53", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_set_fonts", u"\u4fdd\u5b58", None))
        self.label_12.setText(QCoreApplication.translate("Dialog_set_fonts", u"\u989c\u8272", None))
        self.checkBox_font.setText(QCoreApplication.translate("Dialog_set_fonts", u"\u66f4\u65b0\u5b57\u4f53", None))
        self.checkBox_font_size.setText(QCoreApplication.translate("Dialog_set_fonts", u"\u66f4\u65b0\u5b57\u53f7", None))
        self.checkBox_font_color.setText(QCoreApplication.translate("Dialog_set_fonts", u"\u66f4\u65b0\u989c\u8272", None))
    # retranslateUi

