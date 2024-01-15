from app.models.session import DBSession, Session
from app.models.alchemy_models.setting import AppSetting


class SettingModel(DBSession):
    def __init__(self):
        pass

    def save(self, data: dict):
        if data.get("id"):
            self.update(data)
        else:
            self.add(data)

    def delete(self, setting_id):
        if setting_id:
            self._delete(AppSetting, setting_id)

    def add(self, data: dict):
        collection = AppSetting(**data)
        self._add(collection)

    @staticmethod
    def update(data: dict):
        print(data)
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(AppSetting, instance_id)
            for key, value in data.items():
                setattr(instance, key, value)

            session.commit()

    def get_data(self):
        return self._get_dict_by_id(AppSetting, 1)

    def get_chrome_user_data_path(self):
        return self._get_by_id(AppSetting, 1)

    def get_azure_key(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.azure_key

    def get_azure_region(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.azure_region

    def get_kiosk(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.kiosk

    def get_screen_offset_x(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.screen_offset_x

    def get_screen_offset_y(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.screen_offset_y

    def get_source_screen_x(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.source_screen_x

    def get_source_screen_y(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.source_screen_y

    def get_js_server(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.js_server

    def get_cesium_base_url(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.cesium_base_url

    def get_font_server(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.font_server

    def get_media_server(self):
        data = self._get_by_id(AppSetting, 1)
        if data:
            return data.media_server
