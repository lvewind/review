from PySide6.QtCore import QObject, Signal


class Sender(QObject):
    save = Signal(dict)
    delete = Signal(int)


class CollectionSender(Sender):
    pass


class EpisodeSender(Sender):
    create_subtitle = Signal(dict)
    move_episode = Signal(dict)


class SubtitleSender(Sender):
    set_font_batch = Signal(dict, list)
    set_speech_batch = Signal(dict, list)


class SubtitleActionSender(Sender):
    pass


class MediaSender(Sender):
    set_font_batch = Signal(dict, list)
    set_media_size_batch = Signal(dict, list)
    move_to_subtitle = Signal(dict)

    save_2d_text = Signal(dict)
    save_2d_image = Signal(dict)
    save_2d_video = Signal(dict)
    save_2d_bgm = Signal(dict)

    save_3d_text = Signal(dict)
    save_3d_image = Signal(dict)
    save_3d_video = Signal(dict)

    save_3d_kml = Signal(dict)
    save_3d_overlay = Signal(dict)
    save_3d_motion_line = Signal(dict)

    get_position_text = Signal()
    get_position_image = Signal()
    get_position_video = Signal()
    get_position_ground_overlay_1 = Signal()
    get_position_ground_overlay_2 = Signal()
    get_position_ground_overlay_3 = Signal()
    get_position_ground_overlay_4 = Signal()
    get_position_ground = Signal()


class SettingSender(Sender):
    pass


class TTSSender(Sender):
    generate_speech = Signal(dict)
    refresh_voice_list = Signal(dict)
    post_voice_list = Signal(dict)
    post_message = Signal(str)


class MainSender(Sender):
    open_earth = Signal()
    init_earth = Signal()

    hide_ui = Signal()
    show_ui = Signal()

    toggle_street_view = Signal()
    set_north = Signal()

    clear_earth = Signal()
    close_search = Signal()

    fly_to_space = Signal()

    set_2d_view = Signal()
    set_3d_view = Signal()

    open_tts = Signal()
    open_setting = Signal()
    open_about = Signal()
    open_manual = Signal()

    open_nasa = Signal()
    download_nasa = Signal()
    update_voices = Signal()

    load_table_collection = Signal(dict, dict)
    load_table_episode = Signal(dict, dict)
    load_table_subtitle = Signal(dict, dict)
    load_table_media = Signal(dict, dict)

    load_table_subtitle_sub = Signal(dict, dict)
    load_table_media_sub = Signal(dict, dict)

    fly_to_place_or_lla = Signal()
