# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tts.ui'
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
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QTextBrowser, QTextEdit,
    QWidget)

class Ui_Dialog_tts(object):
    def setupUi(self, Dialog_tts):
        if not Dialog_tts.objectName():
            Dialog_tts.setObjectName(u"Dialog_tts")
        Dialog_tts.resize(640, 480)
        Dialog_tts.setMinimumSize(QSize(640, 480))
        Dialog_tts.setMaximumSize(QSize(640, 480))
        self.groupBox = QGroupBox(Dialog_tts)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 621, 231))
        self.textEdit_tts_content = QTextEdit(self.groupBox)
        self.textEdit_tts_content.setObjectName(u"textEdit_tts_content")
        self.textEdit_tts_content.setGeometry(QRect(0, 20, 511, 211))
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(520, 20, 101, 191))
        self.comboBox_voice_name = QComboBox(self.groupBox_5)
        self.comboBox_voice_name.setObjectName(u"comboBox_voice_name")
        self.comboBox_voice_name.setGeometry(QRect(0, 20, 101, 26))
        self.comboBox_voice_role = QComboBox(self.groupBox_5)
        self.comboBox_voice_role.setObjectName(u"comboBox_voice_role")
        self.comboBox_voice_role.setGeometry(QRect(0, 60, 101, 26))
        self.comboBox_voice_style = QComboBox(self.groupBox_5)
        self.comboBox_voice_style.setObjectName(u"comboBox_voice_style")
        self.comboBox_voice_style.setGeometry(QRect(0, 100, 101, 26))
        self.pushButton_voice_list = QPushButton(self.groupBox_5)
        self.pushButton_voice_list.setObjectName(u"pushButton_voice_list")
        self.pushButton_voice_list.setGeometry(QRect(0, 150, 101, 31))
        self.groupBox_3 = QGroupBox(Dialog_tts)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 250, 411, 51))
        self.lineEdit_tts_ssml_txt_path = QLineEdit(self.groupBox_3)
        self.lineEdit_tts_ssml_txt_path.setObjectName(u"lineEdit_tts_ssml_txt_path")
        self.lineEdit_tts_ssml_txt_path.setEnabled(False)
        self.lineEdit_tts_ssml_txt_path.setGeometry(QRect(50, 20, 281, 21))
        self.pushButton_tts_ssml_txt_path = QPushButton(self.groupBox_3)
        self.pushButton_tts_ssml_txt_path.setObjectName(u"pushButton_tts_ssml_txt_path")
        self.pushButton_tts_ssml_txt_path.setEnabled(False)
        self.pushButton_tts_ssml_txt_path.setGeometry(QRect(330, 20, 71, 21))
        self.groupBox_4 = QGroupBox(Dialog_tts)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 310, 411, 81))
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 31, 21))
        self.lineEdit_output_name = QLineEdit(self.groupBox_4)
        self.lineEdit_output_name.setObjectName(u"lineEdit_output_name")
        self.lineEdit_output_name.setGeometry(QRect(50, 50, 281, 21))
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 31, 21))
        self.lineEdit_output_path = QLineEdit(self.groupBox_4)
        self.lineEdit_output_path.setObjectName(u"lineEdit_output_path")
        self.lineEdit_output_path.setGeometry(QRect(50, 20, 281, 21))
        self.pushButton_output_path = QPushButton(self.groupBox_4)
        self.pushButton_output_path.setObjectName(u"pushButton_output_path")
        self.pushButton_output_path.setEnabled(True)
        self.pushButton_output_path.setGeometry(QRect(330, 20, 71, 21))
        self.checkBox_auto_overwrite = QCheckBox(self.groupBox_4)
        self.checkBox_auto_overwrite.setObjectName(u"checkBox_auto_overwrite")
        self.checkBox_auto_overwrite.setGeometry(QRect(340, 50, 61, 21))
        self.textBrowser_tts = QTextBrowser(Dialog_tts)
        self.textBrowser_tts.setObjectName(u"textBrowser_tts")
        self.textBrowser_tts.setGeometry(QRect(10, 400, 621, 71))
        self.groupBox_2 = QGroupBox(Dialog_tts)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(430, 250, 91, 141))
        self.radioButton_content = QRadioButton(self.groupBox_2)
        self.radioButton_content.setObjectName(u"radioButton_content")
        self.radioButton_content.setGeometry(QRect(10, 20, 81, 31))
        self.radioButton_content.setChecked(True)
        self.radioButton_ssml = QRadioButton(self.groupBox_2)
        self.radioButton_ssml.setObjectName(u"radioButton_ssml")
        self.radioButton_ssml.setGeometry(QRect(10, 50, 81, 31))
        self.pushButton_start = QPushButton(Dialog_tts)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(530, 260, 101, 131))

        self.retranslateUi(Dialog_tts)

        QMetaObject.connectSlotsByName(Dialog_tts)
    # setupUi

    def retranslateUi(self, Dialog_tts):
        Dialog_tts.setWindowTitle(QCoreApplication.translate("Dialog_tts", u"\u8bed\u97f3\u5408\u6210", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_tts", u"\u8bed\u97f3\u5185\u5bb9", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog_tts", u"\u914d\u97f3/\u89d2\u8272/\u98ce\u683c", None))
        self.pushButton_voice_list.setText(QCoreApplication.translate("Dialog_tts", u"\u66f4\u65b0\u914d\u97f3\u5217\u8868", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog_tts", u"SSML/TXT", None))
        self.pushButton_tts_ssml_txt_path.setText(QCoreApplication.translate("Dialog_tts", u"\u6d4f\u89c8", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog_tts", u"\u8f93\u51fa", None))
        self.label.setText(QCoreApplication.translate("Dialog_tts", u"\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_tts", u"\u76ee\u5f55", None))
        self.pushButton_output_path.setText(QCoreApplication.translate("Dialog_tts", u"\u6d4f\u89c8", None))
        self.checkBox_auto_overwrite.setText(QCoreApplication.translate("Dialog_tts", u"\u8986\u76d6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_tts", u"\u5408\u6210\u9009\u62e9", None))
        self.radioButton_content.setText(QCoreApplication.translate("Dialog_tts", u"\u4f7f\u7528\u5185\u5bb9", None))
        self.radioButton_ssml.setText(QCoreApplication.translate("Dialog_tts", u"\u4f7f\u7528SSML", None))
        self.pushButton_start.setText(QCoreApplication.translate("Dialog_tts", u"\u5f00\u59cb\u5408\u6210", None))
    # retranslateUi

