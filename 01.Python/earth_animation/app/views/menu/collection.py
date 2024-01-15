from PySide6.QtWidgets import QMenu
from PySide6 import QtGui
from PySide6.QtGui import QCursor


# 运行列表右键菜单
class CollectionMenu(QMenu):
    def __init__(self):
        super(CollectionMenu, self).__init__()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.setFont(font)

        self.add_collection = self.addAction("新增")
        self.addSeparator()
        self.edit_collection = self.addAction("编辑")
        self.addSeparator()
        self.run_collection = self.addAction("执行")
        self.addSeparator()
        self.stop_collection = self.addAction("停止")
        self.addSeparator()
        self.delete_collection = self.addAction("删除")

    def show_menu(self):
        self.popup(QCursor.pos())
