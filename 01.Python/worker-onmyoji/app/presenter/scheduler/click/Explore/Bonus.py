from hiworker import *


class OperateBonus(Win32Click):
    def __init__(self):
        super(OperateBonus, self).__init__()

    def change_bonus_status(self, coord: list):
        """
        点击变更加成状态
        :param coord:
        :return:
        """
        self.click_in_circle(coord)

    def close_bonus_panel(self):
        """
        关闭加成面板
        :return:
        """
        self.click_in_template("bonus_close_bonus_panel")

    def slide_up_bonus_list(self):
        """
        向上滑动加成
        :return:
        """
        self.slide_distance_with_template("bonus_slide_up_bonus_list", 30, -80)

    def slide_down_bonus_list(self):
        """
        向下滑动加成
        :return:
        """
        self.slide_distance_with_template("bonus_slide_down_bonus_list", 30, 80)
