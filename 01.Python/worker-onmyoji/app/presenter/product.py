import copy

from PySide6.QtGui import QCursor

from ..models import *
from ..views import *
from app.presenter.data import table_setting, data_chs, data_static


class ProductPresenter:
    def __init__(self):
        self._product = ProductModel()
        self.view_main = ProductsView()
        self.view_add = ProductsAddView()
        self.menu_product = ProductListContextMenuView()
        self.view_main.products_dict = data_static.products
        self.view_main.init_products_table_header(table_setting.products)
        self.view_main.tableWidget_products.customContextMenuRequested.connect(self.show_menu_products)
        self.view_main.tableWidget_products.doubleClicked.connect(self.edit_product)
        self.view_main.tableWidget_products.clicked.connect(self.load_product_option)

        self.view_add.buttonBox.accepted.connect(self.save_product)
        self.bind_menu_product()

        self.view_main.load_combo_box_product_default()
        self.view_main.load_combo_box_product_sub_default()
        self.view_main.load_combo_box_play_stage_default()

        self.view_main.pushButton_reset_job_option.clicked.connect(self.view_main.load_combo_box_product_default)
        self.view_main.comboBox_job_option_play.currentIndexChanged.connect(self.view_main.load_combo_box_product_sub_default)
        self.view_main.comboBox_job_option_play_sub.currentIndexChanged.connect(self.view_main.load_combo_box_play_stage_default)
        self.view_main.pushButton_save_job.clicked.connect(self.save_option)

    def show_main(self):
        self.load_table_products()
        self.view_main.show()

    # 加载产品列表
    def load_table_products(self, select_last_row=False):
        data_to_show = []
        data = self._product.get_all_data()
        if data:
            for data_dict in data:
                if type(data_dict) == dict:
                    data_dict_chs = copy.deepcopy(data_dict)
                    if data_dict.get("play_name_second") == "orochi":
                        chapter_stage = data_chs.product_orochi.get(str(data_dict.get("chapter_stage")), data_dict.get("chapter_stage"))
                    elif data_dict.get("play_name_second") == "sougenbi":
                        chapter_stage = data_chs.product_sougenbi.get(str(data_dict.get("chapter_stage")), data_dict.get("chapter_stage"))
                    else:
                        chapter_stage = data_chs.product.get(str(data_dict.get("chapter_stage")), data_dict.get("chapter_stage"))
                    data_dict_chs.update({
                        "play_name": data_chs.product.get(data_dict.get("play_name"), data_dict.get("play_name")),
                        "play_name_second": data_chs.product.get(data_dict.get("play_name_second"), data_dict.get("play_name_second")),
                        "chapter_stage": chapter_stage
                    })
                    data_to_show.append(data_dict_chs)
        self.view_main.load_table_products(data_to_show, table_setting.products, select_last_row=select_last_row)

    # 绑定函数
    def bind_menu_product(self):
        self.menu_product.add_list_item.triggered.connect(self.view_add.show_add)
        self.menu_product.edit_list_item.triggered.connect(self.edit_product)
        self.menu_product.del_list_item.triggered.connect(self.del_products)
        self.menu_product.refresh_table.triggered.connect(self.load_table_products)

    # 显示菜单
    def show_menu_products(self):
        self.menu_product.popup(QCursor.pos())

    # 编辑产品
    def edit_product(self):
        product_id = self.view_main.get_selected_id()
        if product_id:
            self.view_add.show_edit(self._product.get_data_by_id(product_id))

    def del_products(self):
        product_ids = self.view_main.get_selected_ids()
        for product_id in product_ids:
            self._product.delete(product_id)
        self.load_table_products(False)

    def save_product(self):
        data = self.view_add.get_product_data()
        if data.get("id"):
            self._product.update(data)
        else:
            self._product.add(data)
        self.load_table_products()

    def save_option(self):
        data = self.view_main.get_product_option()
        if data.get("id"):
            self._product.update(data)
            self.load_table_products()

    def load_product_option(self):
        product_id = self.view_main.get_selected_id()
        data = self._product.get_data_by_id(product_id)
        self.view_main.load_option_product(data)
