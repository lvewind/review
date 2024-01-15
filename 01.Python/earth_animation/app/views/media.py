import os

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from .set_fonts import SetFontsView
from app.views.ui import *
from ..views.sender import view_sender

import hiworker


class MediaView(QtWidgets.QDialog, Ui_Dialog_media_edit):
    def __init__(self, icon_path=None):
        super(MediaView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_data)
        self.comboBox_media_show_type.currentIndexChanged.connect(self.refresh_combobox_media_type)
        self.media_type_option = {}
        self.data = {}

    def show_add(self, subtitle_id: int, media_type_option: dict):
        self.media_type_option = media_type_option
        self.data.update({"subtitle_id": subtitle_id})
        self.clear_input()
        self.setWindowTitle("新增媒体")
        self.init_combobox_show_type()
        self.init_combobox_media_type()
        self.show()

    def show_edit(self, data: dict, media_type_option: dict):
        self.clear_input()
        self.media_type_option = media_type_option
        self.setWindowTitle("编辑媒体")
        self.init_combobox_show_type()
        if data:
            self.data = data
            self.lineEdit_media_name.setText(self.data.get("name"))
            count = self.comboBox_media_show_type.count()
            for index in range(count):
                if self.data.get("show_type") == self.comboBox_media_show_type.itemData(index):
                    self.comboBox_media_show_type.setCurrentIndex(index)
                    break
            count = self.comboBox_media_type.count()
            for index in range(count):
                if self.data.get("media_type") == self.comboBox_media_type.itemData(index):
                    self.comboBox_media_type.setCurrentIndex(index)
                    break
            self.doubleSpinBox_media_delay.setValue(self.data.get("media_delay"))
            self.doubleSpinBox_media_time.setValue(self.data.get("media_time"))
            self.show()

    def send_data(self):
        self.close()
        self.data.update({
            "name": self.lineEdit_media_name.text(),
            "media_type": self.comboBox_media_type.currentData(),
            "show_type": self.comboBox_media_show_type.currentData(),
            "media_time": self.doubleSpinBox_media_time.value(),
            "media_delay": self.doubleSpinBox_media_delay.value()
        })
        view_sender.media.save.emit(self.data)

    def clear_input(self):
        self.comboBox_media_type.clear()
        self.comboBox_media_show_type.clear()
        self.lineEdit_media_name.clear()

    def init_combobox_media_type(self, current_show_type=None):
        if current_show_type:
            media_type = self.media_type_option.get(current_show_type)
        else:
            media_type = list(self.media_type_option.values())[0]
        for key, value in media_type.items():
            self.comboBox_media_type.addItem(value, key)

    def init_combobox_show_type(self):
        for key in self.media_type_option.keys():
            self.comboBox_media_show_type.addItem(key, key)

    def refresh_combobox_media_type(self):
        self.comboBox_media_type.clear()
        current_show_type = self.comboBox_media_show_type.currentData()
        self.init_combobox_media_type(current_show_type)


