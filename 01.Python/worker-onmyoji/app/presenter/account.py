from PySide6.QtGui import QCursor

from app.presenter.data.static import *
from ..views import *
from ..views.menu import AccountContextMenuView
from ..models import AccountModel


class AccountPresenter:
    def __init__(self):
        self.view_main = AccountView()
        self.view_add = AccountAddView()
        self.menu_account = AccountContextMenuView()
        self._account = AccountModel()
        self.data = {}
        # 初始化表头
        self.view_main.init_account_table_header(table_setting.account)
        # 显示右键菜单
        self.view_main.tableWidget_account.customContextMenuRequested.connect(self.show_menu_account)
        # 绑定按键
        self.view_add.buttonBox.accepted.connect(self.save_account)
        # 列表双击
        self.view_main.tableWidget_account.doubleClicked.connect(self.edit_account)
        # 绑定右键菜单
        self.bind_menu_account()

    def show_main(self):
        self.load_table_account()
        self.view_main.show()

    def bind_menu_account(self):
        self.menu_account.add_list_item.triggered.connect(self.add_account)
        self.menu_account.edit_list_item.triggered.connect(self.edit_account)
        self.menu_account.del_list_item.triggered.connect(self.del_account)
        self.menu_account.refresh_table.triggered.connect(self.load_table_account)

    def load_table_account(self):
        data = self._account.get_all_data()
        self.view_main.load_table_account(data, table_setting.account)

    def show_menu_account(self):
        self.menu_account.popup(QCursor.pos())

    def add_account(self):
        self.view_add.show_add()

    def edit_account(self):
        account_id = self.view_main.get_selected_id()
        if account_id:
            self.view_add.show_edit(self._account.get_dict_by_id(account_id))

    def del_account(self):
        account_ids = self.view_main.get_selected_ids()
        for account_id in account_ids:
            self._account.delete(account_id)
        self.load_table_account()

    def save_account(self):
        data = self.view_add.get_account_data()
        if data.get("id"):
            self._account.update(data)
        else:
            self._account.add(data)
        self.load_table_account()
