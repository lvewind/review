from sqlalchemy import select
from app.models.session import DBSession, Session
from app.models.alchemy_models import *


class MediaModel(DBSession):
    def __init__(self):
        pass

    def save(self, data: dict):
        if data.get("id"):
            self.update(data)
        else:
            self.add(data)

    def delete(self, media_id):
        if media_id:
            self._delete(Media, media_id)

    def add(self, data: dict):
        subtitle_id = data.get("subtitle_id")
        count = len(self.get_dict_list_by_subtitle(subtitle_id))

        media = Media(
            name=data.get("name"),
            subtitle_id=data.get("subtitle_id"),
            media_type=data.get("media_type"),
            show_type=data.get("show_type"),
            subtitle=data.get("subtitle"),
            sort=count + 1,

            media_2d_text=Media2dText(),
            media_2d_image=Media2dImage(),
            media_2d_video=Media2dVideo(),
            media_2d_bgm=Media2dBGM(),

            media_3d_text=Media3dText(),
            media_3d_image=Media3dImage(),
            media_3d_video=Media3dVideo(),

            media_3d_motion_line=Media3dMotionLine(),
            media_3d_overlay=Media3dOverlay(),
            media_3d_kml=Media3dKml()
        )
        self._add(media)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media, instance_id)
            for key, value in data.items():
                setattr(instance, key, value)

            session.commit()

    def get_dict_list_by_subtitle(self, subtitle_id):
        stmt = select(Media).where(Media.subtitle_id == subtitle_id)
        return self._get_dict_list_with_stmt(stmt)

    def get_dict_list_by_episode(self, episode_id):
        stmt = select(Media).where(Media.episode_id == episode_id)
        return self._get_dict_list_with_stmt(stmt)

    def get_dict_by_id(self, data_id):
        return self._get_dict_by_id(Media, data_id)

    def get_dict_list_by_ids(self, data_ids: list):
        return self._get_dict_list_by_ids(Media, data_ids)

    def get_all_data(self):
        return self._get_all_data(Media)

    def get_id(self, subtitle_id: int, sort: int):
        stmt = select(Media).where(Media.subtitle_id == subtitle_id, Media.sort == sort)
        return self._get_id_with_stmt(stmt)

    def get_ids(self, subtitle_id: int, sorts: list):
        stmt = select(Media).where(Media.subtitle_id == subtitle_id, Media.sort.in_(sorts))
        return self._get_ids_with_stmt(stmt)


class Media2dTextModel(DBSession):
    def __init__(self):
        pass

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media2dText, instance_id)
            instance.name = data.get("name")
            instance.font = data.get("font")
            instance.font_size = data.get("font_size")
            instance.file = data.get("file")
            instance.font_color = data.get("font_color")
            instance.height = data.get("height")
            instance.width = data.get("width")
            instance.top = data.get("top")
            instance.left = data.get("left")
            instance.opacity = data.get("opacity")
            instance.transaction_to_3d = data.get("transaction_to_3d")
            instance.full_screen = data.get("full_screen")
            instance.keep = data.get("keep")

            session.commit()

    def get_dict_by_media(self, media_id):
        stmt = select(Media2dText).where(Media2dText.media_id == media_id)
        return self._get_dict_with_stmt(stmt)


class Media2dImageModel(DBSession):
    def __init__(self):
        pass

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media2dImage, instance_id)
            instance.name = data.get("name")
            instance.file = data.get("file")
            instance.height = data.get("height")
            instance.width = data.get("width")
            instance.top = data.get("top")
            instance.left = data.get("left")
            instance.aspect = data.get("aspect")
            instance.opacity = data.get("opacity")
            instance.transaction_to_3d = data.get("transaction_to_3d")
            instance.full_screen = data.get("full_screen")
            instance.keep = data.get("keep")

            session.commit()

    def get_dict_by_media(self, media_id):
        stmt = select(Media2dImage).where(Media2dImage.media_id == media_id)
        return self._get_dict_with_stmt(stmt)


class Media2dVideoModel(DBSession):
    def __init__(self):
        pass

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media2dVideo, instance_id)
            instance.name = data.get("name")
            instance.file = data.get("file")
            instance.height = data.get("height")
            instance.width = data.get("width")
            instance.top = data.get("top")
            instance.left = data.get("left")
            instance.opacity = data.get("opacity")
            instance.transaction_to_3d = data.get("transaction_to_3d")
            instance.full_screen = data.get("full_screen")
            instance.keep = data.get("keep")

            session.commit()

    def get_dict_by_media(self, media_id):
        stmt = select(Media2dVideo).where(Media2dVideo.media_id == media_id)
        return self._get_dict_with_stmt(stmt)


