# -*- coding: UTF-8 -*-
"""
JSON读写扩展
"""
import os
import json
import zipfile


class JsonReadWrite:
    def __init__(self):
        pass

    @staticmethod
    def load_json_file(json_file_path=None):
        """
        # 加载单个JSON文件
        :return: list
        """
        if json_file_path:
            if os.path.isfile(json_file_path):

                try:
                    with open(json_file_path, "r", encoding="UTF-8") as fr:
                        json_data = json.loads(fr.read())
                        return json_data
                except json.decoder.JSONDecodeError:
                    print("未能成功读取" + json_file_path + "文件数据")
            else:
                print("文件 " + json_file_path + "不存在")
        else:
            return []

    @staticmethod
    def load_json_files(json_files_folder):
        """
        # 加载目录下所有JSON文件
        :return: 返回JSON数据字典
        """
        # 定义用于载入当前目录所有JSON数据的字典
        all_data_dict = {}
        # 路径不存在时，创建路径
        if not os.path.exists(json_files_folder):
            os.makedirs(json_files_folder, exist_ok=True)
            return False
        else:
            json_file_list = os.listdir(json_files_folder)
            for json_file_name in json_file_list:
                if ".json" in json_file_name:
                    try:
                        with open(os.path.join(json_files_folder, json_file_name), "r", encoding="utf-8") as fr:
                            temp_dict = json.loads(fr.read())
                    except json.decoder.JSONDecodeError:
                        pass
                    if temp_dict:
                        all_data_dict.update(temp_dict)
        return all_data_dict

    @staticmethod
    def load_json_files_from_zip(zip_file_path, zip_pwd=None):
        """
        # 加载目录下所有zip中的所有JSON文件
        :return:
        """
        # 定义用于载入当前目录所有JSON数据的字典
        all_data_dict = {}
        # 路径不存在时，创建路径
        if os.path.isfile(zip_file_path):
            zf = zipfile.ZipFile(zip_file_path)
            # 列出压缩包内的JSON文件
            json_file_list = zf.namelist()
            # 解压文件并读取内容转为字典
            if zip_pwd:
                zip_pwd = zip_pwd.encode('utf-8')
            for json_file_name in json_file_list:
                if ".json" in json_file_name:
                    source_binary = zf.read(json_file_name, pwd=zip_pwd)
                    json_decode = source_binary.decode()
                    try:
                        temp_dict = json.loads(json_decode)
                        all_data_dict.update(temp_dict)
                    except json.decoder.JSONDecodeError:
                        pass
            return all_data_dict
        else:
            print("压缩包文件不存在 " + zip_file_path)

    @staticmethod
    def save_json(new_data, file_path, file_name):
        """
        :param new_data:
        :param file_path:
        :param file_name:
        :return:
        """
        # 路径不存在时，创建路径
        if not os.path.exists(file_path):
            os.makedirs(file_path, exist_ok=True)

        # 打开用于写入数据的JSON文件
        fw = open(os.path.join(file_path, file_name), "w", encoding="utf-8")
        # 把字典转化为json写入到文件
        fw.write(str(json.dumps(new_data, ensure_ascii=False)))
        fw.close()
