from .base import *


class AppSetting(Base):
    __tablename__ = "earth_setting"

    id: Mapped[int] = mapped_column(primary_key=True)
    chrome_user_data_path: Mapped[str] = mapped_column(String(128))
    azure_key: Mapped[str]
    azure_region: Mapped[str]
    kiosk: Mapped[int]

    screen_offset_x: Mapped[int]
    screen_offset_y: Mapped[int]
    source_screen_x: Mapped[int]
    source_screen_y: Mapped[int]

    js_server: Mapped[str]
    cesium_base_url: Mapped[str]
    font_server: Mapped[str]
    media_server: Mapped[str]