class Media2dBgmModel(DBSession):
    def __init__(self):
        pass

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media2dBGM, instance_id)
            instance.name = data.get("name")
            instance.file = data.get("file")

            session.commit()

    def get_dict_by_media(self, media_id):
        stmt = select(Media2dBGM).where(Media2dBGM.media_id == media_id)
        return self._get_dict_with_stmt(stmt)


class Media3dTextModel(DBSession):
    def __init__(self):
        pass

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media3dText, instance_id)
            instance.name = data.get("name")
            instance.file = data.get("file")

            instance.font = data.get("font")
            instance.font_color = data.get("font_color")
            instance.font_size = data.get("font_size")

            instance.longitude = data.get("longitude")
            instance.latitude = data.get("latitude")
            instance.altitude = data.get("altitude")

            instance.height = data.get("height")
            instance.width = data.get("width")
            instance.depth = data.get("depth")
            instance.keep = data.get("keep")
            instance.parallel = data.get("parallel")

            session.commit()

    def get_dict_by_media(self, media_id):
        stmt = select(Media3dText).where(Media3dText.media_id == media_id)
        return self._get_dict_with_stmt(stmt)


class Media3dImageModel(DBSession):
    def __init__(self):
        pass

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media3dImage, instance_id)
            instance.name = data.get("name")
            instance.file = data.get("file")

            instance.longitude = data.get("longitude")
            instance.latitude = data.get("latitude")
            instance.altitude = data.get("altitude")

            instance.height = data.get("height")
            instance.width = data.get("width")
            instance.aspect = data.get("aspect")
            instance.depth = data.get("depth")
            instance.keep = data.get("keep")
            instance.parallel = data.get("parallel")

            session.commit()

    def get_dict_by_media(self, media_id):
        stmt = select(Media3dImage).where(Media3dImage.media_id == media_id)
        return self._get_dict_with_stmt(stmt)


class Media3dVideoModel(DBSession):
    def __init__(self):
        pass

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media3dVideo, instance_id)
            instance.name = data.get("name")
            instance.file = data.get("file")

            instance.longitude = data.get("longitude")
            instance.latitude = data.get("latitude")
            instance.altitude = data.get("altitude")

            instance.height = data.get("height")
            instance.width = data.get("width")
            instance.depth = data.get("depth")
            instance.keep = data.get("keep")
            instance.parallel = data.get("parallel")

            session.commit()

    def get_dict_by_media(self, media_id):
        stmt = select(Media3dVideo).where(Media3dVideo.media_id == media_id)
        return self._get_dict_with_stmt(stmt)


class Media3dMotionLineModel(DBSession):
    def __init__(self):
        pass

    def get_dict_by_media(self, media_id):
        stmt = select(Media3dMotionLine).where(Media3dMotionLine.media_id == media_id)
        return self._get_dict_with_stmt(stmt)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media3dMotionLine, instance_id)
            instance.name = data.get("name")
            instance.file = data.get("file")

            instance.color = data.get("color")
            instance.line_weight = data.get("line_weight")
            instance.motion_speed = data.get("motion_speed")

            instance.motion_time = data.get("motion_time")
            instance.line_divide = data.get("line_divide")
            instance.full_screen = data.get("keep")
            instance.keep = data.get("parallel")

            session.commit()


class Media3dKmlModel(DBSession):
    def __init__(self):
        pass

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media3dKml, instance_id)
            instance.name = data.get("name")
            instance.file = data.get("file")
            instance.keep = data.get("keep")
            session.commit()

    def get_dict_by_media(self, media_id):
        stmt = select(Media3dKml).where(Media3dKml.media_id == media_id)
        return self._get_dict_with_stmt(stmt)


class Media3dOverlayModel(DBSession):
    def __init__(self):
        pass

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Media3dOverlay, instance_id)
            instance.name = data.get("name")
            instance.file = data.get("file")
            instance.longitude_1 = data.get("longitude_1")
            instance.longitude_2 = data.get("longitude_2")
            instance.longitude_3 = data.get("longitude_3")
            instance.longitude_4 = data.get("longitude_4")
            instance.latitude_1 = data.get("latitude_1")
            instance.latitude_2 = data.get("latitude_2")
            instance.latitude_3 = data.get("latitude_3")
            instance.latitude_4 = data.get("latitude_4")
            instance.keep = data.get("keep")

            session.commit()

    def get_dict_by_media(self, media_id):
        stmt = select(Media3dOverlay).where(Media3dOverlay.media_id == media_id)
        return self._get_dict_with_stmt(stmt)
