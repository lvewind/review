import os

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from app.views.ui import Ui_Dialog_set_fonts


class SetFontsView(QtWidgets.QDialog, Ui_Dialog_set_fonts):
    def __init__(self, icon_path=None):
        super(SetFontsView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)
        self.setWindowTitle("正在批量设置 [字幕] 字体")

    def clear_combobox(self):
        self.comboBox_font.clear()
        self.comboBox_font_size.clear()
        self.comboBox_font_color.clear()
