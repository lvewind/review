from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtCore import Qt, QRect
from PySide6 import QtWidgets
import sys
import os
import win32gui
import json
import cv2
import numpy
import copy
from tools.source.ui.capture_tool import Ui_MainWindow_CaptureTool
from hiworker.capture.capture_win32api import capture_dc_to_cv


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow_CaptureTool):
    def __init__(self, short_title="Earth",
                 image_path="data/image/",
                 coordinate_path="data/coordinate/",
                 is_emulator=False,
                 save_template_img=True):
        """
        初始化截图工具UI
        :param short_title: 需要截图的窗口的短标题
        :param image_path: 截图保存路径
        :param coordinate_path: 坐标保存路径
        :param is_emulator: 是否是截取模拟器
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.image_path = os.path.abspath(os.path.join(os.getcwd(), "..", image_path))
        self.coordinate_path = os.path.abspath(os.path.join(os.getcwd(), "..", coordinate_path))
        print("image_path", self.image_path)
        print("coordinate_path", self.coordinate_path)
        if not os.path.exists(self.image_path):
            os.makedirs(self.image_path, exist_ok=True)
        if not os.path.exists(self.coordinate_path):
            os.makedirs(self.coordinate_path, exist_ok=True)
        self.short_title = short_title
        self.is_emulator = is_emulator
        self.save_template_img = save_template_img

        self.json_file_list = [
            "battle.json",
            "bonus.json",
            "bounty_seals.json",
            "chapter.json",
            "collection.json",
            "daily.json",
            "earthly.json",
            "encounter.json",
            "explore.json",
            "evo_materials.json",
            "friend.json",
            "game_on_start.json",
            "guild.json",
            "guild_feast.json",
            "illustrated_handbook.json",
            "invite.json",
            "mall.json",
            "mpay_login.json",
            "pet.json",
            "realm_raid.json",
            "shikigami.json",
            "souls.json",
            "story.json",
            "summon.json",
            "talismanoass.json",
            "team.json",
            "totem.json",
            "user.json",
            "yard.json",
        ]
        self.window_list = {}

        self.get_window_list()
        self.fill_combo_box_json_list()
        self.bind_function()
        self.capture_window = CaptureWindow(self.image_path, self.coordinate_path, self.save_template_img)

    def bind_function(self):
        self.pushButton_capture.clicked.connect(lambda: self.show_capture_widget(True))
        self.pushButton_set_coordinate.clicked.connect(lambda: self.show_capture_widget(False))
        self.radioButton_sandbox.toggled.connect(self.get_window_list)
        self.radioButton_sandbox_login.toggled.connect(self.get_window_list)
        self.radioButton_emulator.toggled.connect(self.get_window_list)

    def show_capture_widget(self, save_template_img: bool):
        """
        显示截图层
        :return:
        """
        windows_title = self.comboBox_window_list.currentText()
        hwnd = win32gui.FindWindow(None, windows_title)
        # 如果是模拟器，获取子窗口句柄
        if self.is_emulator:
            hwnd = self.get_emulator_window_sub_hwnd()
        # 获取窗口位置
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        _left, _top, _right, _bottom = win32gui.GetClientRect(hwnd)
        print("窗口位置：", left, top, right, bottom)
        print("客户区大小：", _left, _top, _right, _bottom)

        self.capture_window.hwnd = hwnd
        self.capture_window.template_name = self.lineEdit_template_name.text()
        self.capture_window.json_filename = self.comboBox_json_list.currentText()

        if self.is_emulator:
            self.capture_window.setGeometry(left, top, _right, _bottom)
        else:
            if self.radioButton_sandbox_login.isChecked():
                self.capture_window.setGeometry(left, top, _right, _bottom)
            else:
                self.capture_window.setGeometry(left + 8, top + 31, _right, _bottom)
        self.capture_window.set_capture_display(_right, _bottom)
        self.capture_window.save_template_img = save_template_img
        self.capture_window.show()

    def load_capture_option(self):
        """
        # 加载截图类参数
        :return:
        """
        pass

    def get_emulator_window_hwnd(self):
        """
        # 获取模拟器窗口句柄
        :return:
        """
        windows_title = self.comboBox_window_list.currentText()
        hwnd = win32gui.FindWindow(None, windows_title)
        return win32gui.FindWindowEx(hwnd, 0, None, "sub")

    def get_emulator_window_sub_hwnd(self):
        """
        # 获取模拟器窗口句柄
        :return:
        """
        windows_title = self.comboBox_window_list.currentText()
        hwnd = win32gui.FindWindow(None, windows_title)
        the_render_hwnd = win32gui.FindWindowEx(hwnd, 0, None, "Chrome Legacy Window")
        if the_render_hwnd:
            return the_render_hwnd
        else:
            return None

    def get_window_list(self):
        self.window_list = {}

        def _get_window_list(hwnd, window_list):
            if self.radioButton_sandbox.isChecked():
                # self.short_title = "Google Earth - Google Chrome"
                self.is_emulator = False
            elif self.radioButton_sandbox_login.isChecked():
                # self.short_title = "Google Earth - Google Chrome"
                self.is_emulator = False
            elif self.radioButton_emulator.isChecked():
                # self.short_title = "Google Earth - Google Chrome"
                self.is_emulator = True
            if win32gui.IsWindow(hwnd) \
                    and win32gui.IsWindowEnabled(hwnd) \
                    and win32gui.IsWindowVisible(hwnd) \
                    and win32gui.GetWindowText(hwnd).find(self.short_title) >= 0:
                window_list.update({win32gui.GetWindowText(hwnd): win32gui.GetWindowText(hwnd)})

        # 枚举相关窗口
        win32gui.EnumWindows(_get_window_list, self.window_list)
        self.fill_combo_box_window_list()

    def fill_combo_box_window_list(self):
        self.comboBox_window_list.clear()
        # 填充窗口句柄下拉菜单
        for k, v in self.window_list.items():
            if k != "":
                self.comboBox_window_list.addItem(str(k), v)

    def fill_combo_box_json_list(self):
        # 填充文件名下来菜单
        self.json_file_list.sort()
        for t in self.json_file_list:
            if t != "":
                self.comboBox_json_list.addItem(str(t), str(t))


class CaptureWindow(QtWidgets.QMainWindow):
    def __init__(self, image_path, json_path, save_template_img):
        """
        初始化截图功能类
        :param image_path: 图像保存路径
        :param json_path: json路径
        :param save_template_img: 是否保存临时图像
        """
        super(CaptureWindow, self).__init__()
        # 设置窗口标记（无边框）
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.image_path = image_path
        self.json_path = json_path
        self.save_template_img = save_template_img

        self.hwnd = 0
        self.template_name = ""
        self.json_filename = ""

        self.im = 0
        self.start = (0, 0)  # 开始坐标点
        self.end = (0, 0)  # 结束坐标点
        self.label = IMLabel(self)
        # self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")

    def set_capture_display(self, _right, _bottom):
        """
        显示截图图层
        :param _right:
        :param _bottom:
        :return:
        """
        self.im = self.get_src_image_by_win32()
        im_rgb = copy.copy(self.im)
        height, width, bytes_per_component = im_rgb.shape
        bytes_per_line = 3 * width
        cv2.cvtColor(im_rgb, cv2.COLOR_BGR2RGB, im_rgb)
        q_img = QImage(im_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap(q_img)
        self.label.setGeometry(QRect(0, 0, _right, _bottom))
        self.label.setPixmap(pixmap)
        self.label.setCursor(Qt.CrossCursor)

    def screenshots(self, start, end):
        """
        保存截图
        :param start: 起点坐标
        :param end: 终点坐标
        :return:
        """
        print(start, end)
        print("当前截图窗口句柄：", self.hwnd)
        left = min(start[0], end[0])
        top = min(start[1], end[1])
        right = max(start[0], end[0])
        bottom = max(start[1], end[1])
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])
        im_crop = self.im[top:bottom, left:right]

        # 打开已存在的JSON文件用于加载已有数据
        json_dict = {}
        try:
            fr = open(os.path.join(self.json_path, self.json_filename), "r")
            try:
                json_dict = json.loads(fr.read())
            except json.decoder.JSONDecodeError:
                pass
            finally:
                if fr:
                    fr.close()
        except FileNotFoundError:
            pass

        # 原JSON文件中没有当前模板的key，添加当前key
        if self.template_name not in json_dict:
            json_dict.update({self.template_name: {}})
        # 保存区域数据
        json_dict[self.template_name].update({"left": left - 1, "top": top - 1, "right": right + 1, "bottom": bottom + 1})
        # 需要保存模板截图、找图区域、图片宽高
        if self.save_template_img:
            # print(self.image_path + "\\" + self.template_name + ".png")
            cv2.imwrite(self.image_path + "\\" + self.template_name + ".png", im_crop)
            im_size = {"width": width, "height": height}
            json_dict[self.template_name].update(im_size)
        # 打开JSON文件用于写入数据
        json_file = os.path.join(self.json_path, self.json_filename)
        fw = open(json_file, "w")
        print("当前截图JSON数据：", json_dict[self.template_name])
        fw.write(str(json.dumps(json_dict)))  # 把字典转化为json写入到文件
        fw.close()
        self.close()
        self.hide()

    def get_src_image_by_qt5(self):
        """
        # 获取所需要检测的图片，返回CV2图片对象
        :return:
        """
        screen = QtWidgets.QApplication.primaryScreen()
        q_image = screen.grabWindow(self.hwnd).toImage()
        img = q_image.convertToFormat(QImage.Format_RGB888)
        width = img.width()
        height = img.height()
        ptr = img.bits()
        # ptr = img.constBits()
        ptr.setsize(img.byteCount())
        arr = numpy.array(ptr).reshape((height, width, 3))  # Copies the storage
        img = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

        cv2.imwrite(os.path.abspath(os.path.join(os.getcwd(), "..", "data", "whole_scene_by_Qt5.png")), img)
        # cv2.imshow("OpenCV", img)
        # cv2.waitKey()
        return img

    def get_src_image_by_win32(self):
        return capture_dc_to_cv(self.hwnd)

    def mousePressEvent(self, event):
        """
        # 点击左键开始选取截图区域
        :param event:
        :return:
        """

        if event.button() == Qt.LeftButton:
            self.start = (int(event.position().x()), int(event.position().y()))
            self.label.start = self.start

    def mouseReleaseEvent(self, event):
        """
        # 鼠标左键释放开始截图操作
        :param event:
        :return:
        """
        if event.button() == Qt.LeftButton:
            self.end = (int(event.position().x()), int(event.position().y()))
            self.label.end = self.end
            self.screenshots(self.start, self.end)
            # 进行重新绘制
            self.update()

    def mouseMoveEvent(self, event):
        """
        # 鼠标左键按下的同时移动鼠标绘制截图辅助线
        :param event:
        :return:
        """
        if event.buttons() and Qt.LeftButton:
            self.end = (int(event.position().x()), int(event.position().y()))
            self.label.end = self.end
            # 进行重新绘制
            self.update()

    # def paintEvent(self, event):
    #     super().paintEvent(event)
    #     x = self.start[0]
    #     y = self.start[1]
    #     w = self.end[0] - x
    #     h = self.end[1] - y
    #
    #     pp = QPainter(self)
    #     pp.drawRect(x, y, w, h)


class IMLabel(QtWidgets.QLabel):
    start = (0, 0)  # 开始坐标点
    end = (0, 0)  # 结束坐标点

    def paintEvent(self, event):
        super().paintEvent(event)
        x = self.start[0]
        y = self.start[1]
        w = self.end[0] - x
        h = self.end[1] - y

        pp = QPainter(self)
        pp.drawRect(x, y, w, h)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
