from PySide6 import QtWidgets

import hiworker
from hiworker.views.ui.source import Ui_Dialog_run_list_add
from .ui import *


class RunListView(QtWidgets.QMainWindow, Ui_MainWindowRunList):
    def __init__(self):
        super(RunListView, self).__init__()
        self.setupUi(self)
        self.action_product = self.menubar.addAction("产品")
        self.action_plan = self.menubar.addAction("计划")
        self.action_account = self.menubar.addAction("账号")
        self.action_run_env = self.menubar.addAction("机器")

    def init_run_list_table_header(self, table_setting: dict):
        """
        初始化表头
        :return:
        """
        hiworker.TableLoad.init_table_header(self.tableWidget_run_list, table_setting)

    def init_run_count_table_header(self, table_setting: dict):
        hiworker.TableLoad.init_table_header(self.tableWidget_run_count, table_setting)

    def init_run_count_table(self, table_setting: dict):
        hiworker.TableLoad.init_table_col(self.tableWidget_run_count, table_setting)

    def load_table_run_list(self, data: list, table_setting: dict):
        """
        加载运行列表
        :return:
        """
        hiworker.TableLoad.load_table(self.tableWidget_run_list, data, table_setting)

    def load_table_row_run_list(self, row: int, data: dict, table_setting: dict):
        """
        加载运行列表单行
        :param table_setting:
        :param data:
        :param row:
        :return:
        """
        hiworker.TableLoad.load_table_row(self.tableWidget_run_list, data, row, table_setting)

    def load_run_list_item_not_save(self, run_id, text, col_name: str, table_setting: dict):
        row_count = self.tableWidget_run_list.rowCount()
        for row in range(row_count):  # 获取对应ID的行号
            row_id = int(self.tableWidget_run_list.item(row, 0).text())
            if int(run_id) == int(row_id):
                col_setting = table_setting.get(col_name)
                col = col_setting.get("col")
                hiworker.TableLoad.set_table_cell(self.tableWidget_run_list, text, row, col)
                break

    def load_run_list_run_time(self, run_id, text, table_setting: dict):
        row_count = self.tableWidget_run_list.rowCount()
        for row in range(row_count):  # 获取对应ID的行号
            row_id = int(self.tableWidget_run_list.item(row, 0).text())
            if int(run_id) == int(row_id):
                col_setting = table_setting.get("run_time")
                col = col_setting.get("col")
                hiworker.TableLoad.set_table_cell(self.tableWidget_run_list, text, row, col, is_time=True)
                break

    def load_table_run_count(self, data: dict, table_setting: dict):
        hiworker.TableLoad.load_table_col(self.tableWidget_run_count, data, 1, table_setting)

    def load_table_run_count_item(self, data: dict, table_setting: dict):
        hiworker.TableLoad.load_table_col(self.tableWidget_run_count, data, 1, table_setting)

    def get_selected_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_run_list)

    def get_selected_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_run_list)


class RunListAddView(QtWidgets.QDialog, Ui_Dialog_run_list_add):
    def __init__(self):
        super(RunListAddView, self).__init__()
        self.setupUi(self)

    def show_add(self):
        self.spinBoxadd_new_count.clear()
        self.spinBoxadd_new_count.setFocus()
        self.show()


