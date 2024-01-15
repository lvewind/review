from PySide6 import QtWidgets

from .source.dialog_emulator_creating import Ui_Dialog_create_emulator
from ...signal.signal import signal_hi_worker


# 模拟器初始化进度对话框
class DialogEmulatorRemove(QtWidgets.QDialog, Ui_Dialog_create_emulator):
    def __init__(self):
        super(DialogEmulatorRemove, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("正在删除模拟器")
        self.label_4.setText("正在删除模拟器")
        self.label.setText("正在删除")
        self.label_2.setText("号，共")
        signal_hi_worker.show_remove_process.connect(self.show_process)
        signal_hi_worker.refresh_current_remove.connect(self.refresh_current_remove)
        signal_hi_worker.finish_remove_process.connect(self.finish_remove_process)

    def show_process(self, total: int):
        self.label_total_creating_emulator.setText(str(total))
        self.show()

    def refresh_current_remove(self, current_remove):
        self.label_current_creating_emulator.setText(str(current_remove))

    def finish_remove_process(self):
        self.label_current_disk_speed.setText("删除已完成")
