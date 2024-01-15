from hiworker import *


class OperateRealmRaid(Win32Click):
    def __init__(self):
        super(OperateRealmRaid, self).__init__()

    def close_realm_raid_panel(self):
        """
        关闭结界突破面板
        :return:
        """
        self.click_in_template("realm_raid_is_realm_raid_panel_close_button")

    def select_realm_raid_panel_person(self):
        """
        选择个人突破
        :return:
        """
        self.click_in_template("realm_raid_is_realm_raid_panel_person")

    def select_guild_realm_raid_panel_guild(self):
        """
        选择寮突破
        :return:
        """
        self.click_in_template("realm_raid_is_realm_raid_panel_guild")

    def refresh_realm_raid(self):
        """
        刷新突破
        :return:
        """
        self.click_in_template("realm_raid_is_realm_raid_refresh_button")

    def refresh_realm_raid_frog(self):
        """
        刷新突破
        :return:
        """
        self.click_in_template("realm_raid_is_realm_raid_refresh_button_frog")

    def confirm_refresh_realm_raid(self):
        """
        确认刷新突破
        :return:
        """
        self.click_in_template("realm_raid_is_refresh_confirm_button")

    def click_realm_raid_target_1(self):
        """
        点击第1个突破
        :return:
        """
        self.click_in_template("realm_raid_click_realm_raid_target_1")

    def click_realm_raid_target_2(self):
        """
        点击第2个突破
        :return:
        """
        self.click_in_template("realm_raid_click_realm_raid_target_2")

    def click_realm_raid_target_3(self):
        """
        点击第3个突破
        :return:
        """
        self.click_in_template("realm_raid_click_realm_raid_target_3")

    def click_realm_raid_target_4(self):
        """
        点击第4个突破
        :return:
        """
        self.click_in_template("realm_raid_click_realm_raid_target_4")

    def click_realm_raid_target_5(self):
        """
        点击第5个突破
        :return:
        """
        self.click_in_template("realm_raid_click_realm_raid_target_5")

    def click_realm_raid_target_6(self):
        """
        点击第6个突破
        :return:
        """
        self.click_in_template("realm_raid_click_realm_raid_target_6")

    def click_realm_raid_target_7(self):
        """
        点击第7个突破
        :return:
        """
        self.click_in_template("realm_raid_click_realm_raid_target_7")

    def click_realm_raid_target_8(self):
        """
        点击第8个突破
        :return:
        """
        self.click_in_template("realm_raid_click_realm_raid_target_8")

    def click_realm_raid_target_9(self):
        """
        点击第9个突破
        :return:
        """
        self.click_in_template("realm_raid_click_realm_raid_target_9")

    def click_guild_realm_raid_target(self, coord: list):
        """
        点击寮突破目标
        :param coord:
        :return:
        """
        self.click_in_circle([coord[0], coord[1] - 20], 30)

    def attack_realm_raid(self, coord: list):
        """
        攻击
        :param coord:
        :return:
        """
        self.click_in_circle(coord)

    def unlock_realm_raid_cast(self):
        """
        解除阵容锁定
        :return:
        """
        self.click_in_template("realm_raid_is_realm_cast_lock")

    def unlock_realm_raid_cast_frog(self):
        """
        解除阵容锁定
        :return:
        """
        self.click_in_template("realm_raid_is_realm_cast_lock_frog")

    def lock_realm_raid_cast(self):
        """
        锁定阵容
        :return:
        """
        self.click_in_template("realm_raid_is_realm_cast_unlock")

    def lock_realm_raid_cast_frog(self):
        """
        锁定阵容
        :return:
        """
        self.click_in_template("realm_raid_is_realm_cast_unlock_frog")

    def unlock_realm_raid_guild_cast(self):
        """
        解除寮突破阵容锁定
        :return:
        """
        self.click_in_template("realm_raid_is_guild_realm_cast_lock")

    def lock_realm_raid_guild_cast(self):
        """
        锁定寮突破阵容
        :return:
        """
        self.click_in_template("realm_raid_is_guild_realm_cast_unlock")

    def slide_up_guild_realm_raid_list(self):
        """
        向上滑动寮突列表
        :return:
        """
        self.slide_distance_with_template("realm_raid_slide_up_guild_realm_raid_list", 20, -400)
