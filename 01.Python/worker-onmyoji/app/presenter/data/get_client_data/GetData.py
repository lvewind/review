import time
import numpy
import cv2

from hiworker import *

from app.presenter.scheduler.play.Common.Common import Common
from app.presenter.data import data_user


mutex = ThreadLock()


class GetData(Common):
    def __init__(self, run_id):
        """
        获取数据类初始化
        :param run_id: 需要更新数据的运行列表id
        """
        self.run_id = run_id
        window_title = data_user.execute_data.read_row_field(self.run_id, "em_name")
        super(GetData, self).__init__(window_title)
        self.tess = Tesseract()
        # self.tess = tess
        self.window_title = window_title
        self.tolerance = 64
        self.coin_list = []
        self.coin_value = 0
        self.diamond_value = 0
        self.ticket_value = 0
        self.sea_heart_value = 0
        self.energy_value = 0
        self.gold_soul_value = 0
        self.bomb_value = 0
        self.freeze_value = 0
        self.speed_shoot_value = 0
        self.lock_in_value = 0
        self.other_data_time_sleep = 3
        self.time_sleep_after_ocr = 0.5
        self.time_sleep_after_not_available = 0.5
        data_user.execute_data.update_rows_field(self.run_id, "coin", 0)
        data_user.execute_data.update_rows_field(self.run_id, "top_coin", 0)

    def delete_tess(self):
        pass
        # self.tess.__del__()

    def get_capture_template_crop_img(self, template):
        """
        获取模板裁剪后的截图
        :param template:
        :return:
        """
        # 获取窗口句柄
        hwnd = win32_window.get_handle(self.window_title)
        # 获取的句柄有效
        if hwnd:
            # 根据句柄获取CV2原图
            cv2_capture = capture_dc_to_cv(hwnd)
            # 获取的CV2图像有效
            if type(cv2_capture) == numpy.ndarray:
                # 根据模板【裁剪】CV2图像
                box = coordinate_data.read_coord(template)
                cv2_crop = cv2_capture[box[1]:box[3], box[0]:box[2]]
                # cv2.imshow("", cv2_crop)
                # cv2.waitKey()
                return cv2_crop

    def is_rgb_color_in_data_area(self, cv2_crop, rgb_color):
        """
        检测给定图片是否有指定颜色
        :param cv2_crop:
        :param rgb_color:
        :return:
        """
        # 判断im_cv2是否有效
        if type(cv2_crop) == numpy.ndarray:
            # 将im_cv2转换为hsv色彩空间
            hsv_img = cv2.cvtColor(cv2_crop, cv2.COLOR_BGR2HSV)
            # 获取颜色矩阵大小
            rows, cols, dimension = hsv_img.shape
            # 转换目标RGB颜色转为HSV颜色
            hsv_color = cv2.cvtColor(numpy.array([[rgb_color]], numpy.uint8), cv2.COLOR_RGB2HSV)
            has_other_color = False
            # 遍历矩阵，对比HSV颜色
            for i in range(rows):
                for j in range(cols):
                    # 计算目标颜色H差
                    colour_difference_h = abs(int(hsv_color[0, 0][0]) - int(hsv_img[i, j][0]))
                    # 计算目标颜色S差
                    colour_difference_s = abs(int(hsv_color[0, 0][1]) - int(hsv_img[i, j][1]))
                    # 计算目标颜色V差
                    colour_difference_v = abs(int(hsv_color[0, 0][2]) - int(hsv_img[i, j][2]))

                    # 判断色差是否存在指定颜色
                    if (colour_difference_h <= self.tolerance) and (colour_difference_s <= self.tolerance) and (
                            colour_difference_v <= self.tolerance):
                        # 有目标颜色，跳出检测
                        has_other_color = True
                        break
                    # 没有目标颜色
                    else:
                        has_other_color = False
            # 返回目标颜色存在状态
            return has_other_color
        # 传入的CV2图像无效，等效于存在其他颜色，返回True
        else:
            return True

    def get_coin_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的金币数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        time.sleep(self.time_sleep_after_ocr)
        ocr_number = self.tess.ocr_output_src_number(cv2_crop, color_threshold, data_color)
        if ocr_number:
            return ocr_number
        else:
            return False

    def get_diamond_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的钻石数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        ocr_str = self.tess.ocr_output_src_number(cv2_crop, color_threshold, data_color)
        if type(ocr_str) == int:
            self.diamond_value = ocr_str
        time.sleep(self.other_data_time_sleep)

    def get_energy_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的钻石数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        ocr_str = self.tess.ocr_output_src_number(cv2_crop, color_threshold, data_color)
        if type(ocr_str) == int:
            self.energy_value = ocr_str
        time.sleep(self.other_data_time_sleep)

    def get_ticket_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的奖券数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        ocr_str = self.tess.ocr_output_src_number(cv2_crop, color_threshold, data_color)
        if type(ocr_str) == int:
            self.ticket_value = ocr_str
        time.sleep(self.other_data_time_sleep)

    def get_sea_heart_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的海洋之心数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        ocr_str = self.tess.ocr_output_src_number(cv2_crop, color_threshold, data_color)
        if type(ocr_str) == int:
            self.sea_heart_value = ocr_str
        time.sleep(self.other_data_time_sleep)

    def get_gold_soul_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的海洋之心数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        ocr_str = self.tess.ocr_output_src_number(cv2_crop, color_threshold, data_color)
        if type(ocr_str) == int:
            self.gold_soul_value = ocr_str
        time.sleep(self.other_data_time_sleep)

    def get_bomb_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的弹头数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        ocr_str = self.tess.ocr_output_number(cv2_crop, color_threshold, data_color)
        if type(ocr_str) == int:
            self.bomb_value = ocr_str
        time.sleep(self.other_data_time_sleep)

    def get_freeze_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的冰冻数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        ocr_str = self.tess.ocr_output_number(cv2_crop, color_threshold, data_color)
        if type(ocr_str) == int:
            self.freeze_value = ocr_str
        time.sleep(self.other_data_time_sleep)

    def get_speed_shoot_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的速射数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        ocr_str = self.tess.ocr_output_number(cv2_crop, color_threshold, data_color)
        if type(ocr_str) == int:
            self.speed_shoot_value = ocr_str
        time.sleep(self.other_data_time_sleep)

    def get_lock_number_from_img(self, cv2_crop, color_threshold=180, data_color=1):
        """
        获取给定图片中的锁定数据
        :param cv2_crop:
        :param color_threshold:
        :param data_color:
        :return:
        """
        ocr_str = self.tess.ocr_output_number(cv2_crop, color_threshold, data_color)
        if type(ocr_str) == int:
            self.lock_in_value = ocr_str
        time.sleep(self.other_data_time_sleep)

    def update_current_coin(self):
        """
        更新当前金币数量
        :return:
        """
        if self.coin_value:
            last_coin = int(data_user.execute_data.read_row_field(self.run_id, "coin"))
            mutex.lock()
            if self.coin_value < last_coin:
                coin_d_value = last_coin / self.coin_value
                if coin_d_value <= 7:
                    data_user.execute_data.update_rows_field(self.run_id, "coin", self.coin_value)
                    top_coin = data_user.execute_data.read_row_field(self.run_id, "top_coin")
                    if self.coin_value > top_coin:
                        data_user.execute_data.update_rows_field(self.run_id, "top_coin", self.coin_value)
                    self.coin_value = 0

            else:
                data_user.execute_data.update_rows_field(self.run_id, "coin", self.coin_value)
                top_coin = data_user.execute_data.read_row_field(self.run_id, "top_coin")
                if self.coin_value > top_coin:
                    data_user.execute_data.update_rows_field(self.run_id, "top_coin", self.coin_value)
            self.coin_value = 0
