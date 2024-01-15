from PySide6 import QtWidgets

from .source.dialog_info import Ui_Dialog_info
from ...signal.signal import signal_hi_worker


# 信息提示对话框
class DialogInfo(QtWidgets.QDialog, Ui_Dialog_info):
    def __init__(self, bind_signal=True):
        super(DialogInfo, self).__init__()
        self.setupUi(self)
        if bind_signal:
            signal_hi_worker.show_info.connect(self.show_info)
            signal_hi_worker.close_info.connect(self.close)

    def show_info(self, message):
        self.label_info.setText(message)
        self.show()
