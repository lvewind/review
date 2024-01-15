from app.models.session import DBSession
from .alchemy_models import RunEnv


class RunEnvModel(DBSession):
    def __init__(self):
        pass

    def add(self, data: dict):
        sandboxie = RunEnv(
            name=data.get("name"),
            env_type=data.get("env_type")
        )
        self._add(sandboxie)

    def delete(self, instance_id: int):
        self._delete(RunEnv, instance_id)

    def update(self, data: dict):
        pass

    def get_dict_by_id(self, instance_id):
        return self._get_dict_by_id(RunEnv, instance_id)

    def get_all_data(self):
        return self._get_all_data(RunEnv)

    def get_name(self, instance_id: int):
        data = self._get_dict_by_id(RunEnv, instance_id)
        return data.get("name")

    def get_env_type(self, instance_id: int):
        data = self._get_dict_by_id(RunEnv, instance_id)
        return data.get("env_type")

    def clear_table(self):
        self._clear_table(RunEnv)

    def get_sandboxie(self):
        pass

    def get_emulator(self):
        pass
