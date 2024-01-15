import copy
import os

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from app.views.ui import Ui_Dialog_setting
from app.views.sender import view_sender


class SettingView(QtWidgets.QDialog, Ui_Dialog_setting):
    def __init__(self, icon_path=None):
        super(SettingView, self).__init__()
        self.setupUi(self)
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.user_data_dir = ""
        self.pushButton_save_setting.clicked.connect(self.send_data)
        self.pushButton_user_data_dir.clicked.connect(self.set_chrome_user_data_dir)
        self.data = {}

    def show_edit(self, data):
        if data:
            self.data = data
            self.lineEdit_user_data_dir.setText(self.data.get("chrome_user_data_path"))
            self.lineEdit_azure_key.setText(self.data.get("azure_key"))
            self.lineEdit_azure_region.setText(self.data.get("azure_region"))
            self.checkBox_kiosk.setChecked(True if self.data.get("kiosk") else False)
            if self.data.get("screen_offset_x"):
                self.spinBox_screen_offset_x.setValue(self.data.get("screen_offset_x"))
            if self.data.get("screen_offset_y"):
                self.spinBox_screen_offset_y.setValue(self.data.get("screen_offset_y"))
            if self.data.get("source_screen_x"):
                self.spinBox_source_screen_x.setValue(self.data.get("source_screen_x"))
            if self.data.get("source_screen_y"):
                self.spinBox_source_screen_y.setValue(self.data.get("source_screen_y"))

            if self.data.get("js_server"):
                self.lineEdit_js_server.setText(self.data.get("js_server"))
            if self.data.get("cesium_base_url"):
                self.lineEdit_cesium_base_url.setText(self.data.get("cesium_base_url"))
            if self.data.get("font_server"):
                self.lineEdit_font_server.setText(self.data.get("font_server"))
            if self.data.get("media_server"):
                self.lineEdit_media_server.setText(self.data.get("media_server"))
        self.show()

    def send_data(self):
        self.close()
        self.data.update({
            "chrome_user_data_path": self.lineEdit_user_data_dir.text(),
            "azure_key": self.lineEdit_azure_key.text(),
            "azure_region": self.lineEdit_azure_region.text(),
            "kiosk": 1 if self.checkBox_kiosk.isChecked() else 0,

            "screen_offset_x": self.spinBox_screen_offset_x.value(),
            "screen_offset_y": self.spinBox_screen_offset_y.value(),
            "source_screen_x": self.spinBox_source_screen_x.value(),
            "source_screen_y": self.spinBox_source_screen_y.value(),

            "js_server": self.lineEdit_js_server.text(),
            "cesium_base_url": self.lineEdit_cesium_base_url.text(),
            "font_server": self.lineEdit_font_server.text(),
            "media_server": self.lineEdit_media_server.text()
        })
        view_sender.setting.save.emit(copy.deepcopy(self.data))

    def set_chrome_user_data_dir(self):
        self.user_data_dir = QtWidgets.QFileDialog.getExistingDirectory(self, caption='选择Chrome用户数据目录')
        if self.user_data_dir:
            self.lineEdit_user_data_dir.setText(self.user_data_dir)
