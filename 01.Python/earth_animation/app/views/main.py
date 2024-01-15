import os

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from app.views.ui.main import Ui_MainWindow
from app.views.sender import view_sender

import hiworker


class MainView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, icon_path=None):
        super(MainView, self).__init__()
        self.setupUi(self)
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))

        self.pushButton_open_earth.clicked.connect(view_sender.main.open_earth.emit)
        self.pushButton_init_earth.clicked.connect(view_sender.main.init_earth.emit)
        self.pushButton_hide_earth_ui.clicked.connect(view_sender.main.hide_ui.emit)
        self.pushButton_show_earth_ui.clicked.connect(view_sender.main.show_ui.emit)
        self.pushButton_street_view.clicked.connect(view_sender.main.toggle_street_view.emit)
        self.pushButton_heading_0.clicked.connect(view_sender.main.set_north.emit)
        self.pushButton_clear_all_data.clicked.connect(view_sender.main.clear_earth.emit)
        self.pushButton_close_search.clicked.connect(view_sender.main.close_search.emit)
        self.pushButton_zoom_to_space.clicked.connect(view_sender.main.fly_to_space.emit)
        self.pushButton_set_2d_view.clicked.connect(view_sender.main.set_2d_view.emit)
        self.pushButton_set_3d_view.clicked.connect(view_sender.main.set_3d_view.emit)
        self.pushButton_fly_to_place_or_lla.clicked.connect(view_sender.main.fly_to_place_or_lla.emit)

        self.lineEdit_fly_to_place_or_lla.returnPressed.connect(view_sender.main.fly_to_place_or_lla.emit)

        self.action_open_earth.triggered.connect(view_sender.main.open_earth.emit)
        self.action_tts_panel.triggered.connect(view_sender.main.open_tts.emit)
        self.action_update_voices.triggered.connect(view_sender.main.update_voices.emit)
        self.action_setting.triggered.connect(view_sender.main.open_setting.emit)
        self.action_about.triggered.connect(view_sender.main.open_about.emit)
        self.action_manual.triggered.connect(view_sender.main.open_manual.emit)
        self.action_open_nasa.triggered.connect(view_sender.main.open_nasa.emit)
        self.action_download_nasa.triggered.connect(view_sender.main.download_nasa.emit)

        view_sender.main.load_table_collection.connect(self.load_table_collection)
        view_sender.main.load_table_episode.connect(self.load_table_episode)
        view_sender.main.load_table_subtitle.connect(self.load_table_subtitle)
        view_sender.main.load_table_media.connect(self.load_table_media)

        view_sender.main.load_table_subtitle_sub.connect(self.load_table_subtitle_action)
        view_sender.main.load_table_media_sub.connect(self.load_table_media_sub)

    # 初始化表格
    def init_table_collection(self, header_collection):
        hiworker.TableLoad.init_table_header(self.tableWidget_collection, header_collection)

    def init_table_episode(self, header_episode):
        hiworker.TableLoad.init_table_header(self.tableWidget_episode, header_episode)

    def init_table_subtitle(self, header_subtitle):
        hiworker.TableLoad.init_table_header(self.tableWidget_subtitle, header_subtitle)

    def init_table_media(self, header_media):
        hiworker.TableLoad.init_table_header(self.tableWidget_media, header_media)

    def init_table_subtitle_action(self, header_subtitles_sub):
        hiworker.TableLoad.init_table_header(self.tableWidget_subtitle_action, header_subtitles_sub, is_horizontal=False)

    def init_table_media_sub(self, header_media_sub):
        hiworker.TableLoad.init_table_header(self.tableWidget_media_sub, header_media_sub, is_horizontal=False)

    # 加载表格数据
    def load_table_collection(self, data: list, cols_setting):
        hiworker.TableLoad.load_table(self.tableWidget_collection, data, cols_setting)

    def load_table_episode(self, data: list, cols_setting, select_first_row=False):
        hiworker.TableLoad.load_table(self.tableWidget_episode, data, cols_setting, order_by="sort", select_first_row=select_first_row)

    def load_table_subtitle(self, data: list, cols_setting, select_first_row=False):
        hiworker.TableLoad.load_table(self.tableWidget_subtitle, data, cols_setting, order_by="sort", select_first_row=select_first_row)

    def load_table_media(self, data: list, cols_setting, select_first_row=False):
        hiworker.TableLoad.load_table(self.tableWidget_media, data, cols_setting, order_by="sort", select_first_row=select_first_row)

    def load_table_subtitle_action(self, data: dict, cols_setting):
        hiworker.TableLoad.load_table(self.tableWidget_subtitle_action, [data], cols_setting, is_vertical=True)

    def load_table_media_sub(self, data: dict, cols_setting):
        hiworker.TableLoad.init_table_header(self.tableWidget_media_sub, cols_setting, is_horizontal=False)
        hiworker.TableLoad.load_table(self.tableWidget_media_sub, [data], cols_setting, is_vertical=True)

    # 获取表格数据
    def get_collection_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_collection)

    def get_collection_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_collection)

    def get_episode_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_episode)

    def get_episode_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_episode)

    def get_subtitle_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_subtitle)

    def get_subtitle_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_subtitle)

    def get_media_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_media)

    def get_media_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_media)

    # 显示字幕时间
    def display_audio_and_run_time(self, audio_time: float, run_time: float):
        if not audio_time:
            audio_time = ""
        if not run_time:
            run_time = ""
        self.label_total_audio_time.setText(str(audio_time))
        self.label_total_run_time.setText(str(run_time))
