from PySide6 import QtWidgets

from .source.dialog_run_list_add import Ui_Dialog_run_list_add
from ...signal.signal import signal_hi_worker


# 模拟器初始化进度对话框
class DialogEmulatorAdd(QtWidgets.QDialog, Ui_Dialog_run_list_add):
    def __init__(self):
        super(DialogEmulatorAdd, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("新增模拟器")
        self.label_3.setText("请输入要增加的模拟器数量")
        self.buttonBox.accepted.connect(self.creat_emulator)

    def creat_emulator(self):
        add_count = self.spinBoxadd_new_count.value()
        if add_count:
            signal_hi_worker.create_emulator.emit(add_count)
