import os

from PySide6 import QtWidgets

import hiworker
from .common import CommonDataListView
from .ui import *


class AccountView(QtWidgets.QMainWindow, Ui_MainWindowAccount):
    def __init__(self):
        super(AccountView, self).__init__()
        self.setupUi(self)

    def init_account_table_header(self, table_setting: dict):
        hiworker.TableLoad.init_table_header(self.tableWidget_account, table_setting)

    # 客户页面
    def load_table_account(self, data: list, table_setting: dict, select_last_row=False):
        hiworker.TableLoad.load_table(self.tableWidget_account, data, table_setting, select_last_row=select_last_row)

    def get_selected_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_account)

    def get_selected_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_account)


# 列表项创建/编辑对话框
class AccountAddView(QtWidgets.QDialog, Ui_DialogAccount):
    def __init__(self):
        super(AccountAddView, self).__init__()
        self.setupUi(self)

        self.pushButton_regional.clicked.connect(self.show_regional_list)
        self.pushButton_teamup_img.clicked.connect(self.open_teamup_img_folder)
        self.pushButton_login_img.clicked.connect(self.open_login_img_folder)

        self.dialog_regional_list = CommonDataListView("请选择角色所在服务器")
        self.dialog_teammate_img_list = CommonDataListView("请选择组队队友选择列表图片")
        self.dialog_login_img_list = CommonDataListView("请选择登录界面图片")

        self.data = {}

    def show_add(self):
        self.data = {}
        self.lineEdit_new_list_name.clear()
        self.radioButton_android.setChecked(True)
        self.lineEdit_regional.clear()
        self.checkBox_remember_password.setChecked(False)
        self.checkBox_change_role.setChecked(False)
        self.lineEdit_teamup_img.clear()
        self.lineEdit_login_img.clear()
        self.show()

    def show_edit(self, account_dict: dict):
        self.data = account_dict
        self.lineEdit_new_list_name.setText(account_dict.get("name"))
        if account_dict.get("platform") == "AOS":
            self.radioButton_android.setChecked(True)
        elif account_dict.get("platform") == "iOS":
            self.radioButton_iOS.setChecked(True)
        self.lineEdit_regional.setText(account_dict.get("regional"))
        self.checkBox_remember_password.setChecked(account_dict.get("remember_password", 0))
        self.checkBox_change_role.setChecked(account_dict.get("change_role", 0))
        self.lineEdit_teamup_img.setText(account_dict.get("teamup_img"))
        self.lineEdit_login_img.setText(account_dict.get("login_img"))
        self.show()

    def show_regional_list(self):
        self.dialog_regional_list.show()

    def open_teamup_img_folder(self):
        file_name = self.open_folder("storage/user/teamup_img", "选择组队图片")
        self.lineEdit_teamup_img.setText(os.path.splitext(file_name)[0])

    def open_login_img_folder(self):
        file_name = self.open_folder("storage/user/login_img", "选择登录图片")
        self.lineEdit_login_img.setText(os.path.splitext(file_name)[0])

    def open_folder(self, path: str, caption: str):
        cwd = os.path.abspath("")
        img_path = cwd + os.path.sep + path
        openfile_name, openfile_type = QtWidgets.QFileDialog.getOpenFileName(self, caption=caption, dir=img_path, filter="*.png")
        file_name = openfile_name.split("/")
        file_name = file_name[len(file_name) - 1]
        return file_name

    def get_account_data(self):
        name = self.lineEdit_new_list_name.text()
        platform = 0
        if self.radioButton_android.isChecked():
            platform = "AOS"
        elif self.radioButton_iOS.isChecked():
            platform = "iOS"
        # regional = self.lineEdit_regional.text()
        remember_password = self.checkBox_remember_password.isChecked()
        change_role = self.checkBox_change_role.isChecked()
        teamup_img = self.lineEdit_teamup_img.text()
        login_img = self.lineEdit_login_img.text()
        self.data.update({
            "name": name,
            "platform": platform,
            "remember_password": 1 if remember_password else 0,
            "change_role": 1 if change_role else 0,
            "teamup_img": teamup_img,
            "login_img": login_img
        })

        return self.data
