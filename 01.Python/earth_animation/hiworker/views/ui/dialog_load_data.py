from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from .dialog_info import Ui_Dialog_info
from ...signal.signal import signal_hi_worker


# 信息提示对话框
class DialogLoadData(QtWidgets.QDialog, Ui_Dialog_info):
    def __init__(self):
        super(DialogLoadData, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.buttonBox.hide()
        signal_hi_worker.show_load_data.connect(self.show_load_data)
        signal_hi_worker.close_info.connect(self.close)

    def show_load_data(self, message):
        self.label_info.setText(message)
        self.show()
