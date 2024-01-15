import math
import os

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from app.views.ui import *
from app.views.ui.common import Ui_Dialog_set_voices
from .set_fonts import SetFontsView

from app.views.sender import view_sender


class SubtitleView(QtWidgets.QDialog, Ui_Dialog_subtitle_edit):
    def __init__(self, icon_path=None):
        super(SubtitleView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.comboBox_voice_name.currentIndexChanged.connect(self.init_combobox_voice_role_style)
        self.data = {}
        self.voices = []
        self.fonts = []
        self.font_color = {}
        self.init_combobox_font_size()
        self.pushButton.clicked.connect(self.send_data)

    def show_add(self):
        pass

    def show_edit(self, data: dict, voices: list, fonts: list, font_color: dict):
        self.fonts = fonts
        self.font_color = font_color
        self.voices = voices
        self.init_combobox_voice_name()
        self.init_combobox_voice_role_style()
        self.init_font_list()
        self.data = data
        self.doubleSpinBox_audio_time.setEnabled(False)
        self.doubleSpinBox_audio_time.setValue(self.data.get("audio_time"))
        self.doubleSpinBox_ext_time.setValue(self.data.get("ext_time"))

        self.doubleSpinBox_voice_rate.setValue(self.data.get("voice_rate"))
        self.doubleSpinBox_voice_pitch.setValue(self.data.get("voice_pitch"))
        self.doubleSpinBox_voice_volume.setValue(self.data.get("voice_volume"))

        for index in range(self.comboBox_voice_name.count()):
            if self.data.get("voice_name") == self.comboBox_voice_name.itemData(index):
                self.comboBox_voice_name.setCurrentIndex(index)
                break
        for index in range(self.comboBox_voice_role.count()):
            if self.data.get("voice_role") == self.comboBox_voice_role.itemText(index):
                self.comboBox_voice_role.setCurrentIndex(index)
                break
        for index in range(self.comboBox_voice_style.count()):
            if self.data.get("voice_style") == self.comboBox_voice_style.itemText(index):
                self.comboBox_voice_style.setCurrentIndex(index)
                break

        for index in range(self.comboBox_font.count()):
            if self.data.get("font") == self.comboBox_font.itemData(index):
                self.comboBox_font.setCurrentIndex(index)
                break
        for index in range(self.comboBox_font_color.count()):
            if self.data.get("font_color") == self.comboBox_font_color.itemData(index):
                self.comboBox_font_color.setCurrentIndex(index)
                break
        for index in range(self.comboBox_font_size.count()):
            if self.data.get("font_size") == self.comboBox_font_size.itemData(index):
                self.comboBox_font_size.setCurrentIndex(index)
                break

        self.show()

    def send_data(self):
        self.close()
        self.data.update(
            {
                "ext_time": self.doubleSpinBox_ext_time.value(),
                "font": self.comboBox_font.currentData(),
                "font_size": self.comboBox_font_size.currentData(),
                "font_color": self.comboBox_font_color.currentData(),
                "voice_local_name": self.comboBox_voice_name.currentText(),
                "voice_name": self.comboBox_voice_name.currentData(),
                "voice_role": self.comboBox_voice_role.currentText(),
                "voice_style": self.comboBox_voice_style.currentText(),
                "voice_rate": self.doubleSpinBox_voice_rate.value(),
                "voice_volume": self.doubleSpinBox_voice_volume.value(),
                "voice_pitch": self.doubleSpinBox_voice_pitch.value()
            }
        )
        view_sender.subtitle.save.emit(self.data)

    def init_combobox_voice_name(self):
        self.comboBox_voice_name.clear()
        for index, voice in enumerate(self.voices):
            local_name = voice.get("local_name")
            short_name = voice.get("short_name")
            self.comboBox_voice_name.addItem(local_name, short_name)
            if local_name == "云希":
                self.comboBox_voice_name.setCurrentIndex(index)

    def init_combobox_voice_role_style(self):
        self.comboBox_voice_role.clear()
        self.comboBox_voice_style.clear()
        current_index = self.comboBox_voice_name.currentIndex()
        if current_index >= 0:
            voice_style = self.voices[current_index].get("style_list")
            self.comboBox_voice_style.addItem("default")
            if voice_style:
                self.comboBox_voice_style.addItems(voice_style)
            voice_role = self.voices[current_index].get("role_play_list")
            self.comboBox_voice_role.addItem("default")
            if voice_role:
                self.comboBox_voice_role.addItems(voice_role)

    def init_combobox_font_size(self):
        self.comboBox_font_size.clear()
        for font_size in range(1, 25):
            self.comboBox_font_size.addItem(str(font_size) + "em", str(font_size) + "em")

    def init_font_list(self):
        self.comboBox_font.clear()
        self.comboBox_font_color.clear()
        for font in self.fonts:
            self.comboBox_font.addItem(font, font)
        for key, value in self.font_color.items():
            self.comboBox_font_color.addItem(value, key)


class SubtitleActionView(QtWidgets.QDialog, Ui_Dialog_subtitle_action_edit):
    def __init__(self, icon_path=None):
        super(SubtitleActionView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)
        self.setWindowTitle("字幕动作编辑")

        self.checkBox_2D_view.clicked.connect(self.set_check_box_with_2d_view_clicked)
        self.checkBox_3D_view.clicked.connect(self.set_check_box_with_3d_view_clicked)
        self.comboBox_fly_type.currentIndexChanged.connect(self.set_enable_with_fly_type)

        self.spinBox_slide_speed.valueChanged.connect(self.show_slide_time)
        self.spinBox_slide_speed.valueChanged.connect(self.show_zoom_time)
        self.spinBox_zoom_time.valueChanged.connect(self.show_zoom_time)

        self.data = {}

        self.pushButton.clicked.connect(self.send_data)

    def show_add(self):
        pass

    def show_edit(self, data: dict, fly_type: dict):
        self.data = data
        self.init_fly_type(fly_type)
        for index in range(self.comboBox_fly_type.count()):
            if data.get("fly_type") == self.comboBox_fly_type.itemData(index):
                self.comboBox_fly_type.setCurrentIndex(index)
                break
        self.doubleSpinBox_fly_speed.setValue(data.get("fly_speed") if data.get("fly_speed") else 1)
        self.checkBox_2D_view.setChecked(data.get("set_2d_view") if data.get("set_2d_view") else 0)
        self.checkBox_3D_view.setChecked(data.get("set_3d_view") if data.get("set_2d_view") else 0)

        self.lineEdit_target_place_name.setText(data.get("fly_to_place") if data.get("fly_to_place") else "")
        self.lineEdit_target_longitude.setText(data.get("fly_to_longitude") if data.get("fly_to_longitude") else "")
        self.lineEdit_target_latitude.setText(data.get("fly_to_latitude") if data.get("fly_to_latitude") else "")
        self.lineEdit_target_altitude.setText(data.get("fly_to_altitude") if data.get("fly_to_altitude") else "")

        self.lineEdit_heading.setText(data.get("heading") if data.get("heading") else "")
        self.lineEdit_tilt.setText(data.get("tilt") if data.get("tilt") else "")

        self.lineEdit_target_start_x.setText(str(data.get("start_x")) if data.get("start_x") else "")
        self.lineEdit_target_start_y.setText(str(data.get("start_y")) if data.get("start_y") else "")
        self.lineEdit_target_end_x.setText(str(data.get("end_x")) if data.get("end_x") else "")
        self.lineEdit_target_end_y.setText(str(data.get("end_y")) if data.get("end_y") else "")
        self.spinBox_slide_speed.setValue(data.get("slide_speed") if data.get("slide_speed") else 0)
        self.spinBox_zoom_time.setValue(data.get("zoom_times") if data.get("zoom_times") else 0)
        self.show()

    def send_data(self):
        self.close()
        self.data.update({
            "fly_type": self.comboBox_fly_type.currentData(),
            "fly_to_place": self.lineEdit_target_place_name.text(),
            "fly_to_longitude": self.lineEdit_target_longitude.text(),
            "fly_to_latitude": self.lineEdit_target_latitude.text(),
            "fly_to_altitude": self.lineEdit_target_altitude.text(),
            "heading": self.lineEdit_heading.text(),
            "tilt": self.lineEdit_tilt.text(),
            "set_2d_view": 1 if self.checkBox_2D_view.isChecked() else 0,
            "set_3d_view": 1 if self.checkBox_3D_view.isChecked() else 0,
            "fly_speed": self.doubleSpinBox_fly_speed.value(),
            "start_x": int(self.lineEdit_target_start_x.text()) if self.lineEdit_target_start_x.text() else 0,
            "start_y": int(self.lineEdit_target_start_y.text()) if self.lineEdit_target_start_y.text() else 0,
            "end_x": int(self.lineEdit_target_end_x.text()) if self.lineEdit_target_end_x.text() else 0,
            "end_y": int(self.lineEdit_target_end_y.text()) if self.lineEdit_target_end_y.text() else 0,
            "slide_speed": int(self.spinBox_slide_speed.value()),
            "zoom_times": int(self.spinBox_zoom_time.value())
        })
        view_sender.subtitle_action.save.emit(self.data)

    def init_fly_type(self, fly_type):
        self.comboBox_fly_type.clear()
        for key, value in fly_type.items():
            self.comboBox_fly_type.addItem(value, key)

    def set_check_box_with_3d_view_clicked(self):
        self.checkBox_2D_view.setChecked(False)

    def set_check_box_with_2d_view_clicked(self):
        self.checkBox_3D_view.setChecked(False)

    def set_enable_with_fly_type(self):
        self.groupBox_heading_tilt_view.setEnabled(False)
        self.groupBox_screen_action.setEnabled(False)
        self.groupBox_set_2d_3d_view.setEnabled(False)
        self.groupBox_fly.setEnabled(False)

        current_fly_type = self.comboBox_fly_type.currentData()
        match current_fly_type:
            case ("heading" | "tilt"):
                self.groupBox_heading_tilt_view.setEnabled(True)
            case "set_view":
                self.groupBox_set_2d_3d_view.setEnabled(True)
            case ("screen_move" | "screen_heading_tilt" | "screen_zoom_in" | "screen_zoom_out"):
                self.groupBox_screen_action.setEnabled(True)
            case ("lla" | "place_name"):
                self.groupBox_fly.setEnabled(True)
                if current_fly_type == "lla":
                    self.lineEdit_target_longitude.setEnabled(True)
                    self.lineEdit_target_latitude.setEnabled(True)
                    self.lineEdit_target_altitude.setEnabled(True)
                    self.pushButton_get_position.setEnabled(True)
                    self.lineEdit_target_place_name.setEnabled(False)
                elif current_fly_type == "place_name":
                    self.lineEdit_target_place_name.setEnabled(True)
                    self.lineEdit_target_longitude.setEnabled(False)
                    self.lineEdit_target_latitude.setEnabled(False)
                    self.lineEdit_target_altitude.setEnabled(False)
                    self.pushButton_get_position.setEnabled(False)

    def show_slide_time(self):
        start_x = int(self.lineEdit_target_start_x.text()) if self.lineEdit_target_start_x.text() else 0
        start_y = int(self.lineEdit_target_start_y.text()) if self.lineEdit_target_start_y.text() else 0

        end_x = int(self.lineEdit_target_end_x.text()) if self.lineEdit_target_end_x.text() else 0
        end_y = int(self.lineEdit_target_end_y.text()) if self.lineEdit_target_end_y.text() else 0
        step = self.spinBox_slide_speed.value()
        if start_x and start_y and end_x and end_y and step:
            slide_time = math.sqrt((end_x - start_x) ** 2 + (start_y - end_y) ** 2) / step * 0.01
            self.label_slide_time.setText(str(round(slide_time, 2)) + "s")
        else:
            self.label_slide_time.setText("")

    def show_zoom_time(self):
        step = self.spinBox_slide_speed.value()
        times = self.spinBox_zoom_time.value()
        if step and times:
            self.label_zoom_time.setText(str(round((times * 0.01 / step), 2)) + "s")
        else:
            self.label_zoom_time.setText("")


class SubtitleSetFontsView(SetFontsView):
    def __init__(self, icon_path=None):
        super(SubtitleSetFontsView, self).__init__(icon_path)
        self.setWindowTitle("正在批量设置 [字幕] 字体")

        self.pushButton.clicked.connect(self.send_data)
        self.data = {}
        self.subtitle_ids = []

    def show_edit(self, subtitle_ids: list, font_list: dict, font_color: dict):
        self.subtitle_ids = subtitle_ids
        self.clear_combobox()
        for font in font_list:
            self.comboBox_font.addItem(font, font)
        if font_color and type(font_color) == dict:
            for key, value in font_color.items():
                self.comboBox_font_color.addItem(value, key)
        for n in range(1, 25):
            self.comboBox_font_size.addItem(str(n) + "em", str(n) + "em")

        self.show()

    def send_data(self):
        self.close()
        self.data.update({
            "font": self.comboBox_font.currentText() if self.checkBox_font.isChecked() else "",
            "font_size": self.comboBox_font_size.currentText() if self.checkBox_font_size.isChecked() else "",
            "font_color": self.comboBox_font_color.currentData() if self.checkBox_font_color.isChecked() else ""
        })
        view_sender.subtitle.set_font_batch.emit(self.data, self.subtitle_ids)


class SubtitleSetVoicesView(QtWidgets.QDialog, Ui_Dialog_set_voices):
    def __init__(self, icon_path=None):
        super(SubtitleSetVoicesView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.setWindowTitle("正在批量设置 [字幕] 配音")

        self.pushButton.clicked.connect(self.send_data)

        self.comboBox_voice_name.currentIndexChanged.connect(self.init_combobox_voice_role_style)
        self.voice_list = []
        self.data = {}
        self.subtitle_ids = []

    def show_edit(self, subtitle_ids: list, voice_list: list):
        self.voice_list = voice_list
        self.subtitle_ids = subtitle_ids
        self.comboBox_voice_name.clear()
        for index, voice in enumerate(self.voice_list):
            local_name = voice.get("local_name")
            short_name = voice.get("short_name")
            self.comboBox_voice_name.addItem(local_name, short_name)
            if local_name == "云希":
                self.comboBox_voice_name.setCurrentIndex(index)
        self.show()

    def send_data(self):
        self.close()
        self.data.update({
            "voice_local_name": self.comboBox_voice_name.currentText(),
            "voice_name": self.comboBox_voice_name.currentData(),
            "voice_role": self.comboBox_voice_role.currentText(),
            "voice_style": self.comboBox_voice_style.currentText(),
            "voice_rate": self.doubleSpinBox_voice_rate.value(),
            "voice_volume": self.doubleSpinBox_voice_volume.value(),
            "voice_pitch": self.doubleSpinBox_voice_pitch.value()
        })
        view_sender.subtitle.set_speech_batch.emit(self.data, self.subtitle_ids)

    def init_combobox_voice_role_style(self):
        self.comboBox_voice_role.clear()
        self.comboBox_voice_style.clear()
        current_index = self.comboBox_voice_name.currentIndex()
        if current_index >= 0:
            voice_style = self.voice_list[current_index].get("style_list")
            self.comboBox_voice_style.addItem("default")
            if voice_style:
                self.comboBox_voice_style.addItems(voice_style)
            voice_role = self.voice_list[current_index].get("role_play_list")
            self.comboBox_voice_role.addItem("default")
            if voice_role:
                self.comboBox_voice_role.addItems(voice_role)
