from .base import *


class Collection(Base):
    __tablename__ = "collection"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    sort: Mapped[int] = mapped_column(default=0)


class Episode(Base):
    __tablename__ = "episode"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    content: Mapped[str]
    sort: Mapped[int] = mapped_column(default=0)
    display_subtitles: Mapped[int] = mapped_column(default=0)
    speech_audio_synchronize: Mapped[int] = mapped_column(default=0)
    collection_id: Mapped[int] = mapped_column(ForeignKey("collection.id"))
    # collection_id: Mapped[int]


class Subtitle(Base):
    __tablename__ = "subtitle"

    id: Mapped[int] = mapped_column(primary_key=True)
    episode_id: Mapped[int]
    name: Mapped[str]

    audio_file: Mapped[str] = mapped_column(default="")
    audio_time: Mapped[float] = mapped_column(default=0)
    ext_time: Mapped[float] = mapped_column(default=0)
    font: Mapped[str] = mapped_column(default="工业黑简体")
    font_size: Mapped[str] = mapped_column(default="6em")
    font_color: Mapped[str] = mapped_column(default="ffffff")
    media_count: Mapped[int] = mapped_column(default=0)
    sort: Mapped[int] = mapped_column(default=0)
    is_empty: Mapped[int] = mapped_column(default=0)

    voice_local_name: Mapped[str] = mapped_column(default="云希")
    voice_name: Mapped[str] = mapped_column(default="zh-CN-YunxiNeural")
    voice_role: Mapped[str] = mapped_column(default="default")
    voice_style: Mapped[str] = mapped_column(default="default")
    voice_rate: Mapped[float] = mapped_column(default=1)
    voice_volume: Mapped[float] = mapped_column(default=1)
    voice_pitch: Mapped[float] = mapped_column(default=1)

    subtitle_action: Mapped["SubtitleAction"] = relationship(back_populates="subtitle", cascade="all, delete-orphan")


class SubtitleAction(Base):
    __tablename__ = "subtitle_action"

    id: Mapped[int] = mapped_column(primary_key=True)
    subtitle_id: Mapped[int] = mapped_column(ForeignKey("subtitle.id"))
    name: Mapped[Optional[str]]
    fly_type: Mapped[Optional[str]]
    fly_to_place: Mapped[Optional[str]]
    fly_to_longitude: Mapped[Optional[str]]
    fly_to_latitude: Mapped[Optional[str]]
    fly_to_altitude: Mapped[Optional[str]]
    heading: Mapped[Optional[str]]
    tilt: Mapped[Optional[str]]
    set_2d_view: Mapped[Optional[int]]
    set_3d_view: Mapped[Optional[int]]
    fly_speed: Mapped[Optional[int]]
    start_x: Mapped[Optional[int]]
    start_y: Mapped[Optional[int]]
    end_x: Mapped[Optional[int]]
    end_y: Mapped[Optional[int]]
    slide_speed: Mapped[Optional[int]]
    zoom_times: Mapped[Optional[int]]

    subtitle: Mapped["Subtitle"] = relationship(back_populates="subtitle_action")


class Media(Base):
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    media_type: Mapped[Optional[str]]
    show_type: Mapped[Optional[str]]
    media_time: Mapped[Optional[float]] = mapped_column(default=0)
    media_delay: Mapped[Optional[float]] = mapped_column(default=0)
    sort: Mapped[Optional[int]]
    subtitle: Mapped[Optional[str]]
    subtitle_id: Mapped[int] = mapped_column(ForeignKey("subtitle.id"))
    episode_id: Mapped[Optional[int]]

    media_2d_text: Mapped["Media2dText"] = relationship(back_populates="media", cascade="all, delete-orphan")
    media_2d_image: Mapped["Media2dImage"] = relationship(back_populates="media", cascade="all, delete-orphan")
    media_2d_video: Mapped["Media2dVideo"] = relationship(back_populates="media", cascade="all, delete-orphan")
    media_2d_bgm: Mapped["Media2dBGM"] = relationship(back_populates="media", cascade="all, delete-orphan")

    media_3d_text: Mapped["Media3dText"] = relationship(back_populates="media", cascade="all, delete-orphan")
    media_3d_image: Mapped["Media3dImage"] = relationship(back_populates="media", cascade="all, delete-orphan")
    media_3d_video: Mapped["Media3dVideo"] = relationship(back_populates="media", cascade="all, delete-orphan")

    media_3d_motion_line: Mapped["Media3dMotionLine"] = relationship(back_populates="media", cascade="all, delete-orphan")
    media_3d_overlay: Mapped["Media3dOverlay"] = relationship(back_populates="media", cascade="all, delete-orphan")
    media_3d_kml: Mapped["Media3dKml"] = relationship(back_populates="media", cascade="all, delete-orphan")


