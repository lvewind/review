from hiworker import *


class OperateChapter(Win32Click):
    def __init__(self):
        super(OperateChapter, self).__init__()

    def close_chapter_panel(self):
        """
        关闭章节面板
        :return:
        """
        self.click_in_template("chapter_is_chapter_panel_close_button")

    def select_chapter_panel_hard(self):
        """
        选择困难副本
        :return:
        """
        self.click_in_template("chapter_is_chapter_panel_hard_not_selected")

    def select_chapter_panel_simple(self):
        """
        选择简单副本
        :return:
        """
        self.click_in_template("chapter_is_chapter_panel_simple_not_selected")

    def teamup_chapter_panel_hard(self):
        """
        组队困难章节
        :return:
        """
        self.click_in_template("chapter_teamup_chapter_panel_hard")

    def start_chapter_panel(self):
        """
        开始简单副本
        :return:
        """
        self.click_in_template("chapter_start_chapter_panel")

    def slide_chapter_stage_to_top(self):
        """
        向上滑动章节看列表
        :return:
        """
        self.slide_distance_with_template("chapter_slide_up_chapter_stage", 30, 180)

    def slide_chapter_stage_to_bottom(self):
        """
        向下滑动章节列表
        :return:
        """
        self.slide_distance_with_template("chapter_slide_down_chapter_stage", 30, -180)

    def select_chapter_create_team_panel_any(self):
        """
        选中公开队伍
        :return:
        """
        self.click_in_template("chapter_is_chapter_create_team_panel_any_selected")

    def select_chapter_create_team_panel_friend(self):
        """
        选中仅好友
        :return:
        """
        self.click_in_template("chapter_is_chapter_create_team_panel_friend_selected")

    def select_chapter_create_team_panel_only(self):
        """
        选中仅邀请
        :return:
        """
        self.click_in_template("chapter_is_chapter_create_team_panel_only_selected")

    def create_team_chapter_2(self):
        """
        点击创建队伍
        :return:
        """
        self.click_in_template("chapter_create_team_chapter_2")

    def slide_chapter_zone_to_left(self):
        """
        狗粮副本滑动到左边
        :return:
        """
        self.slide_distance_with_template("chapter_slide_chapter_zone_to_left", 400, 50, 8)

    def slide_chapter_zone_to_right(self):
        """
        狗粮副本滑动到右边
        :return:
        """
        self.slide_distance_with_template("chapter_slide_chapter_zone_to_right", -400, 50, 8)

    def confirm_continue_invite_chapter_panel(self):
        """
        确认继续邀请
        :return:
        """
        self.click_in_template("chapter_confirm_invite_chapter_panel")

    def cancel_continue_invite_chapter_panel(self):
        """
        取消继续要请
        :return:
        """
        self.click_in_template("chapter_cancel_invite_chapter_panel")

    def unlock_chapter_cast(self):
        """
        取消阵容锁定
        :return:
        """
        self.click_in_template("chapter_is_chapter_cast_unlock")

    def unlock_chapter_cast_novice(self):
        """
        取消阵容锁定
        :return:
        """
        self.click_in_template("chapter_is_chapter_cast_unlock_novice")

    def lock_chapter_cast(self):
        """
        锁定阵容
        :return:
        """
        self.click_in_template("chapter_is_chapter_cast_lock")

    def lock_chapter_cast_novice(self):
        """
        锁定阵容
        :return:
        """
        self.click_in_template("chapter_is_chapter_cast_lock_novice")

    def open_chapter_change_dog_food_panel(self):
        """
        打开换狗粮场景
        :return:
        """
        self.click_in_template("chapter_open_chapter_change_dog_food_panel")

    def open_chapter_change_dog_food_type_select_panel(self):
        """
        打开狗粮类型选中面板
        :return:
        """
        self.click_in_template("chapter_open_chapter_change_dog_food_type_select_panel")

    def select_chapter_change_dog_food_m_list_button(self):
        """
        选择素材狗粮
        :return:
        """
        self.click_in_template("chapter_is_chapter_change_dog_food_m_list_button")

    def select_chapter_change_dog_food_n_list_button(self):
        """
        选择N卡狗粮
        :return:
        """
        self.click_in_template("chapter_is_chapter_change_dog_food_n_list_button")

    def slide_chapter_dog_list_to_right(self):
        """
        滑动狗粮列表到右边
        :return:
        """
        self.slide_distance_with_template("chapter_slide_chapter_dog_list_to_right", -300, 30)

    def slide_chapter_dog_list_to_left(self):
        """
        滑动狗粮列表到左边
        :return:
        """
        self.slide_distance_with_template("chapter_slide_chapter_dog_list_to_left", 300, 30)

    def quit_chapter_zone(self):
        """
        退出狗粮副本
        :return:
        """
        self.click_in_template("chapter_is_chapter_zone_quit_button")

    def confirm_quit_chapter_zone(self):
        """
        确认退出狗粮副本
        :return:
        """
        self.click_in_template("chapter_is_chapter_zone_quit_confirm")

    def set_chapter_feed_doll_panel_auto_feed_active(self):
        """
        设置樱饼自动喂食
        :return:
        """
        self.click_in_template("chapter_is_chapter_feed_doll_panel_auto_feed_active")

    def open_chapter_feed_doll_panel(self):
        """
        打开狗粮副本内樱饼界面
        :return:
        """
        self.click_in_template("chapter_open_chapter_feed_doll_panel")
