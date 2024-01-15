from PySide6.QtWidgets import QMenu
from PySide6 import QtGui


# Emulator列表右键菜单
class EmulatorListContextMenuView(QMenu):
    def __init__(self):
        super(EmulatorListContextMenuView, self).__init__()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.add_list_item = self.addAction("创建")
        self.separator_1 = self.addSeparator()
        self.launch_emulator = self.addAction("启动")
        self.close_emulator = self.addAction("关闭")
        self.separator_2 = self.addSeparator()
        self.del_list = self.addAction("删除")
        self.refresh_table = self.addAction("刷新")
