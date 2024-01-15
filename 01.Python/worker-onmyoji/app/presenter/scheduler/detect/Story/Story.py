from hiworker import *


class DetectStory(DetectImage):
    def __init__(self):
        super(DetectStory, self).__init__()

    def find_npc_prompt_in_yard(self):
        """
        庭院查找NPC提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_find_npc_prompt_in_yard")
        return result, coord

    def find_npc_prompt_with_hand_in_yard(self):
        """
        庭院查找NPC提示的"手"图标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_npc_prompt_with_hand_in_yard")
        return result, coord

    def find_npc_prompt_in_story(self):
        """
        剧情中查找NPC提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_npc_prompt_in_story")
        return result, coord

    def find_npc_prompt_in_story_2(self):
        """
        剧情中查找NPC提示2
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_npc_prompt_in_story_2")
        return result, coord

    def find_npc_prompt_in_story_3(self):
        """
        剧情中查找NPC提示3
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_npc_prompt_in_story_3")
        return result, coord

    def find_npc_prompt_in_story_with_tips(self):
        """
        剧情中查找NPC提示标签
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_npc_prompt_in_story_with_tips")
        return result, coord

    def is_playing_movie(self):
        """
        播放剧情
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_playing_movie")
        return result

    def is_playing_movie_accelerate(self):
        """
        剧情已加速
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_playing_movie_accelerate")
        return result

    def find_fox_dog_prompt_in_yard(self):
        """
        庭院查找小白提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_fox_dog_prompt_in_yard")
        return result, coord

    def is_novice_tips_in_yard(self):
        """
        庭院查找新手提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_novice_tips_in_yard")
        return result

    def is_novice_gift_panel(self):
        """
        新手礼包界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_novice_gift_panel")
        return result

    def is_novice_gift_panel_got_day_1(self):
        """
        新手礼包界面第一天
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_novice_gift_panel_got_day_1")
        return result

    def is_novice_gift_panel_got_day_2(self):
        """
        新手礼包界面第二天
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_novice_gift_panel_got_day_2")
        return result

    # def is_novice_gift_panel_got_day_3(self):
    #     result, coord, max_similarity = self.find_in_template_area("story_is_novice_gift_panel_got_day_3")
    #     return  result
    #
    # def is_novice_gift_panel_got_day_4(self):
    #     result, coord, max_similarity = self.find_in_template_area("story_is_novice_gift_panel_got_day_4")
    #     return  result
    #
    # def is_novice_gift_panel_got_day_5(self):
    #     result, coord, max_similarity = self.find_in_template_area("story_is_novice_gift_panel_got_day_5")
    #     return  result
    #
    # def is_novice_gift_panel_got_day_6(self):
    #     result, coord, max_similarity = self.find_in_template_area("story_is_novice_gift_panel_got_day_6")
    #     return  result
    #
    # def is_novice_gift_panel_got_day_7(self):
    #     result, coord, max_similarity = self.find_in_template_area("story_is_novice_gift_panel_got_day_7")
    #     return  result
    #
    # def is_novice_gift_panel_got_day_8(self):
    #     result, coord, max_similarity = self.find_in_template_area("story_is_novice_gift_panel_got_day_8")
    #     return  result

    def is_novice_task_panel(self):
        """
        新手任务面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_novice_task_panel")
        return result

    def find_novice_task_accept_button(self):
        """
        新手任务领取按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_novice_task_accept_button")
        return result, coord

    def find_novice_task_get_prize_button(self):
        """
        新手任务奖励领取按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_novice_task_get_prize_button")
        return result, coord

    def find_novice_task_daruma_prize(self):
        """
        新手任务达摩奖励
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("story_find_novice_task_daruma_prize", 0.9)
        return result, coord

    def is_novice_task_close_button(self):
        """
        新手任务关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_novice_task_close_button")
        return result

    def find_skip_dialog_button(self):
        """
        跳过对话按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_skip_dialog_button")
        return result, coord

    def find_skip_shikigami_cv_button(self):
        """
        跳过动画按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_skip_shikigami_cv_button")
        return result, coord

    def is_click_to_select_technique_tips(self):
        """
        新手教程技能提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_click_to_select_technique_button")
        return result

    def is_click_to_release_technique_target_tips(self):
        """
        新手教程释放技能提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_click_to_release_technique_target_button")
        return result

    def find_release_technique_target_dog_1(self):
        """
        新手教程点怪提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_release_technique_target_dog")
        return result, coord

    def find_release_technique_target_dog_2(self):
        """
        新手教程点怪提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_release_technique_target_dog_2")
        return result, coord

    def find_release_technique_target_guiqing(self):
        """
        新手教程点怪提示
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("story_find_release_technique_target_guiqing", 0.7)
        return result, coord

    def is_novice_tips_panel(self):
        """
        新手提示面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_novice_tips_panel")
        return result

    def is_shield_tips(self):
        """
        护盾技能提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shield_tips")
        return result

    def is_shield_cd_two_second(self):
        """
        护盾技能cd冷却2
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shield_cd_toe_second")
        return result

    def find_release_shield_target(self):
        """
        查找护盾释放目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_release_shield_target")
        return result, coord

    def is_technique_cd_tips(self):
        """
        技能CD提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_technique_cd_tips")
        return result

    def is_technique_active_1(self):
        """
        技能激活1
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_technique_active_1")
        return result

    def is_summon_with_hand_tips_in_yard(self):
        """
        庭院召唤提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_summon_with_hand_tips")
        return result

    def is_summon_with_hand_tips_in_summon_room(self):
        """
        召唤房间召唤提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_summon_with_hand_tips_in_summon_room")
        return result

    def is_summon_by_jade_with_hand_tips_in_summon_room(self):
        """
        勾玉召唤提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_summon_by_jade_with_hand_tips_in_summon_room")
        return result

    def is_summon_normal_with_hand_tips_in_summon_room(self):
        """
        普通召唤提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_summon_normal_with_hand_tips_in_summon_room")
        return result,

    def is_summon_panel_in_summon_room(self):
        """
        召唤界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_summon_panel_in_summon_room")
        return result

    def is_battling_scroll_tips(self):
        """
        行动条提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_battling_scroll_tips")
        return result

    def is_guguniao_turn(self):
        """
        咕咕鸟回合
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_guguniao_turn")
        return result

    def find_a_battling_target(self):
        """
        查找战斗目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_a_battling_target")
        return result, coord

    def is_seimei_position(self):
        """
        是否有晴明
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_seimei_position")
        return result

    def is_technique_1(self):
        """
        技能是否存在
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_technique_1")
        return result

    def is_technique_2(self):
        """
        技能是否存在
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_technique_2")
        return result

    def is_technique_3(self):
        """
        技能是否存在
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_technique_3")
        return result

    def is_ghost_fire_tips(self):
        """
        鬼火条提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_ghost_fire_tips")
        return result

    def is_ghost_fire_tips_2(self):
        """
        鬼火条提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_ghost_fire_tips_2")
        return result

    def is_ghost_fire_tips_3(self):
        """
        鬼火条提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_ghost_fire_tips_3")
        return result

    def is_has_three_ghost_fire(self):
        """
        3点以上鬼火
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_has_three_ghost_fire", 0.925)
        return result

    def is_xuenv_tips_hand(self):
        """
        雪女提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_xuenv_tips_hand")
        return result

    def find_need_three_ghost_fire(self):
        """
        查找需要三点鬼火提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_need_three_ghost_fire")
        return result, coord

    def find_seimei_vision(self):
        """
        晴明视角图标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_seimei_vision")
        return result, coord

    def find_seimei_vision_half_bottom(self):
        """
        清明视角图标 半个
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_seimei_vision_half_bottom")
        return result, coord

    def find_npc_question_mark(self):
        """
        剧情中的问号
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_npc_question_mark")
        return result, coord

    def is_seimei_technique_1(self):
        """
        晴明技能
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_seimei_technique_1")
        return result

    def is_seimei_technique_3(self):
        """
        晴明技能
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_seimei_technique_3")
        return result

    def is_voice_extent_download_panel(self):
        """
        语音扩展包下载提示界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_voice_extent_download_panel")
        return result

    def is_voice_extent_download_panel_cancel_button(self):
        """
        语音扩展包取消按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_voice_extent_download_panel_cancel_button")
        return result, coord

    def is_shikigami_button_tips(self):
        """
        式神按键提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_button_tips")
        return result

    def is_shikigami_detail_button_tips(self):
        """
        事情详情提示
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("story_is_shikigami_detail_button_tips")
        return result

    def is_shikigami_detail_panel(self):
        """
        式神详情面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_panel")
        return result

    # def is_shikigami_panel(self):
    #     result, coord, max_similarity = self.find_in_template_area("story_is_shikigami_panel")
    #     return result

    def is_shikigami_detail_souls_button_tips(self):
        """
        式神御魂提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_button_tips")
        return result

    def is_shikigami_detail_souls_change_button_tips(self):
        """
        御魂更改提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_change_button_tips")
        return result

    def is_shikigami_detail_souls_change_panel(self):
        """
        御魂详情面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_change_panel")
        return result

    def is_shikigami_detail_souls_change_panel_tips(self):
        """
        御魂变更面板提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_change_panel_tips")
        return result

    def is_shikigami_detail_souls_change_position_checked(self):
        """
        御魂位置选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_change_position_checked")
        return result

    def is_shikigami_detail_souls_load_button(self):
        """
        御魂装备按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_load_button")
        return result

    def is_shikigami_detail_souls_empty_1(self):
        """
        御魂为空
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_1")
        return result

    def is_shikigami_detail_souls_empty_2(self):
        """
        御魂为空
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_2")
        return result

    def is_shikigami_detail_souls_empty_3(self):
        """
        御魂为空
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_3")
        return result

    def is_shikigami_detail_souls_empty_4(self):
        """
        御魂为空
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_4")
        return result

    def is_shikigami_detail_souls_empty_5(self):
        """
        御魂为空
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_5")
        return result

    def is_shikigami_detail_souls_empty_6(self):
        """
        御魂为空
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_6")
        return result

    def is_shikigami_detail_souls_empty_selected_1(self):
        """
        御魂为空被选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_selected_1")
        return result

    def is_shikigami_detail_souls_empty_selected_2(self):
        """
        御魂为空被选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_selected_2")
        return result

    def is_shikigami_detail_souls_empty_selected_3(self):
        """
        御魂为空被选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_selected_3")
        return result

    def is_shikigami_detail_souls_empty_selected_4(self):
        """
        御魂为空被选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_selected_4")
        return result

    def is_shikigami_detail_souls_empty_selected_5(self):
        """
        御魂为空被选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_selected_5")
        return result

    def is_shikigami_detail_souls_empty_selected_6(self):
        """
        御魂为空被选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_detail_souls_empty_selected_6")
        return result

    def find_souls_in_shikigami_panel(self):
        """
        在式神面板查找御魂
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_souls_in_shikigami_panel")
        return result, coord

    def find_story_task_finish_in_yard_1(self):
        """
        庭院查找任务完成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_story_task_finish_in_yard_1")
        return result, coord

    def find_story_task_finish_in_yard_2(self):
        """
        庭院查找任务完成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_story_task_finish_in_yard_2")
        return result, coord

    def find_exclamation_marks_in_yard(self):
        """
        庭院查找感叹号
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_find_exclamation_marks_in_yard")
        return result, coord

    def is_explore_entrance_tips_panel(self):
        """
        探索入口提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_exploer_entrance_tips_panel")
        return result

    def is_souls_entrance_tips_panel(self):
        """
        御魂入口提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_souls_entrance_tips_panel")
        return result

    def is_entrance_tips_panel_common(self):
        """
        入口提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_entrance_tips_panel_common")
        return result

    def is_tips_big_panel(self):
        """
        提示大面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_tips_big_panel")
        return result

    def is_explore_entrance_tips_panel_close_button(self):
        """
        探索入口提示关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_exploer_entrance_tips_panel_close_button")
        return result

    def is_summon_all_button(self):
        """
        碎片召唤所有按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_summon_all_button")
        return result

    def is_summon_single_button(self):
        """
        碎片单次召唤按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_summon_single_button")
        return result

    def is_yard_approach(self):
        """
        庭院被点近了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_yard_approach")
        return result

    def find_unlock_new_chapter_tips(self):
        """
        查找新章节解锁提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_unlock_new_chapter_tips")
        return result, coord

    def find_tip_with_hand(self):
        """
        查找提示手
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("story_find_tip_with_hand", 0.9)
        return result, coord

    def is_story_scene(self):
        """
        剧情场景
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_story_scene")
        return result

    def find_battle_button_in_story_scene(self):
        """
        剧情场景中查找战斗图标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_battle_button_in_story_scene")
        return result, coord

    def find_technique_target_common(self):
        """
        查找技能释放目标
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("story_find_technique_target_common", 0.8)
        return result, coord

    def is_shikigami_souls_panel(self):
        """
        式神御魂面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_shikigami_souls_panel")
        return result

    def is_onmyoji_unlock_panel(self):
        """
        阴阳师解锁界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_onmyoji_unlock_panel")
        return result

    def is_relate_phone_panel(self):
        """
        手机绑定界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_relate_phone_panel")
        return result

    def is_jade_card_buy_panel(self):
        """
        勾玉卡购买面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_jade_card_buy_panel")
        return result

    def is_auto_battle_lock(self):
        """
        自动战斗锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_auto_battle_lock")
        return result

    def is_name_pet_panel(self):
        """
        宠物命名界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("story_is_name_pet_panel")
        return result
