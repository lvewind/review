import os

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from app.views.ui import Ui_Dialog_name_edit
from app.views.sender import *


class CollectionView(QtWidgets.QDialog, Ui_Dialog_name_edit):
    def __init__(self, icon_path=None):
        super(CollectionView, self).__init__()
        self.setupUi(self)
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))

        self.data = {}

        self.pushButton.clicked.connect(self.send_data)

    def show_add(self):
        self.data = {}
        self.setWindowTitle("新增系列")
        self.lineEdit.clear()
        self.lineEdit.setFocus()
        self.show()

    def show_edit(self, data: dict):
        self.data = data
        if data.get("id"):
            self.setWindowTitle("编辑系列")
            self.lineEdit.setText(data.get("name"))
            self.lineEdit.setFocus()
            self.show()

    def send_data(self):
        name = self.lineEdit.text()
        if name:
            self.close()
            self.data.update({
                "name": name
            })
            view_sender.collection.save.emit(self.data)
