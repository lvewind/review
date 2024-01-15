import os

from sqlalchemy import create_engine, select, inspect
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker, scoped_session

from app.models.alchemy_models import *

data_path = "data/user"
db_file_name = "user.db"
db_path = os.path.join(os.getcwd(), data_path, db_file_name)
engine = create_engine('sqlite:///' + db_path, echo=False)
Session = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(engine)


class DBSession:

    @staticmethod
    def _execute(stmt):
        with Session() as session:
            return session.execute(stmt)

    @staticmethod
    def _scalars(stmt):
        with Session() as session:
            return session.scalars(stmt)

    @staticmethod
    def _add(instance):
        with Session() as session:
            session.add(instance)
            data_dict = {c.key: getattr(instance, c.key) for c in inspect(instance).mapper.column_attrs}
            session.commit()
            return data_dict

    @staticmethod
    def _delete(entity, index: int):
        with Session() as session:
            instance = session.get(entity, index)
            session.delete(instance)
            session.commit()

    @staticmethod
    def _get_dict_list_by_ids(entity, id_set: list):
        data_list = []
        with Session() as session:
            stmt = select(entity)
            data = session.scalars(stmt).all()
            if data:
                for o in data:
                    if o.id in id_set:
                        data_list.append({c.key: getattr(o, c.key) for c in inspect(o).mapper.column_attrs})
        return data_list

    @staticmethod
    def _get_dict_by_id(entity, index: int):
        with Session() as session:
            data = session.get(entity, index)
            if data:
                return {c.key: getattr(data, c.key) for c in inspect(data).mapper.column_attrs}
            else:
                return {}

    @staticmethod
    def _get_secondary_by_id(entity, index: int, secondary: str):
        with Session() as session:
            data = session.get(entity, index)
            if data:
                secondary_list = getattr(data, secondary)
                if secondary_list:

                    return [{c.key: getattr(d, c.key) for c in inspect(d).mapper.column_attrs} for d in secondary_list]
                else:
                    return []
            else:
                return []

    @staticmethod
    def _get_by_id(entity, index: int):
        with Session() as session:
            return session.get(entity, index)

    @staticmethod
    def _get_all_data(entity):
        data_list = []
        with Session() as session:
            stmt = select(entity)
            data = session.scalars(stmt).all()
            if data:
                for o in data:
                    data_list.append({c.key: getattr(o, c.key) for c in inspect(o).mapper.column_attrs})
        return data_list

    @staticmethod
    def _get_dict_with_stmt(stmt):
        with Session() as session:
            try:
                data = session.scalars(stmt).one()
                return {c.key: getattr(data, c.key) for c in inspect(data).mapper.column_attrs}
            except NoResultFound:
                return {}

    @staticmethod
    def _get_dict_list_with_stmt(stmt):
        data_list = []
        with Session() as session:
            data = session.scalars(stmt).all()
            if data:
                for o in data:
                    data_list.append({c.key: getattr(o, c.key) for c in inspect(o).mapper.column_attrs})
        return data_list

    @staticmethod
    def _get_id_with_stmt(stmt):
        with Session() as session:
            try:
                data = session.scalars(stmt).first()
                if data:
                    return data.__dict__.get("id")
            except NoResultFound:
                return 0

    @staticmethod
    def _get_ids_with_stmt(stmt):
        ids = []
        with Session() as session:
            data = session.scalars(stmt).all()
            if data:
                for o in data:
                    ids.append(o.__dict__.get("id"))
        return ids

    def _clear_table(self, entity):
        all_data = self._get_all_data(entity)
        for data in all_data:
            self._delete(entity, data.get("id"))
