# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_size.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog_set_3d_size(object):
    def setupUi(self, Dialog_set_3d_size):
        if not Dialog_set_3d_size.objectName():
            Dialog_set_3d_size.setObjectName(u"Dialog_set_3d_size")
        Dialog_set_3d_size.setWindowModality(Qt.ApplicationModal)
        Dialog_set_3d_size.resize(320, 240)
        Dialog_set_3d_size.setMinimumSize(QSize(320, 240))
        Dialog_set_3d_size.setMaximumSize(QSize(320, 240))
        self.pushButton = QPushButton(Dialog_set_3d_size)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 180, 81, 31))
        self.label_30 = QLabel(Dialog_set_3d_size)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(40, 110, 31, 31))
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_24 = QLabel(Dialog_set_3d_size)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(40, 30, 31, 31))
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_23 = QLabel(Dialog_set_3d_size)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(40, 70, 31, 31))
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.spinBox_media_height = QSpinBox(Dialog_set_3d_size)
        self.spinBox_media_height.setObjectName(u"spinBox_media_height")
        self.spinBox_media_height.setGeometry(QRect(80, 70, 101, 31))
        self.spinBox_media_height.setMinimum(1)
        self.spinBox_media_height.setMaximum(99999)
        self.spinBox_media_height.setValue(100)
        self.spinBox_media_width = QSpinBox(Dialog_set_3d_size)
        self.spinBox_media_width.setObjectName(u"spinBox_media_width")
        self.spinBox_media_width.setGeometry(QRect(80, 30, 101, 31))
        self.spinBox_media_width.setMinimum(1)
        self.spinBox_media_width.setMaximum(99999)
        self.spinBox_media_width.setValue(100)
        self.spinBox_media_depth = QSpinBox(Dialog_set_3d_size)
        self.spinBox_media_depth.setObjectName(u"spinBox_media_depth")
        self.spinBox_media_depth.setGeometry(QRect(80, 110, 101, 31))
        self.spinBox_media_depth.setMinimum(1)
        self.spinBox_media_depth.setMaximum(99999)
        self.spinBox_media_depth.setValue(1)
        self.checkBox_media_width = QCheckBox(Dialog_set_3d_size)
        self.checkBox_media_width.setObjectName(u"checkBox_media_width")
        self.checkBox_media_width.setGeometry(QRect(200, 30, 81, 31))
        self.checkBox_media_width.setChecked(True)
        self.checkBox_media_height = QCheckBox(Dialog_set_3d_size)
        self.checkBox_media_height.setObjectName(u"checkBox_media_height")
        self.checkBox_media_height.setGeometry(QRect(200, 70, 81, 31))
        self.checkBox_media_depth = QCheckBox(Dialog_set_3d_size)
        self.checkBox_media_depth.setObjectName(u"checkBox_media_depth")
        self.checkBox_media_depth.setGeometry(QRect(200, 110, 81, 31))

        self.retranslateUi(Dialog_set_3d_size)

        QMetaObject.connectSlotsByName(Dialog_set_3d_size)
    # setupUi

    def retranslateUi(self, Dialog_set_3d_size):
        Dialog_set_3d_size.setWindowTitle(QCoreApplication.translate("Dialog_set_3d_size", u"\u6279\u91cf\u8bbe\u7f6e3D\u56fe\u7247\u5c3a\u5bf8", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_set_3d_size", u"\u4fdd\u5b58", None))
        self.label_30.setText(QCoreApplication.translate("Dialog_set_3d_size", u"\u7eb5\u6df1", None))
        self.label_24.setText(QCoreApplication.translate("Dialog_set_3d_size", u"\u5bbd\u5ea6", None))
        self.label_23.setText(QCoreApplication.translate("Dialog_set_3d_size", u"\u9ad8\u5ea6", None))
        self.checkBox_media_width.setText(QCoreApplication.translate("Dialog_set_3d_size", u"\u66f4\u65b0\u5bbd\u5ea6", None))
        self.checkBox_media_height.setText(QCoreApplication.translate("Dialog_set_3d_size", u"\u66f4\u65b0\u5bbd\u5ea6", None))
        self.checkBox_media_depth.setText(QCoreApplication.translate("Dialog_set_3d_size", u"\u66f4\u65b0\u7eb5\u6df1", None))
    # retranslateUi

