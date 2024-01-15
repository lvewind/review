from app.models.session import DBSession, Session
from .alchemy_models import AppSetting


class AppSettingModel(DBSession):
    def __init__(self):
        pass

    def set_option(self, option, value):
        setting_data = self._get_dict_by_id(AppSetting, 1)
        if setting_data:
            setting_data.update({option: value})
            self.update(setting_data)
        else:
            self._add(AppSetting())
            self.set_option(option, value)

    def read_option(self, option):
        setting_data = self._get_dict_by_id(AppSetting, 1)
        if setting_data:
            return setting_data.get(option)
        else:
            self._add(AppSetting())
            return ""

    def get_all_options(self):
        return self._get_dict_by_id(AppSetting, 1)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(AppSetting, instance_id)
            for key, value in data.items():
                setattr(instance, key, value)

            session.commit()
