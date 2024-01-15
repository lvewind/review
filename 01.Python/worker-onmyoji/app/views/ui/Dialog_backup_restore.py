# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_backup_restore.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog_backup_restore(object):
    def setupUi(self, Dialog_backup_restore):
        if not Dialog_backup_restore.objectName():
            Dialog_backup_restore.setObjectName(u"Dialog_backup_restore")
        Dialog_backup_restore.setWindowModality(Qt.ApplicationModal)
        Dialog_backup_restore.resize(320, 160)
        Dialog_backup_restore.setMinimumSize(QSize(320, 160))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(11)
        Dialog_backup_restore.setFont(font)
        self.label = QLabel(Dialog_backup_restore)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 90, 71, 16))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(9)
        self.label.setFont(font1)
        self.label_2 = QLabel(Dialog_backup_restore)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 90, 41, 16))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Dialog_backup_restore)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 90, 21, 16))
        self.label_3.setFont(font1)
        self.label_current = QLabel(Dialog_backup_restore)
        self.label_current.setObjectName(u"label_current")
        self.label_current.setGeometry(QRect(120, 90, 31, 16))
        self.label_current.setFont(font1)
        self.label_current.setAlignment(Qt.AlignCenter)
        self.label_total_count = QLabel(Dialog_backup_restore)
        self.label_total_count.setObjectName(u"label_total_count")
        self.label_total_count.setGeometry(QRect(210, 90, 31, 16))
        self.label_total_count.setFont(font1)
        self.label_total_count.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Dialog_backup_restore)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 30, 101, 16))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Dialog_backup_restore)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 60, 131, 16))
        self.label_5.setFont(font1)
        self.label_finish = QLabel(Dialog_backup_restore)
        self.label_finish.setObjectName(u"label_finish")
        self.label_finish.setGeometry(QRect(120, 120, 91, 16))
        self.label_finish.setFont(font1)
        self.label_finish.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog_backup_restore)

        QMetaObject.connectSlotsByName(Dialog_backup_restore)
    # setupUi

    def retranslateUi(self, Dialog_backup_restore):
        Dialog_backup_restore.setWindowTitle(QCoreApplication.translate("Dialog_backup_restore", u"\u6b63\u5728\u8fdb\u884c", None))
        self.label.setText(QCoreApplication.translate("Dialog_backup_restore", u"\u6b63\u5728\u5907\u4efd\u7b2c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_backup_restore", u"\u4e2a\uff0c\u5171", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_backup_restore", u"\u4e2a", None))
        self.label_current.setText("")
        self.label_total_count.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog_backup_restore", u"\u6b63\u5728\u8fdb\u884c\u6388\u6743\u5907\u4efd", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_backup_restore", u"\u5b8c\u6210\u4e4b\u524d\u8bf7\u52ff\u5173\u95ed\u7a0b\u5e8f", None))
        self.label_finish.setText("")
    # retranslateUi

