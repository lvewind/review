from PySide6.QtWidgets import QMenu
from PySide6 import QtGui
from PySide6.QtGui import QCursor


# 运行列表右键菜单
class MediaMenu(QMenu):
    def __init__(self):
        super(MediaMenu, self).__init__()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.setFont(font)

        self.add_media = self.addAction("新增媒体")
        self.addSeparator()
        self.edit_media = self.addAction("设置媒体")
        self.addSeparator()
        self.edit_media_prop = self.addAction("编辑数据")
        self.addSeparator()
        self.run_medias = self.addAction("执行")
        self.addSeparator()
        self.copy_media = self.addAction("复制")
        self.move_media = self.addAction("移动")
        self.addSeparator()
        self.edit_fonts = self.addAction("批量字体")
        self.edit_size = self.addAction("批量大小")
        self.addSeparator()
        self.open_media = self.addAction("打开目录")
        self.addSeparator()
        self.delete_media = self.addAction("删除媒体")

    def show_menu(self):
        self.popup(QCursor.pos())
