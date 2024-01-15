from PySide6.QtCore import QObject, Signal


class PresenterSignal(QObject):
    load_table_collection = Signal()
    load_table_episode = Signal()
    load_table_subtitle = Signal()
    load_table_subtitle_sub = Signal()
    load_table_media = Signal()
    load_table_media_sub = Signal()


presenter_signal = PresenterSignal()
