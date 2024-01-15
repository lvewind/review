from sqlalchemy import select
from app.models.session import DBSession, Session
from app.models.alchemy_models import Subtitle, SubtitleAction


class SubtitleModel(DBSession):
    def __init__(self):
        pass

    def save(self, data: dict):
        if data.get("id"):
            self.update(data)
        else:
            self.add(data)

    def delete(self, subtitle_id):
        if subtitle_id:
            self._delete(Subtitle, subtitle_id)

    def add(self, data: dict):
        collection = Subtitle(**data)
        self._add(collection)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Subtitle, instance_id)
            for key, value in data.items():
                setattr(instance, key, value)
            session.commit()

    def get_all_data(self):
        return self._get_all_data(Subtitle)

    def get_dict_by_id(self, data_id):
        return self._get_dict_by_id(Subtitle, data_id)

    def get_dict_list_by_ids(self, data_ids):
        return self._get_dict_list_by_ids(Subtitle, data_ids)

    def get_dict_list_by_episode_id(self, episode_id):
        stmt = select(Subtitle).where(Subtitle.episode_id == episode_id)
        return self._get_dict_list_with_stmt(stmt)

    def get_id(self, episode_id: int, sort: int):
        stmt = select(Subtitle).where(Subtitle.episode_id == episode_id, Subtitle.sort == sort)
        return self._get_id_with_stmt(stmt)

    def get_ids(self, episode_id: int, sorts: list):
        stmt = select(Subtitle).where(Subtitle.episode_id == episode_id, Subtitle.sort.in_(sorts))
        return self._get_ids_with_stmt(stmt)


class SubtitleActionModel(DBSession):
    def __init__(self):
        pass

    def save(self, data: dict):
        if data.get("id"):
            self.update(data)

    def delete(self, subtitle_id):
        if subtitle_id:
            self._delete(SubtitleAction, subtitle_id)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(SubtitleAction, instance_id)
            for key, value in data.items():
                setattr(instance, key, value)
            session.commit()

    def get_all_data(self):
        return self._get_all_data(SubtitleAction)

    def get_dict_by_subtitle_id(self, data_id):
        stmt = select(SubtitleAction).where(SubtitleAction.subtitle_id == data_id)
        return self._get_dict_with_stmt(stmt)

    def get_dict_list_by_ids(self, data_ids):
        return self._get_dict_list_by_ids(SubtitleAction, data_ids)
