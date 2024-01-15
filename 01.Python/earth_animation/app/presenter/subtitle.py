import keyboard

import win32api

from app.web_driver.web_driver import earth_driver
from .speech import speech
from .signal import presenter_signal

from ..utils import *
from ..views import *
from ..static import *
from ..models import *


class SubtitlePresenter:
    def __init__(self):
        self._view = SubtitleView()
        self._view_subtitle_action = SubtitleActionView()
        self._view_set_font = SubtitleSetFontsView()
        self._view_set_voice = SubtitleSetVoicesView()

        self.menu = SubtitleMenu()
        self._collection = CollectionModel()
        self._episode = EpisodeModel()
        self._media = MediaModel()
        self._subtitle = SubtitleModel()
        self._subtitle_action = SubtitleActionModel()
        self._setting = SettingModel()

        self.voices = load_voice_list_from_json(self._setting.get_azure_key())

        view_sender.subtitle.save.connect(self.save)
        view_sender.subtitle_action.save.connect(self.update_action)
        view_sender.subtitle.set_font_batch.connect(self.set_subtitle_batch)
        view_sender.subtitle.set_speech_batch.connect(self.set_subtitle_batch)

        view_sender.subtitle_action.save.connect(self.update_action)

    def save(self, data):
        if data.get("id"):
            self.update(data)
        else:
            self.add(data)

    def update_action(self, data):
        self._subtitle_action.update(data)
        view_sender.main.load_table_subtitle_sub.emit(data, header_subtitles_sub)

    def add(self, data):
        self._subtitle.add(data)
        data = self._subtitle.get_dict_list_by_episode_id(data.get("episode_id"))
        view_sender.main.load_table_subtitle.emit(data, header_subtitle)

    def update(self, data):
        self._subtitle.update(data)
        data = self._subtitle.get_dict_list_by_episode_id(data.get("episode_id"))
        view_sender.main.load_table_subtitle.emit(data, header_subtitle)

    def show_add(self):
        pass

    def show_edit(self, subtitle_id: int):
        if subtitle_id:
            data = self._subtitle.get_dict_by_id(subtitle_id)
            self._view.show_edit(data, self.voices, get_font_list(), get_font_color())

    def show_edit_action(self, subtitle_id):
        if subtitle_id:
            data = self._subtitle_action.get_dict_by_subtitle_id(subtitle_id)
            self._view_subtitle_action.show_edit(data, fly_type)

    def show_set_fonts(self, subtitle_ids):
        self._view_set_font.show_edit(subtitle_ids, get_font_list(), get_font_color())

    def show_set_voice(self, subtitle_ids):
        self._view_set_voice.show_edit(subtitle_ids, self.voices)

    def set_subtitle_batch(self, data: dict, subtitle_ids: list):
        if subtitle_ids:
            episode_id = self._subtitle.get_dict_by_id(subtitle_ids[0])
            episode_id = episode_id.get("episode_id")
            for subtitle_id in subtitle_ids:
                data.update({"id": subtitle_id})
                self._subtitle.update(data)
            data = self._subtitle.get_dict_list_by_episode_id(episode_id)
            view_sender.main.load_table_subtitle.emit(data, header_subtitle)

    # 获取语音时长
    def search_audio(self, subtitle_ids, episode_id, collection_id):
        if subtitle_ids:
            episode_name = self._episode.get_dict_by_id(episode_id).get("name")
            collection_name = self._collection.get_dict_by_id(collection_id).get("name")
            if episode_name and collection_name:
                subtitles = self._subtitle.get_dict_list_by_ids(subtitle_ids)
                speech_audio_synchronize = 1
                for subtitle_data in subtitles:
                    if subtitle_data:
                        if subtitle_data.get("is_empty"):
                            # 空字幕
                            self._subtitle.update({"audio_time": 0, "audio_file": "", "id": subtitle_data.get("id")})
                        else:
                            # 非空字幕
                            wav_folder = os.path.join(os.getcwd(), "data", "media", collection_name, episode_name, "wav")
                            if not os.path.exists(wav_folder):
                                os.makedirs(wav_folder, exist_ok=True)
                            wav_name = subtitle_data.get("audio_file", "")
                            if not wav_name:
                                wav_name = subtitle_data.get("name", "") + ".wav"
                            wav_path = os.path.join(wav_folder, wav_name)
                            audio_time = get_wav_time(wav_path)
                            if not audio_time:
                                speech_audio_synchronize = 0
                                wav_name = ""
                            self._subtitle.update({"audio_file": wav_name, "audio_time": audio_time, "id": subtitle_data.get("id")})
                presenter_signal.load_table_subtitle.emit()
                self._episode.update({"speech_audio_synchronize": speech_audio_synchronize, "id": episode_id})

    def sum_subtitle_total_time(self, episode_id):
        total_audio_time = 0
        total_run_time = 0
        subtitle_count = 0
        subtitles = self._subtitle.get_dict_list_by_episode_id(episode_id)
        if subtitles:
            for data in subtitles:
                audio_time = 0 if data.get("audio_time") is None else data.get("audio_time")
                ext_time = 0 if data.get("ext_time") is None else data.get("ext_time")
                total_audio_time += audio_time
                total_run_time += (audio_time + ext_time)
                subtitle_count += 1
            return round(total_audio_time, 2), round(total_run_time, 2)
        else:
            return 0, 0

    def open_media_folder(self, collection_id, episode_id):
        collection_name = self._collection.get_dict_by_id(collection_id).get("name")
        episode_name = self._episode.get_dict_by_id(episode_id).get("name")
        subtitle_folder = os.path.join(os.getcwd(), "data", "media", collection_name, episode_name)
        if not os.path.exists(subtitle_folder):
            os.makedirs(subtitle_folder, exist_ok=True)
        os.startfile(subtitle_folder)

    def update_audio_time(self):
        pass

    def create_speech_with_subtitle(self, subtitle_ids, collection_id, episode_id):
        print("开始生成语音")
        if subtitle_ids:
            collection_name = self._collection.get_dict_by_id(collection_id).get("name")
            episode_name = self._episode.get_dict_by_id(episode_id).get("name")
            wav_folder = os.path.join(os.getcwd(), "data", "media", collection_name, episode_name, "wav")
            if not os.path.exists(wav_folder):
                os.makedirs(wav_folder, exist_ok=True)
            for subtitle_id in subtitle_ids:
                subtitle_data = self._subtitle.get_dict_by_id(subtitle_id)
                subtitle_content = subtitle_data.get("name")
                if "[blank]" in subtitle_content:
                    continue
                file_name = os.path.join(wav_folder, subtitle_content + ".wav")

                speech.save_file_from_content(subtitle_content, file_name)

                subtitle_data.update({"audio_file": subtitle_content + ".wav"})
                self._subtitle.update(subtitle_data)
            else:
                print("语音生成完成")
                self.search_audio(subtitle_ids, episode_id, collection_id)
        else:
            print("未执行任何操作")

    def get_screen_coord(self):
        keyboard.wait("1")
        app_setting = self._setting.get_data()
        app_setting.read_setting()
        start_x, start_y = win32api.GetCursorPos()
        start_x = start_x - app_setting.screen_offset_x
        start_y = start_y - app_setting.screen_offset_y

        keyboard.wait("1")
        end_x, end_y = win32api.GetCursorPos()
        end_x = end_x - app_setting.screen_offset_x
        end_y = end_y - app_setting.screen_offset_y

    @staticmethod
    def get_camera_position():
        camera_position = earth_driver.get_camera_position()
        longitude, latitude, altitude, camera_altitude = parse_coord(camera_position)
        return {"longitude": longitude, "latitude": latitude, "altitude": altitude, "camera_altitude": camera_altitude}

    @staticmethod
    def get_heading_tilt():
        camera_state = earth_driver.get_camera_state()
        heading = str(camera_state.get("heading", ""))
        tilt = str(camera_state.get("tilt", ""))
        return {"heading": heading, "tilt": tilt}

    def show_menu(self):
        self.menu.show_menu()
