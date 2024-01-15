from hiworker import *


class OperateSummon(Win32Click):
    def __init__(self):
        super(OperateSummon, self).__init__()

    def click_free_summon_button(self):
        """
        免费召唤
        :return:
        """
        self.click_in_template("summon_is_summon_free_button")

    def click_summon_normal_confirm_button(self):
        """
        确认普通召唤
        :return:
        """
        self.click_in_template("summon_is_normal_summon_confirm_button")

    def click_summon_normal_button(self):
        """
        普通召唤
        :return:
        """
        self.click_in_template("summon_is_normal_summon_button")

    def click_summon_normal_again_button(self):
        """
        再次普通召唤
        :return:
        """
        self.click_in_template("summon_is_normal_summon_again_button")

    def click_summon_mystery_button(self):
        """
        神秘召唤
        :return:
        """
        self.click_in_template("summon_is_summon_mystery_button")

    def close_summon_mystery_buy_amulet_panel(self):
        """
        关闭神秘召唤界面
        :return:
        """
        self.click_in_template("summon_close_summon_mystery_buy_amulet_panel")

    def skip_summon_share(self):
        """
        跳过分享
        :return:
        """
        self.click_in_template("summon_skip_summon_share")

    def click_summon_back_button(self):
        """
        从召唤返回
        :return:
        """
        self.click_in_template("summon_is_summon_back_button")

    def quit_summon_room(self):
        """
        退出召唤房间
        :return:
        """
        self.click_in_template("summon_is_summon_room_quit_button")

    def click_summon_confirm_button(self):
        """
        确认神秘召唤
        :return:
        """
        self.click_in_template("summon_is_summon_confirm_button")
