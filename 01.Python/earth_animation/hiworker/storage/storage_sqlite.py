"""
SQLite存取模块
"""
import json
import sqlite3
import threading
import os

sqlite_mutex = threading.Lock()


class StorageSQLite(object):
    def __init__(self, table: str, db_config: dict):
        """
        初始化存取实例
        :param table: 表名称
        :param db_config: {"data_path": , "db_file_name": } 数据库文件配置
        """
        self.table = table
        self.data = []
        self.parent_table = ""
        self.save_to_file = True
        data_path = db_config.get("data_path")
        db_file_name = db_config.get("db_file_name")
        self.db_file = os.path.join(data_path, db_file_name)
        self.refresh_data()

    def refresh_data(self):
        """
        刷新数据到内存字典
        :return:
        """
        self.data = self.db_get_all_data()

    def db_add_row(self, data_dict: dict):
        """
        添加数据行
        :param data_dict: 数据字典
        :return:
        """
        columns, values = self.dict_to_query_add(data_dict)
        query = " ".join(["INSERT INTO", self.table, "DEFAULT VALUES"])
        if columns:
            query = " ".join(["INSERT INTO", self.table, columns, "VALUES", values])
        return self.execute_query_write(query)

    def db_add_rows(self, data_dict_list: list):
        """
        添加多行数据
        :param data_dict_list: 数据字典列表
        :return:
        """
        add_results = []
        if data_dict_list:
            for data_dict in data_dict_list:
                add_result = self.db_add_row(data_dict)
                add_results.append(add_result)
        return add_results

    def db_del_row(self, refer_value, refer="id"):
        """
        删除数据行
        :param refer_value: 参考字段值
        :param refer: 参考字段名
        :return:
        """
        query = " ".join(["DELETE FROM", self.table, "WHERE", refer, "=", str(refer_value)])
        self.execute_query_write(query)

    def db_del_rows(self, refer_value_list: list, refer="id"):
        """
        删除多行数据
        :param refer_value_list: 数据字典列表
        :param refer: 参考字段名
        :return:
        """
        if refer_value_list:
            for refer_value in refer_value_list:
                self.db_del_row(refer_value, refer=refer)

    def db_update_row(self, data_dict: dict, refer="id", ref_value=None):
        """
        更新数据行
        :param data_dict: 新数据字典
        :param refer: 参考字段名
        :param ref_value: 参考字段值
        :return:
        """
        if ref_value:
            refer_value = ref_value
        else:
            refer_value = data_dict.get(refer)
        placeholder = self.dict_to_query_update(data_dict)
        if placeholder:
            if type(refer_value) == str:
                query = " ".join(["UPDATE", self.table, "SET", placeholder, "WHERE", refer, "=", "'" + str(refer_value) + "'"])
            else:
                query = " ".join(["UPDATE", self.table, "SET", placeholder, "WHERE", refer, "=", str(refer_value)])
            self.execute_query_write(query)

    def db_update_rows(self, data_dict_list: list, refer="id"):
        """
        更新多行数据
        :param data_dict_list: 数据字典列表
        :param refer: 参考字段名
        :return:
        """
        if data_dict_list:
            for data_dict in data_dict_list:
                self.db_update_row(data_dict, refer=refer)

    def db_update_rows_field(self, index_list: list, field: str, value):
        """
        更新多个数据行的单个字段
        :param index_list: 索引列表
        :param field: 要更新的字段名称
        :param value: 新的字段值
        :return:
        """
        if index_list:
            for index in index_list:
                self.db_update_row({"id": index, field: value})

    def db_read_row(self, refer_value, refer="id", only_first=False):
        """
        读取字段行数据
        :param refer_value: 参考值
        :param refer: 参考名
        :param only_first: 只返回第一个值
        :return:
        """
        if type(refer_value) == str:
            query = " ".join(["SELECT * FROM", self.table, "WHERE", refer, "=", "'" + str(refer_value) + "'"])
        else:
            query = " ".join(["SELECT * FROM", self.table, "WHERE", refer, "=", str(refer_value)])
        result, description = self.execute_query_read(query)
        result_to_dict_list = self.result_to_dict_list(result, description)
        if not (only_first is True):
            return result_to_dict_list
        return result_to_dict_list[0] if len(result_to_dict_list) >= 1 else False

    def db_read_rows(self, refer_value_list: list, refer="id"):
        """
        读取多行数据
        :param refer_value_list: 参考值列表
        :param refer: 参考字段名
        :return:
        """
        rows = []
        if refer_value_list:
            for refer_value in refer_value_list:
                rows.extend(self.db_read_row(refer_value, refer=refer))
        return rows

    def db_read_row_field(self, target_field: str, refer_value, refer="id", only_first=True):
        """
        读取数据行中的单个字段
        :param target_field: 需要读取的字段
        :param refer_value: 参考值
        :param refer: 参考字段
        :param only_first: 只返回第一个值
        :return:
        """
        if type(refer_value) == str:
            query = " ".join(["SELECT", target_field, "FROM", self.table, "WHERE", refer, "=", "'" + str(refer_value) + "'"])
        else:
            query = " ".join(["SELECT", target_field, "FROM", self.table, "WHERE", refer, "=", str(refer_value)])
        result, description = self.execute_query_read(query)
        if result:
            return self.result_to_list(result, only_first)

    def db_get_all_data(self):
        """
        获取数据表中的额所有数据
        :return:
        """
        query = " ".join(["SELECT * FROM", self.table])
        result, description = self.execute_query_read(query)
        return self.result_to_dict_list(result, description)

    @staticmethod
    def list_sort_key(element: dict):
        return element["id"]

    def execute_query_write(self, query, commit=True):
        """
        执行SQL写入操作
        :param query:
        :param commit:
        :return:
        """

        with sqlite_mutex:
            try:
                db = sqlite3.connect(self.db_file)
                cursor = db.cursor()
                cursor.execute(query)
                if commit:
                    db.commit()
                db.close()
                self.refresh_data()
                if self.data:
                    return self.data[-1].get("id")
                else:
                    return False
            except sqlite3.OperationalError as e:
                print("write error", e, query)
                return False
            except sqlite3.IntegrityError as e:
                print("write error", e, query)
                return False

    def execute_query_read(self, query):
        """
        执行SQL读取操作
        :param query:
        :return:
        """
        try:
            db = sqlite3.connect(self.db_file)
            cursor = db.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            description = []
            for header in cursor.description:
                description.append(header[0])
            db.close()
            return result, description
        except sqlite3.OperationalError as e:
            print("read error", e, query)
            return False, False

    @staticmethod
    def result_to_dict_list(result, description):
        """
        字符串转JSON
        :param result:
        :param description:
        :return:
        """
        if not result:
            return []
        result_list = []
        for result_tuple in result:
            result_dict = {}
            for index, value in enumerate(result_tuple):
                if type(value) == str and ("[" and "]" or "{" and "}") in value and "[[]]" not in value:
                    value = json.loads(value)
                result_dict.update({description[index]: value})
            result_list.append(result_dict)
        return result_list

    @staticmethod
    def result_to_list(result, only_first=True):
        """
        字符串转JSON
        :param result:
        :param only_first:
        :return:
        """
        if only_first:
            value = result[0][0]
            if type(value) == str and ("[" and "]" or "{" and "}") in value:
                return json.loads(value)
            else:
                return value
        else:
            result_list = []
            for result_tuple in result:
                for value in result_tuple:
                    result_list.append(value)
            return result_list

    @staticmethod
    def dict_to_query_add(data_dict: dict):
        """
        JSON转SQL新增语句
        :param data_dict:
        :return:
        """
        columns = ""
        values = []
        if data_dict:
            for key, value in data_dict.items():
                columns += str(key) + ", "
                if type(value) == int or type(value) == str:
                    values.append(value)
                else:
                    values.append(json.dumps(value, ensure_ascii=False))
            values = json.dumps(values, ensure_ascii=False)
            columns = "(" + columns.rstrip(", ") + ")"
            values = "(" + values.rstrip("]").lstrip("[") + ")"
            return columns, values
        else:
            return False, False

    @staticmethod
    def dict_to_query_update(data_dict: dict):
        """
        JSON转SQL更新语句
        :param data_dict:
        :return:
        """
        placeholder = ""
        for key, value in data_dict.items():
            if type(value) == int:
                placeholder += key + "=" + str(value) + ", "
            elif type(value) == str:
                placeholder += key + "= '" + str(value) + "', "
            else:
                placeholder += key + "= '" + json.dumps(value, ensure_ascii=False) + "', "
        return placeholder.rstrip(", ")
