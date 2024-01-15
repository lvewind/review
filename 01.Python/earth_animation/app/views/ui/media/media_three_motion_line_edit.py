# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'media_three_motion_line_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Dialog_media_three_motion_line_edit(object):
    def setupUi(self, Dialog_media_three_motion_line_edit):
        if not Dialog_media_three_motion_line_edit.objectName():
            Dialog_media_three_motion_line_edit.setObjectName(u"Dialog_media_three_motion_line_edit")
        Dialog_media_three_motion_line_edit.setWindowModality(Qt.ApplicationModal)
        Dialog_media_three_motion_line_edit.resize(480, 540)
        self.pushButton = QPushButton(Dialog_media_three_motion_line_edit)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 460, 121, 41))
        self.groupBox_three = QGroupBox(Dialog_media_three_motion_line_edit)
        self.groupBox_three.setObjectName(u"groupBox_three")
        self.groupBox_three.setGeometry(QRect(10, 20, 461, 421))
        self.pushButton_media_three = QPushButton(self.groupBox_three)
        self.pushButton_media_three.setObjectName(u"pushButton_media_three")
        self.pushButton_media_three.setGeometry(QRect(390, 30, 71, 61))
        self.plainTextEdit_media_path_three = QPlainTextEdit(self.groupBox_three)
        self.plainTextEdit_media_path_three.setObjectName(u"plainTextEdit_media_path_three")
        self.plainTextEdit_media_path_three.setGeometry(QRect(0, 30, 391, 61))
        self.groupBox_motion_line = QGroupBox(self.groupBox_three)
        self.groupBox_motion_line.setObjectName(u"groupBox_motion_line")
        self.groupBox_motion_line.setGeometry(QRect(0, 170, 461, 131))
        self.label_33 = QLabel(self.groupBox_motion_line)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(310, 30, 31, 31))
        self.label_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_25 = QLabel(self.groupBox_motion_line)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(160, 30, 31, 31))
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.spinBox_motion_line_weight = QSpinBox(self.groupBox_motion_line)
        self.spinBox_motion_line_weight.setObjectName(u"spinBox_motion_line_weight")
        self.spinBox_motion_line_weight.setGeometry(QRect(190, 30, 111, 31))
        self.spinBox_motion_line_weight.setMinimum(1)
        self.spinBox_motion_line_weight.setMaximum(6400000)
        self.spinBox_motion_line_weight.setValue(100)
        self.spinBox_motion_line_speed = QSpinBox(self.groupBox_motion_line)
        self.spinBox_motion_line_speed.setObjectName(u"spinBox_motion_line_speed")
        self.spinBox_motion_line_speed.setGeometry(QRect(340, 30, 111, 31))
        self.spinBox_motion_line_speed.setMinimum(1)
        self.spinBox_motion_line_speed.setMaximum(99999)
        self.spinBox_motion_line_speed.setValue(1)
        self.label_19 = QLabel(self.groupBox_motion_line)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 30, 31, 31))
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.comboBox_motion_line_color = QComboBox(self.groupBox_motion_line)
        self.comboBox_motion_line_color.setObjectName(u"comboBox_motion_line_color")
        self.comboBox_motion_line_color.setGeometry(QRect(40, 30, 111, 31))
        self.spinBox_motion_line_time = QSpinBox(self.groupBox_motion_line)
        self.spinBox_motion_line_time.setObjectName(u"spinBox_motion_line_time")
        self.spinBox_motion_line_time.setGeometry(QRect(340, 80, 111, 31))
        self.spinBox_motion_line_time.setMinimum(1)
        self.spinBox_motion_line_time.setMaximum(99999)
        self.spinBox_motion_line_time.setValue(1)
        self.spinBox_motion_line_divide = QSpinBox(self.groupBox_motion_line)
        self.spinBox_motion_line_divide.setObjectName(u"spinBox_motion_line_divide")
        self.spinBox_motion_line_divide.setGeometry(QRect(190, 80, 111, 31))
        self.spinBox_motion_line_divide.setMinimum(1)
        self.spinBox_motion_line_divide.setMaximum(6400000)
        self.spinBox_motion_line_divide.setValue(100)
        self.label_34 = QLabel(self.groupBox_motion_line)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(310, 80, 31, 31))
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_35 = QLabel(self.groupBox_motion_line)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(160, 80, 31, 31))
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.spinBox_motion_line_height = QSpinBox(self.groupBox_motion_line)
        self.spinBox_motion_line_height.setObjectName(u"spinBox_motion_line_height")
        self.spinBox_motion_line_height.setGeometry(QRect(40, 80, 111, 31))
        self.spinBox_motion_line_height.setMinimum(1)
        self.spinBox_motion_line_height.setMaximum(6400000)
        self.spinBox_motion_line_height.setValue(100)
        self.label_36 = QLabel(self.groupBox_motion_line)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 80, 31, 31))
        self.label_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.retranslateUi(Dialog_media_three_motion_line_edit)

        QMetaObject.connectSlotsByName(Dialog_media_three_motion_line_edit)
    # setupUi

    def retranslateUi(self, Dialog_media_three_motion_line_edit):
        Dialog_media_three_motion_line_edit.setWindowTitle(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"\u4fdd\u5b58", None))
        self.groupBox_three.setTitle(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"\u8fd0\u52a8\u66f2\u7ebf\u8bbe\u7f6e", None))
        self.pushButton_media_three.setText(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"\u6d4f\u89c8\u6587\u4ef6", None))
        self.plainTextEdit_media_path_three.setPlaceholderText(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"KML\u6587\u4ef6\u8def\u5f84", None))
        self.groupBox_motion_line.setTitle(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"3D\u66f2\u7ebf\u8bbe\u7f6e", None))
        self.label_33.setText(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"\u901f\u5ea6", None))
        self.label_25.setText(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"\u7ebf\u5bbd", None))
        self.label_19.setText(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"\u989c\u8272", None))
        self.label_34.setText(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"\u65f6\u95f4", None))
        self.label_35.setText(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"\u6bb5\u6570", None))
        self.label_36.setText(QCoreApplication.translate("Dialog_media_three_motion_line_edit", u"\u9ad8\u5ea6", None))
    # retranslateUi

