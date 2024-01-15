import time

from PySide6 import QtWidgets
from PySide6.QtCore import QTime

import hiworker
from .ui import *


class PlanView(QtWidgets.QMainWindow, Ui_MainWindowPlan):
    def __init__(self):
        super(PlanView, self).__init__()
        self.setupUi(self)

    def init_plan_table_header(self, table_setting: dict):
        hiworker.TableLoad.init_table_header(self.tableWidget_plan, table_setting)

    def init_plan_sub_table_header(self, table_setting: dict):
        hiworker.TableLoad.init_table_header(self.tableWidget_plan_sub, table_setting)

    # 单计划页面
    def load_table_plan(self, data: list, table_setting: dict, select_last_row=False):
        hiworker.TableLoad.load_table(self.tableWidget_plan, data, table_setting, select_last_row=select_last_row)

    def load_table_plan_sub(self, data: list, table_setting: dict, select_last_row=False):
        hiworker.TableLoad.load_table(self.tableWidget_plan_sub, data, table_setting, select_last_row=select_last_row)

    def bind_func_plan(self):
        self.tableWidget_plan.clicked.connect(self.load_table_plan_sub)

    def get_plan_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_plan)

    def get_plan_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_plan)

    def get_plan_sub_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_plan_sub)

    def get_plan_sub_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_plan_sub)

    def get_plan_sub_assoc_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_plan_sub, id_col=1)

    def get_plan_sub_assoc_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_plan_sub, id_col=1)


class PlanSingleAddView(QtWidgets.QDialog, Ui_Dialog_plan_list_add):
    def __init__(self):
        super(PlanSingleAddView, self).__init__()
        self.setupUi(self)
        self.data = {}

    def show_add(self):
        self.data = {}
        self.lineEdit_new_list_name.clear()
        self.checkBox_close_env.setChecked(False)
        self.show()

    def show_edit(self, data: dict):
        self.data = data
        self.lineEdit_new_list_name.setText(data.get("name"))
        self.checkBox_close_env.setChecked(True) if data.get("close_env") else self.checkBox_close_env.setChecked(False)
        if data.get("timing_start"):
            m, s = divmod(data.get("timing_start"), 60)
            h, m = divmod(m, 60)
            # _time = QTime()
            # _time.setHMS(h, m, s)
            self.timeEdit_timing_start.setTime(QTime(h, m, s))
        self.show()

    def get_data(self):
        clock = self.timeEdit_timing_start.time()
        timing_start = clock.hour() * 3600 + clock.minute() * 60 + clock.second()
        self.data.update({
            "name": self.lineEdit_new_list_name.text(),
            "close_env": 1 if self.checkBox_close_env.isChecked() else 0,
            "timing_start": timing_start
        })
        return self.data


# 列表项创建/编辑对话框
class PlanSingleSubAddView(QtWidgets.QDialog, Ui_Dialog_common_data_list):
    def __init__(self):
        super(PlanSingleSubAddView, self).__init__()
        self.setupUi(self)

        self.tableWidget_data_list.setColumnWidth(0, 40)
        self.tableWidget_data_list.setColumnWidth(1, 240)
        self.data = {}
        self.assoc_data = {}
        self.products_data = []
        self.tableWidget_data_list.clicked.connect(self.update_assoc_data)
        self.is_add = True

    def show_add(self, plan_data: dict, products: list, col_setting: dict):
        """
        显示新增对话框
        """
        self.is_add = True
        self.data = plan_data
        self.products_data = products
        self.setWindowTitle("添加[" + self.data.get("name") + "]子项")
        hiworker.TableLoad.load_table(self.tableWidget_data_list, self.products_data, col_setting)
        self.show()

    def show_edit(self, plan_data: dict, assoc_id: int, products: list, col_setting: dict):
        """
        显示编辑对话框
        """
        self.is_add = False
        self.data = plan_data
        self.assoc_data = {"id": assoc_id, "plan_id": plan_data.get("id")}
        self.products_data = products
        self.setWindowTitle("编辑[" + self.data.get("name") + "]子项")
        hiworker.TableLoad.load_table(self.tableWidget_data_list, self.products_data, col_setting)
        self.show()

    def get_product_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_data_list)

    def update_assoc_data(self):
        product_id = hiworker.TableRead.get_current_data_id(self.tableWidget_data_list)
        if product_id:
            self.assoc_data.update({"product_id": product_id})
