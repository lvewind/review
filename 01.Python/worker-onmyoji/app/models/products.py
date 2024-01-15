from sqlalchemy import text, delete

from app.models.session import DBSession, Session
from .alchemy_models import Product, PlanProductAssociation


class ProductModel(DBSession):
    def __int__(self):
        pass

    def get_all_data(self):
        return self._get_all_data(Product)

    def get_data_by_id(self, instance_id: int):
        return self._get_dict_by_id(Product, instance_id)

    @staticmethod
    def delete(instance_id: int):
        with Session() as session:
            product = session.get(Product, instance_id)
            plan_assoc = product.plan_association
            for o in plan_assoc:
                session.delete(o)
            session.delete(product)
            session.commit()
        # self._delete(Product, instance_id)

    def add(self, data: dict):
        collection = Product(
            name=data.get("name")
        )
        self._add(collection)

    @staticmethod
    def update(data: dict):
        with Session() as session:
            instance_id = data.get("id")
            instance = session.get(Product, instance_id)
            for key, value in data.items():
                setattr(instance, key, value)

            session.commit()
