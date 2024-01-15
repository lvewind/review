from hiworker import *
from hiworker.utils.data.coord import Coordinate
from hiworker.utils.data.img import InitImage
import cv2
import numpy


class CheckCapture(DetectImage, Win32Click):
    def __init__(self, window_title, coord_data: Coordinate, im_data: InitImage):
        super(CheckCapture, self).__init__(window_title, coord_data, im_data)
        self.env_type = 1
        self.coord_data = coord_data
        self.im_data = im_data
        # self.get_client_data = Tesseract(language=b"chi_sim_fzbwks")
        self.correction_window = False

    def check_scene(self, scene="yard", mode="common", similarity=0.8):
        for template in self.im_data.data:
            if template.find(scene) == 0:
                if mode == "common":
                    result = self.check_common(template, similarity)
                else:
                    result = self.check_dynamic(template, similarity)
                if result[0]:
                    print(result, ": ", template)
                else:
                    print("*******", result, ": ", template)
                break
        else:
            print("图片: ", scene, "不存在或未加载")

    def check_common(self, template: str, similarity):
        result, coord, max_similarity = self.find_in_template_rect(template, similarity=similarity)
        return result, coord

    def check_dynamic(self, template: str, similarity):
        result, coord, max_similarity = self.find_in_dynamic_scene(template, similarity=similarity)
        return result, coord

    def click_common(self, template: str):
        self.click_in_template(template)

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
    from_zip = False
    check_coord = Coordinate(data_path="../data/coordinate", zip_file=".64.zip")
    check_im = InitImage(img_path="../data/image/",
                         zip_file="64.zip",
                         login_image_path="../data/user/login_img/",
                         team_up_image_path="../data/user/teamup_img/")
    print(check_coord.data_path)
    print(check_im.path)
    if check_coord.load_coord(from_zip=from_zip):
        print("正在加载[图像数据]，请稍后。。。")
        if check_im.load_all_image(from_zip=from_zip):
            print("[图像数据]加载完成")
        else:
            print("[数据image]加载失败，请检查数据")
    else:
        print("[数据coordinate]加载失败，请检查数据")
    check_capture = CheckCapture("[#] [Onmyoji02] 阴阳师-网易游戏 [#]", coord_data=check_coord, im_data=check_im)
    # check_capture.check_scene(scene="yard", mode="other")
    check_capture.check_time = 10
    # check_capture.debug = True
    print("开始检测图像：")
    check_capture.check_scene(scene="evo_materials_is_evo_stage_selected_9", similarity=0.92)
