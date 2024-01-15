# -*- coding: UTF-8 -*-
"""
WIN32操作模拟
"""
import win32api
import win32con
import win32gui
import random
import math
import time
from typing import Union

from pywintypes import error as pywintypes_error

from .handle import Win32Handle
from ..data.coord import Coordinate


class Win32Click(Win32Handle):
    def __init__(self):
        super(Win32Click, self).__init__()
        self.window_title = ""
        self.slide_speed = 20
        self.sleep_after_slide = 0.8
        self.coordinate_data: Union[Coordinate, None] = None

    def set_data(self, window_title: str, coordinate_data: Coordinate):
        self.window_title = window_title
        self.coordinate_data = coordinate_data

    def set_click_option(self, window_title=None, slide_speed=10, sleep_after_slide=1):
        if window_title:
            self.window_title = window_title
        self.slide_speed = slide_speed
        self.sleep_after_slide = sleep_after_slide

    def click_in_template(self, template: str, sleep_after_click=0):
        """
        # 给定模板名称，随机点击该模板区域
        :param template: 模板名称
        :param sleep_after_click: 点击后延时
        :return:
        """

        # 处理坐标
        start_x, start_y, max_extent_x, max_extent_y = self.generate_coord_and_coord_extent_by_template(template)
        coord = self.coordinate_data.read_coord(template)  # 获取模板位置

        # 有效区域内的椭圆
        ellipse_theta_ratio = random.uniform(0, 2)
        ellipse_theta = ellipse_theta_ratio * math.pi
        if max_extent_x >= max_extent_y:
            # 焦点在x轴平行方向上的椭圆
            # 椭圆长轴2a = 模板尺寸长边x，在x轴平行方向
            ellipse_a = max_extent_x / 2
            ellipse_b = max_extent_y / 2
            ellipse_rand_a = random.uniform(0, ellipse_a)
            ellipse_rand_b = random.uniform(0, ellipse_b)
            point_x = int(coord[0]) + int(ellipse_a + ellipse_rand_a * math.cos(ellipse_theta))
            point_y = int(coord[1]) + int(ellipse_b + ellipse_rand_b * math.sin(ellipse_theta))

        else:
            # 焦点在y轴平行方向上的椭圆
            # 椭圆长轴2a = 模板尺寸长边y，在y轴平行方向
            ellipse_a = max_extent_y / 2
            ellipse_b = max_extent_x / 2
            ellipse_rand_a = random.uniform(0, ellipse_a)
            ellipse_rand_b = random.uniform(0, ellipse_b)
            point_x = int(coord[0]) + int(ellipse_b + ellipse_rand_b * math.sin(ellipse_theta))
            point_y = int(coord[1]) + int(ellipse_a + ellipse_rand_a * math.cos(ellipse_theta))

        if self.zoom_mode:  # 缩放模式已开启
            point_x, point_y = self.set_zoom(point_x, point_y)  # 获取缩放后的点击坐标
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.window_title, "click_in_template: ", template, (point_x, point_y))
        self.click_point((point_x, point_y), sleep_after_click)

    def click_in_circle(self, coordinate, max_radius=20, sleep_after_click=0):
        """
        # 给定坐标点，在以该点为圆心的区域内随机点击
        :param coordinate: 指定坐标点
        :param max_radius: 点击半径
        :param sleep_after_click: 点击后延时
        :return:
        """
        if random.randint(0, 1) == 1:
            r = 1
        else:
            r = -1
        point_x = int(coordinate[0]) + random.randint(1, max_radius) * r
        if random.randint(0, 1) == 1:
            r = 1
        else:
            r = -1
        point_y = int(coordinate[1]) + random.randint(1, max_radius) * r

        if self.zoom_mode:  # 缩放模式已开启
            point_x, point_y = self.set_zoom(point_x, point_y)  # 获取缩放后的点击坐标
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.window_title, "click_in_circle: ", (point_x, point_y))
        self.click_point((point_x, point_y), sleep_after_click)

    def click_point(self, coordinate: tuple, sleep_after_click=0):
        """
        # 精确点击某一个点，不推荐直接使用
        #慎用
        :param coordinate: 点击坐标
        :param sleep_after_click: 点击坐标
        :return:
        """
        hwnd = self.get_handle(self.window_title)
        try:
            click_point = win32api.MAKELONG(coordinate[0], coordinate[1])
            # win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_point)
            time.sleep(random.uniform(0.05, 0.15))
            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, click_point)
            if not sleep_after_click:
                time.sleep(random.uniform(0.1, 1))
            else:
                time.sleep(sleep_after_click)
        except pywintypes_error:
            pass

    def slide_distance_with_template(self, template, distance_x, distance_y, max_end_extent=40):
        """
        从指定模板为起点滑动一段距离
        :param template: 模板名称
        :param distance_x: X轴距离
        :param distance_y: Y轴距离
        :param max_end_extent: 滑动偏移
        :return:
        """

        # 设置拖动起始坐标
        start_x, start_y, max_extent_x, max_extent_y = self.generate_coord_and_coord_extent_by_template(template)
        # 设置拖动终点分坐标
        end_x, end_y = self.generate_coord_end_random(start_x, start_y, distance_x, distance_y, max_end_extent)
        # 开始拖动
        self.drag_a_to_b(start_x, start_y, end_x, end_y)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.window_title, "slide_distance_with_template: ",
              template, start_x, start_y, end_x, end_y)

    def slide_distance_with_point(self, start_coord, distance_x, distance_y, max_end_extent=10):
        """
        从指定模板为起点滑动一段距离
        :param start_coord: 起点坐标
        :param distance_x: X轴距离
        :param distance_y: Y轴距离
        :param max_end_extent: 滑动偏移
        :return:
        """

        # 设置拖动起始坐标
        start_x, start_y = self.generate_coord_start_random(start_coord, max_end_extent)
        # 设置拖动终点分坐标
        end_x, end_y = self.generate_coord_end_random(start_x, start_y, distance_x, distance_y, max_end_extent)
        # 开始拖动
        self.drag_a_to_b(start_x, start_y, end_x, end_y)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.window_title, "slide_distance_with_point: ", start_x, start_y, "to", end_x,
              end_y)

    def drag_a_to_b_with_template(self, template, end_coord, max_end_extent=20):
        """
        以指定模板为起点，滑动到指定终点
        :param template: 模板名称
        :param end_coord: 终点坐标
        :param max_end_extent: 滑动偏移
        :return:
        """
        # 设置拖动起始坐标
        start_x, start_y, max_extent_x, max_extent_y = self.generate_coord_and_coord_extent_by_template(template)
        # 设置拖动终点分坐标
        end_x, end_y = self.generate_coord_end_random(end_coord[0], end_coord[1], 1, 1, max_end_extent)
        # 开始拖动
        self.drag_a_to_b(start_x, start_y, end_x, end_y)

    def drag_a_to_b_with_point(self, start_coord, end_coord, max_start_extent=20, max_end_extent=20):
        """
        以指定坐标为起点，滑动到终点坐标
        :param start_coord: 起始坐标
        :param end_coord: 终点坐标
        :param max_start_extent: 起点偏移
        :param max_end_extent: 终点偏移
        :return:
        """
        start_x = start_coord[0] + random.randint(1, max_start_extent)
        start_y = start_coord[1] + random.randint(1, max_start_extent)
        # 设置拖动终点分坐标
        end_x = end_coord[0] + random.randint(1, max_end_extent)
        end_y = end_coord[1] + random.randint(1, max_end_extent)

        if self.zoom_mode:
            start_x, start_y = self.set_zoom(start_x, start_y)
            end_x, end_y = self.set_zoom(end_x, end_y)

        # 开始拖动
        self.drag_a_to_b(start_x, start_y, end_x, end_y)

    def drag_a_to_b(self, start_x, start_y, end_x, end_y, key_type="left"):
        """
        以指定坐标为起点，滑动到终点坐标（不带偏移）
        :param start_x: 起始X坐标
        :param start_y: 起始Y坐标
        :param end_x: 终点X坐标
        :param end_y: 终点Y坐标
        :param key_type: 按键类型
        :return:
        """
        # 获取窗口句柄
        hwnd = self.get_handle(self.window_title)
        if hwnd:
            try:
                # 转化鼠标起始按下和终止弹起坐标
                click_point1 = win32api.MAKELONG(start_x, start_y)
                up_point = win32api.MAKELONG(end_x, end_y)
                # 激活需要操作窗口
                try:
                    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
                    if key_type == "left":
                        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_point1)
                    elif key_type == "middle":
                        win32gui.SendMessage(hwnd, win32con.WM_MBUTTONDOWN, win32con.MK_MBUTTON, click_point1)
                    elif key_type == "right":
                        win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, click_point1)
                except pywintypes_error:
                    pass
                time.sleep(0.1)
                # 设置拖动步进(速度)
                if self.slide_speed:
                    step = self.slide_speed
                else:
                    step = random.randint(8, 16)
                # 计算拖动坐标偏移
                distance_x = end_x - start_x
                distance_y = end_y - start_y
                # 斜率存在，计算斜率和截距
                if distance_x:
                    k = round(distance_y / distance_x, 5)
                    b = start_y - (start_x * k)

                    # 斜率小于0
                    if k < 0:
                        # 坡度小，以X轴为步进基准
                        if -1 < k < 0:
                            # 若移动距离为负数，设置坐标递增值为负数
                            if distance_x < 0:
                                step = -step
                            self.stepper_based_on_the_x_axis(start_x, distance_x, step, k, b, up_point)
                        # 坡度大， 以Y轴为步进基准
                        elif k < - 1:
                            # 若移动距离为负数，设置坐标递增值为负数
                            if distance_y < 0:
                                step = -step
                            self.stepper_based_on_the_y_axis(start_y, distance_y, step, k, b, up_point)

                    # 斜率大于0
                    elif k > 0:
                        # 坡度大， 以Y轴为步进基准
                        if k > 1:
                            # 若移动距离为负数，设置坐标递增值为负数
                            if distance_y < 0:
                                step = -step
                            self.stepper_based_on_the_y_axis(start_y, distance_y, step, k, b, up_point)
                        # 坡度小，以X轴为步进基准
                        elif 0 < k < 1:
                            # 若移动距离为负数，设置坐标递增值为负数
                            if distance_x < 0:
                                step = -step
                            self.stepper_based_on_the_x_axis(start_x, distance_x, step, k, b, up_point)

                    # 斜率为0， 水平移动
                    elif k == 0:

                        if distance_x < 0:
                            step = -step
                        self.stepper_based_on_the_x_axis(start_x, distance_x, step, k, b, up_point)
                # 斜率不存在, 垂直移动
                elif distance_x == 0:
                    if distance_y < 0:
                        step = -step
                    self.stepper_based_on_the_y_axis_without_k(start_x, start_y, distance_y, step, up_point)
                # 释放鼠标
                try:
                    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
                    if key_type == "left":
                        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, up_point)
                    elif key_type == "middle":
                        win32gui.SendMessage(hwnd, win32con.WM_MBUTTONUP, win32con.MK_MBUTTON, up_point)
                    elif key_type == "right":
                        win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, up_point)
                except pywintypes_error:
                    pass
            except pywintypes_error:
                pass
        time.sleep(self.sleep_after_slide)

    def stepper_based_on_the_x_axis(self, start_x, distance_x, step, k, b, key_type="left"):
        """
        # 基于X轴步进
        :param start_x: 起点X轴坐标
        :param distance_x: X轴上的滑动距离
        :param step: 滑动步进
        :param k: 斜率
        :param b: B
        :param key_type: 按键类型
        :return:
        """
        # 获取窗口句柄
        hwnd = self.get_handle(self.window_title)
        if hwnd:
            try:
                for x in range(0, distance_x, step):
                    time.sleep(0.01)
                    current_x = start_x + x
                    current_y = math.floor(current_x * k) + int(b)
                    self.send_mouse_move(hwnd, current_x, current_y, key_type)

            except pywintypes_error:
                print("基于X轴滑动时，窗口句柄丢失")

    def stepper_based_on_the_y_axis(self, start_y, distance_y, step, k, b, key_type="left"):
        """
        基于Y轴步进
        :param start_y:
        :param distance_y:
        :param step:
        :param k:
        :param b:
        :param key_type:
        :return:
        """
        # 获取窗口句柄
        hwnd = self.get_handle(self.window_title)
        if hwnd:
            try:
                for y in range(0, distance_y, step):
                    time.sleep(0.01)
                    current_y = start_y + y
                    current_x = int((current_y - b) / k)
                    self.send_mouse_move(hwnd, current_x, current_y, key_type)
            except pywintypes_error:
                print("基于Y轴滑动时，窗口句柄丢失")

    def stepper_based_on_the_y_axis_without_k(self, start_x, start_y, distance_y, step, key_type="left"):
        """
        # 斜率不存在时，基于Y轴步进
        :param start_x:
        :param start_y:
        :param distance_y:
        :param step:
        :param key_type:
        :return:
        """
        # 获取窗口句柄
        hwnd = self.get_handle(self.window_title)
        if hwnd:
            try:
                for y in range(0, distance_y, step):
                    time.sleep(0.01)
                    current_y = start_y + y
                    current_x = start_x
                    self.send_mouse_move(hwnd, current_x, current_y, key_type)
            except pywintypes_error:
                print("竖直滑动时，窗口句柄丢失")

    @staticmethod
    def send_mouse_move(hwnd, current_x, current_y, key_type="left"):
        if key_type == "left":
            win32api.SendMessage(hwnd,
                                 win32con.WM_MOUSEMOVE,
                                 win32con.MK_LBUTTON,
                                 win32api.MAKELONG(current_x, current_y))
        else:
            win32api.SendMessage(hwnd,
                                 win32con.WM_MOUSEMOVE,
                                 win32con.MK_MBUTTON,
                                 win32api.MAKELONG(current_x, current_y))

    def send_mouse_zoom(self, screen_x, screen_y, scroll_times: int, scroll_up=True):
        hwnd = self.get_handle(self.window_title)
        if hwnd:
            if scroll_up:
                scroll_speed = self.slide_speed
            else:
                scroll_speed = -self.slide_speed
            for i in range(scroll_times):
                win32api.SendMessage(hwnd, win32con.WM_MOUSEWHEEL,
                                     win32api.MAKELONG(0, scroll_speed),
                                     win32api.MAKELONG(screen_x, screen_y))
                time.sleep(0.01)

    def generate_coord_and_coord_extent_by_template(self, template):
        coord = self.coordinate_data.read_coord(template)  # 获取模板位置
        max_extent_x = self.coordinate_data.read_size(template)[0]  # 获取模板尺寸宽
        if not max_extent_x:  # 模板尺寸宽为0，
            max_extent_x = int((coord[2] - coord[0]) / 2)  # 根据模板位置计算坐标偏移量X
        max_extent_y = self.coordinate_data.read_size(template)[1]  # 获取模板尺寸高
        if not max_extent_y:  # 模板尺寸高度为0，
            max_extent_y = int((coord[3] - coord[1]) / 2)  # 根据模板位置计算坐标偏移量Y

        start_x = int((coord[0] + random.randint(1, max_extent_x)))
        start_y = int((coord[1] + random.randint(1, max_extent_y)))
        if self.zoom_mode:
            start_x, start_y = self.set_zoom(start_x, start_y)
            max_extent_x, max_extent_y = self.set_zoom(max_extent_x, max_extent_y)
        return start_x, start_y, max_extent_x, max_extent_y

    def generate_coord_start_random(self, start_coord, max_end_extent):
        # 设置拖动起始坐标
        start_x = start_coord[0] + random.randint(1, max_end_extent)
        start_y = start_coord[1] + random.randint(1, max_end_extent)
        if self.zoom_mode:
            start_x, start_y = self.set_zoom(start_x, start_y)
        return int(start_x), int(start_y)

    def generate_coord_end_random(self, start_x, start_y, distance_x, distance_y, max_end_extent):
        # 设置拖动终点分坐标
        end_x = start_x + distance_x + random.randint(1, max_end_extent)
        end_y = start_y + distance_y + random.randint(1, max_end_extent)
        if self.zoom_mode:
            end_x, end_y = self.set_zoom(end_x, end_y)
        return int(end_x), int(end_y)

    def set_zoom(self, point_x, point_y):
        hwnd = self.get_handle(self.window_title)
        if hwnd:
            try:
                client_rect = win32gui.GetClientRect(hwnd)
                if not client_rect[2] == self.standard_size[0]:
                    fx = client_rect[2] / self.standard_size[0]  # 获取缩放比例
                    return point_x * fx, point_y * fx  # 返回缩放后的坐标
                else:
                    return point_x, point_y  # 窗口没有缩放，返回原坐标
            except pywintypes_error:
                return point_x, point_y  # 窗口异常，返回原坐标
