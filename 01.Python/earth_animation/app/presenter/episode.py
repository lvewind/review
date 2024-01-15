import re
import os
import xlwings as xw

from .signal import presenter_signal
from .speech import speech
from .message import message

from ..static import header_episode

from ..views import *
from ..utils import get_wav_time, dict_sort
from ..models import EpisodeModel, SubtitleModel, CollectionModel, MediaModel


class EpisodePresenter:
    def __init__(self):
        view_sender.episode.save.connect(self.save)
        self._view = EpisodeView()
        self.menu = EpisodeMenu()
        self._collection = CollectionModel()
        self._episode = EpisodeModel()
        self._subtitle = SubtitleModel()
        self._media = MediaModel()

    def save(self, data: dict):
        if data.get("id"):
            self.update(data)
        else:
            self.add(data)

    def add(self, data: dict):
        self._episode.add(data)
        data = self._episode.get_all_data()
        view_sender.main.load_table_collection.emit(data, header_episode)

    def update(self, data: dict):
        self._episode.update(data)
        new_data = self._episode.get_all_data()
        view_sender.main.load_table_episode.emit(new_data, header_episode)

    def delete(self, episode_id: int):
        self._episode.delete(episode_id)
        new_data = self._episode.get_all_data()
        view_sender.main.load_table_episode.emit(new_data, header_episode)

    def show_add(self, collection_id: int):
        self._view.show_add(collection_id)

    def show_edit(self, episode_id: int):
        if episode_id:
            data = self._episode.get_dict_by_id(episode_id)
            self._view.show_edit(data)

    def create_subtitle(self, episode_ids: list):
        message.show_message("开始生成字幕")
        for episode_id in episode_ids:
            if episode_id:
                episode_data = self._episode.get_dict_by_id(episode_id)
                content = episode_data.get("content")
                content_split = re.split(r'[;:，。；：？?！!\s]', content)
                old_subtitles = self._subtitle.get_dict_list_by_episode_id(episode_id)
                old_subtitles.sort(key=dict_sort)
                message.show_message("[ " + episode_data.get("content") + " ]")
                sort = 0
                for old_subtitle in old_subtitles:
                    sort = sort + 1
                    if "[blank]" in old_subtitle.get("name"):
                        self._subtitle.update({"id": old_subtitle.get("id"), "sort": sort})
                        continue
                    elif content_split:
                        tts_subtitle = content_split.pop(0)
                        self._subtitle.update({"id": old_subtitle.get("id"), "name": tts_subtitle, "episode_id": episode_id, "sort": sort})
                        message.show_message(str(sort) + "." + tts_subtitle)
                    else:
                        if not("[blank]" in old_subtitle.get("name")):
                            self._subtitle.delete(old_subtitle.get("id"))
                else:
                    if content_split:
                        for tts_subtitle in content_split:
                            sort = sort + 1
                            self._subtitle.add({"name": tts_subtitle, "episode_id": episode_id, "sort": sort})
                            message.show_message(str(sort) + "." + tts_subtitle)

        message.show_message("生成字幕结束")

    def import_places_from_excel(self, excel_path, collection_id):
        source_list = []
        try:
            wb = xw.Book(excel_path)
            sht_count = len(wb.sheets)
            for sht_n in range(sht_count):
                empty_lines = 0
                sht = wb.sheets[sht_n]
                for row in range(2, 999):
                    if empty_lines >= 10:
                        break
                    name = sht.range("A" + str(row)).value
                    content = sht.range("B" + str(row)).value

                    if not name:
                        empty_lines += 1
                    else:
                        empty_lines = 0
                        source_list.append({
                            "collection_id": collection_id,
                            "name": name,
                            "content": content
                        })
        except ValueError:
            pass
        if source_list:
            for place in source_list:
                self._episode.add(place)

    def create_speech(self, episode_ids):
        message.show_message("开始生成语音")
        episodes = self._episode.get_dict_list_by_ids(episode_ids)
        collection_id = episodes[0].get("collection_id")
        for episode_data in episodes:
            episode_name = episode_data.get("name")
            if not episode_name:
                continue
            else:
                collection_name = self._collection.get_dict_by_id(episode_data.get("collection_id")).get("name")
                wav_folder = os.path.join(os.getcwd(), "data", "media", collection_name, episode_name, "wav")
                if not os.path.exists(wav_folder):
                    os.makedirs(wav_folder, exist_ok=True)
                subtitles = self._subtitle.get_dict_list_by_episode_id(episode_data.get("id"))
                if not subtitles:
                    continue
                for subtitle_data in subtitles:
                    subtitle_content = subtitle_data.get("name")
                    if subtitle_content and not ("[blank]" in subtitle_content):
                        wav_file = subtitle_content + ".wav"
                        message.show_message("正在生成：" + wav_file)
                        file_name = os.path.join(wav_folder, wav_file)
                        speech.save_file_from_content(subtitle_content, file_name)
                        audio_time = get_wav_time(file_name)
                        subtitle_data.update({"audio_file": wav_file, "audio_time": audio_time})
                        self._subtitle.update(subtitle_data)
        message.show_message("语音生成完成")
        self.search_audio(collection_id, episode_ids)

    def search_audio(self, collection_id: int, episode_ids: list):

        collection_data = self._collection.get_dict_by_id(collection_id)
        collection_name = collection_data.get("name")
        episodes = self._episode.get_dict_list_by_ids(episode_ids)
        for episode_data in episodes:
            has_error = False
            wav_folder = os.path.join(os.getcwd(), "data", "media", collection_name, episode_data.get("name"), "wav")
            subtitles = self._subtitle.get_dict_list_by_episode_id(episode_data.get("id"))
            if subtitles:
                for subtitle_data in subtitles:
                    subtitle_content = subtitle_data.get("name")
                    if subtitle_content:
                        file_name = subtitle_content + ".wav"
                        audio_path = os.path.join(wav_folder, file_name)
                        audio_time = get_wav_time(audio_path)
                        if not audio_time:
                            file_name = ""
                            has_error = True
                        self._subtitle.update({"audio_file": file_name, "audio_time": audio_time, "id": subtitle_data.get("id")})
            if has_error:
                speech_audio_synchronize = 0
            else:
                speech_audio_synchronize = 1
            self._episode.update({"speech_audio_synchronize": speech_audio_synchronize, "id": episode_data.get("id")})
        presenter_signal.load_table_episode.emit()
        presenter_signal.load_table_subtitle.emit()

    def search_media(self, episode_ids):
        for episode_id in episode_ids:
            subtitles = self._subtitle.get_dict_list_by_episode_id(episode_id)
            print(subtitles)
            if subtitles:
                medias = self._media.get_dict_list_by_episode(episode_id)
                if medias:
                    for subtitle_data in subtitles:
                        subtitle_name = subtitle_data.get("name")
                        media_count = 0
                        for media_data in medias:
                            media_subtitle = media_data.get("subtitle")
                            if subtitle_name == media_subtitle:
                                media_data.update({"subtitle_id": subtitle_data.get("id")})
                                self._media.update(media_data)
                                media_count += 1
                        subtitle_data.update({"media_count": media_count})
                        self._subtitle.update(subtitle_data)

    def show_menu(self):
        self.menu.show_menu()