class Media2dText(Base):
    __tablename__ = "media_2d_text"

    id: Mapped[int] = mapped_column(primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    name: Mapped[Optional[str]]
    file: Mapped[str] = mapped_column(default="")

    font: Mapped[Optional[str]]
    font_size: Mapped[Optional[str]]
    font_color: Mapped[Optional[str]]

    height: Mapped[Optional[int]]
    width: Mapped[Optional[int]]
    top: Mapped[Optional[int]]
    left: Mapped[Optional[int]]
    opacity: Mapped[Optional[float]]
    aspect: Mapped[Optional[float]]

    transaction_to_3d: Mapped[Optional[int]]
    full_screen: Mapped[Optional[int]]
    keep: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_2d_text")


class Media2dImage(Base):
    __tablename__ = "media_2d_image"

    id: Mapped[int] = mapped_column(primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    name: Mapped[Optional[str]]
    file: Mapped[str] = mapped_column(default="")

    height: Mapped[Optional[int]]
    width: Mapped[Optional[int]]
    top: Mapped[Optional[int]]
    left: Mapped[Optional[int]]
    opacity: Mapped[Optional[float]]
    aspect: Mapped[Optional[float]]

    transaction_to_3d: Mapped[Optional[int]]
    full_screen: Mapped[Optional[int]]
    keep: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_2d_image")


class Media2dVideo(Base):
    __tablename__ = "media_2d_video"

    id: Mapped[int] = mapped_column(primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    name: Mapped[Optional[str]]
    file: Mapped[str] = mapped_column(default="")

    height: Mapped[Optional[int]]
    width: Mapped[Optional[int]]
    top: Mapped[Optional[int]]
    left: Mapped[Optional[int]]
    opacity: Mapped[Optional[float]]
    aspect: Mapped[Optional[float]]

    transaction_to_3d: Mapped[Optional[int]]
    full_screen: Mapped[Optional[int]]
    keep: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_2d_video")


class Media2dBGM(Base):
    __tablename__ = "media_2d_bgm"

    id: Mapped[int] = mapped_column(primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    name: Mapped[Optional[str]]
    file: Mapped[str] = mapped_column(default="")

    full_screen: Mapped[Optional[int]]
    keep: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_2d_bgm")


class Media3dText(Base):
    __tablename__ = "media_3d_text"

    id: Mapped[int] = mapped_column(primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    name: Mapped[Optional[str]]
    file: Mapped[str] = mapped_column(default="")

    font: Mapped[Optional[int]]
    font_color: Mapped[Optional[int]]
    font_size: Mapped[Optional[int]]

    longitude: Mapped[Optional[float]]
    latitude: Mapped[Optional[float]]
    altitude: Mapped[Optional[float]]

    height: Mapped[Optional[int]]
    width: Mapped[Optional[int]]
    depth: Mapped[Optional[int]]
    aspect: Mapped[Optional[float]]

    keep: Mapped[Optional[int]]
    parallel: Mapped[Optional[int]]
    sprite: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_3d_text")


class Media3dImage(Base):
    __tablename__ = "media_3d_image"

    id: Mapped[int] = mapped_column(primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    name: Mapped[Optional[str]]
    file: Mapped[str] = mapped_column(default="")

    longitude: Mapped[Optional[float]]
    latitude: Mapped[Optional[float]]
    altitude: Mapped[Optional[float]]

    height: Mapped[Optional[int]]
    width: Mapped[Optional[int]]
    depth: Mapped[Optional[int]]
    aspect: Mapped[Optional[float]]

    keep: Mapped[Optional[int]]
    parallel: Mapped[Optional[int]]
    sprite: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_3d_image")


class Media3dVideo(Base):
    __tablename__ = "media_3d_video"

    id: Mapped[int] = mapped_column(primary_key=True)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    name: Mapped[Optional[str]]
    file: Mapped[str] = mapped_column(default="")

    longitude: Mapped[Optional[float]]
    latitude: Mapped[Optional[float]]
    altitude: Mapped[Optional[float]]

    height: Mapped[Optional[int]]
    width: Mapped[Optional[int]]
    depth: Mapped[Optional[int]]
    aspect: Mapped[Optional[float]]

    keep: Mapped[Optional[int]]
    parallel: Mapped[Optional[int]]
    sprite: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_3d_video")


class Media3dMotionLine(Base):
    __tablename__ = "media_3d_motion_line"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))

    file: Mapped[str] = mapped_column(default="")

    color: Mapped[Optional[int]]
    line_weight: Mapped[Optional[float]]

    motion_speed: Mapped[Optional[int]]
    motion_time: Mapped[Optional[float]]
    line_divide: Mapped[Optional[int]]
    height: Mapped[Optional[float]]

    keep: Mapped[Optional[int]]
    parallel: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_3d_motion_line")


class Media3dOverlay(Base):
    __tablename__ = "media_3d_overlay"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))

    file: Mapped[str] = mapped_column(default="")

    longitude_1: Mapped[Optional[float]]
    latitude_1: Mapped[Optional[float]]

    longitude_2: Mapped[Optional[float]]
    latitude_2: Mapped[Optional[float]]

    longitude_3: Mapped[Optional[float]]
    latitude_3: Mapped[Optional[float]]

    longitude_4: Mapped[Optional[float]]
    latitude_4: Mapped[Optional[float]]

    keep: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_3d_overlay")


class Media3dKml(Base):
    __tablename__ = "media_3d_kml"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))

    file: Mapped[str] = mapped_column(default="")
    keep: Mapped[Optional[int]]

    media: Mapped["Media"] = relationship(back_populates="media_3d_kml")