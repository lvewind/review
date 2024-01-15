from .session import DBSession, Session
from .alchemy_models import RunList


class RunListModel(DBSession):
    def __int__(self):
        pass

    def add(self):
        self._add(RunList())

    def delete(self, instance_id: int):
        if instance_id:
            self._delete(RunList, instance_id)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(RunList, instance_id)
            for key, value in data.items():
                setattr(instance, key, value)

            session.commit()

    def get_all_data(self):
        return self._get_all_data(RunList)

    def get_dict_by_id(self, instance_id: int):
        return self._get_dict_by_id(RunList, instance_id)

    def get_env_type(self, instance_id: int):
        data = self._get_dict_by_id(RunList, instance_id)
        if data:
            return data.get("env_type")

    def get_env_id(self, instance_id: int):
        data = self._get_dict_by_id(RunList, instance_id)
        if data:
            return data.get("run_env_id")

    def get_account_id(self, instance_id):
        data = self._get_dict_by_id(RunList, instance_id)
        return data.get("account_id")

    def get_teammate_id(self, instance_id):
        data = self._get_dict_by_id(RunList, instance_id)
        return data.get("teammate_id")

    def get_teammate_type(self, instance_id):
        data = self._get_dict_by_id(RunList, instance_id)
        return data.get("teammate_type")
