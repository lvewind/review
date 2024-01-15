import os
import zipfile

import numpy
import cv2


class InitImage:
    def __init__(self,
                 img_path="data/image/",
                 zip_file="64.zip",
                 zip_pwd="U2FsdGVkX1+r0PadCFzr1UrxWnUiM9Clic9C+ze90dY=",
                 login_image_path="data/user/login_img/",
                 team_up_image_path="data/user/teamup_img/"
                 ):
        """
        初始化图片数据类
        """
        self.path = img_path
        self.zip_file = zip_file
        self.zip_pwd = zip_pwd
        self.login_image_path = login_image_path,
        self.team_up_image_path = team_up_image_path
        self.data = {}

    def set_option(self, img_path: None, zip_file: None, zip_pwd: None):
        """
        设置图像数据配置项目
        :param img_path:  str 图像文件目录
        :param zip_file: str 图像压缩包名称
        :param zip_pwd: str 图像压缩包密码
        :return: None
        """
        if img_path:
            self.path = img_path
        if zip_file:
            self.zip_file = zip_file
        if zip_pwd:
            self.zip_pwd = zip_pwd

    def load_all_image(self, from_zip=True):
        """
        加载所有图像数据
        :param from_zip: bool 是否从压缩包加载图像数据
        :return: bool 加载成功True, 加载失败False
        """
        self.load_login_image()
        self.load_teammate_img()
        if from_zip:
            return self.load_image_from_zip()
        else:
            return self.load_image_from_folder()

    def load_login_image(self):
        """
         加载登录图像
        :return: bool 加载成功返回True, 失败False
        """
        path = "data/user/login_img/"
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            return False
        else:
            img_file_list = os.listdir(path)
            for img_file_name in img_file_list:
                if ".png" in img_file_name:
                    template_name = img_file_name[0:len(img_file_name) - 4]
                    template_dict = {template_name: cv2.imread(path + img_file_name)}
                    self.data.update(template_dict)
            return True

    def load_teammate_img(self):
        """
         加载队友图像
        :return: bool 加载成功返回True, 失败False
        """
        path = "data/user/teamup_img/"
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            return False
        else:
            img_file_list = os.listdir(path)
            for img_file_name in img_file_list:
                if ".png" or ".PNG" in img_file_name:
                    template_name = img_file_name[0:len(img_file_name) - 4]
                    template_dict = {template_name: cv2.imread(path + img_file_name)}
                    self.data.update(template_dict)
            return True

    def load_image_from_folder(self):
        """
         从文件夹加载图像数据
        :return: bool 加载成功返回True, 失败False
        """
        if not os.path.exists(self.path):
            os.makedirs(self.path, exist_ok=True)
            return False
        else:
            img_file_list = os.listdir(self.path)
            for img_file_name in img_file_list:
                if ".png" in img_file_name:
                    template_name = img_file_name[0:len(img_file_name) - 4]
                    template_dict = {template_name: cv2.imread(self.path + img_file_name)}
                    self.data.update(template_dict)
            self.load_login_image()
            self.load_teammate_img()
            return True

    def load_image_from_zip(self):
        """
         从压缩包加载图像数据
        :return: bool 加载成功返回True, 失败False
        """
        if not os.path.exists(self.path):  # 目录不存在，创建目录
            os.makedirs(self.path, exist_ok=True)
            return False
        elif os.path.exists(self.path + self.zip_file):
            zf = zipfile.ZipFile(self.path + self.zip_file)
            img_file_list = zf.namelist()
            # 解压文件并读取内容转为字典
            for img_file_name in img_file_list:
                if ".png" in img_file_name:
                    source_binary = zf.read(img_file_name, pwd=self.zip_pwd.encode('utf-8'))
                    image_binary = numpy.asarray(bytearray(source_binary), dtype="uint8")
                    template_name = img_file_name[0:len(img_file_name) - 4]
                    template_dict = {template_name: cv2.imdecode(image_binary, cv2.IMREAD_COLOR)}
                    self.data.update(template_dict)
            self.load_login_image()
            self.load_teammate_img()
            return True
        else:
            return False

    def read_template(self, template_name):
        """
        读取图模板的图片数据
        :param template_name: 模板名称
        :return: CV矩阵数据
        """
        return self.data.get(template_name, False)

