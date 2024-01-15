from app.models.session import DBSession, Session
from .alchemy_models import CounterRecord
from sqlalchemy import select


class CounterRecordModel(DBSession):
    def __init__(self):
        pass

    def add(self, data: dict):
        return self._add(CounterRecord(**data))

    def update(self):
        pass

    def get_record_item_by_record_id(self, record_id: str, item_name: str):
        record = self.get_record_by_record_id(record_id)
        if record:
            return record.get(item_name)
        else:
            return ""

    def get_record_by_record_id(self, record_id: str):
        stmt = select(CounterRecord).where(CounterRecord.record_id == record_id)
        data = self._get_dict_with_stmt(stmt)
        if data:
            return data
        else:
            return self.add({"record_id": record_id})

    def get_all_data(self):
        return self._get_all_data(CounterRecord)

    @staticmethod
    def increase_record_item_value(instance_id, key):
        with Session() as session:
            instance = session.get(CounterRecord, instance_id)
            new_value = instance.value + 1
            setattr(instance, key, new_value)
            session.commit()

    def increase_record_item_value_by_record_id(self, record_id: str, record_item: str):
        _data = self.get_record_by_record_id(record_id)
        if not _data:
            data = {"record_id": record_id, record_item: 1}
            self.add(data)
        else:
            with Session() as session:
                stmt = select(CounterRecord).where(CounterRecord.record_id == record_id)
                instance = session.scalar(stmt)
                if _data.get(record_item):
                    new_value = _data.get(record_item) + 1
                else:
                    new_value = 1
                setattr(instance, record_item, new_value)
                session.commit()
