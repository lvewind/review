import os.path

from ..json import JsonReadWrite


class Coordinate(JsonReadWrite):
    def __init__(self, data_path="data/coordinate", zip_file="data/coordinate/64.zip"):
        """
        初始化坐标数据类
        """
        super(Coordinate, self).__init__()
        self.data = {}
        self.data_path = os.path.join(os.getcwd(), data_path)
        self.zip_file = os.path.join(os.getcwd(), zip_file)
        # self.load_coord()

    def load_coord(self, from_zip=True):
        """
        加载坐标数据到self.data
        :param from_zip: bool 是否从zip压缩包加载
        :return: None
        """
        if from_zip:
            return self.load_coord_from_zip()
        else:
            return self.load_coord_from_folder()

    def load_coord_from_folder(self):
        """
        从文件夹加载坐标数据到self.data
        :return: bool 数据有效返回True, 否则False
        """
        self.data = self.load_json_files(self.data_path)
        if len(self.data) > 0:
            return True
        else:
            return False

    def load_coord_from_zip(self):
        """
        从压缩包加载坐标数据到self.data
        :return: bool 数据有效返回True, 否则False
        """
        zip_path = os.path.join(self.data_path, self.zip_file)
        self.data = self.load_json_files_from_zip(zip_path, "U2FsdGVkX1826P+lqv/SP5kHh4PcuUpf1OgQF4CeuZg=")
        if len(self.data) > 0:
            return True
        else:
            return False

    def read_coord(self, template):
        """
        读取模板坐标数据
        :param template: 需要读取的模板名称
        :return: [left, top, right, bottom] 坐标区域, False 模板不存在
        """
        if template in self.data:
            box = [self.data[template]["left"],
                   self.data[template]["top"],
                   self.data[template]["right"],
                   self.data[template]["bottom"]]
        else:
            box = False
        return box

    def read_size(self, template):
        """
        读取模板尺寸
        :param template: 需要读取的模板名称
        :return: [width, height] 坐标区域, False 模板不存在
        """
        if template in self.data:
            size = [self.data[template].get("width", 0), self.data[template].get("height", 0)]
        else:
            size = False
        return size

    def set_coord(self, template, box):
        """
        设置模板坐标数据
        :param template: 需要设置的模板名称
        :param box: [left, top, right, bottom] 模板坐标
        :return: None
        """
        tmp_coord = {"left": box[0], "top": box[1], "right": box[2], "bottom": box[3]}
        self.data[template].update(tmp_coord)

    def set_size(self, template, size):
        tmp_size = {template: {"width": size[0], "height": size[1]}}
        self.data[template].update(tmp_size)

    def save_coord(self, option, box):
        pass

