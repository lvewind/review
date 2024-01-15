from app.static import *
from app.views import *
from app.models import CollectionModel


class CollectionPresenter:
    def __init__(self):
        view_sender.collection.save.connect(self.save)
        self._view = CollectionView()
        self.menu = CollectionMenu()
        self._collection = CollectionModel()

    def save(self, data: dict):
        if data:
            data_id = data.get("id")
            if data_id:
                self.update(data)
            else:
                self.add(data)

    def add(self, data: dict):
        self._collection.add(data)
        data = self._collection.get_all_data()
        view_sender.main.load_table_collection.emit(data, header_collection)

    def update(self, data: dict):
        self._collection.update(data)
        new_data = self._collection.get_all_data()
        view_sender.main.load_table_collection.emit(new_data, header_collection)

    def delete(self, collection_id):
        self._collection.delete(collection_id)
        new_data = self._collection.get_all_data()
        view_sender.main.load_table_collection.emit(new_data, header_collection)

    def show_add(self):
        self._view.show_add()

    def show_edit(self, collection_id: int):
        if collection_id:
            data = self._collection.get_dict_by_id(collection_id)
            self._view.show_edit(data)

    def show_menu(self):
        self.menu.show_menu()