# 列表项创建/编辑对话框
class RunListSetTeammateView(QtWidgets.QDialog, Ui_Dialog_run_list_teammate_list):
    def __init__(self):
        super(RunListSetTeammateView, self).__init__()
        self.setupUi(self)
        self.run_id = 0
        self.last_teammate_run_id = 0
        self.setupUi(self)
        self.tableWidget_data_list.setColumnWidth(2, 120)

        self.tableWidget_data_list.clicked.connect(self.update_teammate_id)
        self.radioButton_teammate_type_is_friends.clicked.connect(self.update_teammate_type)
        self.radioButton_teammate_type_is_guild.clicked.connect(self.update_teammate_type)
        self.radioButton_teammate_type_is_recent.clicked.connect(self.update_teammate_type)
        self.radioButton_teammate_type_is_cross.clicked.connect(self.update_teammate_type)
        self.radioButton_teammate_type_is_default.clicked.connect(self.update_teammate_type)

        self.data = {}
        self.data_all = []

    def show_edit(self, data: dict, data_all: list, col_setting: dict):
        self.data = data
        self.data_all = data_all
        match data.get("teammate_type"):
            case 2:
                self.radioButton_teammate_type_is_friends.setChecked(True)
            case 3:
                self.radioButton_teammate_type_is_guild.setChecked(True)
            case 4:
                self.radioButton_teammate_type_is_recent.setChecked(True)
            case 5:
                self.radioButton_teammate_type_is_cross.setChecked(True)
            case _:
                self.radioButton_teammate_type_is_default.setChecked(True)
        hiworker.TableLoad.init_table_header(self.tableWidget_data_list, col_setting)
        hiworker.TableLoad.load_table(self.tableWidget_data_list, data_all, col_setting)
        self.show()

    def update_teammate_id(self):
        teammate_id = hiworker.TableRead.get_current_data_id(self.tableWidget_data_list)
        if teammate_id:
            self.data.update({"teammate_id": teammate_id})

    def update_teammate_type(self):
        if self.radioButton_teammate_type_is_friends.isChecked():
            teammate_type = 2
        elif self.radioButton_teammate_type_is_guild.isChecked():
            teammate_type = 3
        elif self.radioButton_teammate_type_is_guild.isChecked():
            teammate_type = 4
        elif self.radioButton_teammate_type_is_guild.isChecked():
            teammate_type = 5
        else:
            teammate_type = 0
        self.data.update({"teammate_type": teammate_type})


# 列表项创建/编辑对话框
class RunListSetEnvView(QtWidgets.QDialog, Ui_Dialog_common_data_list):
    def __init__(self):
        super(RunListSetEnvView, self).__init__()
        self.setupUi(self)
        self.tableWidget_data_list.clicked.connect(self.set_data)
        self.setWindowTitle("选择运行环境")
        self.data = {}
        self.env_list = []
        self.col_setting = {}

    def show_edit(self, data: dict, env_list: list, col_setting: dict):
        self.env_list = env_list
        self.data = data
        hiworker.TableLoad.init_table_header(self.tableWidget_data_list, col_setting)
        hiworker.TableLoad.load_table(self.tableWidget_data_list, self.env_list, col_setting)
        self.show()

    def set_data(self):
        run_env_id = hiworker.TableRead.get_current_data_id(self.tableWidget_data_list)
        if run_env_id:
            self.data.update({"run_env_id": run_env_id})


# 列表项创建/编辑对话框
class RunListSetAccountView(QtWidgets.QDialog, Ui_Dialog_common_data_list):
    def __init__(self):
        super(RunListSetAccountView, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("选择需要绑定的账户")
        self.tableWidget_data_list.setColumnWidth(0, 40)
        self.tableWidget_data_list.setColumnWidth(1, 240)
        self.tableWidget_data_list.clicked.connect(self.set_data)
        self.data = {}

    def show_edit(self, data: dict, accounts: list, table_setting: dict):
        self.data = data
        hiworker.TableLoad.init_table_header(self.tableWidget_data_list, table_setting)
        hiworker.TableLoad.load_table(self.tableWidget_data_list, accounts, table_setting)
        self.show()

    def set_data(self):
        account_id = hiworker.TableRead.get_current_data_id(self.tableWidget_data_list)
        if account_id:
            self.data.update({"account_id": account_id})


# 列表项创建/编辑对话框
class RunListSetPlanView(QtWidgets.QDialog, Ui_Dialog_common_data_list):
    def __init__(self):
        super(RunListSetPlanView, self).__init__()
        self.setupUi(self)
        self.current_run_id = 0
        self.tableWidget_data_list.setColumnWidth(0, 40)
        self.tableWidget_data_list.setColumnWidth(1, 240)
        self.tableWidget_data_list.clicked.connect(self.set_data)

        self.data = []

    def show_edit(self, data: list, plan_data: list, table_setting: dict):
        self.data = data
        hiworker.TableLoad.init_table_header(self.tableWidget_data_list, table_setting)
        hiworker.TableLoad.load_table(self.tableWidget_data_list, plan_data, table_setting)
        self.show()

    def set_data(self):
        plan_id = hiworker.TableRead.get_current_data_id(self.tableWidget_data_list)
        if plan_id:
            for data in self.data:
                data.update({"plan_id": plan_id})
