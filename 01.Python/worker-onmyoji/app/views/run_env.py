from PySide6 import QtWidgets

import hiworker
from .ui import Ui_MainWindowRunEnv


class RunEnvView(QtWidgets.QMainWindow, Ui_MainWindowRunEnv):
    def __init__(self):
        super(RunEnvView, self).__init__()
        self.setupUi(self)

    def init_emulator_table_header(self, table_setting: dict):
        hiworker.TableLoad.init_table_header(self.tableWidget_emulator, table_setting)

    def init_sandbox_table_header(self, table_setting: dict):
        hiworker.TableLoad.init_table_header(self.tableWidget_sandbox, table_setting)

    # 机器管理
    def load_table_emulator_list(self, data: list, table_setting: dict):
        hiworker.TableLoad.load_table(self.tableWidget_emulator, data, table_setting)

    def load_table_sandbox_list(self, data: list, table_setting: dict):
        hiworker.TableLoad.load_table(self.tableWidget_sandbox, data, table_setting)

    def get_selected_sandbox_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_sandbox)

    def get_selected_emulator_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_emulator)
