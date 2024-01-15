from PySide6.QtWidgets import QMenu
from PySide6 import QtGui


# Sandbox列表右键菜单
class SandboxListContextMenuView(QMenu):
    def __init__(self):
        super(SandboxListContextMenuView, self).__init__()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.refresh_table = self.addAction("刷新")
        self.separator_1 = self.addSeparator()
        self.launch_sandbox = self.addAction("启动")
        self.close_sandbox = self.addAction("关闭")
