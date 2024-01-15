import os

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from app.views.ui import Ui_Dialog_place_edit
from app.views.sender import *


class EpisodeView(QtWidgets.QDialog, Ui_Dialog_place_edit):
    def __init__(self, icon_path=None):
        super(EpisodeView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.data = {}

        self.pushButton_save_place.clicked.connect(self.send_data)

    def show_add(self, collection_id: int):
        if collection_id:
            self.data.update({"collection_id": collection_id})
            self.lineEdit_name.clear()
            self.textEdit_content.clear()
            self.lineEdit_name.setFocus()
            self.setWindowTitle("新增剧集")
            self.show()

    def show_edit(self, data: dict):
        self.data = data
        self.textEdit_content.setPlainText(data.get("content"))
        self.lineEdit_name.setText(data.get("name"))
        self.checkBox_show_subtitles.setChecked(True if data.get("display_subtitles") else False)
        self.setWindowTitle("编辑剧集内容：" + str(data.get("id")) + data.get("name"))
        self.textEdit_content.setFocus()
        self.show()

    def send_data(self):
        self.close()
        self.data.update(
            {
                "name": self.lineEdit_name.text(),
                "content": self.textEdit_content.toPlainText(),
                "display_subtitles": 1 if self.checkBox_show_subtitles.isChecked() else 0
            }
        )
        view_sender.episode.save.emit(self.data)
