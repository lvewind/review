from hiworker import *


class OperateTeam(Win32Click):
    def __init__(self):
        super(OperateTeam, self).__init__()

    def close_teamup_panel(self):
        """
        关闭组队面板
        :return:
        """
        self.click_in_template("team_is_team_panel_quit_button")

    def select_team_panel_seal(self):
        """
        选择妖气封印
        :return:
        """
        self.click_in_template("team_is_team_panel_seal")

    def select_team_panel_exp(self):
        """
        选择经验怪
        :return:
        """
        self.click_in_template("team_is_team_panel_exp")

    def select_team_panel_coin(self):
        """
        选择金币怪
        :return:
        """
        self.click_in_template("team_is_team_panel_coin")

    def select_team_panel_nen(self):
        """
        选择年兽
        :return:
        """
        self.click_in_template("team_is_team_panel_nen")

    def select_team_panel_kraken(self):
        """
        选择石距
        :return:
        """
        self.click_in_template("team_is_team_panel_kraken")

    def refresh_team_panel(self):
        """
        刷新队伍
        :return:
        """
        self.click_in_template("team_is_team_panel_refresh_button")

    def team_auto_match(self):
        """
        自动匹配
        :return:
        """
        self.click_in_template("team_is_team_panel_auto_macth_button")

    def slide_up_team_list(self):
        """
        上划队伍列表
        :return:
        """
        self.slide_distance_with_template("team_slide_up_team_list", distance_x=50, distance_y=-200)

    def select_team_seal_tiaotiaogege(self):
        """
        选择跳跳哥哥
        :return:
        """
        self.click_in_template("team_is_team_seal_tiaotiaogege")

    def select_team_seal_jiaotu(self):
        """
        选择椒图
        :return:
        """
        self.click_in_template("team_is_team_seal_jiaotu")

    def select_team_seal_gunv(self):
        """
        选择骨女
        :return:
        """
        self.click_in_template("team_is_team_seal_gunv")

    def select_team_seal_egui(self):
        """
        选择饿鬼
        :return:
        """
        self.click_in_template("team_is_team_seal_egui")

    def select_team_seal_erkounv(self):
        """
        选择二口女
        :return:
        """
        self.click_in_template("team_is_team_seal_erkounv")

    def select_team_seal_haifangzhu(self):
        """
        选择海坊主
        :return:
        """
        self.click_in_template("team_is_team_seal_haifangzhu")

    def select_team_seal_guishihei(self):
        """
        选择鬼使黑
        :return:
        """
        self.click_in_template("team_is_team_seal_guishihei")

    def select_team_seal_xiaosongwan(self):
        """选择小松丸"""
        self.click_in_template("team_is_team_seal_xiaosongwan")

    def select_team_seal_rihefang(self):
        """
        选择日和坊
        :return:
        """
        self.click_in_template("team_is_team_seal_rihefang")

    def slide_up_team_seal_list(self):
        """
        上划妖气封印列表
        :return:
        """
        self.slide_distance_with_template("team_slide_up_team_seal_list", distance_x=50, distance_y=-200)

    def slide_down_team_seal_list(self):
        """
        下滑邀请封印列表
        :return:
        """
        self.slide_distance_with_template("team_slide_down_team_seal_list", distance_x=50, distance_y=200)

    def create_team_1(self):
        """
        创建队伍1
        :return:
        """
        self.click_in_template("team_is_create_team_button")

    def create_team_2(self):
        """
        创建队伍二
        :return:
        """
        self.click_in_template("team_is_create_team_button_2")

    def cancel_create_team(self):
        """
        取消创建队伍
        :return:
        """
        self.click_in_template("team_cancel_create_team")

    def select_create_team_panel_any(self):
        """
        选择公开队伍
        :return:
        """
        self.click_in_template("team_is_create_team_panel_any_selected")

    def select_create_team_panel_friend(self):
        """
        选择仅好友队伍
        :return:
        """
        self.click_in_template("team_is_create_team_panel_friend_selected")

    def select_create_team_panel_only(self):
        """
        选择仅邀请队伍
        :return:
        """
        self.click_in_template("team_is_create_team_panel_only_selected")

    def close_cooperation_teamup_panel(self):
        """
        关闭组队面板
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_panel_quit_button")

    def challenge_cooperation_teamup(self):
        """
        挑战
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_challenge_button_yellow")

    def open_bonus_panel_teamup(self):
        """
        打开加成面板
        :return:
        """
        self.click_in_template("explore_open_bonus_panel_teamup")

    def click_invite_teammate_plus_button(self):
        """
        点击邀请加号按钮
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_panel_invite_button")

    def click_invite_teammate_plus_button_right(self):
        """
        点击右边邀请加号按钮
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_panel_invite_button_chapter")

    def click_cooperation_teamup_friend_panel_invite_button(self):
        """
        点击邀请
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_friend_panel_invite_button")

    def click_cooperation_teamup_friend_panel_cancel_button(self):
        """
        点击取消邀请
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_friend_panel_cancel_button")

    def select_cooperation_teamup_friend_panel_friend(self):
        """
        选择需要邀请的好友
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_friend_panel_friend")

    def select_cooperation_teamup_friend_panel_friend_chapter(self):
        """
        选择需要邀请的狗粮好友面板
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_friend_panel_friend_chapter")

    def select_cooperation_teamup_friend_panel_recent(self):
        """
        选择最近面板
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_friend_panel_recent")

    def select_cooperation_teamup_friend_panel_cross(self):
        """
        选择跨服好友
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_friend_panel_cross")

    def select_cooperation_teamup_friend_panel_guild(self):
        """
        选择寮友
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_friend_panel_guild")

    def slide_up_cooperation_friend_list(self):
        """
        上划组队好友列表
        :return:
        """
        self.slide_distance_with_template("team_slide_up_cooperation_friend_list", 50, 20)

    def confirm_quit_cooperation_teamup_panel(self):
        """
        确认退出协战队伍
        :return:
        """
        self.click_in_template("team_is_cooperation_teamup_panel_confirm_quit")

    def change_cooperation_doll_active(self):
        """
        开启协战队伍小纸人
        :return:
        """
        self.click_in_template("team_is_cooperation_doll_active")

    def change_cooperation_cast_lock(self):
        """
        协战队伍锁定阵容
        :return:
        """
        self.click_in_template("team_is_cooperation_cast_lock_up")

    def change_cooperation_cast_lock_longche(self):
        """
        协战队伍锁定阵容
        :return:
        """
        self.click_in_template("team_is_cooperation_cast_lock_up_longche")

    def set_feed_doll_panel_auto_feed_active(self):
        """
        激活自动喂食
        :return:
        """
        self.click_in_template("team_is_feed_doll_panel_auto_feed_active")

    def open_cooperation_feed_doll_panel(self):
        """
        打开自动喂食面板
        :return:
        """
        self.click_in_template("team_open_coorperation_feed_doll_panel")
