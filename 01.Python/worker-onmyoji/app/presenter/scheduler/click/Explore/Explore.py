from hiworker import *


class OperateExplore(Win32Click):
    def __init__(self):
        super(OperateExplore, self).__init__()

    def quit_explore(self):
        """
        退出探索地图
        :return:
        """
        self.click_in_template("explore_is_explore_quit_button")

    def open_evo(self):
        """
        打开觉醒
        :return:
        """
        self.click_in_template("explore_is_evo_entrance")

    def open_souls(self):
        """
        打开御魂
        :return:
        """
        self.click_in_template("explore_is_soul_entrance", sleep_after_sleep=2)

    def open_realm_raid(self):
        """
        打开突破
        :return:
        """
        self.click_in_template("explore_is_realm_raid_entrance")

    def open_totem(self):
        """
        打开御灵
        :return:
        """
        self.click_in_template("explore_is_totem_entrance")

    def open_stories(self):
        """
        打开平安百物语
        :return:
        """
        self.click_in_template("explore_is_stories_entrance")

    def open_delegate(self):
        """
        打开式神委派
        :return:
        """
        self.click_in_template("explore_is_delegate_entrance")

    def open_secret_zone(self):
        """
        打开秘闻
        :return:
        """
        self.click_in_template("explore_is_secret_zone_entrance")

    def open_area_boss(self):
        """
        打开地域鬼王
        :return:
        """
        self.click_in_template("explore_is_area_boss_entrance")

    def open_tales(self):
        """
        打开平安奇谭
        :return:
        """
        self.click_in_template("explore_is_tales_entrance")

    def open_bonus_panel_explore(self):
        """
        打开加成面板
        :return:
        """
        self.click_in_template("explore_is_bonus_button")

    def open_chapter_panel(self, coord):
        """
        打开狗粮面板
        :param coord:
        :return:
        """
        self.click_in_circle([coord[0], coord[1] + 40], 30)

    def click_seal_panel_in_explore_challenge_button(self):
        """
        挑战妖气封印
        :return:
        """
        self.click_in_circle("explore_is_seal_panel_in_explore_challenge_button")
