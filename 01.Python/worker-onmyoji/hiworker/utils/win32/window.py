# -*- coding: UTF-8 -*-
"""
目标窗口操作
"""
import win32gui
import win32con
import win32api
import os
import _ctypes
import math

from pywintypes import error as pywintypes_error
import pyvda


class Win32Window(object):
    def __init__(self):
        self.correction_window_position = [8, 8, 1152, 679]
        self.window_width_with_span = self.correction_window_position[2] + 16
        self.window_high_with_span = self.correction_window_position[3]
        self.window_row_span = 120

    def set_option(self, correction_window_position: None):
        """
        设置win32操作参数
        :param correction_window_position:
        :return:
        """
        self.correction_window_position = correction_window_position if correction_window_position else [8, 8, 1152, 679]

    def set_window_position_by_title(self, window_title, x=64, y=64):
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            try:
                win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, x, y,
                                      self.correction_window_position[2],
                                      self.correction_window_position[3], win32con.SWP_SHOWWINDOW)
                win32gui.SetForegroundWindow(hwnd)
            except TypeError as e:
                print(window_title, e)
            except pywintypes_error as ie:
                print(window_title, ie)

    @staticmethod
    def set_window_top(window_title: str):
        """
        置顶窗口
        :param window_title:
        :return:
        """
        try:
            hwnd = win32gui.FindWindow(None, window_title)
            win32gui.SetForegroundWindow(hwnd)
        except pywintypes_error as e:
            print(e)

    def set_window_left_top(self, window_title_list: list):
        if window_title_list:
            current_desktop = pyvda.GetCurrentDesktopNumber()
            for window_title in window_title_list:
                self.set_window_position_by_title(window_title)
            self.go_to_desktop(current_desktop)

    def sort_window_on_own_desktop(self, window_title_list: list, offset_x=0, offset_y=0):
        if window_title_list:
            self.tile_window_on_own_desktop(window_title_list, sort_mode=True, offset_x=offset_x, offset_y=offset_y)

    def tile_window_on_own_desktop(self, window_title_list: list, sort_mode=False, offset_x=0, offset_y=0):
        if window_title_list:
            last_desktop = pyvda.GetCurrentDesktopNumber()
            desktop_count = pyvda.GetDesktopCount()
            for i in range(1, desktop_count + 1):
                # 获取虚拟桌面的窗口列表
                target_desktop_active_window = self.get_target_desktop_window_list(window_title_list, i)
                if target_desktop_active_window:
                    # 获取窗口数量
                    window_count = len(target_desktop_active_window)
                    # 获取屏幕大小
                    screen_rect = self.get_system_screen_rect()
                    # 计算窗口行数
                    if sort_mode:
                        max_row = int((screen_rect[1] - self.window_high_with_span) / self.window_row_span)
                    else:
                        max_row = int(screen_rect[1]/self.window_high_with_span)
                    # 计算窗口列数
                    max_col = math.ceil(window_count/max_row)
                    # 初始化当前行数
                    current_row = 1
                    # 计算列间距和第一个窗口x坐标
                    if max_col * self.window_width_with_span > screen_rect[0] + offset_x:
                        start_x = 8
                        end_x = screen_rect[0] + offset_x - self.window_width_with_span
                        space_x = end_x - start_x
                        col_span = int(space_x / (max_col - 1)) - self.window_width_with_span
                    else:
                        start_x = (screen_rect[0] + offset_x) - (max_col * self.window_width_with_span)
                        col_span = 16

                    # 初始化第一个窗口坐标
                    sort_x = start_x
                    sort_y = 8 + offset_y

                    # 设置窗口位置
                    for window in target_desktop_active_window:
                        if current_row <= max_row:
                            self.set_window_position_by_title(window.get("title"), sort_x, sort_y)
                        else:
                            current_row = 1
                            sort_y = 8
                            sort_x += (self.correction_window_position[2] + col_span)
                            self.set_window_position_by_title(window.get("title"), sort_x, sort_y)
                        current_row += 1
                        if sort_mode:
                            sort_y += self.window_row_span
                        else:
                            sort_y += self.window_high_with_span

            self.go_to_desktop(last_desktop)

    def go_to_desktop_with_window(self, window_title: str):
        run_item_hwnd = win32gui.FindWindow(None, window_title)
        if run_item_hwnd:
            desktop_number = pyvda.GetWindowDesktopNumber(run_item_hwnd)
            self.go_to_desktop(desktop_number)

    @staticmethod
    def get_last_desktop_count():
        return pyvda.GetDesktopCount()

    @staticmethod
    def get_target_desktop_window_list(window_title_list, desktop: int):
        target_desktop_active_window = []
        for title_item in window_title_list:
            hwnd = win32gui.FindWindow(None, title_item.get("title"))
            if hwnd:
                try:
                    if desktop == pyvda.GetWindowDesktopNumber(hwnd):
                        target_desktop_active_window.append(title_item)
                except _ctypes.COMError:
                    pass
        return target_desktop_active_window

    @staticmethod
    def terminate_window(window_title: str):
        """
        关闭窗口
        :param window_title:
        :return:
        """
        hwnd = win32gui.FindWindow(None, window_title)
        win32api.SendMessage(hwnd, win32con.WM_DESTROY, 0, 0)

    @staticmethod
    def move_window_to_desktop(window_title_list: list, desktop: int):
        if not desktop:
            desktop = pyvda.GetCurrentDesktopNumber()
        max_desktop = pyvda.GetDesktopCount()
        if max_desktop < desktop:
            desktop = max_desktop
        for window_title in window_title_list:
            hwnd = win32gui.FindWindow(None, window_title)
            if hwnd:
                try:
                    pyvda.MoveWindowToDesktopNumber(hwnd, desktop)
                except _ctypes.COMError as e:
                    print(e)

    @staticmethod
    def open_folder(path=os.path.abspath("..") + os.path.sep + "storage" + os.path.sep + "backup"):
        if os.path.exists(path):
            os.system("explorer.exe %s" % path)
        else:
            os.makedirs(path, exist_ok=True)
            os.system("explorer.exe %s" % path)

    @staticmethod
    def get_system_screen_rect():
        screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        return [screen_x, screen_y]

    @staticmethod
    def go_to_desktop(desktop: int):
        hwnd = win32gui.GetActiveWindow()
        try:
            pyvda.MoveWindowToDesktopNumber(hwnd, desktop)
        except _ctypes.COMError:
            pass
        pyvda.GoToDesktopNumber(desktop)


win32_window = Win32Window()
