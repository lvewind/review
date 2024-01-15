from hiworker.capture.capture_win32api import capture_dc_to_cv
from hiworker.win32 import Win32Window
from app.load_data import coord_data
import cv2
import numpy
import time
import os


class CaptureAuto:
    def __init__(self, window_title, path, color_threshold, data_color=1):
        self.window_title = window_title
        self.color_threshold = color_threshold
        self.data_color = data_color
        self.path = os.path.abspath(os.path.join(os.getcwd(), path))
        self.env_type = 1

    def save_img_rgb(self, template, im_name):
        box = coord_data.read_coord(template)
        im = self.capture_img_rgb(box)
        cv2.imwrite(self.path + im_name + ".png", im)

    def save_img_monocolour(self, template, im_name):
        box = coord_data.read_coord(template)
        im = self.capture_img_rgb(box)
        im_monocolour = self.change_rgb_to_monocolour(im)
        # cv2.imshow(im_name, im_monocolour)
        # cv2.waitKey()
        cv2.imwrite(self.path + im_name + ".png", im_monocolour)

    # 匹配模板
    def capture_img_rgb(self, box):
        # 获取窗口句柄
        hwnd = Win32Window.get_handle(self.window_title, self.env_type)
        # 获取的句柄有效
        if hwnd:
            # 根据句柄获取CV2原图
            cv2_capture = capture_dc_to_cv(hwnd)
            cv2.imshow("", cv2_capture)
            cv2.waitKey()

            # 获取的CV2图像有效
            if type(cv2_capture) == numpy.ndarray:
                # 根据模板坐标【裁剪】CV2图像
                cv2_crop = cv2_capture[box[1]:box[3], box[0]:box[2]]
                return cv2_crop

        else:
            return False

    def change_rgb_to_monocolour(self, im_cv2):

        # 获取源图信息
        img_shape = im_cv2.shape
        height = img_shape[0]
        width = img_shape[1]
        # 二值化源图
        im_src = numpy.zeros((height, width, 1), numpy.uint8)
        im_gray = cv2.cvtColor(im_cv2, cv2.COLOR_BGR2GRAY)
        if self.data_color > 0:
            for row in range(height):
                for col in range(width):
                    if im_gray[row, col] < self.color_threshold:
                        im_src[row, col] = 255
                    else:
                        im_src[row, col] = 0
        elif self.data_color <= 0:
            for row in range(height):
                for col in range(width):
                    if im_gray[row, col] > self.color_threshold:
                        im_src[row, col] = 255
                    else:
                        im_src[row, col] = 0
        return im_src

    def change_rgb_to_monocolour_ext(self, im_cv2):
        # 获取源图信息
        img_shape = im_cv2.shape
        height = img_shape[0]
        width = img_shape[1]
        # 创建扩展背景
        im_bg = numpy.zeros((height + 60, width + 90, 1), numpy.uint8)
        im_bg.fill(255)
        im_src = self.change_rgb_to_monocolour(im_cv2)
        # 合并图层
        im_bg[30:height + 30, 30:width + 30] = im_src
        return im_bg

    def save_img_big(self):
        # 获取窗口句柄
        hwnd = Win32Window.get_handle(self.window_title, self.env_type)
        # 获取的句柄有效
        if hwnd:
            # 根据句柄获取CV2原图
            cv2_capture = capture_dc_to_cv(hwnd)
            # cv2.imshow("", cv2_capture)
            # cv2.waitKey()
            time_s = time.time()
            time_ms = time_s * 10000
            im_name = str(int(time_ms))
            print(im_name)
            cv2.imwrite(self.path + im_name + ".png", cv2_capture)


capture_auto = CaptureAuto("模拟器", "../storage/img", 190)
i = 0
while True:
    capture_auto.save_img_big()
    time.sleep(0.5)
    i += 1
    print(i)
