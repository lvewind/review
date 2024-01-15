from PySide6.QtWidgets import QMenu
from PySide6 import QtGui
from PySide6.QtGui import QCursor


# 运行列表右键菜单
class SubtitleMenu(QMenu):
    def __init__(self):
        super(SubtitleMenu, self).__init__()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.setFont(font)

        self.edit_prop = self.addAction("设置字幕")
        self.addSeparator()
        self.run_subtitles = self.addAction("执行")
        self.addSeparator()
        self.edit_action = self.addAction("编辑动作")
        self.addSeparator()
        self.insert_blank = self.addAction("插入空行")
        self.addSeparator()
        self.delete_blank = self.addAction("删除空行")
        self.addSeparator()
        self.up_blank = self.addAction("上移空行")
        self.addSeparator()
        self.down_blank = self.addAction("下移空行")
        self.addSeparator()
        self.get_audio = self.addAction("生成语音")
        self.search_audio = self.addAction("搜索语音")
        self.addSeparator()
        self.edit_fonts = self.addAction("批量字体")
        self.edit_voices = self.addAction("批量配音")
        self.addSeparator()
        self.open_media = self.addAction("打开目录")
        self.search_media = self.addAction("查询媒体")
        # self.delete_media = self.addAction("删除媒体")
        # self.create_subtitle = self.addAction("生成字幕")
        # self.addSeparator()

    def show_menu(self):
        self.popup(QCursor.pos())
