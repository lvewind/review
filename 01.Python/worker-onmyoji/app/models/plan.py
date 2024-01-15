from sqlalchemy import inspect

from app.models.session import DBSession, Session
from .alchemy_models import Plan, Product, PlanProductAssociation


class PlanModel(DBSession):
    def __init__(self):
        pass

    def add(self, data):
        self._add(Plan(**data))

    @staticmethod
    def delete(instance_id: id):
        with Session() as session:
            plan = session.get(Plan, instance_id)
            product_assoc = plan.product_association
            for o in product_assoc:
                session.delete(o)
            session.delete(plan)
            session.commit()

    @staticmethod
    def update(data):
        with Session() as session:
            instance = session.get(Plan, data.get("id"))
            for key, value in data.items():
                setattr(instance, key, value)
            session.commit()

    def get_name(self, instance_id: int):
        data = self._get_dict_by_id(Plan, instance_id)
        return data.get("name")

    def get_all_data(self):
        return self._get_all_data(Plan)

    def get_dict_by_id(self, instance_id: int):
        return self._get_dict_by_id(Plan, instance_id)

    @staticmethod
    def get_products(instance_id: int):
        data_list = []
        with Session() as session:
            plan = session.get(Plan, instance_id)
            data_assoc = plan.product_association
            for a in data_assoc:
                o = a.product
                p = {c.key: getattr(o, c.key) for c in inspect(o).mapper.column_attrs}
                p.update({"sort_order": a.sort_order, "assoc_id": a.id})
                data_list.append(p)
        return data_list

    @staticmethod
    def add_products_assoc(instance_id: int, product_ids: list):
        with Session() as session:
            plan = session.get(Plan, instance_id)
            for product_id in product_ids:
                product = session.get(Product, product_id)
                plan.product_association.append(PlanProductAssociation(product=product, sort_order=len(plan.product_association) + 1))
            session.commit()

    def delete_products_assoc(self, assoc_ids: list):
        with Session() as session:
            for assoc_id in assoc_ids:
                self._delete(PlanProductAssociation, assoc_id)
            session.commit()

    @staticmethod
    def update_product_assoc(data: dict):
        with Session() as session:
            instance = session.get(PlanProductAssociation, data.get("id"))
            for key, value in data.items():
                setattr(instance, key, value)
            session.commit()
