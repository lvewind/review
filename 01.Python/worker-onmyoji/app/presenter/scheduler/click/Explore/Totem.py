from hiworker import *


class OperateTotem(Win32Click):
    def __init__(self):
        super(OperateTotem, self).__init__()

    def quit_totem_zone_select_panel(self):
        """
        退出御灵选择界面
        :return:
        """
        self.click_in_template("totem_is_totem_zone_select_panel_quit_button")

    def quit_totem_stage_panel(self):
        """
        退出御灵层数界面
        :return:
        """
        self.click_in_template("totem_is_totem_stage_panel_quit_button")

    def select_totem_zone_panel_shenlong(self):
        """
        选择神龙
        :return:
        """
        self.click_in_template("totem_select_totem_zone_panel_shenlong")

    def select_totem_zone_panel_baizhangzhu(self):
        """
        选择白藏主
        :return:
        """
        self.click_in_template("totem_select_totem_zone_panel_baizhangzhu")

    def select_totem_zone_panel_heibao(self):
        """
        选择黑豹
        :return:
        """
        self.click_in_template("totem_select_totem_zone_panel_heibao")

    def select_totem_zone_panel_kongque(self):
        """
        选择孔雀
        :return:
        """
        self.click_in_template("totem_select_totem_zone_panel_kongque")

    def select_totem_stage_panel_shenlong(self):
        """
        选择神龙
        :return:
        """
        self.click_in_template("totem_is_totem_stage_panel_shenlong")

    def select_totem_stage_panel_baizhangzhu(self):
        """
        选择白藏主
        :return:
        """
        self.click_in_template("totem_is_totem_stage_panel_baizhangzhu")

    def select_totem_stage_panel_heibao(self):
        """
        选择黑豹
        :return:
        """
        self.click_in_template("totem_is_totem_stage_panel_heibao")

    def select_totem_stage_panel_kongque(self):
        """
        选择孔雀
        :return:
        """
        self.click_in_template("totem_is_totem_stage_panel_kongque")

    def select_totem_stage_1(self):
        """
        选择一层
        :return:
        """
        self.click_in_template("totem_is_totem_stage_selected_1")

    def select_totem_stage_2(self):
        """
        选择二层
        :return:
        """
        self.click_in_template("totem_is_totem_stage_selected_2")

    def select_totem_stage_3(self):
        """
        选择三层
        :return:
        """
        self.click_in_template("totem_is_totem_stage_selected_3")

    def challenge_totem(self):
        """
        挑战
        :return:
        """
        self.click_in_template("totem_is_totem_challenge_button")

    def unlock_totem_cast(self):
        """
        解锁阵容
        :return:
        """
        self.click_in_template("totem_is_totem_cast_lock")

    def lock_totem_cast(self):
        """
        锁定阵容
        :return:
        """
        self.click_in_template("totem_is_totem_cast_unlock")

    def change_totem_auto_challenge(self):
        """
        切换自动挑战
        :return:
        """
        self.click_in_template("totem_is_totem_auto_battle")
