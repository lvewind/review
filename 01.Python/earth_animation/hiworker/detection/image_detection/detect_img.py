# -*- coding: UTF-8 -*-
"""
# 图片检测模块
"""
import cv2
import numpy
import time
from typing import Union

from ..capture import *
from ...utils import *


class DetectImage(Win32Handle):
    def __init__(self):
        super(DetectImage, self).__init__()
        self.window_title = ""
        self.hwnd = None
        self.similarity = 0.8
        self.check_time = 1
        self.cpu_down_time = 0.1
        self.show_dc_img = False
        self.show_trim = False
        self.debug = False
        self.coordinate_data: Union[Coordinate, None] = None
        self.image_data: Union[InitImage, None] = None

    def set_data(self, window_title: str, image_data: InitImage, coordinate_data: Coordinate):
        self.window_title = window_title
        self.coordinate_data = coordinate_data
        self.image_data = image_data

    def set_detect_option(self, window_title=None, similarity=0.8, check_time=1, cpu_down_time=0.01,
                          show_dc_img=False, show_trim=False, debug=False):
        """
        设置检测实例基本参数
        :param window_title: 窗口标题
        :param similarity: 相似度
        :param check_time: 动态时间
        :param cpu_down_time: cpu执行间隔
        :param show_dc_img: 显示DC截图
        :param show_trim: 显示裁剪结果
        :param debug: 是否开启debug模式
        :return:
        """
        if window_title:
            self.window_title = window_title

        self.similarity = similarity
        self.check_time = check_time
        self.cpu_down_time = cpu_down_time
        self.show_dc_img = show_dc_img
        self.show_trim = show_trim
        self.debug = debug

    def find_in_dynamic_scene(self, template, similarity=0.8, check_t=None):
        """
        在动态画面查找图片
        :param check_t: 查找时间
        :param template: 图片模板名称
        :param similarity: 相似度
        :return:
        """
        if check_t:
            check_time = check_t
        else:
            check_time = self.check_time
        start_time = time.time()
        run_time = 0
        while run_time <= check_time:
            run_time = time.time() - start_time
            # print(image_coordinate)
            result, coord, max_similarity = self.find_in_template_rect(template, similarity)
            if result:
                return result, coord, max_similarity
            else:
                continue
        else:
            return False, [0, 0], max_similarity

    def find_in_template_rect(self, template, similarity=0.8):
        """
        在模板区域内查找图片
        :param template: 模板名称
        :param similarity: 相似度
        :return: [bool， [x, y]] 查找结果以及坐标
        """
        # 读取模板坐标
        area = self.coordinate_data.read_coord(template)

        return self.find_img_in_rect(template, area, similarity)

    def find_in_different_template_rect(self, template, other_template, similarity=0.8):
        """
        在额外的模板区域查找图片
        :param template: 模板名称
        :param other_template: 区域名称
        :param similarity: 相似度
        :return: [bool， [x, y]] 查找结果以及坐标
        """
        # 读取模板坐标
        area = self.coordinate_data.read_coord(other_template)
        return self.find_img_in_rect(template, area, similarity)

    def find_with_point_ext_area(self, template, target_point: list, box: list, similarity=0.8):
        """
        以某个点为中心的区域查找图片
        :param template: 模板名称
        :param target_point: 目标坐标
        :param box: 截图区域
        :param similarity:
        :return: [bool， [x, y]] 查找结果以及坐标
        """
        # 读取模板坐标
        area = [target_point[0] - box[0],
                target_point[1] - box[1],
                target_point[0] + box[2],
                target_point[1] + box[3]]
        return self.find_img_in_rect(template, area, similarity)

    def find_user_template_area(self, user_template, user_coord, similarity=0.8):
        """
        基于check_img_match，查找用户定义图片
        :param user_template: 模板名称
        :param user_coord: 区域名称
        :param similarity: 相似度
        :return: [bool， [x, y]] 查找结果以及坐标
        """
        # 读取模板坐标
        area = self.coordinate_data.read_coord(user_coord)
        return self.find_img_in_rect(user_template, area, similarity)

    def find_img_in_rect(self, template, area: list, similarity=0.8):
        """
        在明确区域内查找图片
        :param template: 模板名称
        :param area: 查找区域
        :param similarity: 相似度
        :return: [bool， [x, y]] 查找结果以及坐标
        """
        if area:
            # 读取模板图像数据
            template_data = self.image_data.read_template(template)
            # 读取模板尺寸
            size = self.coordinate_data.read_size(template)
            if not size:
                if type(template_data) == numpy.ndarray:
                    size = [template_data.shape[1], template_data.shape[0]]
                else:
                    pass
            # 获取窗口原始截图
            source_cv2_capture = capture_dc_to_cv(self.get_handle(self.window_title))

            if type(source_cv2_capture) == numpy.ndarray:  # 成功获取CV2原始图片
                if self.zoom_mode:  # 启用缩放模式，根据缩放比例重设裁剪区域和图片位置
                    src_height, src_width = source_cv2_capture.shape[:2]
                    fx = src_width / self.standard_size[0]
                    area = self.set_zoom_trim_area(area, fx)
                    size = self.set_zoom_trim_size(size, fx)
                    template_data = cv2.resize(template_data, None, fx=fx, fy=fx)  # 缩放用于模板匹配的预设图像数据
                # 裁剪用于匹配的区域
                cv2_crop = self.trim_cv2_img_with_rect(source_cv2_capture, area)
                # 执行模板匹配
                result, coord, max_similarity = self.match_template(cv2_crop, template_data, similarity)
                if result:
                    # 设置找到的图片的中心坐标
                    coord[0] = coord[0] + area[0] + int(size[0] / 2)
                    coord[1] = coord[1] + area[1] + int(size[1] / 2)
                return result, coord, max_similarity
            else:  # 未能获取CV2原始图片
                return False, [0, 0], 0
        else:  # 找不到模板坐标
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.window_title, "找不到模板坐标数据: ", template)
            return False, [0, 0], 0

    def find_color_in_v2_auto(self, template, rgb_color: list):
        """
        在环形区域查找颜色
        :param template: 区域名称
        :param rgb_color: rgb颜色
        :return:
        """
        box_left = [0, 0, 12, 60]
        box_top = [0, 0, 60, 12]
        box_right = [48, 0, 60, 60]
        box_bottom = [0, 48, 60, 60]
        # 获取模板坐标
        box = self.coordinate_data.read_coord(template)
        # box = [795, 475, 855, 535]
        source_cv2_capture = capture_dc_to_cv(self.get_handle(self.window_title))
        if type(source_cv2_capture) == numpy.ndarray:  # 成功获取CV2原始图片
            if self.zoom_mode:  # 启用缩放模式，根据缩放比例重设裁剪区域和图片位置
                src_height, src_width = source_cv2_capture.shape[:2]
                fx = src_width / self.standard_size[0]
                box = self.set_zoom_trim_area(box, fx)
                box_left = self.set_zoom_trim_area(box_left, fx)
                box_top = self.set_zoom_trim_area(box_top, fx)
                box_right = self.set_zoom_trim_area(box_right, fx)
                box_bottom = self.set_zoom_trim_area(box_bottom, fx)

            cv2_crop = self.trim_cv2_img_with_rect(source_cv2_capture, box)  # 获取自动按钮方形截图
            height, width, channel = cv2_crop.shape
            # 方形截图处理为环形透明截图
            im_torus = self.trim_image_to_torus(cv2_crop)
            if self.zoom_mode:  # 启用缩放模式，重新校验截图子区域大小，防止超出范围
                # 处理左截图子区域
                if box_left[3] > height:
                    box_left[3] = height

                # 处理上截图子区域
                if box_top[2] > width:
                    box_top[2] = width

                # 处理右边截图子区域
                if box_right[2] > width:
                    box_right[2] = width
                if box_right[3] > height:
                    box_right[3] = height

                # 处理底部截图子区域
                if box_bottom[2] > width:
                    box_bottom[2] = width
                if box_bottom[3] > height:
                    box_bottom[3] = height
            # 检测自动按钮左边区域
            cv2_crop_left = self.trim_cv2_img_with_rect(im_torus, box_left)
            # cv2.imshow("cv2_crop_left", cv2_crop_left)
            # cv2.waitKey()
            result, coord, max_similarity = self.check_color(cv2_crop_left, rgb_color, 10)
            print(result, coord)
            if result:
                return True
            else:
                # 检测自动按钮上边区域
                cv2_trim_top = self.trim_cv2_img_with_rect(im_torus, box_top)
                # cv2.imshow("cv2_trim_top", cv2_trim_top)
                # cv2.waitKey()
                result, coord, max_similarity = self.check_color(cv2_trim_top, rgb_color, 10)
                print(result, coord)
                if result:
                    return True
                else:
                    # 检测自动按钮右边区域
                    cv2_trim_right = self.trim_cv2_img_with_rect(im_torus, box_right)
                    result, coord, max_similarity = self.check_color(cv2_trim_right, rgb_color, 10)
                    print(result, coord)
                    if result:
                        return True
                    else:
                        # 检测自动按钮下边区域
                        cv2_trim_bottom = self.trim_cv2_img_with_rect(im_torus, box_bottom)
                        result, coord, max_similarity = self.check_color(cv2_trim_bottom, rgb_color, 10)
                        print(result, coord)
                        return result
        else:  # 未能获取CV2原始图片
            return False

    def find_color_with_template_area(self, template, rgb_color: list, tolerance=5):
        """
         在模板区域内查找颜色
        :param template: 区域名称
        :param rgb_color: 目标rgb颜色
        :param tolerance: 容差
        :return: [bool， [x, y]] 查找结果以及坐标
        """
        # 设置找色区域
        area = self.coordinate_data.read_coord(template)
        return self.find_color_in_area(area, rgb_color, tolerance)

    def find_color_with_point_ext_area(self, target_point: list, area_box: list, rgb_color: list, tolerance=5):
        """
        在以某一点为中心的区域查找颜色
        :param target_point: 目标坐标
        :param rgb_color: 目标颜色
        :param area_box: 目标裁剪区域
        :param tolerance: 容差
        :return: [bool， [x, y]] 查找结果以及坐标
        """
        area = [target_point[0] - area_box[0],
                target_point[1] - area_box[1],
                target_point[0] + area_box[2],
                target_point[1] + area_box[3]]
        return self.find_color_in_area(area, rgb_color, tolerance)

    def find_color_in_area(self, area: list, rgb_color: list, tolerance=5):
        """
        在区域内查找颜色
        :param area:  坐标区域
        :param rgb_color: rgb颜色
        :param tolerance: 容差
        :return:
        """
        source_cv2_capture = capture_dc_to_cv(self.get_handle(self.window_title))
        if type(source_cv2_capture) == numpy.ndarray:  # 成功获取CV2原始图片
            if self.zoom_mode:  # 启用缩放模式，根据缩放比例重设裁剪区域和图片位置
                src_height, src_width = source_cv2_capture.shape[:2]
                fx = src_width / self.standard_size[0]
                area = self.set_zoom_trim_area(area, fx)

            cv2_crop = self.trim_cv2_img_with_rect(source_cv2_capture, area)
            if self.show_trim:
                cv2.imshow("", cv2_crop)
                cv2.waitKey()
            result, coord, max_similarity = self.check_color(cv2_crop, rgb_color, tolerance)
            coord[0] = coord[0] + area[0]
            coord[1] = coord[1] + area[1]
            return result
        else:
            return False

    def match_template(self, cv2_img, cv2_template_data, similarity):
        """
        # 匹配模板
        :param cv2_img: 截图数据
        :param cv2_template_data: 模板数据
        :param similarity: 相似度
        :return: True, False; 图片中心坐标，没有匹配图片则返回[0, 0]
        """
        time.sleep(self.cpu_down_time)
        if type(cv2_img) == numpy.ndarray:
            # 图像检测，并返回所有结果
            try:
                result = cv2.matchTemplate(cv2_img, cv2_template_data, cv2.TM_CCOEFF_NORMED)
                if self.debug:
                    print(result.dtype)
                    print(result.strides)
                min_similarity, max_similarity, min_loc, max_loc = cv2.minMaxLoc(result)
                if max_similarity >= similarity:
                    # 满足相似度条件，返回True以及相似度最高的图片相对位置
                    return True, [max_loc[0], max_loc[1]], max_similarity
                else:
                    # 未满足相似度条件，返回False以及相似度最高的图片相对位置
                    return False, [max_loc[0], max_loc[1]], max_similarity
            except cv2.error:
                return False, [0, 0, 0]
        else:
            return False, [0, 0, 0]

    @staticmethod
    def check_color(cv2_img, rgb_color: list, tolerance):
        """
        加测截图中的颜色
        :param cv2_img: 截图数据
        :param rgb_color: 需要检测的颜色
        :param tolerance: 容差
        :return:
        """
        # 图像检测，并返回所有结果
        if type(cv2_img) == numpy.ndarray:
            hsv_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2HSV)
            # 获取颜色矩阵大小
            rows, cols, dimension = hsv_img.shape
            # 转换需要查找的颜色为HSV颜色空间
            hsv_color = cv2.cvtColor(numpy.array([[rgb_color]], numpy.uint8), cv2.COLOR_RGB2HSV)
            # print(hsv_color)
            # 遍历矩阵，对比HSV颜色
            for i in range(rows):
                time.sleep(0.01)
                for j in range(cols):
                    if -tolerance <= int(hsv_color[0, 0][0]) - int(hsv_img[i, j][0]) <= tolerance:
                        if -tolerance <= int(hsv_color[0, 0][1]) - int(hsv_img[i, j][1]) <= tolerance:
                            if -tolerance <= int(hsv_color[0, 0][2]) - int(hsv_img[i, j][2]) <= tolerance:
                                # 满足颜色容差(颜色存在)，返回Ture
                                return True, [j, i], 1
            else:
                return False, [0, 0], 0
        else:
            return False, [0, 0], 0

    def trim_cv2_img_with_rect(self, cv2_img, rect: list):
        """
        根据矩形裁剪图像
        :param cv2_img: 待裁剪的图像数据
        :param rect:  裁剪区域
        :return: None
        """
        if type(cv2_img) == numpy.ndarray:
            cv2_crop = cv2_img[rect[1]:rect[3], rect[0]:rect[2]]
            if self.show_trim:
                cv2.imshow("", cv2_crop)
                cv2.waitKey()
            return cv2_crop

    @staticmethod
    def set_zoom_trim_area(box: list, fx):
        """
        设置裁剪缩放
        :param box: 原始裁剪区域
        :param fx: 缩放比例
        :return:
        """
        for i in range(4):
            box[i] = int(box[i] * fx)
        return box

    @staticmethod
    def set_zoom_trim_size(size: list, fx):
        """
        设置裁剪缩放尺寸
        :param size: 原尺寸
        :param fx: 缩放比例
        :return:
        """
        for i in range(2):
            size[i] = int(size[i] * fx)
        return size

    @staticmethod
    def check_color_sub_trim_size(sub_box: list, box: list, sub_box_position="left"):
        """
        裁剪子区域
        :param sub_box:
        :param box:
        :param sub_box_position:
        :return:
        """
        b_height = box[3] - box[1]
        b_width = box[2] - box[0]
        if sub_box_position == "left":
            if sub_box[3] > b_height:
                sub_box[3] = b_height
        elif sub_box_position == "top":
            if sub_box[2] > b_width:
                sub_box[2] = b_width
        elif sub_box_position == "right" or sub_box_position == "bottom":
            if sub_box[2] > b_width:
                sub_box[2] = b_width
            if sub_box[3] > b_height:
                sub_box[3] = b_height
        return sub_box

    @staticmethod
    def trim_image_to_torus(cv2_crop):
        """
        将图片转换为透明环形
        :param cv2_crop:
        :return:
        """
        height, width, channel = cv2_crop.shape
        height = int(height)
        width = int(width)
        im_black = numpy.zeros((height, width, 1), numpy.uint8)
        im_black.fill(0)
        im_black = cv2.circle(im_black, (width // 2, height // 2), min(height, width) // 2, (1,), -1)
        # cv2.imshow("im_black", im_black)
        # cv2.waitKey()
        im_trim = numpy.zeros((height, width, 3), numpy.uint8)
        # 复制前3个通道
        im_trim[:, :, 0] = numpy.multiply(cv2_crop[:, :, 0], im_black[:, :, 0])
        im_trim[:, :, 1] = numpy.multiply(cv2_crop[:, :, 1], im_black[:, :, 0])
        im_trim[:, :, 2] = numpy.multiply(cv2_crop[:, :, 2], im_black[:, :, 0])
        return im_trim
