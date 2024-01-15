from hiworker import *


class OperateStory(Win32Click):
    def __init__(self):
        super(OperateStory, self).__init__()

    def click_novice_tips_in_yard(self):
        """
        关闭新手提示
        :return:
        """
        self.click_in_template("story_is_novice_tips_in_yard")

    def get_novice_gift_panel_day_1(self):
        """
        获取第一天新手奖励
        :return:
        """
        self.click_in_template("story_get_novice_gift_panel_day_1")

    def click_seimei_technique_1(self):
        """
        关闭晴明教程1
        :return:
        """
        self.click_in_template("story_is_seimei_technique_1")

    def click_to_release_technique_target_dog(self):
        """
        点击教程目标狗粮1
        :return:
        """
        self.click_in_template("story_find_release_technique_target_dog")

    def click_to_release_technique_target_dog_2(self):
        """
       点击教程目标狗粮2
       :return:
       """
        self.click_in_template("story_find_release_technique_target_dog_2")

    def close_novice_tips_panel(self):
        """
        关闭新手提示面板
        :return:
        """
        self.click_in_template("story_close_novice_tips_panel")

    def click_shield_tips(self):
        """
        点击护盾提示
        :return:
        """
        self.click_in_template("story_is_shield_tips")

    def set_playing_movie_accelerate(self):
        """
        设置剧情播放加速
        :return:
        """
        self.click_in_template("story_is_playing_movie")

    def draw_summon_task(self):
        """
        画图召唤
        :return:
        """
        self.slide_distance_with_template("story_draw_summon_task", 30, 384)

    def close_novice_task_close_button(self):
        """
        关闭新手任务
        :return:
        """
        self.click_in_template("story_is_novice_task_close_button")

    def skip_battling_scroll_tips(self):
        """
        跳过战斗行动条提示
        :return:
        """
        self.click_in_template("story_is_battling_scroll_tips")

    def click_shikigami_detail_button_tips(self):
        """
        跳过式神详情提示
        :return:
        """
        self.click_in_template("story_is_shikigami_detail_button_tips")

    def check_shikigami_detail_souls_change_position(self):
        """
        跳过御魂提示
        :return:
        """
        self.click_in_template("story_is_shikigami_detail_souls_change_position_checked")

    def click_shikigami_detail_souls_empty_1(self):
        """
        点击御魂位置1
        :return:
        """
        self.click_in_template("story_is_shikigami_detail_souls_empty_1")

    def click_shikigami_detail_souls_empty_2(self):
        """
        点击御魂位置2
        :return:
        """
        self.click_in_template("story_is_shikigami_detail_souls_empty_2")

    def click_shikigami_detail_souls_empty_3(self):
        """
        点击御魂位置3
        :return:
        """
        self.click_in_template("story_is_shikigami_detail_souls_empty_3")

    def click_shikigami_detail_souls_empty_4(self):
        """
        点击御魂位置4
        :return:
        """
        self.click_in_template("story_is_shikigami_detail_souls_empty_4")

    def click_shikigami_detail_souls_empty_5(self):
        """
        点击御魂位置5
        :return:
        """
        self.click_in_template("story_is_shikigami_detail_souls_empty_5")

    def click_shikigami_detail_souls_empty_6(self):
        """
        点击御魂位置6
        :return:
        """
        self.click_in_template("story_is_shikigami_detail_souls_empty_6")

    def load_shikigami_detail_souls(self):
        """
        装备御魂
        :return:
        """
        self.click_in_template("story_is_shikigami_detail_souls_load_button")

    def quit_shikigami_detail_souls_panel(self):
        """
        退出御魂详情界面
        :return:
        """
        self.click_in_template("story_quit_shikigami_detail_souls_panel")

    def quit_shikigami_panel(self):
        """
        退出式神面板
        :return:
        """
        self.click_in_template("story_quit_shikigami_panel")

    def close_explorer_entrance_tips_panel(self):
        """
        关闭探索入口提示
        :return:
        """
        self.click_in_template("story_is_exploer_entrance_tips_panel_close_button")

    def click_summon_single_button(self):
        """
        单次召唤
        :return:
        """
        self.click_in_template("story_is_summon_single_button")

    def close_yard_approach(self):
        """
        关闭庭院提示
        :return:
        """
        self.click_in_template("story_is_yard_approach")

    def close_voice_extent_download_panel_cancel_button(self):
        """
        关闭语音下载提示
        :return:
        """
        self.click_in_template("story_is_voice_extent_download_panel_cancel_button")

    def close_onmyoji_unlock_panel(self):
        """
        关闭式神锁定面板
        :return:
        """
        self.click_in_template("story_close_onmyoji_unlock_panel")

    def quit_story_scene(self):
        """
        退出剧情场景
        :return:
        """
        self.click_in_template("story_quit_story_scene")

    def cancel_relate_phone_panel(self):
        """
        取消绑定手机界面
        :return:
        """
        self.click_in_template("story_cancel_relate_phone_panel")

    def cancel_jade_card_buy_panel(self):
        """
        关闭勾玉购买面板
        :return:
        """
        self.click_in_template("story_cancel_jade_card_buy_panel")

    def click_empty_area_in_story(self):
        """
        点击空白处
        :return:
        """
        self.click_in_template("story_click_empty_area_in_story")

    def cancel_name_pet_panel(self):
        """
        取消宠物命名
        :return:
        """
        self.click_in_template("story_cancel_name_pet_panel")
