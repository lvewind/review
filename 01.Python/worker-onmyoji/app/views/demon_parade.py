from PySide6 import QtWidgets
from app.views.ui import Ui_Dialog_plan_list_add, Ui_Dialog_demon_parade_table


# 列表项创建/编辑对话框
class DemonParadeListView(QtWidgets.QDialog, Ui_Dialog_plan_list_add):
    def __init__(self):
        super(DemonParadeListView, self).__init__()
        self.setupUi(self)
        self.demon_parade_id = 0
        self.save_mode = 0
        self.groupBox_close_game.hide()

    def show_add(self):
        self.set_add_option()
        self.show()

    def set_add_option(self):
        self.setWindowTitle("新增百鬼夜行项")
        self.save_mode = 0
        self.lineEdit_new_list_name.clear()

    def show_edit(self, data_dict: dict):
        self.set_edit_option(data_dict)
        self.show()

    def set_edit_option(self, data_dict: dict):
        self.setWindowTitle("编辑百鬼夜行项")
        self.save_mode = 1
        self.lineEdit_new_list_name.setText(str(data_dict.get("name", "")))
        self.demon_parade_id = data_dict.get("id", 0)


# 列表项创建/编辑对话框
class DemonParadeTableView(QtWidgets.QDialog, Ui_Dialog_demon_parade_table):
    def __init__(self):
        super(DemonParadeTableView, self).__init__()
        self.setupUi(self)
