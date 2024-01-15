from sqlalchemy import select
from app.models.session import DBSession, Session
from app.models.alchemy_models import Episode


class EpisodeModel(DBSession):
    def __init__(self):
        pass

    def save(self, data: dict):
        if data.get("id"):
            self.update(data)
        else:
            self.add(data)

    def delete(self, episode_id):
        if episode_id:
            self._delete(Episode, episode_id)

    def add(self, data: dict):
        collection = Episode(**data)
        self._add(collection)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Episode, instance_id)
            for key, value in data.items():
                setattr(instance, key, value)

            session.commit()

    def get_all_data(self):
        return self._get_all_data(Episode)

    def get_dict_by_id(self, data_id):
        return self._get_dict_by_id(Episode, data_id)

    def get_dict_list_by_ids(self, data_ids):
        return self._get_dict_list_by_ids(Episode, data_ids)

    def get_dict_list_by_collection_id(self, collection_id):
        stmt = select(Episode).where(Episode.collection_id == collection_id)
        return self._get_dict_list_with_stmt(stmt)

    def get_dict_by_collection_id_and_sort_id(self, collection_id: int, sort: int):
        stmt = select(Episode).where(Episode.collection_id == collection_id, Episode.sort == sort)
        return self._get_dict_with_stmt(stmt)

    def get_ids(self, collection_id: int, sort_list: list):
        stmt = select(Episode).where(Episode.collection_id == collection_id, Episode.sort.in_(sort_list))
        return self._get_ids_with_stmt(stmt)

    def get_id(self, collection_id: int, sort: int):
        stmt = select(Episode).where(Episode.collection_id == collection_id, Episode.sort == sort)
        return self._get_id_with_stmt(stmt)
