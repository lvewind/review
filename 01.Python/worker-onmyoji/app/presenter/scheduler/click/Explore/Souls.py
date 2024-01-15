from hiworker import *


class OperateSouls(Win32Click):
    def __init__(self):
        super(OperateSouls, self).__init__()

    def quit_souls_zone_panel_quit_button(self):
        """
        退出御魂面板
        :return:
        """
        self.click_in_template("souls_is_souls_zone_select_panel_quit_button")

    def select_souls_zone_orochi(self):
        """
        选择八岐大蛇
        :return:
        """
        self.click_in_template("souls_is_souls_zone_orochi")

    def select_souls_zone_sougenbi(self):
        """
        选择业原火
        :return:
        """
        self.click_in_template("souls_is_souls_zone_sougenbi")

    def select_souls_zone_himiko(self):
        """
        选择卑弥呼
        :return:
        """
        self.click_in_template("souls_is_souls_zone_sun_fall")

    def quit_souls_stage_panel(self):
        """
        退出御魂层数选择界面
        :return:
        """
        self.click_in_template("souls_is_souls_stage_panel_button")

    def select_souls_stage_panel_orochi(self):
        """
        在层数选择界面选择八岐大蛇
        :return:
        """
        self.click_in_template("souls_is_souls_stage_panel_orochi")

    def select_souls_stage_panel_sougenbi(self):
        """
        在层数选择界面选择业原火
        :return:
        """
        self.click_in_template("souls_select_souls_stage_panel_sougenbi")

    def select_souls_stage_panel_himiko(self):
        """
        在层数选择界面选择卑弥呼
        :return:
        """
        self.click_in_template("souls_is_souls_stage_panel_himiko")

    def select_souls_orochi_stage(self, coord):
        """
        选择八岐大蛇层数
        :param coord:
        :return:
        """
        self.click_in_circle(coord, 30)

    def teamup_souls(self):
        """
        御魂组队
        :return:
        """
        self.click_in_template("souls_is_souls_teamup_button")

    def challenge_orochi(self):
        """
        挑战八岐大蛇
        :return:
        """
        self.click_in_template("souls_is_souls_orochi_challenge_button")

    def challenge_sougenbi(self):
        """
        挑战业原火
        :return:
        """
        self.click_in_template("souls_is_souls_sougenbi_challenge_button")

    def challenge_himiko(self):
        """
        挑战卑弥呼
        :return:
        """
        self.click_in_template("souls_is_souls_himiko_challenge_button")

    def unlock_souls_cast(self):
        """
        解除阵容锁定
        :return:
        """
        self.click_in_template("souls_is_souls_cast_lock")

    def lock_souls_cast(self):
        """
        锁定阵容
        :return:
        """
        self.click_in_template("souls_is_souls_cast_unlock")

    def change_souls_auto_challenge(self):
        """
        切换自动挑战
        :return:
        """
        self.click_in_template("souls_is_souls_auto_battle")

    def select_sougenbi_1(self):
        """
        选择贪
        :return:
        """
        self.click_in_template("souls_select_sougenbi_greedy")

    def select_sougenbi_2(self):
        """
        选择嗔
        :return:
        """
        self.click_in_template("souls_select_sougenbi_angry")

    def select_sougenbi_3(self):
        """
        选择痴
        :return:
        """
        self.click_in_template("souls_select_sougenbi_fooly")

    def select_himiko_stage_1(self):
        """
        选择卑弥呼1
        :return:
        """
        self.click_in_template("souls_is_souls_himiko_stage_selected_1")

    def select_himiko_stage_2(self):
        """
        选择卑弥呼2
        :return:
        """
        self.click_in_template("souls_is_souls_himiko_stage_selected_2")

    def select_himiko_stage_3(self):
        """
        选择卑弥呼3
        :return:
        """
        self.click_in_template("souls_is_souls_himiko_stage_selected_3")

    def open_souls_feed_doll_panel(self):
        """
        打开小纸人喂食面板
        :return:
        """
        self.click_in_template("souls_open_souls_feed_doll_panel")
