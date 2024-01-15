from PySide6.QtGui import QCursor

from ..models import *
from ..views import *
from app.presenter.data import table_setting


class PlanPresenter:
    def __init__(self):
        self.view_main = PlanView()
        self.view_plan_add = PlanSingleAddView()
        self.view_plan_sub_add = PlanSingleSubAddView()
        
        self.menu_plan = PlanListContextMenuView()
        self.menu_plan_day = PlanListContextMenuView()
        self.menu_plan_week = PlanListContextMenuView()
        self.menu_plan_month = PlanListContextMenuView()

        self.menu_plan_sub = PlanListContextMenuView()
        self.menu_plan_day_sub = PlanListContextMenuView()
        self.menu_plan_week_sub = PlanListContextMenuView()
        self.menu_plan_month_sub = PlanListContextMenuView()

        self._product = ProductModel()
        self._plan = PlanModel()

        self.init_table_header()
        self.show_menu()
        self.bind_menu_plan()
        self.bind_dialog_accepted()

        self.load_table_plan()
        self.view_main.tableWidget_plan.doubleClicked.connect(self.show_edit_plan)

    def show_main(self):
        self.view_main.show()

    def init_table_header(self):
        self.view_main.init_plan_table_header(table_setting.plan)
        self.view_main.init_plan_sub_table_header(table_setting.plan_sub)
        
    def show_menu(self):
        self.view_main.tableWidget_plan.customContextMenuRequested.connect(self.show_menu_plan)
        self.view_main.tableWidget_plan_sub.customContextMenuRequested.connect(self.show_menu_plan_sub)

    def bind_dialog_accepted(self):
        self.view_plan_add.buttonBox.accepted.connect(self.save_plan)

        self.view_plan_sub_add.buttonBox.accepted.connect(self.save_plan_sub)

    ################
    # 单次计划
    ################
    def save_plan(self):
        data = self.view_plan_add.get_data()
        if data:
            if data.get("id"):
                self._plan.update(data)
            else:
                self._plan.add(data)
            self.load_table_plan()

    def save_plan_sub(self):
        if self.view_plan_sub_add.is_add:
            product_ids = self.view_plan_sub_add.get_product_ids()
            plan_id = self.view_main.get_plan_id()
            self._plan.add_products_assoc(plan_id, product_ids)
        else:
            assoc_data = self.view_plan_sub_add.assoc_data
            self._plan.update_product_assoc(assoc_data)
        self.load_table_plan_sub()

    def load_table_plan(self, select_last_row=False):
        data = self._plan.get_all_data()
        self.view_main.load_table_plan(data, table_setting.plan, select_last_row=select_last_row)

    def load_table_plan_sub(self, select_last_row=False):
        plan_id = self.view_main.get_plan_id()
        plan_sub = self._plan.get_products(plan_id)
        plan_sub_sort = sorted(plan_sub, key=lambda x: x["sort_order"])
        self.view_main.load_table_plan_sub(plan_sub_sort, table_setting.plan_sub, select_last_row=select_last_row)

    def show_menu_plan(self):
        self.menu_plan.popup(QCursor.pos())

    def show_menu_plan_sub(self):
        self.menu_plan_sub.popup(QCursor.pos())

    def bind_menu_plan(self):
        self.menu_plan.add_list_item.triggered.connect(self.show_add_plan)
        self.menu_plan.edit_list_item.triggered.connect(self.show_edit_plan)
        self.menu_plan.del_list_item.triggered.connect(self.del_plan)
        self.menu_plan.refresh_table.triggered.connect(self.load_table_plan)

        self.menu_plan_sub.add_list_item.triggered.connect(self.show_add_plan_sub)
        self.menu_plan_sub.edit_list_item.triggered.connect(self.show_edit_plan_sub)
        self.menu_plan_sub.del_list_item.triggered.connect(self.del_plan_sub)
        self.menu_plan_sub.refresh_table.triggered.connect(self.load_table_plan_sub)

        self.view_main.tableWidget_plan.clicked.connect(self.load_table_plan_sub)

    def show_add_plan(self):
        self.view_plan_add.show_add()

    def show_edit_plan(self):
        instance_id = self.view_main.get_plan_id()
        data = self._plan.get_dict_by_id(instance_id)
        self.view_plan_add.show_edit(data)

    def del_plan(self):
        plan_ids = self.view_main.get_plan_ids()
        for plan_id in plan_ids:
            self._plan.delete(plan_id)
        self.load_table_plan()
        self.load_table_plan_sub()

    def show_add_plan_sub(self):
        plan_id = self.view_main.get_plan_id()
        if plan_id:
            plan_data = self._plan.get_dict_by_id(plan_id)
            product_data = self._product.get_all_data()
            self.view_plan_sub_add.show_add(plan_data, product_data, table_setting.plan_sub_add)

    def show_edit_plan_sub(self):
        plan_assoc_id = self.view_main.get_plan_sub_assoc_id()
        plan_id = self.view_main.get_plan_id()
        if plan_assoc_id:
            plan_data = self._plan.get_dict_by_id(plan_id)
            product_data = self._product.get_all_data()
            self.view_plan_sub_add.show_edit(plan_data, plan_assoc_id, product_data, table_setting.plan_sub_add)

    def del_plan_sub(self):
        plan_sub_assoc_ids = self.view_main.get_plan_sub_assoc_ids()
        self._plan.delete_products_assoc(plan_sub_assoc_ids)
        self.load_table_plan_sub()
