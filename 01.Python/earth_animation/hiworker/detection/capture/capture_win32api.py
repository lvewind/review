# -*- coding: UTF-8 -*-
"""
基于pywin32获取窗口截图
"""
import win32con
import win32gui
import win32ui
import cv2
import numpy
import pywintypes


def capture_dc_to_cv(hwnd):
    """
    :param hwnd: 需要截图的窗口句柄
    :return: 返回截取到的图片(cv2格式)，句柄异常时返回False
    """
    if hwnd:
        try:
            # 获取窗口客户区大小, 用于创建DC位图
            _left, _top, _right, _bottom = win32gui.GetClientRect(hwnd)
            client_w = _right - _left
            client_h = _bottom - _top
            # print(client_w, client_h)
            # 设置截取的窗口大小参数
            # client_w = 960
            # client_h = 540
            # 返回句柄窗口的设备环境、覆盖整个窗口，包括非客户区，标题栏，菜单，边框
            hwnd_dc = win32gui.GetDC(hwnd)
            # 创建设备描述表
            mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
            # 创建内存设备描述表
            # time.sleep(5)
            save_dc = mfc_dc.CreateCompatibleDC()
            # 创建位图对象
            save_bit_map = win32ui.CreateBitmap()
            save_bit_map.CreateCompatibleBitmap(mfc_dc, client_w, client_h)
            save_dc.SelectObject(save_bit_map)
            # 截图至内存设备描述表
            img_dc = mfc_dc
            mem_dc = save_dc
            try:
                mem_dc.BitBlt((0, 0), (client_w, client_h), img_dc, (0, 0), win32con.SRCCOPY)
            except win32ui.error:
                win32gui.DeleteObject(save_bit_map.GetHandle())
                save_dc.DeleteDC()
                return False
            # save_bit_map.SaveBitmapFile(mem_dc, 'whole_scene_by_win32.bmp')

            # 改变下行决定是否截图整个窗口
            # windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 1)
            # windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 0)
            # 获取位图信息
            # bmp_info = save_bit_map.GetInfo()
            bmp_str = save_bit_map.GetBitmapBits(True)
            img = numpy.frombuffer(bmp_str, dtype='uint8')
            img.shape = (client_h, client_w, 4)

            # 内存释放
            win32gui.DeleteObject(save_bit_map.GetHandle())
            save_dc.DeleteDC()
            mfc_dc.DeleteDC()

            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

            # 返回整个客户区截图
            return img
        except pywintypes.error:
            return False
    else:
        return False