class MediaScreenView(QtWidgets.QDialog, Ui_Dialog_media_screen_text_image_video_edit):
    def __init__(self, media_type: str, icon_path=None):
        super(MediaScreenView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.pushButton.clicked.connect(self.send_data)
        self.pushButton_media.clicked.connect(self.choose_media)

        self.media_type = media_type
        match media_type:
            case "text":
                self.setWindowTitle("编辑2D文字")
                self.groupBox_screen.setTitle("2D文字设置")
                self.pushButton_media.setDisabled(True)
                self.plainTextEdit_media_path.setPlaceholderText("输入文字内容")
            case "image":
                self.setWindowTitle("编辑2D图片")
                self.groupBox_screen.setTitle("2D图片设置")
                self.groupBox_screen_font.setDisabled(True)
                self.plainTextEdit_media_path.setPlaceholderText("输入图片路径")
            case "video":
                self.setWindowTitle("编辑2D视频")
                self.groupBox_screen.setTitle("2D视频设置")
                self.groupBox_screen_font.setDisabled(True)
                self.plainTextEdit_media_path.setPlaceholderText("输入视频路径")
        self.data = {}

    def show_edit(self, data: dict, fonts: list, font_color: dict):
        self.clear_input()
        self.init_combobox_fonts(fonts, font_color)
        if data:
            self.data = data
            font_count = self.comboBox_font.count()
            for index in range(font_count):
                if data.get("font") == self.comboBox_font.itemText(index):
                    self.comboBox_font.setCurrentIndex(index)
                    break
            font_color_count = self.comboBox_font_color.count()
            for index in range(font_color_count):
                if data.get("font_color") == self.comboBox_font_color.itemData(index):
                    self.comboBox_font_color.setCurrentIndex(index)
                    break
            font_size_count = self.comboBox_font_size.count()
            for index in range(font_size_count):
                if data.get("font_size") == self.comboBox_font_size.itemText(index):
                    self.comboBox_font_size.setCurrentIndex(index)
                    break
            self.plainTextEdit_media_path.setPlainText(data.get("file"))
            self.spinBox_media_2d_top.setValue(0 if not data.get("top") else data.get("top"))
            self.spinBox_media_2d_left.setValue(0 if not data.get("left") else data.get("left"))
            self.spinBox_media_2d_width.setValue(0 if not data.get("width") else data.get("width"))
            self.spinBox_media_2d_height.setValue(0 if not data.get("height") else data.get("height"))
            self.doubleSpinBox_media_2d_opacity.setValue(
                1.0 if data.get("opacity") is None else data.get("opacity"))
            self.checkBox_media_2d_full_screen.setChecked(
                True if data.get("full_screen") else False)
            self.checkBox_media_2d_to_three_after_display.setChecked(
                True if data.get("transaction_to_3d") else False)

            self.show()
        else:
            print("数据为空")

    def send_data(self):
        self.close()

        self.data.update({
            "file": self.plainTextEdit_media_path.toPlainText(),
            "font": self.comboBox_font.currentData(),
            "font_color": self.comboBox_font_color.currentData(),
            "font_size": self.comboBox_font_size.currentText(),
            "width": self.spinBox_media_2d_width.value(),
            "height": self.spinBox_media_2d_height.value(),
            "top": self.spinBox_media_2d_top.value(),
            "left": self.spinBox_media_2d_left.value(),
            "opacity": self.doubleSpinBox_media_2d_opacity.value(),
            "full_screen": 1 if self.checkBox_media_2d_full_screen.isChecked() else 0,
            "transaction_to_3d": 1 if self.checkBox_media_2d_to_three_after_display.isChecked() else 0,
            "keep": 1 if self.checkBox_media_2d_to_side_after_display.isChecked() else 0
        })
        match self.media_type:
            case "text":
                view_sender.media.save_2d_text.emit(self.data)
            case "image":
                view_sender.media.save_2d_image.emit(self.data)
            case "video":
                view_sender.media.save_2d_video.emit(self.data)

    def clear_input(self):
        self.comboBox_font_color.clear()
        self.comboBox_font.clear()
        self.comboBox_font_size.clear()
        self.plainTextEdit_media_path.clear()
        self.checkBox_media_2d_full_screen.setChecked(False)
        self.checkBox_media_2d_to_three_after_display.setChecked(False)
        self.checkBox_media_2d_to_side_after_display.setChecked(False)
        self.doubleSpinBox_media_2d_opacity.setValue(1)

    def choose_media(self):
        if self.media_type == "image":
            media_filter = '(*.jpg; *.png; *.bmp; *.webp; *.jfif; *.jpeg)'
        else:
            media_filter = '(*.mp4; *.mkv; *.mov; *.avi; *.flv; *.mpeg)'
        media_path, result = QtWidgets.QFileDialog.getOpenFileName(caption="选择媒体", filter=media_filter, parent=self)
        if os.path.isfile(media_path):
            self.plainTextEdit_media_path.setPlainText(media_path)

    def init_combobox_fonts(self, fonts: list, font_color: dict):
        for font in fonts:
            self.comboBox_font.addItem(font, font)
        for key, value in font_color.items():
            self.comboBox_font_color.addItem(value, key)
        for n in range(25):
            size = str(2 * n + 1) + "em"
            self.comboBox_font_size.addItem(size, size)


class MediaBgmView(QtWidgets.QDialog, Ui_Dialog_media_screen_bgm_edit):
    def __init__(self, icon_path=None):
        super(MediaBgmView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.pushButton.clicked.connect(self.send_data)
        self.pushButton_media_three.clicked.connect(self.choose_media)

        self.data = {}

    def show_edit(self, data: dict):
        if data:
            self.data = data
            self.show()
        else:
            print("数据为空")

    def send_data(self):
        self.close()
        self.data.update(
            {
                "file": self.plainTextEdit_media_path_three.toPlainText()
            }
        )
        view_sender.media.save_2d_bgm.emit(self.data)

    def choose_media(self, is_3d=True):
        media_filter = '(*.mp3; *.ogg; *.wav)'
        media_path, result = QtWidgets.QFileDialog.getOpenFileName(caption="选择媒体", filter=media_filter, parent=self)
        if os.path.isfile(media_path):
            self.plainTextEdit_media_path_three.setPlainText(media_path)


class MediaThreeView(QtWidgets.QDialog, Ui_Dialog_media_three_text_image_video_edit):
    def __init__(self, media_type: str, icon_path=None):
        super(MediaThreeView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.pushButton.clicked.connect(self.send_data)
        self.pushButton_media_three.clicked.connect(self.choose_media)

        self.media_type = media_type
        match media_type:
            case "text":
                self.setWindowTitle("编辑3D文字")
                self.groupBox_three.setTitle("3D文字设置")
                self.pushButton_media_three.setDisabled(True)
                self.plainTextEdit_media_path_three.setPlaceholderText("输入文字内容")
                self.pushButton_get_position.clicked.connect(view_sender.media.get_position_text.emit)
            case "image":
                self.setWindowTitle("编辑3D图片")
                self.groupBox_three.setTitle("3D图片设置")
                self.groupBox_font_three.setDisabled(True)
                self.plainTextEdit_media_path_three.setPlaceholderText("输入图片路径")
                self.pushButton_get_position.clicked.connect(view_sender.media.get_position_image.emit)
            case "video":
                self.setWindowTitle("编辑3D视频")
                self.groupBox_three.setTitle("3D视频设置")
                self.groupBox_font_three.setDisabled(True)
                self.plainTextEdit_media_path_three.setPlaceholderText("输入视频路径")
                self.pushButton_get_position.clicked.connect(view_sender.media.get_position_video.emit)
        self.data = {}

    def show_edit(self, data: dict, fonts: list, font_color: dict):
        self.clear_input()
        self.setWindowTitle("编辑媒体")
        self.init_combobox_fonts(fonts, font_color)
        if data:
            self.data = data
            self.plainTextEdit_media_path_three.setPlainText(data.get("file"))

            font_count = self.comboBox_font_three.count()
            for index in range(font_count):
                if data.get("font") == self.comboBox_font_three.itemText(index):
                    self.comboBox_font_three.setCurrentIndex(index)
                    break
            font_color_count = self.comboBox_font_color_three.count()
            for index in range(font_color_count):
                if data.get("font_color") == self.comboBox_font_color_three.itemData(index):
                    self.comboBox_font_color_three.setCurrentIndex(index)
                    break
            font_size_count = self.comboBox_font_size_three.count()
            for index in range(font_size_count):
                if data.get("font_size") == self.comboBox_font_size_three.itemText(index):
                    self.comboBox_font_size_three.setCurrentIndex(index)
                    break

            self.lineEdit_media_longitude.setText(
                str(data.get("longitude")) if data.get("longitude") else "")
            self.lineEdit_media_latitude.setText(
                str(data.get("latitude")) if data.get("latitude") else "")
            self.lineEdit_media_altitude.setText(
                str(data.get("altitude")) if data.get("longitude") else "")

            self.spinBox_media_3d_height.setValue(data.get("height") if data.get("height") else 0)
            self.spinBox_media_3d_width.setValue(data.get("width") if data.get("width") else 0)
            self.spinBox_media_3d_depth.setValue(data.get("depth") if data.get("depth") else 0)

            self.checkBox_media_3d_tile.setChecked(True if data.get("parallel") else False)
            self.checkBox_media_3d_always_show.setChecked(True if data.get("keep") else False)

            self.show()
        else:
            print("数据为空")

    def send_data(self):
        self.close()

        self.data.update({
            "file": self.plainTextEdit_media_path_three.toPlainText(),
            "font": self.comboBox_font_three.currentData(),
            "font_color": self.comboBox_font_color_three.currentData(),
            "font_size": self.comboBox_font_size_three.currentText(),

            "longitude": float(self.lineEdit_media_longitude.text()) if self.lineEdit_media_longitude.text() else 0,
            "latitude": float(self.lineEdit_media_latitude.text()) if self.lineEdit_media_latitude.text() else 0,
            "altitude": float(self.lineEdit_media_altitude.text()) if self.lineEdit_media_altitude.text() else 0,
            "width": self.spinBox_media_3d_width.value(),
            "height": self.spinBox_media_3d_height.value(),
            "depth": self.spinBox_media_3d_depth.value(),

            "keep": self.checkBox_media_3d_always_show.isChecked(),
            "parallel": self.checkBox_media_3d_tile.isChecked()
        })
        match self.media_type:
            case "text":
                view_sender.media.save_3d_text.emit(self.data)
            case "image":
                view_sender.media.save_3d_image.emit(self.data)
            case "video":
                view_sender.media.save_3d_video.emit(self.data)

    def clear_input(self):
        self.comboBox_font_color_three.clear()
        self.comboBox_font_three.clear()
        self.comboBox_font_size_three.clear()

    def choose_media(self):
        if self.media_type == "image":
            media_filter = '(*.jpg; *.png; *.bmp; *.webp; *.jfif; *.jpeg)'
        else:
            media_filter = '(*.mp4; *.mkv; *.mov; *.avi; *.flv; *.mpeg)'
        media_path, result = QtWidgets.QFileDialog.getOpenFileName(caption="选择媒体", filter=media_filter, parent=self)
        if os.path.isfile(media_path):
            self.plainTextEdit_media_path_three.setPlainText(media_path)

    def init_combobox_fonts(self, fonts: list, font_color: dict):
        for font in fonts:
            self.comboBox_font_three.addItem(font, font)
        for key, value in font_color.items():
            self.comboBox_font_color_three.addItem(value, key)
        for n in range(25):
            size = str(2 * n + 1) + "em"
            self.comboBox_font_size_three.addItem(size, size)


class MediaThreeKmlView(QtWidgets.QDialog, Ui_Dialog_media_three_kml_edit):
    def __init__(self, icon_path=None):
        super(MediaThreeKmlView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.pushButton.clicked.connect(self.send_data)
        self.pushButton_media_three.clicked.connect(self.choose_media)

        self.media_type_option = {}
        self.data = {}

    def show_edit(self, data: dict):
        if data:
            self.data = data
            self.plainTextEdit_media_path_three.setPlainText(data.get("file"))

            self.show()
        else:
            print("数据为空")

    def send_data(self):
        self.close()
        self.data.update({"file": self.plainTextEdit_media_path_three.toPlainText()})
        view_sender.media.save_3d_kml.emit(self.data)

    def choose_media(self):
        media_filter = '(*.kml)'
        media_path, result = QtWidgets.QFileDialog.getOpenFileName(caption="选择媒体", filter=media_filter, parent=self)
        if os.path.isfile(media_path):
            self.plainTextEdit_media_path_three.setPlainText(media_path)


class MediaThreeOverlayView(QtWidgets.QDialog, Ui_Dialog_media_three_overlay_edit):
    def __init__(self, icon_path=None):
        super(MediaThreeOverlayView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.pushButton.clicked.connect(self.send_data)
        self.pushButton_media_three.clicked.connect(self.choose_media)

        self.pushButton_get_position_ground_overlay_1.clicked.connect(view_sender.media.get_position_ground_overlay_1.emit)
        self.pushButton_get_position_ground_overlay_2.clicked.connect(view_sender.media.get_position_ground_overlay_2.emit)
        self.pushButton_get_position_ground_overlay_3.clicked.connect(view_sender.media.get_position_ground_overlay_3.emit)
        self.pushButton_get_position_ground_overlay_4.clicked.connect(view_sender.media.get_position_ground_overlay_4.emit)
        self.pushButton_get_position_ground_overlay.clicked.connect(view_sender.media.get_position_ground.emit)

        self.media_type_option = {}
        self.data = {}

    def show_edit(self, data: dict):
        if data:
            self.data = data
            self.plainTextEdit_media_path_three.setPlainText(data.get("file"))
            self.lineEdit_media_ground_overlay_lon_1.setText(
                str(data.get("longitude_1")) if data.get("longitude_1") else "")
            self.lineEdit_media_ground_overlay_lon_2.setText(
                str(data.get("longitude_2")) if data.get("longitude_2") else "")
            self.lineEdit_media_ground_overlay_lon_3.setText(
                str(data.get("longitude_3")) if data.get("longitude_3") else "")
            self.lineEdit_media_ground_overlay_lon_4.setText(
                str(data.get("longitude_4")) if data.get("longitude_4") else "")

            self.lineEdit_media_ground_overlay_lat_1.setText(
                str(data.get("latitude_1")) if data.get("latitude_1") else "")
            self.lineEdit_media_ground_overlay_lat_2.setText(
                str(data.get("latitude_2")) if data.get("latitude_2") else "")
            self.lineEdit_media_ground_overlay_lat_3.setText(
                str(data.get("latitude_3")) if data.get("latitude_3") else "")
            self.lineEdit_media_ground_overlay_lat_4.setText(
                str(data.get("latitude_4")) if data.get("latitude_4") else "")

            self.show()
        else:
            print("数据为空")

    def send_data(self):
        self.close()
        self.data.update({
            "file": self.plainTextEdit_media_path_three.toPlainText(),
            "longitude_1": float(self.lineEdit_media_ground_overlay_lon_1.text()) if self.lineEdit_media_ground_overlay_lon_1.text() else 0,
            "longitude_2": float(self.lineEdit_media_ground_overlay_lon_2.text()) if self.lineEdit_media_ground_overlay_lon_2.text() else 0,
            "longitude_3": float(self.lineEdit_media_ground_overlay_lon_3.text()) if self.lineEdit_media_ground_overlay_lon_3.text() else 0,
            "longitude_4": float(self.lineEdit_media_ground_overlay_lon_4.text()) if self.lineEdit_media_ground_overlay_lon_4.text() else 0,
            "latitude_1": float(self.lineEdit_media_ground_overlay_lat_1.text()) if self.lineEdit_media_ground_overlay_lat_1.text() else 0,
            "latitude_2": float(self.lineEdit_media_ground_overlay_lat_2.text()) if self.lineEdit_media_ground_overlay_lat_2.text() else 0,
            "latitude_3": float(self.lineEdit_media_ground_overlay_lat_3.text()) if self.lineEdit_media_ground_overlay_lat_3.text() else 0,
            "latitude_4": float(self.lineEdit_media_ground_overlay_lat_4.text()) if self.lineEdit_media_ground_overlay_lat_4.text() else 0
        })
        view_sender.media.save_3d_overlay.emit(self.data)

    def choose_media(self):
        media_filter = '(*.jpg; *.png; *.bmp; *.webp; *.jfif; *.jpeg)'
        media_path, result = QtWidgets.QFileDialog.getOpenFileName(caption="选择媒体", filter=media_filter, parent=self)
        if os.path.isfile(media_path):
            self.plainTextEdit_media_path_three.setPlainText(media_path)


class MediaThreeMotionLineView(QtWidgets.QDialog, Ui_Dialog_media_three_motion_line_edit):
    def __init__(self, icon_path=None):
        super(MediaThreeMotionLineView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.pushButton.clicked.connect(self.send_data)
        self.pushButton_media_three.clicked.connect(self.choose_media)

        self.data = {}

    def show_edit(self, data: dict, color: dict):
        self.clear_input()

        if data:
            for key, value in color.items():
                self.comboBox_motion_line_color.addItem(value, key)
            self.data = data
            self.plainTextEdit_media_path_three.setPlainText(data.get("file"))

            for index in range(self.comboBox_motion_line_color.count()):
                pass
            self.spinBox_motion_line_speed.setValue(data.get("speed") if data.get("speed") else 0)
            self.spinBox_motion_line_weight.setValue(data.get("line_weight") if data.get("line_weight") else 0)
            self.show()
        else:
            print("数据为空")

    def send_data(self):
        self.close()
        self.data.update({
            "file": self.plainTextEdit_media_path_three.toPlainText(),
            "color": self.comboBox_motion_line_color.currentData(),
            "line_weight": self.spinBox_motion_line_weight.value(),
            "motion_speed": self.spinBox_motion_line_speed.value(),
            "line_divide": self.spinBox_motion_line_divide.value(),
            "motion_time": self.spinBox_motion_line_time.value(),
            "height": self.spinBox_motion_line_height.value()
        })

        view_sender.media.save_3d_motion_line.emit(self.data)

    def clear_input(self):
        self.comboBox_motion_line_color.clear()

    def choose_media(self):
        media_filter = '(*.kml)'
        media_path, result = QtWidgets.QFileDialog.getOpenFileName(caption="选择媒体", filter=media_filter, parent=self)
        if os.path.isfile(media_path):
            self.plainTextEdit_media_path_three.setPlainText(media_path)


class MediaMoveDialog(QtWidgets.QDialog, Ui_Dialog_media_move):
    def __init__(self, icon_path=None):
        super(MediaMoveDialog, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.pushButton.clicked.connect(view_sender.media.move_to_subtitle.emit)
        self.table_header_init = False
        self.data = {}

    def show_edit(self, subtitles: list, table_header_media_move: dict):
        if not self.table_header_init:
            hiworker.TableLoad.init_table_header(self.tableWidget_media_move, table_header_media_move)
            self.table_header_init = True
        hiworker.TableLoad.load_table(self.tableWidget_media_move, subtitles, table_header_media_move)
        self.show()

    def send_data(self):
        self.close()
        self.data.update({
            "subtitle_id": hiworker.TableRead.get_current_data_id(self.tableWidget_media_move)
        })
        view_sender.media.move_to_subtitle.emit(self.data)


class MediaSetFontsView(SetFontsView):
    def __init__(self, icon_path=None):
        super(MediaSetFontsView, self).__init__(icon_path)

        self.setWindowTitle("正在批量设置 [媒体] 字体")

        self.pushButton.clicked.connect(self.send_data)

        self.data = {}

    def show_edit(self, font_list: dict, font_color: dict):
        self.clear_combobox()
        for font in font_list:
            self.comboBox_font.addItem(font, font)
        if font_color and type(font_color) == dict:
            for key, value in font_color.items():
                self.comboBox_font_color.addItem(value, key)
        font_size = 1
        a = 1
        b = 1
        for n in range(2, 28):
            if n > 2:
                font_size = a + b
                a = b
                b = font_size
            self.comboBox_font_size.addItem(str(font_size) + "em", str(font_size) + "em")
        self.show()

    def send_data(self):
        self.close()
        self.data.update({
            "font": self.comboBox_font.currentText(),
            "font_size": self.comboBox_font_size.currentText(),
            "font_color": self.comboBox_font_color.currentData()
        })
        view_sender.media.set_font_batch.emit(self.data)


class MediaSetSizeDialog(QtWidgets.QDialog, Ui_Dialog_set_3d_size):
    def __init__(self, icon_path=None):
        super(MediaSetSizeDialog, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)
        self.data_ids = []
        self.pushButton.clicked.connect(self.send_data)
        self.data = {}

    def show_edit(self):
        self.spinBox_media_width.clear()
        self.spinBox_media_height.clear()
        self.spinBox_media_depth.clear()
        self.show()

    def send_data(self):
        self.close()
        self.data.update({
            "width": self.spinBox_media_width.value(),
            "height": self.spinBox_media_height.value(),
            "depth": self.spinBox_media_depth.value(),
            "update_width": self.checkBox_media_width.isChecked(),
            "update_height": self.checkBox_media_height.isChecked(),
            "update_depth": self.checkBox_media_depth.isChecked(),

        })
        view_sender.media.set_font_batch.emit(self.data)
