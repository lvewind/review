from hiworker import *


class OperateEarthly(Win32Click):
    def __init__(self):
        super(OperateEarthly, self).__init__()

    def close_earthly_map(self):
        """
        关闭现世逢魔地图
        :return:
        """
        self.click_in_template("earthly_is_earthly_map_close_button")
