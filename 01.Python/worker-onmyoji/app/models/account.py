from app.models.session import DBSession, Session
from app.models.alchemy_models import Account


class AccountModel(DBSession):
    def __init__(self):
        pass

    def save(self, data: dict):
        if data.get("id"):
            self.update(data)
        else:
            self.add(data)

    def delete(self, data_id):
        if data_id:
            self._delete(Account, data_id)

    def add(self, data: dict):
        collection = Account(**data)
        self._add(collection)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Account, instance_id)
            for key, value in data.items():
                setattr(instance, key, value)

            session.commit()

    def get_all_data(self):
        return self._get_all_data(Account)

    def get_dict_by_id(self, data_id):
        return self._get_dict_by_id(Account, data_id)

    def get_dict_list_by_ids(self, data_ids):
        collections = []
        for data_id in data_ids:
            collections.append(self._get_dict_by_id(Account, data_id))
        return collections

    def get_name(self, data_id):
        data = self._get_dict_by_id(Account, data_id)
        return data.get("name")
