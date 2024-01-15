from .sender import *


class ViewSender:
    def __init__(self):
        self.collection = CollectionSender()
        self.episode = EpisodeSender()
        self.main = MainSender()
        self.media = MediaSender()
        self.setting = SettingSender()
        self.subtitle = SubtitleSender()
        self.subtitle_action = SubtitleActionSender()
        self.tts = TTSSender()


view_sender = ViewSender()


__all__ = [
    "view_sender"
]
