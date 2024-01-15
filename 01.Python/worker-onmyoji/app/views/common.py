from PySide6 import QtWidgets
from app.views.ui import Ui_Dialog_common_data_list, Ui_Dialog_plan_list_add

import hiworker


# 列表项创建/编辑对话框
class CommonDataListView(QtWidgets.QDialog, Ui_Dialog_common_data_list):
    def __init__(self, title):
        super(CommonDataListView, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(title)
        self.tableWidget_data_list.setColumnWidth(0, 40)
        self.tableWidget_data_list.setColumnWidth(1, 240)
        self.data_id = 0
        self.plan_type = ""
        self.run_id_list = []

    def get_data_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_data_list)

    def show_set_plan(self, run_id_list, plan_type, data_plan: list):
        self.plan_type = plan_type
        self.run_id_list = run_id_list
        self.show()

    def load_data(self, data: list, col_setting: dict):
        hiworker.TableLoad.load_table(self.tableWidget_data_list, data, col_setting)


class PlanListView(QtWidgets.QDialog, Ui_Dialog_plan_list_add):
    def __init__(self, dialog_title: str, plan_type: str):
        super(PlanListView, self).__init__()
        self.setupUi(self)
        self.plan_id = 0
        self.save_mode = 0
        self.plan_type = plan_type
        self.dialog_title = dialog_title

    def show_add(self):
        self.set_add_option()
        self.show()

    def set_add_option(self):
        self.save_mode = 0
        self.setWindowTitle("新增" + self.dialog_title + "项")  # 设置窗口标题
        self.lineEdit_new_list_name.clear()  # 清空输入框
        self.checkBox_close_game_when_finished.setChecked(False)

    def show_edit(self, data_dict: dict):
        self.set_edit_option(data_dict)
        self.show()

    def set_edit_option(self, data_dict: dict):
        self.save_mode = 1
        self.setWindowTitle("编辑" + self.dialog_title + "项")
        self.lineEdit_new_list_name.setText(str(data_dict.get("name", "")))  # 显示原来得名称
        self.checkBox_close_game_when_finished.setChecked(data_dict.get("close_env", False))
        self.plan_id = data_dict.get("id", 0)  # 保存id
