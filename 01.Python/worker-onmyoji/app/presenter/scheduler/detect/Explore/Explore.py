from hiworker import *


class DetectExplore(DetectImage):
    def __init__(self):
        super(DetectExplore, self).__init__()

    def is_explore(self):
        """
        是否是探索地图
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_explore", 0.7)
        return result

    def is_explore_quit_button(self):
        """
        探索地图退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_explore_quit_button")
        return result

    def is_evo_entrance(self):
        """
        觉醒入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_evo_entrance")
        return result

    def is_soul_entrance(self):
        """
        御魂入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_soul_entrance")
        return result

    def is_realm_raid_entrance(self):
        """
        突破入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_realm_raid_entrance")
        return result

    def is_totem_entrance(self):
        """
        御灵入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_totem_entrance")
        return result

    def is_stories_entrance(self):
        """
        百物语入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_stories_entrance")
        return result

    def is_delegate_entrance(self):
        """
        委派入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_delegate_entrance")
        return result

    def is_secret_zone_entrance(self):
        """
        秘闻入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_secret_zone_entrance")
        return result

    def is_area_boss_entrance(self):
        """
        地鬼入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_area_boss_entrance")
        return result

    def is_tales_entrance(self):
        """
        平安奇谭入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_tales_entrance")
        return result

    def find_bonus_button_in_explore(self):
        """
        查找加成按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("explore_is_bonus_button", check_t=3)
        return result, coord

    def find_chapter_entrance_1(self):
        """
        查找章节1
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_1", 0.9)
        return result, coord

    def find_chapter_entrance_2(self):
        """
        查找章节2
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_2", 0.9)
        return result, coord

    def find_chapter_entrance_3(self):
        """
        查找章节3
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_3", 0.9)
        return result, coord

    def find_chapter_entrance_4(self):
        """
        查找章节4
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_4", 0.9)
        return result, coord

    def find_chapter_entrance_5(self):
        """
        查找章节5
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_5", 0.9)
        return result, coord

    def find_chapter_entrance_6(self):
        """
        查找章节6
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_6", 0.9)
        return result, coord

    def find_chapter_entrance_7(self):
        """
        查找章节7
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_7", 0.9)
        return result, coord

    def find_chapter_entrance_8(self):
        """
        查找章节8
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_8", 0.9)
        return result, coord

    def find_chapter_entrance_9(self):
        """
        查找章节9
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_9", 0.9)
        return result, coord

    def find_chapter_entrance_10(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_10", 0.9)
        return result, coord

    def find_chapter_entrance_11(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_11", 0.9)
        return result, coord

    def find_chapter_entrance_12(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_12", 0.9)
        return result, coord

    def find_chapter_entrance_13(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_13", 0.9)
        return result, coord

    def find_chapter_entrance_14(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_14", 0.9)
        return result, coord

    def find_chapter_entrance_15(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_15", 0.9)
        return result, coord

    def find_chapter_entrance_16(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_16", 0.9)
        return result, coord

    def find_chapter_entrance_17(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_17", 0.9)
        return result, coord

    def find_chapter_entrance_18(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_18", 0.9)
        return result, coord

    def find_chapter_entrance_19(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_19", 0.9)
        return result, coord

    def find_chapter_entrance_20(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_20", 0.9)
        return result, coord

    def find_chapter_entrance_21(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_21", 0.9)
        return result, coord

    def find_chapter_entrance_22(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_22", 0.9)
        return result, coord

    def find_chapter_entrance_23(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_23", 0.9)
        return result, coord

    def find_chapter_entrance_24(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_24", 0.9)
        return result, coord

    def find_chapter_entrance_25(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_25", 0.9)
        return result, coord

    def find_chapter_entrance_26(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_26", 0.9)
        return result, coord

    def find_chapter_entrance_27(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_27", 0.9)
        return result, coord

    def find_chapter_entrance_28(self):
        """
        查找章节
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_chapter_entrance_28", 0.9)
        return result, coord

    def is_need_to_set_realm(self):
        """
        需要设置结界
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_need_to_set_realm", 0.65)
        return result

    def is_kraken_in_explore(self):
        """
        查找石距
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_kraken_in_explore")
        return result

    def find_seal_in_explore(self):
        """
        查找妖气封印
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_seal_in_explore")
        return result, coord

    def find_prize_box_in_explore(self):
        """
        查找宝箱
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_prize_box_in_explore")
        return result, coord

    def is_seal_panel_in_explore(self):
        """
        妖气界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_seal_panel_in_explore")
        return result

    def is_seal_panel_in_explore_challenge_button(self):
        """
        妖气界面挑战按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("explore_is_seal_panel_in_explore_challenge_button")
        return result
