from hiworker import *


class DetectBonus(DetectImage):
    def __init__(self):
        super(DetectBonus, self).__init__()

    def is_bonus_panel(self):
        """
        是否存在加成界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bonus_is_bonus_panel")
        return result

    def find_bonus_evo(self):
        """
        查找觉醒加成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bonus_find_bonus_evo", 0.9)
        return result, coord

    def find_bonus_souls(self):
        """
        查找御魂加成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bonus_find_bonus_souls", 0.9)
        return result, coord

    def find_bonus_coin_50(self):
        """
        查找金币50加成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bonus_find_bonus_coin_50", 0.9)
        return result, coord

    def find_bonus_coin_100(self):
        """
        查找金币100加成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bonus_find_bonus_coin_100", 0.9)
        return result, coord

    def find_bonus_exp_50(self):
        """
        查找经验50加成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bonus_find_bonus_exp_50", 0.9)
        return result, coord

    def find_bonus_exp_100(self):
        """
        查找经验100加成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bonus_find_bonus_exp_100", 0.9)
        return result, coord

    def is_bonus_on(self, coord: list):
        """
        判断加成是否开启
        :param coord:
        :return:
        """
        return self.find_color_with_point_ext_area(coord, [12, 12, 12, 12], [243, 238, 193], tolerance=5)

    def is_new_area_bonus(self):
        """
        是否存在额外加成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bonus_is_new_area_bonus")
        return result
