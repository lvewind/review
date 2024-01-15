# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_run_list_set_teammate.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QGroupBox, QHeaderView, QRadioButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog_run_list_teammate_list(object):
    def setupUi(self, Dialog_run_list_teammate_list):
        if not Dialog_run_list_teammate_list.objectName():
            Dialog_run_list_teammate_list.setObjectName(u"Dialog_run_list_teammate_list")
        Dialog_run_list_teammate_list.setWindowModality(Qt.ApplicationModal)
        Dialog_run_list_teammate_list.resize(320, 420)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Dialog_run_list_teammate_list.setFont(font)
        self.buttonBox = QDialogButtonBox(Dialog_run_list_teammate_list)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(90, 370, 161, 32))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(8)
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tableWidget_data_list = QTableWidget(Dialog_run_list_teammate_list)
        if (self.tableWidget_data_list.columnCount() < 3):
            self.tableWidget_data_list.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_data_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_data_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_data_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_data_list.setObjectName(u"tableWidget_data_list")
        self.tableWidget_data_list.setGeometry(QRect(10, 70, 301, 291))
        self.tableWidget_data_list.setFont(font1)
        self.tableWidget_data_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_data_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_data_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_data_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_data_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_data_list.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_data_list.horizontalHeader().setHighlightSections(False)
        self.tableWidget_data_list.verticalHeader().setVisible(False)
        self.tableWidget_data_list.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_data_list.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_data_list.verticalHeader().setHighlightSections(False)
        self.groupBox_teammate_type_radio = QGroupBox(Dialog_run_list_teammate_list)
        self.groupBox_teammate_type_radio.setObjectName(u"groupBox_teammate_type_radio")
        self.groupBox_teammate_type_radio.setGeometry(QRect(10, 10, 301, 51))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setBold(False)
        self.groupBox_teammate_type_radio.setFont(font2)
        self.groupBox_teammate_type_radio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.radioButton_teammate_type_is_cross = QRadioButton(self.groupBox_teammate_type_radio)
        self.radioButton_teammate_type_is_cross.setObjectName(u"radioButton_teammate_type_is_cross")
        self.radioButton_teammate_type_is_cross.setGeometry(QRect(250, 20, 51, 21))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(9)
        font3.setBold(False)
        self.radioButton_teammate_type_is_cross.setFont(font3)
        self.radioButton_teammate_type_is_friends = QRadioButton(self.groupBox_teammate_type_radio)
        self.radioButton_teammate_type_is_friends.setObjectName(u"radioButton_teammate_type_is_friends")
        self.radioButton_teammate_type_is_friends.setGeometry(QRect(70, 20, 51, 21))
        self.radioButton_teammate_type_is_friends.setFont(font3)
        self.radioButton_teammate_type_is_default = QRadioButton(self.groupBox_teammate_type_radio)
        self.radioButton_teammate_type_is_default.setObjectName(u"radioButton_teammate_type_is_default")
        self.radioButton_teammate_type_is_default.setGeometry(QRect(10, 20, 51, 21))
        self.radioButton_teammate_type_is_default.setFont(font3)
        self.radioButton_teammate_type_is_default.setChecked(True)
        self.radioButton_teammate_type_is_guild = QRadioButton(self.groupBox_teammate_type_radio)
        self.radioButton_teammate_type_is_guild.setObjectName(u"radioButton_teammate_type_is_guild")
        self.radioButton_teammate_type_is_guild.setGeometry(QRect(130, 20, 51, 21))
        self.radioButton_teammate_type_is_guild.setFont(font3)
        self.radioButton_teammate_type_is_recent = QRadioButton(self.groupBox_teammate_type_radio)
        self.radioButton_teammate_type_is_recent.setObjectName(u"radioButton_teammate_type_is_recent")
        self.radioButton_teammate_type_is_recent.setGeometry(QRect(190, 20, 51, 21))
        self.radioButton_teammate_type_is_recent.setFont(font3)

        self.retranslateUi(Dialog_run_list_teammate_list)
        self.buttonBox.accepted.connect(Dialog_run_list_teammate_list.accept)
        self.buttonBox.rejected.connect(Dialog_run_list_teammate_list.reject)

        QMetaObject.connectSlotsByName(Dialog_run_list_teammate_list)
    # setupUi

    def retranslateUi(self, Dialog_run_list_teammate_list):
        Dialog_run_list_teammate_list.setWindowTitle(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u9009\u62e9\u961f\u53cb\u6240\u5728\u8fd0\u884c\u5217\u8868", None))
        ___qtablewidgetitem = self.tableWidget_data_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u8fd0\u884c\u5217\u8868ID", None));
        ___qtablewidgetitem1 = self.tableWidget_data_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u597d\u53cb\u8d26\u53f7ID", None));
        ___qtablewidgetitem2 = self.tableWidget_data_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u597d\u53cb\u540d\u79f0", None));
        self.groupBox_teammate_type_radio.setTitle(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u961f\u53cb\u7c7b\u578b", None))
        self.radioButton_teammate_type_is_cross.setText(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u8de8\u533a", None))
        self.radioButton_teammate_type_is_friends.setText(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u597d\u53cb", None))
        self.radioButton_teammate_type_is_default.setText(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u9ed8\u8ba4", None))
        self.radioButton_teammate_type_is_guild.setText(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u5bee\u53cb", None))
        self.radioButton_teammate_type_is_recent.setText(QCoreApplication.translate("Dialog_run_list_teammate_list", u"\u6700\u8fd1", None))
    # retranslateUi

