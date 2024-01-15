# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Dialog_setting(object):
    def setupUi(self, Dialog_setting):
        if not Dialog_setting.objectName():
            Dialog_setting.setObjectName(u"Dialog_setting")
        Dialog_setting.setWindowModality(Qt.ApplicationModal)
        Dialog_setting.resize(720, 480)
        Dialog_setting.setMinimumSize(QSize(720, 480))
        Dialog_setting.setMaximumSize(QSize(720, 480))
        self.groupBox = QGroupBox(Dialog_setting)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 20, 351, 61))
        self.lineEdit_user_data_dir = QLineEdit(self.groupBox)
        self.lineEdit_user_data_dir.setObjectName(u"lineEdit_user_data_dir")
        self.lineEdit_user_data_dir.setGeometry(QRect(10, 20, 271, 31))
        self.pushButton_user_data_dir = QPushButton(self.groupBox)
        self.pushButton_user_data_dir.setObjectName(u"pushButton_user_data_dir")
        self.pushButton_user_data_dir.setGeometry(QRect(280, 20, 71, 31))
        self.groupBox_2 = QGroupBox(Dialog_setting)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(360, 20, 351, 61))
        self.lineEdit_azure_key = QLineEdit(self.groupBox_2)
        self.lineEdit_azure_key.setObjectName(u"lineEdit_azure_key")
        self.lineEdit_azure_key.setGeometry(QRect(10, 20, 271, 31))
        self.lineEdit_azure_region = QLineEdit(self.groupBox_2)
        self.lineEdit_azure_region.setObjectName(u"lineEdit_azure_region")
        self.lineEdit_azure_region.setGeometry(QRect(280, 20, 71, 31))
        self.pushButton_save_setting = QPushButton(Dialog_setting)
        self.pushButton_save_setting.setObjectName(u"pushButton_save_setting")
        self.pushButton_save_setting.setGeometry(QRect(320, 410, 81, 31))
        self.checkBox_kiosk = QCheckBox(Dialog_setting)
        self.checkBox_kiosk.setObjectName(u"checkBox_kiosk")
        self.checkBox_kiosk.setGeometry(QRect(310, 340, 101, 31))
        self.groupBox_3 = QGroupBox(Dialog_setting)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 180, 351, 61))
        self.lineEdit_js_server = QLineEdit(self.groupBox_3)
        self.lineEdit_js_server.setObjectName(u"lineEdit_js_server")
        self.lineEdit_js_server.setGeometry(QRect(10, 20, 331, 31))
        self.groupBox_4 = QGroupBox(Dialog_setting)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 250, 351, 61))
        self.lineEdit_cesium_base_url = QLineEdit(self.groupBox_4)
        self.lineEdit_cesium_base_url.setObjectName(u"lineEdit_cesium_base_url")
        self.lineEdit_cesium_base_url.setGeometry(QRect(10, 20, 331, 31))
        self.groupBox_5 = QGroupBox(Dialog_setting)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(360, 180, 351, 61))
        self.lineEdit_media_server = QLineEdit(self.groupBox_5)
        self.lineEdit_media_server.setObjectName(u"lineEdit_media_server")
        self.lineEdit_media_server.setGeometry(QRect(10, 20, 331, 31))
        self.groupBox_6 = QGroupBox(Dialog_setting)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(360, 250, 351, 61))
        self.lineEdit_font_server = QLineEdit(self.groupBox_6)
        self.lineEdit_font_server.setObjectName(u"lineEdit_font_server")
        self.lineEdit_font_server.setGeometry(QRect(10, 20, 331, 31))
        self.groupBox_7 = QGroupBox(Dialog_setting)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(0, 90, 711, 80))
        self.spinBox_screen_offset_x = QSpinBox(self.groupBox_7)
        self.spinBox_screen_offset_x.setObjectName(u"spinBox_screen_offset_x")
        self.spinBox_screen_offset_x.setGeometry(QRect(80, 30, 91, 31))
        self.spinBox_screen_offset_x.setMinimum(-9999)
        self.spinBox_screen_offset_x.setMaximum(9999)
        self.spinBox_screen_offset_x.setValue(2560)
        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 61, 31))
        self.spinBox_screen_offset_y = QSpinBox(self.groupBox_7)
        self.spinBox_screen_offset_y.setObjectName(u"spinBox_screen_offset_y")
        self.spinBox_screen_offset_y.setGeometry(QRect(260, 30, 91, 31))
        self.spinBox_screen_offset_y.setMinimum(-9999)
        self.spinBox_screen_offset_y.setMaximum(9999)
        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 30, 61, 31))
        self.spinBox_source_screen_x = QSpinBox(self.groupBox_7)
        self.spinBox_source_screen_x.setObjectName(u"spinBox_source_screen_x")
        self.spinBox_source_screen_x.setGeometry(QRect(440, 30, 91, 31))
        self.spinBox_source_screen_x.setMinimum(-9999)
        self.spinBox_source_screen_x.setMaximum(9999)
        self.spinBox_source_screen_x.setValue(2560)
        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 30, 61, 31))
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(540, 30, 61, 31))
        self.spinBox_source_screen_y = QSpinBox(self.groupBox_7)
        self.spinBox_source_screen_y.setObjectName(u"spinBox_source_screen_y")
        self.spinBox_source_screen_y.setGeometry(QRect(610, 30, 91, 31))
        self.spinBox_source_screen_y.setMinimum(-9999)
        self.spinBox_source_screen_y.setMaximum(9999)
        self.spinBox_source_screen_y.setValue(1440)

        self.retranslateUi(Dialog_setting)

        QMetaObject.connectSlotsByName(Dialog_setting)
    # setupUi

    def retranslateUi(self, Dialog_setting):
        Dialog_setting.setWindowTitle(QCoreApplication.translate("Dialog_setting", u"\u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_setting", u"\u6d4f\u89c8\u5668\u914d\u7f6e\u6587\u4ef6\u8def\u5f84", None))
        self.pushButton_user_data_dir.setText(QCoreApplication.translate("Dialog_setting", u"\u6d4f\u89c8", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_setting", u"azure_key", None))
        self.pushButton_save_setting.setText(QCoreApplication.translate("Dialog_setting", u"\u4fdd\u5b58", None))
        self.checkBox_kiosk.setText(QCoreApplication.translate("Dialog_setting", u"\u542f\u7528\u5168\u5c4f\u6a21\u5f0f", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog_setting", u"JsServer", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog_setting", u"CesiumBaseUrl", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog_setting", u"MediaServer", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog_setting", u"FontServer", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog_setting", u"\u526f\u5c4f\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("Dialog_setting", u"\u5c4f\u5e55\u504f\u79fbX", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_setting", u"\u5c4f\u5e55\u504f\u79fbY", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_setting", u"\u539f\u59cb\u5c4f\u5e55\u5bbd", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_setting", u"\u539f\u59cb\u5c4f\u5e55\u9ad8", None))
    # retranslateUi

