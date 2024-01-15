import os
from threading import Thread

from PySide6 import QtWidgets
from PySide6.QtGui import QCursor

import hiworker
from app.presenter.data import table_setting
from ..models import RunEnvModel, AppSettingModel
from ..views import RunEnvView
from ..views.menu import SandboxListContextMenuView, EmulatorListContextMenuView
from .sender import signal_run_env


class RunEnvPresenter:
    def __init__(self):
        self.ini_path = "C:\\Windows\\sandboxie.ini"
        self._run_env = RunEnvModel()
        self._app_setting = AppSettingModel()
        self._run_env.clear_table()

        self.sandboxie = hiworker.SandBox(self._app_setting.read_option("sandbox_path"), self._app_setting.read_option("onmyoji_pc_path"))
        self.sandboxie.set_handle_option(offset_x=self._app_setting.read_option("offset_x"),
                                         offset_y=self._app_setting.read_option("offset_y"))
        self.emulator = hiworker.Emulator(self._app_setting.read_option("emulator_path"))
        # self.emulator.set_handle_option(offset_x=self._app_setting.read_option("offset_x"),
        #                                 offset_y=self._app_setting.read_option("offset_y"))
        self.backup_restore = hiworker.BackupRestore(self.emulator)

        self.view_main = RunEnvView()
        self.view_em_add = hiworker.DialogEmulatorAdd()
        self.menu_sandbox = SandboxListContextMenuView()
        self.menu_emulator = EmulatorListContextMenuView()

        self.update_sandbox_list()
        self.update_emulator_list()

        self.view_main.init_emulator_table_header(table_setting.emulator_list)
        self.view_main.init_sandbox_table_header(table_setting.sandbox_list)

        # 右键菜单显示
        self.view_main.tableWidget_emulator.customContextMenuRequested.connect(self.show_menu_emulator_list)
        self.view_main.tableWidget_sandbox.customContextMenuRequested.connect(self.show_menu_sandbox_list)

        self.bind_menu_sandbox()
        self.bind_menu_emulator()
        self.bind_func_setting()

        signal_run_env.launch_env.connect(self.launch_sandbox)
        signal_run_env.close_env.connect(self.close_sandbox)

    def show_main(self):
        self._run_env.clear_table()
        self.load_table_sandbox()
        self.load_table_emulator()
        self.load_option_setting()
        self.view_main.show()

    def launch_env(self, env_ids: list, env_type: int):
        if env_type == 1:
            self.launch_sandbox(env_ids)
        elif env_type == 2:
            self.launch_emulator(env_ids)

    def close_env(self, env_ids: list, env_type: int):
        if env_type == 1:
            self.close_sandbox(env_ids)
        elif env_type == 2:
            self.close_emulator(env_ids)

    ################################################################
    # 沙箱
    ################################################################
    def show_menu_sandbox_list(self):
        self.menu_sandbox.popup(QCursor.pos())

    def update_sandbox_list(self):
        """
        更新沙箱数据
        :return:
        """
        name_list = self.sandboxie.read_sandbox_name(self.ini_path)
        if name_list:
            name_list.sort()
            for sandbox_name in name_list:
                self._run_env.add({"name": sandbox_name, "env_type": 1})

    def load_table_sandbox(self):
        self.update_sandbox_list()
        data_all = self._run_env.get_all_data()
        data_sandbox_list = []
        for data in data_all:
            if data.get("env_type") == 1:
                data_sandbox_list.append(data)
        self.view_main.load_table_sandbox_list(data_sandbox_list, table_setting.sandbox_list)

    def bind_menu_sandbox(self):
        self.menu_sandbox.refresh_table.triggered.connect(self.update_sandbox_list)
        self.menu_sandbox.launch_sandbox.triggered.connect(self._launch_sandbox)
        self.menu_sandbox.close_sandbox.triggered.connect(self._close_sandbox)

    def _launch_sandbox(self):
        self.launch_sandbox(self.view_main.get_selected_sandbox_ids())

    def _close_sandbox(self):
        self.close_sandbox(self.view_main.get_selected_sandbox_ids())

    def launch_sandbox(self, sandbox_ids: list):
        sandbox_path = self._app_setting.read_option("sandbox_path")
        if not os.path.isfile(sandbox_path):
            print(sandbox_path + "不存在")
            return
        onmyoji_pc_path = self._app_setting.read_option("onmyoji_pc_path")
        if not os.path.isfile(onmyoji_pc_path):
            print(onmyoji_pc_path + "不存在")
            return
        self.sandboxie.set_option(sandbox_path, onmyoji_pc_path)
        sandbox_name_list = []
        for sandbox_id in sandbox_ids:
            sandbox_name = self._run_env.get_name(sandbox_id)
            sandbox_name_list.append({"name": sandbox_name, "window_title": "[#] [" + sandbox_name + "] 阴阳师-网易游戏 [#]"})
        Thread(target=self.sandboxie.launch_sandbox_s, args=(sandbox_name_list, )).start()

    def close_sandbox(self, sandbox_ids: list):
        sandbox_title_list = self.get_sandbox_titles(sandbox_ids)
        for sandbox_title in sandbox_title_list:
            self.sandboxie.close_sandbox(sandbox_title)

    def get_sandbox_titles(self, sandbox_id_list: list):
        sandbox_title_list = []
        for sandbox_id in sandbox_id_list:
            sandbox_title = self._run_env.get_name(sandbox_id)
            sandbox_title = "[#] [" + sandbox_title + "] 阴阳师-网易游戏 [#]"
            sandbox_title_list.append(sandbox_title)
        return sandbox_title_list

    ################################################################
    # 模拟器
    ################################################################
    def show_menu_emulator_list(self):
        self.menu_emulator.popup(QCursor.pos())

    def update_emulator_list(self):
        """
        更新模拟器数据
        :return:
        """
        em_list = self.emulator.list_emulator(self.emulator)
        if em_list:
            em_list.sort(key=lambda x: x["em_id"])
            for em in em_list:
                self._run_env.add({"em_id": em.get("em_id"), "name": em.get("name"), "env_type": 2})

    def load_table_emulator(self):
        self.update_emulator_list()
        data_all = self._run_env.get_all_data()
        data_emulator_list = []
        for data in data_all:
            if data.get("env_type") == 2:
                data_emulator_list.append(data)
        self.view_main.load_table_emulator_list(data_emulator_list, table_setting.emulator_list)

    def bind_menu_emulator(self):
        self.menu_emulator.add_list_item.triggered.connect(self.add_emulator)
        self.menu_emulator.del_list.triggered.connect(self.del_emulator)
        self.menu_emulator.refresh_table.triggered.connect(self.load_table_emulator)
        self.menu_emulator.launch_emulator.triggered.connect(self._launch_emulator)
        self.menu_emulator.close_emulator.triggered.connect(self._close_emulator)

    def add_emulator(self):
        self.view_em_add.show()

    def _launch_emulator(self):
        self.launch_emulator(self.view_main.get_selected_emulator_ids())

    def _close_emulator(self):
        self.close_emulator(self.view_main.get_selected_emulator_ids())

    def launch_emulator(self, launch_list):
        self.emulator.set_launch_option(launch_list, launch_with_app=False)
        self.emulator.start()

    def close_emulator(self, close_list):
        self.emulator.close_emulator_multiple(close_list)

    def del_emulator(self):
        self.emulator.remove_emulator(self.view_main.get_selected_emulator_ids())

    ################################################################
    # 设置
    ################################################################
    def bind_func_setting(self):
        self.view_main.pushButton_browse_onmyoji_pc_path.clicked.connect(self.browse_onmyoji_pc_path)
        self.view_main.pushButton_browse_sandbox_path.clicked.connect(self.browse_sandbox_path)
        self.view_main.pushButton_browse_dnplayer_path.clicked.connect(self.browse_emulator_path)
        self.view_main.spinBox_scroll_count.editingFinished.connect(self.set_scroll_count)
        self.view_main.spinBox_scroll_time.editingFinished.connect(self.set_scroll_time)
        self.view_main.spinBox_cpu_sleep_time.editingFinished.connect(self.set_cpu_sleep_time)
        self.view_main.spinBox_offset_x.editingFinished.connect(self.set_offset_x)
        self.view_main.spinBox_offset_y.editingFinished.connect(self.set_offset_y)

    def load_option_setting(self):
        self.view_main.lineEdit_onmyoji_pc_path.setText(self._app_setting.read_option("onmyoji_pc_path"))
        self.view_main.lineEdit_dnplayer_path.setText(self._app_setting.read_option("emulator_path"))
        self.view_main.lineEdit_sandbox_path.setText(self._app_setting.read_option("sandbox_path"))
        scroll_count = self._app_setting.read_option("scroll_count")
        if scroll_count:
            self.view_main.spinBox_scroll_count.setValue(scroll_count)
        else:
            self.view_main.spinBox_scroll_count.setValue(10)
            self.set_scroll_count()
        scroll_time = self._app_setting.read_option("scroll_time")
        if scroll_time:
            self.view_main.spinBox_scroll_time.setValue(scroll_time)
        else:
            self.view_main.spinBox_scroll_time.setValue(60)
            self.set_scroll_time()
        cpu_sleep_time = self._app_setting.read_option("cpu_sleep_time")
        if cpu_sleep_time:
            self.view_main.spinBox_cpu_sleep_time.setValue(cpu_sleep_time)
        else:
            self.view_main.spinBox_cpu_sleep_time.setValue(5)
            self.set_cpu_sleep_time()

        offset_x = self._app_setting.read_option("offset_x")
        if offset_x:
            self.view_main.spinBox_offset_x.setValue(offset_x)
        else:
            self.view_main.spinBox_offset_x.setValue(0)
        offset_y = self._app_setting.read_option("offset_y")
        if offset_y:
            self.view_main.spinBox_offset_y.setValue(offset_y)
        else:
            self.view_main.spinBox_offset_y.setValue(0)

    def browse_emulator_path(self):
        openfile_name, openfile_type = QtWidgets.QFileDialog.getOpenFileName(self.view_main, caption='选择模拟器路径', filter='dnplayer(dnplayer.exe)')
        if openfile_name:
            self.view_main.lineEdit_dnplayer_path.setText(openfile_name)
            self._app_setting.set_option("emulator_path", openfile_name)
            self.emulator.dnplayer_path = openfile_name
            self.load_table_emulator()

    def browse_sandbox_path(self):
        openfile_name, openfile_type = QtWidgets.QFileDialog.getOpenFileName(self.view_main, caption='选择沙箱路径', filter='Start(Start.exe)')
        if openfile_name:
            self.view_main.lineEdit_sandbox_path.setText(openfile_name)
            self._app_setting.set_option("sandbox_path", openfile_name)

    def browse_onmyoji_pc_path(self):
        print("browse_onmyoji_pc_path")
        openfile_name, openfile_type = QtWidgets.QFileDialog.getOpenFileName(self.view_main, caption='选择阴阳师路径', filter='Launch(Launch.exe)')
        if openfile_name:
            self.view_main.lineEdit_onmyoji_pc_path.setText(openfile_name)
            self._app_setting.set_option("onmyoji_pc_path", openfile_name)

    def set_scroll_count(self):
        self._app_setting.set_option("scroll_count", self.view_main.spinBox_scroll_count.value())

    def set_scroll_time(self):
        self._app_setting.set_option("scroll_time", self.view_main.spinBox_scroll_time.value())

    def set_cpu_sleep_time(self):
        self._app_setting.set_option("cpu_sleep_time", self.view_main.spinBox_cpu_sleep_time.value())

    def set_offset_x(self):
        self._app_setting.set_option("offset_x", self.view_main.spinBox_offset_x.value())

    def set_offset_y(self):
        self._app_setting.set_option("offset_y", self.view_main.spinBox_offset_y.value())
