from PySide6.QtWidgets import QMenu
from PySide6 import QtGui
from PySide6.QtGui import QCursor


# 运行列表右键菜单
class EpisodeMenu(QMenu):
    def __init__(self):
        super(EpisodeMenu, self).__init__()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.setFont(font)

        self.add_episode = self.addAction("新增")
        self.addSeparator()
        self.run_episodes = self.addAction("执行")
        self.addSeparator()
        self.edit_episode = self.addAction("编辑")
        self.addSeparator()
        self.up_episode = self.addAction("上移")
        self.down_episode = self.addAction("下移")
        self.addSeparator()
        self.addSeparator()
        self.create_subtitle = self.addAction("生成字幕")
        self.create_speech = self.addAction("生成语音")
        self.search_audio = self.addAction("搜索语音")
        self.search_media = self.addAction("查询媒体")
        self.import_from_excel = self.addAction("从EXCEL导入")
        self.addSeparator()
        self.delete_episode = self.addAction("删除")

    def show_menu(self):
        self.popup(QCursor.pos())
