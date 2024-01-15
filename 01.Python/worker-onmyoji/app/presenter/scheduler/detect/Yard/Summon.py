from hiworker import *


class DetectSummon(DetectImage):
    def __init__(self):
        super(DetectSummon, self).__init__()

    def is_summon_room(self):
        """
        召唤房间
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_room")
        return result

    def is_summon_room_quit_button(self):
        """
        召唤房间退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_room_quit_button")
        return result

    def is_summon_normal_button(self):
        """
        普通召唤按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_normal_summon_button")
        return result

    def is_summon_normal_confirm_button(self):
        """
        普通召唤确认按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_normal_summon_confirm_button")
        return result

    def is_summon_normal_again_button(self):
        """
        普通召唤再次召唤
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_normal_summon_again_button")
        return result

    def is_summon_free_button(self):
        """
        免费召唤按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_free_button", 0.9)
        return result

    def is_summon_mystery_button(self):
        """
        蓝票召唤按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_mystery_button")
        return result

    def is_summon_mystery_one(self):
        """
        单词召唤
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_mystery_one")
        return result

    def is_summon_mystery_one_selected(self):
        """
        单次召唤界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_mystery_one_selected")
        return result

    def is_summon_mystery_ten(self):
        """
        十连召唤
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_mystery_ten")
        return result

    def is_summon_mystery_ten_selected(self):
        """
        十连召唤界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_mystery_ten_selected", 0.985)
        return result

    def is_summon_mystery_panel_back_button(self):
        """
        召唤界面返回按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_mystery_panel_back_button")
        return result

    def is_summon_mystery_buy_amulet_panel(self):
        """
        购买蓝票提示界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_mystery_buy_amulet_panel")
        return result

    def is_summon_back_button(self):
        """
        召唤界面返回按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_back_button")
        return result

    def is_summon_share_button(self):
        """
        召唤分享按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_share_button")
        return result

    def is_summon_ten_finished(self):
        """
        十连召唤完成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_ten_finished")
        return result

    def is_summon_confirm_button(self):
        """
        召唤确认按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("summon_is_summon_confirm_button")
        return result
