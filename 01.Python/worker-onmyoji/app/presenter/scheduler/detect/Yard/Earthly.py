from hiworker import *


class DetectEarthly(DetectImage):
    def __init__(self):
        super(DetectEarthly, self).__init__()

    def is_earthly_map(self):
        """
        现世封魔地图
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("earthly_is_earthly_map")
        return result

    def is_earthly_map_close_button(self):
        """
        现实逢魔地图关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("earthly_is_earthly_map_close_button")
        return result
