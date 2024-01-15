"""
此模块用于数据库初始化
"""
import sqlite3
import os
import re


class DBCreate:
    def __init__(self, db_create_sql: list, db_path="data\\user", db_file_name="user.db", db_create_sql_file="user.sql"):
        """
        初始化数据库连接对象
        :param db_create_sql: sql指令列表
        :param db_path: 数据库路径
        :param db_file_name: 数据库名称
        :param db_create_sql_file: sql文件
        """
        self.db_create_sql = db_create_sql
        self.app_path = os.path.abspath(os.getcwd())
        self.user_path = os.path.join(self.app_path, db_path)
        if not os.path.exists(self.user_path):
            os.makedirs(self.user_path, exist_ok=True)
        self.db_file = os.path.join(self.user_path, db_file_name)
        self.sql_file = os.path.join(self.user_path, db_create_sql_file)

        self.create_table()

    def create_table(self):
        """
        通过预设的sql指令创建数据表
        :return:  None
        """
        self.db_create_sql = [x.replace('\n', ' ') for x in self.db_create_sql]
        self.db_create_sql = [re.sub(r" +", " ", x) for x in self.db_create_sql]
        con = sqlite3.connect(self.db_file, check_same_thread=False)
        c = con.cursor()
        for sql_item in self.db_create_sql:
            try:
                c.execute(sql_item)
            except sqlite3.OperationalError as e:
                if "already exists" in str(e):
                    pass
                else:
                    print(e)
        con.close()

    def create_table_from_sql_file(self):
        """
        通过sql文件船舰数据表
        :return: None
        """
        try:
            with open(self.sql_file) as f:
                sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
                sql_list = [x.replace('\n', ' ') for x in sql_list]
                sql_list = [re.sub(r" +", " ", x) for x in sql_list]
                con = sqlite3.connect(self.db_file, check_same_thread=False)
                c = con.cursor()
                for sql_item in sql_list:
                    try:
                        c.execute(sql_item)
                    except sqlite3.OperationalError:
                        pass
        except FileNotFoundError:
            pass
        con.close()
