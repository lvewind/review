from ..models.setting import SettingModel
from ..views import *


class SettingPresenter:
    def __init__(self):
        view_sender.setting.save.connect(self.save)
        self._view = SettingView()
        self._setting = SettingModel()

    def save(self, data):
        if data.get("id"):
            self._setting.update(data)
        else:
            self._setting.add(data)

    @staticmethod
    def update(data):
        pass

    def show_setting(self):
        data = self._setting.get_data()
        if not data:
            data = {}
        self._view.show_edit(data)
