from app.load_data import LoadData
import cv2


class CheckCapture(DetectImage, OperateWin32Api):
    def __init__(self, window_title):
        super(CheckCapture, self).__init__(window_title)
        self.env_type = 1
        # self.get_client_data = Tesseract(language=b"chi_sim_fzbwks")
        self.correction_window = False

    def check_common(self, template: str, similarity):
        result, coord = self.find_in_template_area(template, similarity=similarity, debug=True, show_dc_img=True, show_trim=False)
        return result, coord

    def check_dynamic(self, template: str, similarity):
        result, coord = self.find_in_dynamic_scene(template, similarity=similarity, debug=False, latency=1.5)
        return result, coord

    def click_common(self, template: str):
        self.click_in_template(template)

    def verify_ocr_img(self, template, color_threshold, data_color=1):
        box = coord_data.read_coord(template)
        source_cv2_capture = self.get_source_cv2_capture()
        im_trim = self.trim_cv2_img(source_cv2_capture, box)

        self.monocolour_img(im_trim, color_threshold, data_color)

    def verify_ocr_img_by_mask(self, template, hsv_color_lower: list, hsv_color_upper: list, gray_segmentation=50, invert=False):
        box = coord_data.read_coord(template)
        source_cv2_capture = self.get_source_cv2_capture()
        # cv2.imshow("", source_cv2_capture)
        # cv2.waitKey()
        im_trim = self.trim_cv2_img(source_cv2_capture, box)
        # cv2.imshow("", im_trim)
        # cv2.waitKey()
        current_regional = self.ocr.ocr_output_string_ext_by_mask(im_trim, [0, 0, 100], [155, 100, 255])
        print(current_regional)
        self.ocr.ocr_output_string_ext_by_mask(im_trim, hsv_color_lower, hsv_color_upper, gray_segmentation, invert)

    def print_ocr_result(self, template, hsv_color_lower: list, hsv_color_upper: list, gray_segmentation, black_enhanced=0.0):
        box = coord_data.read_coord(template)
        source_cv2_capture = self.get_source_cv2_capture()
        # cv2.imshow("", source_cv2_capture)
        # cv2.waitKey()
        im_trim = self.trim_cv2_img(source_cv2_capture, box)
        # cv2.imshow("", im_trim)
        # cv2.waitKey()
        current_regional = self.ocr.ocr_output_string_ext_by_mask(im_trim,
                                                                  hsv_color_lower,
                                                                  hsv_color_upper,
                                                                  gray_segmentation=gray_segmentation,
                                                                  black_enhanced=black_enhanced)
        print("current_regional", current_regional)

    def find_color_in_img(self, im_cv):
        color = []
        self.find_color_in_v2_auto(im_cv, color)

    @staticmethod
    def monocolour_img(im_cv2, color_threshold, data_color):
        """
        输出二值化原始识别结果
        :param im_cv2: 做识别的cv2图像
        :param color_threshold: 二值化颜色阈值
        :param data_color: 是否反色，-1为反色
        :return:
        """

        # 获取源图信息
        im_height, im_width, im_depth = im_cv2.shape
        # 二值化源图
        im_src = numpy.zeros((im_height, im_width, 1), numpy.uint8)
        im_gray = cv2.cvtColor(im_cv2, cv2.COLOR_BGR2GRAY)
        cv2.imshow("", im_gray)
        cv2.waitKey()
        if data_color > 0:
            for i in range(im_height):
                for j in range(im_width):
                    if im_gray[i, j] < color_threshold:
                        im_src[i, j] = 255
                    else:
                        im_src[i, j] = 255 - im_gray[i, j]
        elif data_color <= 0:
            for i in range(im_height):
                for j in range(im_width):
                    if im_gray[i, j] > color_threshold:
                        im_src[i, j] = 255

        # 创建扩展背景
        im_bg = numpy.zeros((im_height + 20, im_width + 40, 1), numpy.uint8)
        im_bg.fill(255)
        # 合并图层
        im_bg[10:im_height + 10, 20:im_width + 20] = im_src

        # cv2.imshow("", im_bg)
        # cv2.waitKey()

    @staticmethod
    def rgb_to_hsv(rgb_color: list):
        hsv_color = cv2.cvtColor(numpy.array([[rgb_color]], numpy.uint8), cv2.COLOR_RGB2HSV)

        hsv_color = hsv_color.tolist()
        hsv_color = hsv_color[0][0]
        print(hsv_color)
        return hsv_color


if __name__ == "__main__":
    load_data = LoadData(from_zip=False)
    load_data.load_data_coord()

    load_data.load_data_im_data()
    # check_capture = CheckCapture("[#] [Onmyoji01] 登录 [#]")
    check_capture = CheckCapture("[#] [Onmyoji02] 阴阳师-网易游戏 [#]")
    # check_capture = CheckCapture("微信")
    # check_capture.rgb_to_hsv([246, 221, 48])

    print(check_capture.check_common("yard_is_expolore_entrance", similarity=0.9))
    # print(check_capture.find_in_template_area("team_is_cooperation_teamup_friend_panel_friend_chapter", show_trim=True, debug=True))
    # print(check_capture.check_common("bonus_find_bonus_souls", similarity=0.8))
    # print(check_capture.check_common("bonus_find_bonus_coin_50", similarity=0.8))
    # print(check_capture.check_common("bonus_find_bonus_coin_100", similarity=0.8))
    # print(check_capture.check_common("bonus_find_bonus_exp_50", similarity=0.8))
    # print(check_capture.check_common("bonus_find_bonus_exp_100", similarity=0.8))
    # while True:
    # print(check_capture.check_dynamic("story_find_technique_target_common", similarity=0.7))

    # print(check_capture.check_common("fish_circle_is_target_magnification_40"))
