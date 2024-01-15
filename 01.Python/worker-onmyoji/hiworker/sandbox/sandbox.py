# -*- coding: UTF-8 -*-
"""
沙箱控制模块
"""
import subprocess
import win32api
import win32con
import os
import time

from ..utils.win32.handle import Win32Handle
from ..signal import *
from ..thread import Thread


class SandBox(Thread, Win32Handle):
    def __init__(self, sandbox_path: str, program_path: str):
        super(SandBox, self).__init__()
        self.sandbox_path = sandbox_path
        self.program_path = program_path
        self.launch_list = []

    def run(self) -> None:
        self.launch_sandbox_s(self.launch_list)

    def set_option(self, sandbox_path: str, program_path: str):
        """
        设置内部参数
        :param sandbox_path:
        :param program_path:
        :return:
        """
        if program_path:
            self.program_path = program_path
        if sandbox_path:
            self.sandbox_path = sandbox_path

    @staticmethod
    def read_sandbox_name(ini_path):
        """
        读取沙箱名称
        :return:
        """
        if os.path.exists(ini_path):
            ini = open(ini_path, encoding="UTF-16 LE")
            sections = []
            for option in ini.readlines():
                if "[" in option:
                    sections.append(option.rstrip("\n").strip("[").rstrip("]"))
            sections = sections[2:]
            sections.sort()
            return sections
        else:
            print("找不到" + ini_path)
            return []

    def set_launch_list(self, sandbox_title_list: list):
        """
        设置沙箱启动列表
        :param sandbox_title_list:
        :return:
        """
        self.launch_list = sandbox_title_list

    def is_sandbox_running(self, sandbox_title):
        """
        检测置顶沙箱是否启动
        :param sandbox_title:
        :return:
        """
        if self.get_handle(sandbox_title):
            return True
        else:
            return False

    def launch_sandbox_s(self, sandbox_title_list: list):
        """
        批量启动沙箱
        :param sandbox_title_list:
        :return:
        """
        for sandbox_title in sandbox_title_list:
            self.launch_sandbox(sandbox_title.get("name"), sandbox_title.get("window_title"))
            time.sleep(5)
        self.launch_list = []

    def launch_sandbox(self, sandbox_name: str, window_title=None, sandbox_path=None, program_path=None):
        """
        启动单个沙箱
        :param sandbox_name:
        :param window_title:
        :param program_path:
        :param sandbox_path:
        :return:
        """
        self.set_option(sandbox_path, program_path)
        if not os.path.exists(self.program_path):
            signal_hi_worker.show_info.emit("PC端路径无效")
            return
        if not os.path.exists(self.sandbox_path):
            signal_hi_worker.show_info.emit("沙箱路径无效")
            return
        if window_title is None:
            subprocess.Popen([self.sandbox_path, "/box:" + sandbox_name, self.program_path],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        elif not self.is_sandbox_running(window_title):
            subprocess.Popen([self.sandbox_path, "/box:" + sandbox_name, self.program_path],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

    def close_sandbox(self, sandbox_title: str):
        """
        关闭沙箱
        :param sandbox_title:
        :return:
        """
        sb_hwnd = self.get_handle(sandbox_title)
        if sb_hwnd:
            win32api.SendMessage(sb_hwnd, win32con.WM_DESTROY, 0, 0)
