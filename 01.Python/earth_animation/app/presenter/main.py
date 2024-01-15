from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from .app_setting import SettingPresenter
from .collection import CollectionPresenter
from .episode import EpisodePresenter
from .media import MediaPresenter
from .play import Play
from .signal import presenter_signal
from .subtitle import SubtitlePresenter
from .tts import TTSPresenter
from ..models import *
from ..static import *
from ..utils import *
from ..views import view_sender, MainView
from ..web_driver.web_driver import earth_driver


class MainPresenter:
    def __init__(self):
        self.main_window = MainView()
        self.main_window.dialog_info = hiworker.DialogInfo()

        self._collection = CollectionModel()
        self._episode = EpisodeModel()
        self._subtitle = SubtitleModel()

        self._media = MediaModel()
        self._media_2d_text = Media2dTextModel()
        self._media_2d_image = Media2dImageModel()
        self._media_2d_video = Media2dVideoModel()
        self._media_2d_bgm = Media2dBgmModel()

        self._media_3d_text = Media3dTextModel()
        self._media_3d_image = Media3dImageModel()
        self._media_3d_video = Media3dVideoModel()
        self._media_3d_kml = Media3dKmlModel()
        self._media_3d_overlay = Media3dOverlayModel()
        self._media_3d_motion_line = Media3dMotionLineModel()

        self._setting = SettingModel()
        self._subtitle_action = SubtitleActionModel()

        self.collection = CollectionPresenter()
        self.episode = EpisodePresenter()
        self.subtitle = SubtitlePresenter()
        self.media = MediaPresenter()
        self.setting = SettingPresenter()
        self.tts = TTSPresenter()
        self.play = Play("Google Earth - Google Chrome",
                         self._setting.get_source_screen_x(),
                         self._setting.get_source_screen_y(),
                         self._setting.get_screen_offset_x(),
                         self._setting.get_screen_offset_y()
                         )

        self.table_collection = self.main_window.tableWidget_collection
        self.table_episode = self.main_window.tableWidget_episode
        self.table_subtitle = self.main_window.tableWidget_subtitle
        self.table_subtitle_action = self.main_window.tableWidget_subtitle_action
        self.table_media = self.main_window.tableWidget_media
        self.table_media_sub = self.main_window.tableWidget_media_sub

        self.user_data_dir = ""
        self.media_types = [".jpg", ".png", ".bmp", ".mp4"]

        self.bind_signal_main_ui()
        self.bind_signal_presenter()
        self.bind_table_right_click()
        self.bind_table_double_click()
        self.bind_table_click()
        self.init_table()

        self.bind_menu()
        self.load_collection_table()

    # 绑定主界面信号
    def bind_signal_main_ui(self):
        view_sender.main.open_setting.connect(self.setting.show_setting)
        view_sender.main.open_tts.connect(self.tts.show)
        view_sender.main.update_voices.connect(self.update_voice)
        view_sender.main.open_manual.connect(open_help_page)

        view_sender.main.open_earth.connect(self.open_earth)
        view_sender.main.init_earth.connect(self.init_earth)
        view_sender.main.hide_ui.connect(self.hide_earth_ui)
        view_sender.main.show_ui.connect(self.show_earth_ui)
        view_sender.main.toggle_street_view.connect(self.change_stree_view)
        view_sender.main.set_north.connect(self.set_north)
        view_sender.main.clear_earth.connect(self.clear_result)
        view_sender.main.close_search.connect(self.close_search)
        view_sender.main.fly_to_space.connect(self.fly_to_space)
        view_sender.main.set_2d_view.connect(self.set_2d_view)
        view_sender.main.set_3d_view.connect(self.set_3d_view)
        view_sender.main.fly_to_place_or_lla.connect(self.fly_to_place_or_lla)

    # 绑定presenter信号
    def bind_signal_presenter(self):
        presenter_signal.load_table_collection.connect(self.load_collection_table)
        presenter_signal.load_table_episode.connect(self.load_episode_table)
        presenter_signal.load_table_subtitle.connect(self.load_subtitle_table)
        presenter_signal.load_table_subtitle_sub.connect(self.load_subtitle_sub_table)
        presenter_signal.load_table_media.connect(self.load_media_table)
        presenter_signal.load_table_media_sub.connect(self.load_media_sub_table)

    # 绑定表格右键
    def bind_table_right_click(self):
        self.table_collection.customContextMenuRequested.connect(self.collection.show_menu)
        self.table_episode.customContextMenuRequested.connect(self.episode.show_menu)
        self.table_subtitle.customContextMenuRequested.connect(self.subtitle.show_menu)
        self.table_media.customContextMenuRequested.connect(self.media.show_menu)

        self.table_collection.customContextMenuRequested.connect(self.load_episode_table_with_select_first)
        self.table_episode.customContextMenuRequested.connect(self.load_subtitle_table_with_select_first)
        self.table_subtitle.customContextMenuRequested.connect(self.load_subtitle_sub_table)
        self.table_subtitle.customContextMenuRequested.connect(self.load_media_table_with_select_first)
        # self.table_subtitle.clicked.connect(self.load_subtitle_sub_table)
        self.table_media.customContextMenuRequested.connect(self.load_media_sub_table)
        self.table_media.customContextMenuRequested.connect(self.preview_media_src)

    def bind_table_double_click(self):
        self.table_collection.doubleClicked.connect(self.collection_show_edit)
        self.table_episode.doubleClicked.connect(self.episode_show_edit)
        self.table_subtitle.doubleClicked.connect(self.subtitle_show_edit_action)
        self.table_media.doubleClicked.connect(self.media_show_prop_edit)

    def bind_table_click(self):
        self.table_collection.clicked.connect(self.load_episode_table_with_select_first)
        self.table_episode.clicked.connect(self.load_subtitle_table_with_select_first)
        self.table_subtitle.clicked.connect(self.load_subtitle_sub_table)
        self.table_subtitle.clicked.connect(self.load_media_table_with_select_first)
        # self.table_subtitle.clicked.connect(self.load_subtitle_sub_table)
        self.table_media.clicked.connect(self.load_media_sub_table)
        self.table_media.clicked.connect(self.preview_media_src)

    # 绑定右键菜单
    def bind_menu(self):
        self.collection.menu.add_collection.triggered.connect(self.collection_show_add)
        self.collection.menu.edit_collection.triggered.connect(self.collection_show_edit)
        self.collection.menu.delete_collection.triggered.connect(self.collection_delete)
        self.collection.menu.run_collection.triggered.connect(self.play_with_collections)
        self.collection.menu.stop_collection.triggered.connect(self.play.stop)

        self.episode.menu.add_episode.triggered.connect(self.episode_show_add)
        self.episode.menu.edit_episode.triggered.connect(self.episode_show_edit)
        self.episode.menu.delete_episode.triggered.connect(self.episode_delete)
        self.episode.menu.up_episode.triggered.connect(self.episode_move_up)
        self.episode.menu.down_episode.triggered.connect(self.episode_move_down)
        self.episode.menu.create_speech.triggered.connect(self.episode_create_voice)
        self.episode.menu.search_audio.triggered.connect(self.episode_search_audio)
        self.episode.menu.search_media.triggered.connect(self.episode_search_media)
        self.episode.menu.import_from_excel.triggered.connect(self.episode_import_excel)
        self.episode.menu.create_subtitle.triggered.connect(self.episode_create_subtitle)
        self.episode.menu.run_episodes.triggered.connect(self.play_with_episodes)

        self.subtitle.menu.edit_prop.triggered.connect(self.subtitle_show_edit)
        self.subtitle.menu.edit_action.triggered.connect(self.subtitle_show_edit_action)
        self.subtitle.menu.insert_blank.triggered.connect(self.subtitle_insert_blank)
        self.subtitle.menu.delete_blank.triggered.connect(self.subtitle_delete_blank)
        self.subtitle.menu.up_blank.triggered.connect(self.subtitle_up_blank)
        self.subtitle.menu.down_blank.triggered.connect(self.subtitle_down_blank)

        self.subtitle.menu.search_media.triggered.connect(self.episode_search_media)
        # self.subtitle.menu.delete_media.triggered.connect(self.subtitle_delete)
        self.subtitle.menu.open_media.triggered.connect(self.subtitle_open_folder)
        self.subtitle.menu.get_audio.triggered.connect(self.subtitle_create_voice)
        self.subtitle.menu.search_audio.triggered.connect(self.subtitle_search_voice)
        self.subtitle.menu.run_subtitles.triggered.connect(self.play_with_subtitles)
        self.subtitle.menu.edit_fonts.triggered.connect(self.subtitle_set_font)
        self.subtitle.menu.edit_voices.triggered.connect(self.subtitle_set_speech)

        self.media.menu.add_media.triggered.connect(self.media_show_add)
        self.media.menu.edit_media.triggered.connect(self.media_show_edit)
        self.media.menu.edit_media_prop.triggered.connect(self.media_show_prop_edit)
        self.media.menu.open_media.triggered.connect(self.media_open_folder)
        self.media.menu.delete_media.triggered.connect(self.media_delete)
        self.media.menu.run_medias.triggered.connect(self.play_with_medias)
        self.media.menu.edit_fonts.triggered.connect(self.media_set_font)
        self.media.menu.copy_media.triggered.connect(self.media_copy)
        self.media.menu.move_media.triggered.connect(self.media_move_to_subtitle)
        self.media.menu.edit_size.triggered.connect(self.media_set_size)

    # 初始化表格
    def init_table(self):
        self.main_window.init_table_collection(header_collection)
        self.main_window.init_table_episode(header_episode)
        self.main_window.init_table_subtitle(header_subtitle)
        self.main_window.init_table_media(header_media)
        self.main_window.init_table_subtitle_action(header_subtitles_sub)
        # self.main_window.init_table_media_sub(header_media_sub)

    # 加载表格数据
    def load_collection_table(self, select_first_row=False):
        data = self._collection.get_all_data()
        self.main_window.load_table_collection(data, header_collection)

    def load_episode_table_with_select_first(self):
        self.load_episode_table(True)

    def load_episode_table(self, select_first_row=False):
        collection_id = self.get_collection_id()
        if collection_id:
            data = self._episode.get_dict_list_by_collection_id(collection_id)
            self.main_window.load_table_episode(data, header_episode, select_first_row=select_first_row)
        self.load_subtitle_table(select_first_row)

    def load_subtitle_table_with_select_first(self):
        self.load_subtitle_table(True)

    def load_subtitle_table(self, select_first_row=False):
        data = []
        episode_id = self.get_episode_id()
        if episode_id:
            data = self._subtitle.get_dict_list_by_episode_id(episode_id)
        self.main_window.load_table_subtitle(data, header_subtitle, select_first_row=select_first_row)
        total_audio_time, total_run_time = self.subtitle.sum_subtitle_total_time(episode_id)
        self.main_window.display_audio_and_run_time(total_audio_time, total_run_time)
        self.load_media_table(select_first_row)

    def load_subtitle_sub_table(self):
        data = {}
        subtitle_id = self.get_subtitle_id()
        if subtitle_id:
            data = self._subtitle_action.get_dict_by_subtitle_id(subtitle_id)
        self.main_window.load_table_subtitle_action(data, header_subtitles_sub)

    def load_media_table_with_select_first(self):
        self.load_media_table(True)

    def load_media_table(self, select_first_row=False):
        data = []
        subtitle_id = self.get_subtitle_id()
        if subtitle_id:
            data = self._media.get_dict_list_by_subtitle(subtitle_id)
        self.main_window.load_table_media(data, header_media, select_first_row=select_first_row)
        self.preview_media_src()
        self.load_media_sub_table()

    def load_media_sub_table(self):
        media_id = self.get_media_id()
        if not media_id:
            self.main_window.load_table_media_sub({}, [])
        else:
            data = self._media.get_dict_by_id(media_id)
            if data:
                match data.get("show_type"):
                    case "screen":
                        match data.get("media_type"):
                            case "text":
                                media_prop_data = self._media_2d_text.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_2d_text)
                            case "image":
                                media_prop_data = self._media_2d_image.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_2d_image_video)
                            case "video":
                                media_prop_data = self._media_2d_video.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_2d_image_video)
                            case "bgm":
                                media_prop_data = self._media_2d_bgm.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_2d_bgm)
                    case "three":
                        match data.get("media_type"):
                            case "text":
                                media_prop_data = self._media_3d_text.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_3d_text)
                            case "image":
                                media_prop_data = self._media_3d_image.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_3d_image_video)
                            case "video":
                                media_prop_data = self._media_3d_video.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_3d_image_video)
                            case "kml":
                                media_prop_data = self._media_3d_kml.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_3d_kml)
                            case "overlay":
                                media_prop_data = self._media_3d_overlay.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_3d_overlay)
                            case "motion_line":
                                media_prop_data = self._media_3d_motion_line.get_dict_by_media(media_id)
                                self.main_window.load_table_media_sub(media_prop_data, header_media_3d_motion_line)

    def update_voice(self):
        voices = get_voice_list(self._setting.get_azure_key())
        if voices:
            self.tts.voices = voices
            self.subtitle.voices = voices

    # 从表格获取数据id
    def get_collection_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.table_collection)

    def get_collection_id(self):
        return hiworker.TableRead.get_current_data_id(self.table_collection)

    def get_episode_id(self, episode_sort=None):
        collection_id = self.get_collection_id()
        if not episode_sort:
            episode_sort = hiworker.TableRead.get_current_data_id(self.table_episode)
        return self._episode.get_id(collection_id, episode_sort)

    def get_episode_ids(self, episode_sorts=None):
        collection_id = self.get_collection_id()
        if not episode_sorts:
            episode_sorts = hiworker.TableRead.get_selected_data_ids(self.table_episode)
        return self._episode.get_ids(collection_id, episode_sorts)

    def get_subtitle_id(self, subtitle_sort=None):
        episode_id = self.get_episode_id()
        if not subtitle_sort:
            subtitle_sort = hiworker.TableRead.get_current_data_id(self.table_subtitle)
        return self._subtitle.get_id(episode_id, subtitle_sort)

    def get_subtitle_ids(self, subtitle_sorts=None):
        episode_id = self.get_episode_id()
        if not subtitle_sorts:
            subtitle_sorts = hiworker.TableRead.get_selected_data_ids(self.table_subtitle)
        return self._subtitle.get_ids(episode_id, subtitle_sorts)

    def get_subtitle_action_id(self):
        pass

    def get_media_id(self, media_sort=None):
        subtitle_id = self.get_subtitle_id()
        if not media_sort:
            media_sort = hiworker.TableRead.get_current_data_id(self.table_media)
        return self._media.get_id(subtitle_id, media_sort)

    def get_media_ids(self, media_sorts=None):
        subtitle_id = self.get_subtitle_id()
        if not media_sorts:
            media_sorts = hiworker.TableRead.get_selected_data_ids(self.table_media)
        return self._media.get_ids(subtitle_id, media_sorts)

    # collection
    def collection_show_add(self):
        self.collection.show_add()

    def collection_show_edit(self):
        collection_id = hiworker.TableRead.get_current_data_id(self.table_collection)
        self.collection.show_edit(collection_id)

    def collection_delete(self):
        collection_id = hiworker.TableRead.get_current_data_id(self.table_collection)
        self.collection.delete(collection_id)

    def play_with_collections(self):
        collection_data_list = self._collection.get_dict_list_by_ids(self.get_collection_ids())
        for collection_data in collection_data_list:
            episode_data_list = self._episode.get_dict_list_by_collection_id(collection_data.get("id"))
            for episode_data in episode_data_list:
                subtitle_data_list = self._subtitle.get_dict_list_by_episode_id(episode_data.get("id"))
                for subtitle_data in subtitle_data_list:
                    subtitle_action = self._subtitle_action.get_dict_by_subtitle_id(subtitle_data.get("id"))
                    media_data_list = self.generate_medias_data(collection_data.get("name"),
                                                                episode_data.get("name"),
                                                                subtitle_id=subtitle_data.get("id"))
                    subtitle_data.update({"subtitle_action": subtitle_action, "medias": media_data_list})
                episode_data.update({"subtitles": subtitle_data_list})
            collection_data.update({"episodes": episode_data_list})
        self.play.is_medias = False
        self.play.data = collection_data_list
        self.play.start()

    # episode
    def episode_show_add(self):
        collection_id = hiworker.TableRead.get_current_data_id(self.table_collection)
        self.episode.show_add(collection_id)

    def episode_show_edit(self):
        episode_id = self.get_episode_id()
        self.episode.show_edit(episode_id)

    def episode_delete(self):
        episode_id = self.get_episode_id()
        self.episode.delete(episode_id)

    def episode_create_subtitle(self):
        collection_id = hiworker.TableRead.get_current_data_id(self.table_collection)
        episode_sort_ids = hiworker.TableRead.get_selected_data_ids(self.table_episode)
        episode_ids = self._episode.get_ids(collection_id, episode_sort_ids)
        self.episode.create_subtitle(episode_ids)
        self.load_subtitle_table()

    def episode_create_voice(self):
        episode_ids = self.get_episode_ids()
        Thread(target=self.episode.create_speech, args=(episode_ids,)).start()

    def episode_move_up(self):
        current_row_number = hiworker.TableRead.get_current_row_number(self.table_episode)
        if current_row_number > 0:
            episode_id = self.get_episode_id()
            episode_sort = hiworker.TableRead.get_current_data_id(self.table_episode)

            up_episode_sort = hiworker.TableRead.get_row_item_data(self.table_episode, current_row_number - 1, 0)
            up_episode_id = self.get_episode_id(int(up_episode_sort))

            self._episode.update({"id": episode_id, "sort": int(episode_sort) - 1})
            self._episode.update({"id": up_episode_id, "sort": int(up_episode_sort) + 1})
            self.load_episode_table()

    def episode_move_down(self):
        current_row_number = hiworker.TableRead.get_current_row_number(self.table_episode)
        if current_row_number < self.table_episode.rowCount() - 1:
            episode_id = self.get_episode_id()
            episode_sort = hiworker.TableRead.get_current_data_id(self.table_episode)

            down_episode_sort = hiworker.TableRead.get_row_item_data(self.table_episode, current_row_number + 1, 0)
            down_episode_id = self.get_episode_id(int(down_episode_sort))

            self._episode.update({"id": episode_id, "sort": int(episode_sort) + 1})
            self._episode.update({"id": down_episode_id, "sort": int(down_episode_sort) - 1})
            self.load_episode_table()

    def episode_check_voice(self):
        pass

    def episode_search_audio(self):
        collection_id = self.get_collection_id()
        episode_id = self.get_episode_ids()
        self.episode.search_audio(collection_id, episode_id)

    def episode_search_media(self):
        episode_ids = self.get_episode_ids()
        self.episode.search_media(episode_ids)
        self.load_subtitle_table()

    def episode_stop(self):
        pass

    def play_with_episodes(self):
        collection_data = self._collection.get_dict_by_id(self.get_collection_id())
        episode_data_list = self._episode.get_dict_list_by_ids(self.get_episode_ids())
        if episode_data_list:
            for episode_data in episode_data_list:
                subtitle_data_list = self._subtitle.get_dict_list_by_episode_id(episode_data.get("id"))
                for subtitle_data in subtitle_data_list:
                    subtitle_action = self._subtitle_action.get_dict_by_subtitle_id(subtitle_data.get("id"))
                    media_data_list = self.generate_medias_data(collection_data.get("name"),
                                                                episode_data.get("name"),
                                                                subtitle_id=subtitle_data.get("id"))
                    subtitle_data.update({"subtitle_action": subtitle_action, "medias": media_data_list})
                episode_data.update({"subtitles": subtitle_data_list})
            collection_data.update({"episodes": episode_data_list})
        data_to_run = [collection_data]
        self.play.is_medias = False
        self.play.data = data_to_run
        self.play.start()

    def episode_import_excel(self):
        excel_path, result = QtWidgets.QFileDialog.getOpenFileName(caption="选择Excel", filter='(*.xlsx; *.xls)', parent=self.main_window)
        if os.path.isfile(excel_path):
            collection_id = hiworker.TableRead.get_current_data_id(self.table_collection)
            Thread(target=self.episode.import_places_from_excel, args=(excel_path, collection_id)).start()

    # subtitle
    def subtitle_show_edit(self):
        subtitle_id = self.get_subtitle_id()
        self.subtitle.show_edit(subtitle_id)

    def subtitle_show_edit_action(self):
        subtitle_id = self.get_subtitle_id()
        self.subtitle.show_edit_action(subtitle_id)

    def subtitle_delete(self):
        pass

    def subtitle_insert_blank(self):
        insert_sort = hiworker.TableRead.get_current_data_id(self.table_subtitle)

        current_row_number = hiworker.TableRead.get_current_row_number(self.table_subtitle)
        row_count = self.table_subtitle.rowCount()
        for n in range(row_count - 1, current_row_number - 1, -1):
            sort = int(hiworker.TableRead.get_row_item_data(self.table_subtitle, n, 0))
            subtitle_id = self.get_subtitle_id(subtitle_sort=sort)
            self._subtitle.update({"id": subtitle_id, "sort": sort + 1})

        episode_id = self.get_episode_id()
        self._subtitle.add({"name": "[blank]" + hiworker.random_str(12), "sort": insert_sort, "episode_id": episode_id})
        self.load_subtitle_table()

    def subtitle_delete_blank(self):
        subtitle_data = self._subtitle.get_dict_by_id(self.get_subtitle_id())
        if "[blank]" in subtitle_data.get("name"):
            self._subtitle.delete(subtitle_data.get("id"))
            current_row_number = hiworker.TableRead.get_current_row_number(self.table_subtitle)
            row_count = self.table_subtitle.rowCount()
            for n in range(current_row_number + 1, row_count, 1):
                sort = int(hiworker.TableRead.get_row_item_data(self.table_subtitle, n, 0))
                subtitle_id = self.get_subtitle_id(subtitle_sort=sort)
                self._subtitle.update({"id": subtitle_id, "sort": sort - 1})
            self.load_subtitle_table()

    def subtitle_up_blank(self):
        current_row_number = hiworker.TableRead.get_current_row_number(self.table_subtitle)
        if current_row_number > 0:
            subtitle_name = hiworker.TableRead.get_row_item_data(self.table_subtitle, current_row_number, 1)
            if "[blank]" in subtitle_name:
                subtitle_sort_to_up = hiworker.TableRead.get_current_data_id(self.table_subtitle)
                subtitle_id_to_up = self.get_subtitle_id()

                subtitle_sort_to_down = hiworker.TableRead.get_row_item_data(self.table_subtitle, current_row_number - 1, 0)
                subtitle_id_to_down = self.get_subtitle_id(int(subtitle_sort_to_down))

                self._subtitle.update({"id": subtitle_id_to_up, "sort": int(subtitle_sort_to_up) - 1})
                self._subtitle.update({"id": subtitle_id_to_down, "sort": int(subtitle_sort_to_down) + 1})
                self.load_subtitle_table()

    def subtitle_down_blank(self):
        current_row_number = hiworker.TableRead.get_current_row_number(self.table_subtitle)
        if current_row_number < self.table_subtitle.rowCount() - 1:
            subtitle_name = hiworker.TableRead.get_row_item_data(self.table_subtitle, current_row_number, 1)
            if "[blank]" in subtitle_name:
                subtitle_sort_to_down = hiworker.TableRead.get_current_data_id(self.table_subtitle)
                subtitle_id_to_down = self.get_subtitle_id()

                subtitle_sort_to_up = hiworker.TableRead.get_row_item_data(self.table_subtitle, current_row_number + 1, 0)
                subtitle_id_to_up = self.get_subtitle_id(int(subtitle_sort_to_up))
                self._subtitle.update({"id": subtitle_id_to_down, "sort": int(subtitle_sort_to_down) + 1})
                self._subtitle.update({"id": subtitle_id_to_up, "sort": int(subtitle_sort_to_up) - 1})
                self.load_subtitle_table()

    def subtitle_set_font(self):
        subtitle_ids = self.get_subtitle_ids()
        self.subtitle.show_set_fonts(subtitle_ids)

    def subtitle_set_speech(self):
        subtitle_ids = self.get_subtitle_ids()
        self.subtitle.show_set_voice(subtitle_ids)

    def subtitle_open_folder(self):
        collection_id = self.get_collection_id()
        episode_id = self.get_episode_id()
        self.subtitle.open_media_folder(collection_id, episode_id)

    def subtitle_create_voice(self):
        pass

    def subtitle_search_voice(self):
        subtitle_ids = self.get_subtitle_ids()
        episode_id = self.get_episode_id()
        collection_id = self.get_collection_id()
        self.subtitle.search_audio(subtitle_ids, episode_id, collection_id)

    def subtitle_check_voice_time(self):
        pass

    def play_with_subtitles(self):
        collection_data = self._collection.get_dict_by_id(self.get_collection_id())
        episode_data = self._episode.get_dict_by_id(self.get_episode_id())
        collection_data.update({"episodes": [episode_data]})
        subtitle_data_list = self._subtitle.get_dict_list_by_ids(self.get_subtitle_ids())
        if subtitle_data_list:
            for subtitle_data in subtitle_data_list:
                subtitle_action = self._subtitle_action.get_dict_by_subtitle_id(subtitle_data.get("id"))
                media_data_list = self.generate_medias_data(collection_data.get("name"),
                                                            episode_data.get("name"),
                                                            subtitle_id=subtitle_data.get("id"))
                subtitle_data.update({"subtitle_action": subtitle_action, "medias": media_data_list})
                episode_data.update({"subtitles": subtitle_data_list})
        data_to_run = [collection_data]
        self.play.is_medias = False
        self.play.data = data_to_run
        self.play.start()

    # media
    def media_show_add(self):
        subtitle_id = self.get_subtitle_id()
        self.media.show_add(subtitle_id)

    def media_show_edit(self):
        media_id = self.get_media_id()
        self.media.show_edit(media_id)

    def media_show_prop_edit(self):
        media_id = self.get_media_id()
        self.media.show_prop_edit(media_id)

    def media_copy(self):
        pass

    def media_move_to_subtitle(self):
        pass

    def media_delete(self):
        pass

    def media_set_size(self):
        pass

    def media_set_font(self):
        pass

    def media_open_folder(self):
        self.media.open_media_in_media_list(
            self.get_collection_id(),
            self.get_episode_id(),
            self.get_media_id()
        )

    def preview_media_src(self):
        media_id = self.get_media_id()
        if media_id:
            media_data = self._media.get_dict_by_id(media_id)
            if media_data:
                media_type = media_data.get("media_type")
                match media_type:
                    case "image":
                        if media_data.get("show_type") == "screen":
                            media_prop = self._media_2d_image.get_dict_by_media(media_id)
                        else:
                            media_prop = self._media_3d_image.get_dict_by_media(media_id)
                        media_file = "" if media_prop.get("file") is None else media_prop.get("file")
                        image_folder = self.media.get_media_folder(self.get_collection_id(), self.get_episode_id(), media_id)
                        self.qt_show_image(image_folder, media_file)
                    case "overlay":
                        media_prop = self._media_3d_overlay.get_dict_by_media(media_id)
                        media_file = "" if media_prop.get("file") is None else media_prop.get("file")
                        image_folder = self.media.get_media_folder(self.get_collection_id(), self.get_episode_id(), media_id)
                        self.qt_show_image(image_folder, media_file)
                    case "video":
                        self.main_window.label_img.setText("当前媒体是视频，无预览")
                    case "three":
                        self.main_window.label_img.setText("当前媒体是模型，无预览")
                    case "text":
                        if media_data.get("show_type") == "screen":
                            media_prop = self._media_2d_text.get_dict_by_media(media_id)
                        else:
                            media_prop = self._media_3d_text.get_dict_by_media(media_id)
                        media_file = "" if media_prop.get("file") is None else media_prop.get("file")
                        self.main_window.label_img.setText(media_file)
                    case "bgm":
                        self.main_window.label_img.setText("当前媒体是音频，无预览")
                    case _:
                        self.main_window.label_img.setText("当前媒体为空")
        else:
            self.main_window.label_img.setText("当前未选择媒体")

    def qt_show_image(self, image_folder: str, media_file: str):
        media_path = os.path.join(image_folder, media_file)
        if os.path.isfile(media_path):
            pixmap = QPixmap(media_path).scaled(self.main_window.label_img.size(), aspectMode=Qt.KeepAspectRatio)
            self.main_window.label_img.setPixmap(pixmap)
            self.main_window.label_img.repaint()
        else:
            self.main_window.label_img.setText("文件" + media_file + "不存在")

    def play_with_medias(self):
        collection_data = self._collection.get_dict_by_id(self.get_collection_id())
        episode_data = self._episode.get_dict_by_id(self.get_episode_id())
        collection_data.update({"episodes": [episode_data]})
        subtitle_data = self._subtitle.get_dict_by_id(self.get_subtitle_id())
        episode_data.update({"subtitles": [subtitle_data]})

        subtitle_action = self._subtitle_action.get_dict_by_subtitle_id(subtitle_data.get("id"))
        media_data_list = self.generate_medias_data(collection_data.get("name"), episode_data.get("name"))
        subtitle_data.update({"subtitle_action": subtitle_action, "medias": media_data_list})
        subtitle_data.update({"medias": media_data_list})
        data_to_run = [collection_data]
        self.play.is_medias = True
        self.play.data = data_to_run
        self.play.start()

    def generate_medias_data(self, collection_name: str, episode_name: str, subtitle_id=None):
        media_server = self._setting.get_media_server()
        if subtitle_id:
            media_data_list = self._media.get_dict_list_by_subtitle(subtitle_id)
        else:
            media_data_list = self._media.get_dict_list_by_ids(self.get_media_ids())
        for media_data in media_data_list:
            file_url = media_server +  "/" + collection_name + "/" + episode_name + "/" \
                       + media_data.get("show_type") + "/" + media_data.get("media_type") + "/"

            media_2d_text = self._media_2d_text.get_dict_by_media(media_data.get("id"))
            media_2d_image = self._media_2d_image.get_dict_by_media(media_data.get("id"))
            media_2d_video = self._media_2d_video.get_dict_by_media(media_data.get("id"))
            media_2d_bgm = self._media_2d_bgm.get_dict_by_media(media_data.get("id"))

            media_3d_text = self._media_3d_text.get_dict_by_media(media_data.get("id"))
            media_3d_image = self._media_3d_image.get_dict_by_media(media_data.get("id"))
            media_3d_video = self._media_3d_video.get_dict_by_media(media_data.get("id"))

            media_3d_kml = self._media_3d_kml.get_dict_by_media(media_data.get("id"))
            media_3d_motion_line = self._media_3d_motion_line.get_dict_by_media(media_data.get("id"))
            media_3d_overlay = self._media_3d_overlay.get_dict_by_media(media_data.get("id"))

            media_2d_image.update({"file": file_url + media_2d_image.get("file")})
            media_2d_video.update({"file": file_url + media_2d_video.get("file")})

            media_3d_image.update({"file": file_url + media_3d_image.get("file")})
            media_3d_video.update({"file": file_url + media_3d_video.get("file")})

            media_3d_kml.update({"file": file_url + media_3d_kml.get("file")})
            media_3d_motion_line.update({"file": file_url + media_3d_motion_line.get("file")})
            # media_3d_overlay.update({"file": file_url + media_3d_overlay.get("file")})

            media_data.update({
                "subtitle_time": self._subtitle.get_dict_by_id(media_data.get("subtitle_id")).get("audio_time"),

                "media_2d_text": media_2d_text,
                "media_2d_image": media_2d_image,
                "media_2d_video": media_2d_video,
                "media_2d_bgm": media_2d_bgm,

                "media_3d_text": media_3d_text,
                "media_3d_image": media_3d_image,
                "media_3d_video": media_3d_video,
                "media_3d_kml": media_3d_kml,
                "media_3d_motion_line": media_3d_motion_line,
                "media_3d_overlay": media_3d_overlay
            })
        return media_data_list

    def media_move_up(self):
        current_row_number = hiworker.TableRead.get_current_row_number(self.table_media)
        if current_row_number > 0:
            media_id = self.get_media_id()

            media_sort = hiworker.TableRead.get_current_data_id(self.table_media)
            up_media_sort = hiworker.TableRead.get_row_item_data(self.table_media, current_row_number - 1, 0)
            up_media_id = self.get_media_id(int(up_media_sort))

            self._media.update({"id": media_id, "sort": int(media_sort) - 1})
            self._media.update({"id": up_media_id, "sort": int(up_media_sort) + 1})
            self.load_media_table()

    def media_move_down(self):
        current_row_number = hiworker.TableRead.get_current_row_number(self.table_media)
        if current_row_number < self.table_media.rowCount() - 1:
            media_id = self.get_media_id()

            media_sort = hiworker.TableRead.get_current_data_id(self.table_media)
            up_media_sort = hiworker.TableRead.get_row_item_data(self.table_media, current_row_number + 1, 0)
            up_media_id = self.get_media_id(int(up_media_sort))

            self._media.update({"id": media_id, "sort": int(media_sort) + 1})
            self._media.update({"id": up_media_id, "sort": int(up_media_sort) - 1})
            self.load_media_table()

    # 按键功能
    @staticmethod
    def open_earth():
        Thread(target=earth_driver.open_web_page, args=()).start()

    def init_earth(self):
        js_server = self._setting.get_js_server()
        media_server = self._setting.get_media_server()
        font_server = self._setting.get_font_server()
        cesium_base_url = self._setting.get_cesium_base_url()
        Thread(target=earth_driver.init_earth, args=(js_server, media_server, font_server, cesium_base_url)).start()

    @staticmethod
    def hide_earth_ui():
        Thread(target=earth_driver.hide_earth_ui, args=()).start()

    @staticmethod
    def show_earth_ui():
        Thread(target=earth_driver.show_earth_ui, args=()).start()

    @staticmethod
    def change_stree_view():
        Thread(target=earth_driver.show_street_view, args=()).start()

    @staticmethod
    def set_2d_view():
        Thread(target=earth_driver.set_2d_view, args=()).start()

    @staticmethod
    def set_3d_view():
        Thread(target=earth_driver.set_3d_view, args=()).start()

    @staticmethod
    def clear_result():
        Thread(target=earth_driver.clear_all_data, args=()).start()

    @staticmethod
    def close_search():
        Thread(target=earth_driver.close_current_search, args=()).start()

    @staticmethod
    def fly_to_space():
        Thread(target=earth_driver.zoom_to_space, args=()).start()

    @staticmethod
    def set_north():
        Thread(target=earth_driver.set_compass_heading_reset, args=()).start()

    def fly_to_place_or_lla(self):
        place = self.main_window.lineEdit_fly_to_place_or_lla.text()
        Thread(target=earth_driver.search_place, args=(place, )).start()

    @staticmethod
    def set_fullscreen():
        if not earth_driver.driver:
            print("浏览器未打开")
        else:
            earth_driver.driver.fullscreen()

    @staticmethod
    def close_current_search():
        Thread(target=earth_driver.close_current_search, args=()).start()

    @staticmethod
    def download_nasa_data():
        Thread(target=earth_driver.download_nasa_data, args=()).start()

    @staticmethod
    def open_nasa_page():
        Thread(target=earth_driver.open_nasa_page, args=()).start()
