# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'media_edit.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QDoubleSpinBox, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_media_edit(object):
    def setupUi(self, Dialog_media_edit):
        if not Dialog_media_edit.objectName():
            Dialog_media_edit.setObjectName(u"Dialog_media_edit")
        Dialog_media_edit.setWindowModality(Qt.ApplicationModal)
        Dialog_media_edit.resize(480, 540)
        Dialog_media_edit.setMinimumSize(QSize(480, 320))
        self.groupBox_control = QGroupBox(Dialog_media_edit)
        self.groupBox_control.setObjectName(u"groupBox_control")
        self.groupBox_control.setGeometry(QRect(20, 20, 441, 211))
        self.doubleSpinBox_media_delay = QDoubleSpinBox(self.groupBox_control)
        self.doubleSpinBox_media_delay.setObjectName(u"doubleSpinBox_media_delay")
        self.doubleSpinBox_media_delay.setGeometry(QRect(280, 150, 151, 31))
        self.doubleSpinBox_media_delay.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_media_delay.setDecimals(1)
        self.doubleSpinBox_media_delay.setMaximum(100.000000000000000)
        self.doubleSpinBox_media_delay.setStepType(QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_media_delay.setValue(0.000000000000000)
        self.doubleSpinBox_media_time = QDoubleSpinBox(self.groupBox_control)
        self.doubleSpinBox_media_time.setObjectName(u"doubleSpinBox_media_time")
        self.doubleSpinBox_media_time.setGeometry(QRect(280, 90, 151, 31))
        self.doubleSpinBox_media_time.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_media_time.setDecimals(1)
        self.doubleSpinBox_media_time.setMaximum(100.000000000000000)
        self.doubleSpinBox_media_time.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_media_time.setValue(0.000000000000000)
        self.comboBox_media_show_type = QComboBox(self.groupBox_control)
        self.comboBox_media_show_type.setObjectName(u"comboBox_media_show_type")
        self.comboBox_media_show_type.setGeometry(QRect(70, 90, 151, 31))
        self.label_21 = QLabel(self.groupBox_control)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(250, 150, 31, 31))
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9 = QLabel(self.groupBox_control)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 150, 51, 31))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.comboBox_media_type = QComboBox(self.groupBox_control)
        self.comboBox_media_type.setObjectName(u"comboBox_media_type")
        self.comboBox_media_type.setGeometry(QRect(70, 150, 151, 31))
        self.label = QLabel(self.groupBox_control)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 51, 31))
        self.label_4 = QLabel(self.groupBox_control)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 90, 31, 31))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_12 = QLabel(self.groupBox_control)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 90, 51, 31))
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_media_name = QLineEdit(self.groupBox_control)
        self.lineEdit_media_name.setObjectName(u"lineEdit_media_name")
        self.lineEdit_media_name.setGeometry(QRect(70, 30, 361, 31))
        self.pushButton = QPushButton(Dialog_media_edit)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 460, 121, 41))

        self.retranslateUi(Dialog_media_edit)

        QMetaObject.connectSlotsByName(Dialog_media_edit)
    # setupUi

    def retranslateUi(self, Dialog_media_edit):
        Dialog_media_edit.setWindowTitle(QCoreApplication.translate("Dialog_media_edit", u"Dialog", None))
        self.groupBox_control.setTitle(QCoreApplication.translate("Dialog_media_edit", u"\u5a92\u4f53\u8bbe\u7f6e", None))
        self.label_21.setText(QCoreApplication.translate("Dialog_media_edit", u"\u5ef6\u8fdf", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_media_edit", u"\u5a92\u4f53\u7c7b\u578b", None))
        self.label.setText(QCoreApplication.translate("Dialog_media_edit", u"\u5a92\u4f53\u540d\u79f0", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_media_edit", u"\u6301\u7eed", None))
        self.label_12.setText(QCoreApplication.translate("Dialog_media_edit", u"\u663e\u793a\u6a21\u5f0f", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_media_edit", u"\u4fdd\u5b58", None))
    # retranslateUi

