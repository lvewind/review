import time
import os
from threading import Thread

import pydub
from pydub import AudioSegment
from pydub.playback import play as play_wav

import win32api
import win32con

from ..web_driver import earth_driver
from ..static.web_config import WebConfig
from ..utils import generate_overlay_kml
import hiworker


class Play(hiworker.Win32Click, hiworker.Thread):
    def __init__(self, window_title, source_screen_x=2560, source_screen_y=1440, screen_offset_x=0, screen_offset_y=0):
        super(hiworker.Win32Click, self).__init__()
        super(hiworker.Thread, self).__init__()
        super().__init__()
        super().set_data(window_title, hiworker.data.Coordinate())

        self.screen_action = hiworker.Win32Click()
        self.screen_action.set_data(window_title, hiworker.data.Coordinate())
        self.screen_action.set_handle_option(correction_window=False)
        self.data = []
        self.source_screen_x = source_screen_x
        self.source_screen_y = source_screen_y
        self.screen_offset_x = screen_offset_x
        self.screen_offset_y = screen_offset_y
        self.is_medias = False

    def run(self):
        self.stop_flag = False
        earth_driver.hide_earth_ui()
        while not self.stop_flag:
            for collection in self.data:
                if self.stop_flag:
                    break
                episodes = collection.get("episodes")
                for episode in episodes:
                    if self.stop_flag:
                        break
                    subtitles = episode.get("subtitles")
                    for subtitle in subtitles:
                        if self.stop_flag:
                            break
                        if not self.is_medias:
                            if episode.get("display_subtitles"):
                                self.show_subtitle(subtitle)
                            self.play_subtitle_action(subtitle.get("subtitle_action"))

                            self.play_wav(
                                os.path.join(
                                    collection.get("name"),
                                    episode.get("name"),
                                    "wav",
                                    subtitle.get("audio_file")
                                ))
                        self.play_medias(subtitle.get("medias"), collection.get("name"), episode.get("name"))

                        audio_time = 0 if subtitle.get("audio_time") is None else subtitle.get("audio_time")
                        ext_time = 0 if subtitle.get("ext_time") is None else subtitle.get("ext_time")
                        total_time = audio_time + ext_time
                        while total_time > 0:
                            if self.stop_flag:
                                break
                            time.sleep(0.1)
                            total_time -= 0.1
                    else:
                        self.clear_subtitle()
            else:
                self.stop_flag = True
        if not self.is_medias:
            earth_driver.clear_all_data()

    @staticmethod
    def show_subtitle(subtitle: dict):
        earth_driver.display_subtitle(subtitle)

    @staticmethod
    def clear_subtitle():
        earth_driver.clear_subtitle()

    def run_medias(self, medias: list):
        Thread(target=self.play_medias, args=(medias,)).start()

    def play_medias(self, medias: list, collection_name: str, episode_name: str):
        for media in medias:
            if self.stop_flag:
                break
            if media:
                match media.get("show_type"):
                    case "screen":
                        match media.get("media_type"):
                            case "bgm":
                                media_prop = media.get("media_2d_bgm")
                                bgm_name = media_prop.get("file")
                                if bgm_name:
                                    bgm_path = os.path.join(os.getcwd(), "data", "media",
                                                            collection_name,
                                                            episode_name,
                                                            media.get("show_type"),
                                                            media.get("media_type"),
                                                            bgm_name)
                                    self.play_bgm(bgm_path)
                            case "image":
                                earth_driver.display_screen_image(media, media.get("media_2d_image"))
                            case "text":
                                earth_driver.display_screen_text(media, media.get("media_2d_text"))
                            case "video":
                                earth_driver.display_screen_video(media, media.get("media_2d_video"))
                    case "three":
                        match media.get("media_type"):
                            case "text":
                                earth_driver.display_three_text(media, media.get("media_3d_text"))
                            case "image":
                                earth_driver.display_three_image(media, media.get("media_3d_image"))
                            case "video":
                                earth_driver.display_three_video(media, media.get("media_3d_video"))
                            case "kml":
                                earth_driver.display_three_kml(media, media.get("media_3d_kml"))
                            case "motion_line":
                                data_prop = media.get("media_3d_motion_line")
                                data_prop.update({"coordinate_list": [[109.397767184478, 24.30205786783928, 90.73627912468048],
                                                                      [109.4012655382333, 24.30330351308625, 92.3569928125534],
                                                                      [109.402094027743, 24.30686673197053, 90.25504342137668]]})
                                earth_driver.display_three_motion_line(media, data_prop)
                            case "model":
                                earth_driver.display_three_model(media, media.get("media_3d_text"))
                            case "overlay":
                                media_data = media.get("media_3d_overlay")
                                overlay_kml_url = generate_overlay_kml(media_data, collection_name, episode_name, WebConfig.earth_media)
                                media_data.update({"file": overlay_kml_url})
                                earth_driver.display_three_overlay(media, media.get("media_3d_overlay"))

    @staticmethod
    def play_bgm(bgm_path: str):
        try:
            bgm = AudioSegment.from_wav(bgm_path)
            Thread(target=play_wav, args=(bgm,)).start()
        except pydub.exceptions.CouldntDecodeError:
            print("BGM解码错误：" + bgm_path)
        except FileNotFoundError:
            pass

    @staticmethod
    def play_wav(wav_path: str):
        wav_path = os.path.join(os.getcwd(), "data", "media", wav_path)
        try:
            wav = AudioSegment.from_wav(wav_path)
            wav_time = wav.duration_seconds
            if wav_time > 1:
                wav = wav[:-500]
                if wav and (wav_time > 0):
                    Thread(target=play_wav, args=(wav,)).start()
        except pydub.exceptions.CouldntDecodeError:
            print("跳过语音：" + wav_path)
        except FileNotFoundError:
            print("语音不存在:", wav_path)

    def play_subtitle_action(self, subtitle):
        start_x = subtitle.get("start_x")
        start_y = subtitle.get("start_y")
        end_x = subtitle.get("end_x")
        end_y = subtitle.get("end_y")
        if start_x and start_y and end_x and end_y:
            screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
            screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
            start_x = int(start_x * screen_x / self.source_screen_x)
            start_y = int(start_y * screen_y / self.source_screen_y)
            self.screen_action.slide_speed = subtitle.get("slide_speed")
            fly_type = subtitle.get("fly_type")
            action_type = subtitle.get("fly_type")
            match action_type:
                case "screen_move":
                    Thread(target=self.screen_action.drag_a_to_b,
                           args=(start_x, start_y, end_x, end_y, "left",)).start()
                case "screen_heading_tilt":
                    Thread(target=self.screen_action.drag_a_to_b,
                           args=(start_x, start_y, end_x, end_y, "middle",)).start()
                case "close_search_result":
                    Thread(target=earth_driver.close_current_search, args=()).start()
                case "clear_all_data":
                    delay = subtitle.get("ext_time", 0)
                    Thread(target=earth_driver.clear_all_data, args=(delay,)).start()
                case _:
                    zoom_times = subtitle.get("zoom_times")
                    screen_x = self.screen_offset_x + start_x
                    screen_y = self.screen_offset_y + start_y
                    if subtitle.get("fly_type") == "screen_zoom_in":
                        Thread(target=self.screen_action.send_mouse_zoom,
                               args=(screen_x, screen_y, zoom_times, True)).start()
                    elif subtitle.get("fly_type") == "screen_zoom_out":
                        Thread(target=self.screen_action.send_mouse_zoom,
                               args=(screen_x, screen_y, zoom_times, False)).start()
