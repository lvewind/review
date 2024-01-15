"""
数据存取模块
"""
from .storage_sqlite import StorageSQLite
from .storage_json import StorageJSON


class Storage(StorageSQLite):
    def __init__(self, table: str, db_config: dict):
        super(Storage, self).__init__(table, db_config)
