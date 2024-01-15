import os.path

import keyboard
from .signal import presenter_signal
from ..static import *
from ..views import *
from ..utils import *
from ..models import *
from ..web_driver import earth_driver
from PIL import Image


class MediaPresenter:
    def __init__(self):
        view_sender.media.save.connect(self.save)
        view_sender.media.save_2d_text.connect(self.update_2d_text)
        view_sender.media.save_2d_image.connect(self.update_2d_image)
        view_sender.media.save_2d_video.connect(self.update_2d_video)
        view_sender.media.save_2d_bgm.connect(self.update_2d_bgm)

        view_sender.media.save_3d_text.connect(self.update_3d_text)
        view_sender.media.save_3d_image.connect(self.update_3d_image)
        view_sender.media.save_3d_video.connect(self.update_3d_video)
        view_sender.media.save_3d_kml.connect(self.update_3d_kml)
        view_sender.media.save_3d_motion_line.connect(self.update_3d_motion_line)
        view_sender.media.save_3d_overlay.connect(self.update_3d_overlay)

        view_sender.media.get_position_text.connect(self.get_earth_coordination_text)
        view_sender.media.get_position_image.connect(self.get_earth_coordination_image)
        view_sender.media.get_position_video.connect(self.get_earth_coordination_video)

        view_sender.media.get_position_ground_overlay_1.connect(self.get_earth_overlay_coordination_1)
        view_sender.media.get_position_ground_overlay_2.connect(self.get_earth_overlay_coordination_2)
        view_sender.media.get_position_ground_overlay_3.connect(self.get_earth_overlay_coordination_3)
        view_sender.media.get_position_ground_overlay_4.connect(self.get_earth_overlay_coordination_4)
        view_sender.media.get_position_ground.connect(self.get_earth_overlay_coordination_0)

        self._view = MediaView()
        self._view_2d_text = MediaScreenView("text")
        self._view_2d_image = MediaScreenView("image")
        self._view_2d_video = MediaScreenView("video")
        self._view_2d_bgm = MediaBgmView()

        self._view_3d_text = MediaThreeView("text")
        self._view_3d_image = MediaThreeView("image")
        self._view_3d_video = MediaThreeView("video")

        self._view_3d_kml = MediaThreeKmlView()
        self._view_3d_motion_line = MediaThreeMotionLineView()
        self._view_3d_overlay = MediaThreeOverlayView()

        self.menu = MediaMenu()

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

        self._media_3d_overlay = Media3dOverlayModel()
        self._media_3d_kml = Media3dKmlModel()
        self._media_3d_motion_line = Media3dMotionLineModel()

    def save(self, data: dict):
        if data.get("id"):
            self.update(data)
        else:
            self.add(data)

    def add(self, data: dict):

        subtitle_data = self._subtitle.get_dict_by_id(data.get("subtitle_id"))
        subtitle_content = subtitle_data.get("name")
        data.update({"subtitle": subtitle_content})
        self._media.add(data)
        data = self._media.get_dict_list_by_subtitle(data.get("subtitle_id"))
        view_sender.main.load_table_media.emit(data, header_media)

    def update(self, data: dict):
        self._media.update(data)
        data_list = self._media.get_dict_list_by_subtitle(data.get("subtitle_id"))
        view_sender.main.load_table_media.emit(data_list, header_media)

    def update_2d_text(self, data: dict):
        self._media_2d_text.update(data)
        presenter_signal.load_table_media_sub.emit()

    def update_2d_image(self, data: dict):
        self._media_2d_image.update(self.set_data_to_save(data))
        presenter_signal.load_table_media_sub.emit()

    def update_2d_video(self, data: dict):
        self._media_2d_video.update(self.set_data_to_save(data))
        presenter_signal.load_table_media_sub.emit()

    def update_2d_bgm(self, data: dict):
        self._media_2d_bgm.update(self.set_data_to_save(data))
        presenter_signal.load_table_media_sub.emit()

    def update_3d_text(self, data: dict):
        self._media_3d_text.update(data)
        presenter_signal.load_table_media_sub.emit()

    def update_3d_image(self, data: dict):
        self._media_3d_image.update(self.set_data_to_save(data))
        presenter_signal.load_table_media_sub.emit()

    def update_3d_video(self, data: dict):
        self._media_3d_video.update(self.set_data_to_save(data))
        presenter_signal.load_table_media_sub.emit()

    def update_3d_kml(self, data: dict):
        self._media_3d_kml.update(self.set_data_to_save(data))
        presenter_signal.load_table_media_sub.emit()

    def update_3d_motion_line(self, data: dict):
        self._media_3d_motion_line.update(self.set_data_to_save(data))
        presenter_signal.load_table_media_sub.emit()

    def update_3d_overlay(self, data: dict):
        self._media_3d_overlay.update(self.set_data_to_save(data))
        presenter_signal.load_table_media_sub.emit()

    def set_data_to_save(self, data):
        media_data = self._media.get_dict_by_id(data.get("media_id"))
        subtitle_id = media_data.get("subtitle_id")
        subtitle_data = self._subtitle.get_dict_by_id(subtitle_id)

        episode_id = subtitle_data.get("episode_id")
        episode_data = self._episode.get_dict_by_id(episode_id)
        episode_name = episode_data.get("name")

        collection_id = episode_data.get("collection_id")
        collection_data = self._collection.get_dict_by_id(collection_id)
        collection_name = collection_data.get("name")

        media_folder = os.path.join(os.getcwd(),
                                    "data",
                                    "media",
                                    collection_name,
                                    episode_name,
                                    media_data.get("show_type"),
                                    media_data.get("media_type"))
        if not os.path.exists(media_folder):
            os.makedirs(media_folder, exist_ok=True)

        source_file = data.get("file")
        media_name = media_data.get("name") if media_data.get("name") else ""
        new_file_name = create_new_file_name(source_file, media_name, data.get("id"))
        target_file = os.path.join(media_folder, new_file_name)
        copy_file(source_file, target_file)

        if media_data.get("media_type") == "image":
            if os.path.isfile(target_file):
                img = Image.open(target_file)
                aspect = img.width / img.height
                data.update({"aspect": aspect})
        data.update({"file": new_file_name})
        return data

    def delete(self, media_id: int):
        media_data = self._media.get_dict_by_id(media_id)
        self._media.delete(media_id)
        data = self._media.get_dict_list_by_subtitle(media_data.get("subtitle_id"))
        view_sender.main.load_table_media.emit(data, header_media)

    def show_add(self, subtitle_id: int):
        self._view.show_add(subtitle_id, media_type_preset)

    def show_edit(self, media_id: int):
        if media_id:
            data = self._media.get_dict_by_id(media_id)
            self._view.show_edit(data, media_type_preset)

    def show_prop_edit(self, media_id: int):
        if media_id:
            data = self._media.get_dict_by_id(media_id)
            match data.get("show_type"):
                case "screen":
                    match data.get("media_type"):
                        case "text":
                            self._view_2d_text.show_edit(self._media_2d_text.get_dict_by_media(media_id), get_font_list(), get_font_color())
                        case "image":
                            self._view_2d_image.show_edit(self._media_2d_image.get_dict_by_media(media_id), get_font_list(), get_font_color())
                        case "video":
                            self._view_2d_video.show_edit(self._media_2d_video.get_dict_by_media(media_id), get_font_list(), get_font_color())
                        case "bgm":
                            self._view_2d_bgm.show_edit(self._media_2d_bgm.get_dict_by_media(media_id))
                case "three":
                    match data.get("media_type"):
                        case "text":
                            self._view_3d_text.show_edit(self._media_3d_text.get_dict_by_media(media_id), get_font_list(), get_font_color())
                        case "image":
                            self._view_3d_image.show_edit(self._media_3d_image.get_dict_by_media(media_id), get_font_list(), get_font_color())
                        case "video":
                            self._view_3d_video.show_edit(self._media_3d_video.get_dict_by_media(media_id), get_font_list(), get_font_color())
                        case "kml":
                            self._view_3d_kml.show_edit(self._media_3d_kml.get_dict_by_media(media_id))
                        case "overlay":
                            self._view_3d_overlay.show_edit(self._media_3d_overlay.get_dict_by_media(media_id))
                        case "motion_line":
                            self._view_3d_motion_line.show_edit(self._media_3d_motion_line.get_dict_by_media(media_id), get_font_color())

    def open_media_in_media_list(self, collection_id: int, episode_id: int, media_id: int):
        media_folder = self.get_media_folder(collection_id, episode_id, media_id)
        if media_folder:
            if not os.path.exists(media_folder):
                os.makedirs(media_folder, exist_ok=True)
            os.startfile(media_folder)
        else:
            print("文件路径为空.")

    def get_media_folder(self, collection_id, episode_id, media_id):
        collection_name = self._collection.get_dict_by_id(collection_id).get("name")
        episode_name = self._episode.get_dict_by_id(episode_id).get("name")
        media_data = self._media.get_dict_by_id(media_id)
        show_type = media_data.get("show_type")
        media_type = media_data.get("media_type")
        if collection_name and episode_name and media_type:
            return os.path.join(os.getcwd(), "data", "media", collection_name, episode_name, show_type, media_type)
        else:
            return ""

    def get_earth_coordination_text(self):
        Thread(target=self.get_earth_coordination_f, args=("text",)).start()

    def get_earth_coordination_image(self):
        Thread(target=self.get_earth_coordination_f, args=("image",)).start()

    def get_earth_coordination_video(self):
        Thread(target=self.get_earth_coordination_f, args=("video", )).start()

    def get_earth_coordination_f(self, media_type: str):
        keyboard.wait("1")
        camera_position = earth_driver.get_camera_position()
        if camera_position:
            longitude, latitude, altitude, camera_altitude, status = parse_coord(camera_position)
            if status:
                match media_type:
                    case "text":
                        self._view_3d_text.lineEdit_media_longitude.setText(str(longitude))
                        self._view_3d_text.lineEdit_media_latitude.setText(str(latitude))
                        self._view_3d_text.lineEdit_media_altitude.setText(str(altitude))
                    case "image":
                        self._view_3d_image.lineEdit_media_longitude.setText(str(longitude))
                        self._view_3d_image.lineEdit_media_latitude.setText(str(latitude))
                        self._view_3d_image.lineEdit_media_altitude.setText(str(altitude))
                    case "video":
                        self._view_3d_video.lineEdit_media_longitude.setText(str(longitude))
                        self._view_3d_video.lineEdit_media_latitude.setText(str(latitude))
                        self._view_3d_video.lineEdit_media_altitude.setText(str(altitude))

    def get_earth_overlay_coordination_0(self):
        Thread(target=self.get_earth_overlay_coordination_f, args=(0,)).start()

    def get_earth_overlay_coordination_1(self):
        Thread(target=self.get_earth_overlay_coordination_f, args=(1,)).start()

    def get_earth_overlay_coordination_2(self):
        Thread(target=self.get_earth_overlay_coordination_f, args=(2,)).start()

    def get_earth_overlay_coordination_3(self):
        Thread(target=self.get_earth_overlay_coordination_f, args=(3,)).start()

    def get_earth_overlay_coordination_4(self):
        Thread(target=self.get_earth_overlay_coordination_f, args=(4,)).start()

    def get_earth_overlay_coordination_f(self, coord_n=0):
        if coord_n == 1 or coord_n == 0:
            keyboard.wait("1")
            camera_position = earth_driver.get_camera_position()
            longitude, latitude, altitude, camera_altitude, status = parse_coord(camera_position)
            if status:
                self._view_3d_overlay.lineEdit_media_ground_overlay_lon_1.setText(str(longitude))
                self._view_3d_overlay.lineEdit_media_ground_overlay_lat_1.setText(str(latitude))

        if coord_n == 2 or coord_n == 0:
            keyboard.wait("1")
            camera_position = earth_driver.get_camera_position()
            longitude, latitude, altitude, camera_altitude, status = parse_coord(camera_position)
            if status:
                self._view_3d_overlay.lineEdit_media_ground_overlay_lon_2.setText(str(longitude))
                self._view_3d_overlay.lineEdit_media_ground_overlay_lat_2.setText(str(latitude))

        if coord_n == 3 or coord_n == 0:
            keyboard.wait("1")
            camera_position = earth_driver.get_camera_position()
            longitude, latitude, altitude, camera_altitude, status = parse_coord(camera_position)
            if status:
                self._view_3d_overlay.lineEdit_media_ground_overlay_lon_3.setText(str(longitude))
                self._view_3d_overlay.lineEdit_media_ground_overlay_lat_3.setText(str(latitude))

        if coord_n == 4 or coord_n == 0:
            keyboard.wait("1")
            camera_position = earth_driver.get_camera_position()
            longitude, latitude, altitude, camera_altitude, status = parse_coord(camera_position)
            if status:
                self._view_3d_overlay.lineEdit_media_ground_overlay_lon_4.setText(str(longitude))
                self._view_3d_overlay.lineEdit_media_ground_overlay_lat_4.setText(str(latitude))

    def show_menu(self):
        self.menu.show_menu()
