from app.models.session import DBSession, Session
from app.models.alchemy_models import Collection


class CollectionModel(DBSession):
    def __init__(self):
        pass

    def save(self, data: dict):
        if data.get("id"):
            self.update(data)
        else:
            self.add(data)

    def delete(self, collection_id):
        if collection_id:
            self._delete(Collection, collection_id)

    def add(self, data: dict):
        collection = Collection(**data)
        self._add(collection)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Collection, instance_id)

            for key, value in data.items():
                setattr(instance, key, value)

            session.commit()

    def get_all_data(self):
        return self._get_all_data(Collection)

    def get_dict_by_id(self, data_id):
        return self._get_dict_by_id(Collection, data_id)

    def get_dict_list_by_ids(self, data_ids):
        collections = []
        for data_id in data_ids:
            collections.append(self._get_dict_by_id(Collection, data_id))
        return collections
