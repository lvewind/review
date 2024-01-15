from PySide6 import QtWidgets

from .source.dialog_emulator_creating import Ui_Dialog_create_emulator
from ...signal.signal import signal_hi_worker


# 模拟器初始化进度对话框
class DialogEmulatorCreating(QtWidgets.QDialog, Ui_Dialog_create_emulator):
    def __init__(self):
        super(DialogEmulatorCreating, self).__init__()
        self.setupUi(self)
        signal_hi_worker.show_create_process.connect(self.show_process)
        signal_hi_worker.refresh_current_create_process.connect(self.refresh_current_create)
        signal_hi_worker.refresh_disk_speed.connect(self.refresh_disk_speed)
        signal_hi_worker.finish_create_process.connect(self.finish_create_process)

    def show_process(self, total: int):
        self.label_current_creating_emulator.setText(str(1))
        self.label_total_creating_emulator.setText(str(total))
        self.show()

    def refresh_current_create(self, current_creating):
        self.label_current_creating_emulator.setText(str(current_creating))

    def refresh_disk_speed(self, disk_speed: str):
        self.label_current_disk_speed.setText(disk_speed)

    def finish_create_process(self):
        self.label_current_disk_speed.setText("创建已完成")
