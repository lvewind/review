# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_voices.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QDoubleSpinBox, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog_set_voices(object):
    def setupUi(self, Dialog_set_voices):
        if not Dialog_set_voices.objectName():
            Dialog_set_voices.setObjectName(u"Dialog_set_voices")
        Dialog_set_voices.setWindowModality(Qt.ApplicationModal)
        Dialog_set_voices.resize(360, 240)
        Dialog_set_voices.setMinimumSize(QSize(360, 240))
        Dialog_set_voices.setMaximumSize(QSize(360, 240))
        self.groupBox_voice = QGroupBox(Dialog_set_voices)
        self.groupBox_voice.setObjectName(u"groupBox_voice")
        self.groupBox_voice.setGeometry(QRect(20, 20, 321, 141))
        self.comboBox_voice_name = QComboBox(self.groupBox_voice)
        self.comboBox_voice_name.setObjectName(u"comboBox_voice_name")
        self.comboBox_voice_name.setGeometry(QRect(40, 20, 111, 31))
        self.comboBox_voice_role = QComboBox(self.groupBox_voice)
        self.comboBox_voice_role.setObjectName(u"comboBox_voice_role")
        self.comboBox_voice_role.setGeometry(QRect(40, 60, 111, 31))
        self.comboBox_voice_style = QComboBox(self.groupBox_voice)
        self.comboBox_voice_style.setObjectName(u"comboBox_voice_style")
        self.comboBox_voice_style.setGeometry(QRect(40, 100, 111, 31))
        self.label_39 = QLabel(self.groupBox_voice)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 100, 31, 31))
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_40 = QLabel(self.groupBox_voice)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 20, 31, 31))
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_41 = QLabel(self.groupBox_voice)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 60, 31, 31))
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.doubleSpinBox_voice_pitch = QDoubleSpinBox(self.groupBox_voice)
        self.doubleSpinBox_voice_pitch.setObjectName(u"doubleSpinBox_voice_pitch")
        self.doubleSpinBox_voice_pitch.setGeometry(QRect(200, 100, 111, 31))
        self.doubleSpinBox_voice_pitch.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_voice_pitch.setDecimals(1)
        self.doubleSpinBox_voice_pitch.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_voice_pitch.setValue(1.000000000000000)
        self.doubleSpinBox_voice_rate = QDoubleSpinBox(self.groupBox_voice)
        self.doubleSpinBox_voice_rate.setObjectName(u"doubleSpinBox_voice_rate")
        self.doubleSpinBox_voice_rate.setGeometry(QRect(200, 20, 111, 31))
        self.doubleSpinBox_voice_rate.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_voice_rate.setDecimals(1)
        self.doubleSpinBox_voice_rate.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_voice_rate.setValue(1.000000000000000)
        self.label_35 = QLabel(self.groupBox_voice)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(170, 60, 31, 31))
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_34 = QLabel(self.groupBox_voice)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(170, 20, 31, 31))
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_36 = QLabel(self.groupBox_voice)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(170, 100, 31, 31))
        self.label_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.doubleSpinBox_voice_volume = QDoubleSpinBox(self.groupBox_voice)
        self.doubleSpinBox_voice_volume.setObjectName(u"doubleSpinBox_voice_volume")
        self.doubleSpinBox_voice_volume.setGeometry(QRect(200, 60, 111, 31))
        self.doubleSpinBox_voice_volume.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_voice_volume.setDecimals(1)
        self.doubleSpinBox_voice_volume.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_voice_volume.setValue(1.000000000000000)
        self.pushButton = QPushButton(Dialog_set_voices)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 180, 111, 31))

        self.retranslateUi(Dialog_set_voices)

        QMetaObject.connectSlotsByName(Dialog_set_voices)
    # setupUi

    def retranslateUi(self, Dialog_set_voices):
        Dialog_set_voices.setWindowTitle(QCoreApplication.translate("Dialog_set_voices", u"Dialog", None))
        self.groupBox_voice.setTitle(QCoreApplication.translate("Dialog_set_voices", u"\u914d\u97f3", None))
        self.label_39.setText(QCoreApplication.translate("Dialog_set_voices", u"\u98ce\u683c", None))
        self.label_40.setText(QCoreApplication.translate("Dialog_set_voices", u"\u97f3\u6e90", None))
        self.label_41.setText(QCoreApplication.translate("Dialog_set_voices", u"\u89d2\u8272", None))
        self.label_35.setText(QCoreApplication.translate("Dialog_set_voices", u"\u97f3\u91cf", None))
        self.label_34.setText(QCoreApplication.translate("Dialog_set_voices", u"\u8bed\u901f", None))
        self.label_36.setText(QCoreApplication.translate("Dialog_set_voices", u"\u97f3\u9ad8", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_set_voices", u"\u4fdd\u5b58", None))
    # retranslateUi

