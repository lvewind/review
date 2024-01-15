from PySide6.QtWidgets import QMenu
from PySide6 import QtGui


# 计划列表右键菜单
class ProductListContextMenuView(QMenu):
    def __init__(self):
        super(ProductListContextMenuView, self).__init__()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.setFont(font)
        self.add_list_item = self.addAction("新建")
        self.separator_1 = self.addSeparator()
        self.edit_list_item = self.addAction("编辑")
        self.separator_2 = self.addSeparator()
        self.del_list_item = self.addAction("删除")
        self.refresh_table = self.addAction("刷新")
