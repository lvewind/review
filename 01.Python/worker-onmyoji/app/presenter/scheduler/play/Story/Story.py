from ..Common import *
from ..Explore.Chapter import PlayChapter
from ..Explore.RealmRaid import PlayRealmRaid
import copy


class PlayStory(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayStory, self).__init__(play_input)
        # 御魂位状态
        self.is_shikigami_detail_souls_set_1 = False
        self.is_shikigami_detail_souls_set_2 = False
        self.is_shikigami_detail_souls_set_3 = False
        self.is_shikigami_detail_souls_set_4 = False
        self.is_shikigami_detail_souls_set_5 = False
        self.is_shikigami_detail_souls_set_6 = False
        self.souls_novice_done = False
        self.summon_novice_finish = False
        self.chapter = PlayChapter(play_input)
        self.realm_raid = PlayRealmRaid(play_input)
        self.chapter_run_time_preset = 0
        self.is_after_shikigami_upgrade = False
        self.last_chapter = 0

    def run(self):
        self.chapter.play_input = self.play_input
        self.set_default_prop()
        self.set_run_status_default()
        while not self.stop_status:
            # 检测聊天窗口和悬赏封印
            self.check_chat_panel()
            if not self.stop_flag:
                # 正在探索副本
                if self.chapter.isRunning():
                    self.sleep_in_run()

                # 正在结界突破
                elif self.realm_raid.isRunning():
                    self.sleep_in_run()

                # 探索副本完成，判断是否需要转到结界突破
                elif self.chapter.is_finished:
                    # 需要执行结界突破
                    if self.product.story_realm_raid:
                        # 结界突破已完成
                        if self.realm_raid.is_finished:
                            # 解除探索副本完成状态
                            self.chapter.is_finished = False
                            # 解除结界突破完成状态
                            self.realm_raid.is_finished = False
                            # 解除剧情锁定
                            self.is_story_lock = False
                        else:
                            self.run_realm_raid(3)
                    else:
                        self.chapter.is_finished = False
                        self.is_story_lock = False

                # 剧情锁定
                elif self.is_story_lock:
                    if self.is_explore():
                        # 狗粮已运行
                        if self.chapter.isRunning():
                            pass
                        # 狗粮未运行
                        else:
                            signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
                            signal_run_list.set_current_operation.emit(self.run_id, "开启狗粮")
                            # 指定探索副本已找到
                            if self.find_assign_chapter():
                                self.run_chapter(self.product.chapter_stage)

                            else:
                                # 指定探索副本未找到,进入最后的探索副本
                                self.last_chapter = self.find_last_chapter()
                                self.run_chapter(self.last_chapter)
                    elif self.is_yard():
                        signal_run_list.set_current_scene.emit(self.run_id, "庭院")
                        signal_run_list.set_current_operation.emit(self.run_id, "前往探索")
                        if self.is_explore_entrance():
                            self.open_explore()
                        elif self.is_tips_big_panel():
                            self.close_explorer_entrance_tips_panel()
                        elif self.is_yard_approach():
                            self.close_yard_approach()
                        else:
                            result, coord = self.find_skip_shikigami_cv_button()  # 跳过式神介绍
                            if result:
                                signal_run_list.set_current_operation.emit(self.run_id, "跳过式神介绍")
                                self.click_in_circle([coord[0] - 500, coord[1] - 300], 100)
                            else:
                                self.slide_yard_to_right()
                    elif self.is_story_scene():
                        signal_run_list.set_current_scene.emit(self.run_id, "剧情场景")
                        signal_run_list.set_current_operation.emit(self.run_id, "退出剧情场景")
                        self.quit_story_scene()
                # 体力用尽
                elif self.chapter.ap_use_up:
                    if self.product.ap_use_up_restart:
                        self.set_run_list_scheduler_sleep(86400, close_game=self.product.ap_use_up_close_game)
                    else:
                        self.set_run_list_scheduler_stop(close_game=self.product.ap_use_up_close_game)
                else:
                    # 执行剧情
                    play_name_second = self.product.play_name_second
                    if play_name_second == "story_step_1":
                        self.run_story_step_1()
                    elif play_name_second == "story_step_2":
                        pass
            else:
                self .processing_stop()
            self.sleep_in_run()

    def run_story_step_1(self):
        if self.is_novice_tips_panel():
            self.close_novice_tips_panel()
        # 剧情场景
        elif self.is_story_scene():
            self.processing_story_scene()
        # 庭院中
        elif self.is_yard():
            signal_run_list.set_current_scene.emit(self.run_id, "庭院")
            self.souls_novice_done = False
            self.summon_novice_finish = False
            # 任务或提示大界面
            if self.is_tips_big_panel():
                self.processing_tips_big_panel()

            # 扩展语音包下载界面
            elif self.is_voice_extent_download_panel():
                self.close_voice_extent_download_panel_cancel_button()
            elif self.is_name_pet_panel():
                self.cancel_name_pet_panel()
            elif self.is_relate_phone_panel():
                self.cancel_relate_phone_panel()
            elif self.is_bind_phone_panel():
                self.open_bind_phone_input_panel()
            elif self.is_bind_phone_input_panel():
                self.cancel_bind_phone_input_panel()

            else:
                self .processing_novice_special_in_yard()
        elif self.is_battle_ready():
            self.set_battle_ready()
        # 战斗场景
        elif self.is_battle_battling():
            signal_run_list.set_current_scene.emit(self.run_id, "战斗中")
            self .processing_novice_in_battling()
        # 式神御魂界面
        elif self.is_shikigami_souls_panel():
            self.processing_shikigami_souls_panel()

        # 战斗奖励
        elif self.is_battle_win_prize_daruma() or self.is_battle_goods_info_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "战斗奖励")
            self.skip_battle_win(random.randint(1, 3))
        # 战斗失败
        elif self.is_battle_failed_drum():
            self.processing_battle_failed()
            self.is_story_lock = True
        # 过场动画
        elif self.is_playing_movie():
            signal_run_list.set_current_scene.emit(self.run_id, "过场动画")
            signal_run_list.set_current_operation.emit(self.run_id, "看动画")
            self.set_playing_movie_accelerate()
        elif self.is_onmyoji_unlock_panel():
            self.close_onmyoji_unlock_panel()
        # 探索地图中
        elif self.is_explore():
            signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
            signal_run_list.set_current_operation.emit(self.run_id, "退出探索地图")
            self.quit_explore()
        # 召唤界面
        elif self.is_summon_panel_in_summon_room():
            signal_run_list.set_current_scene.emit(self.run_id, "召唤界面")
            self.draw_summon_task()
        # 召唤确定
        elif self.is_summon_confirm_button():
            self.click_summon_confirm_button()
        elif self.is_summon_room():
            result, coord = self.find_tip_with_hand()  # 找提示手指
            if result:
                signal_run_list.set_current_operation.emit(self.run_id, "点提示")
                self.click_in_circle([coord[0] - 40, coord[1] - 50], 32)

        # 式神录
        elif self.is_shikigami_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "式神录")
            if self.is_after_shikigami_upgrade:
                self.quit_shikigami_panel()
            elif self.is_shikigami_detail_button_tips():  # 找提示手指
                self.click_shikigami_detail_button_tips()
            else:
                result, coord = self.find_tip_with_hand()  # 找提示手指
                if result:
                    signal_run_list.set_current_operation.emit(self.run_id, "点提示手")
                    self.click_in_circle([coord[0] - 40, coord[1] - 40], 10)
                else:
                    if self.souls_novice_done:
                        self.quit_shikigami_panel()
                    elif not self.summon_novice_finish:
                        if self.is_summon_single_button():
                            self.click_summon_single_button()
                            self.summon_novice_finish = True
                    else:
                        self.quit_shikigami_panel()
        elif self.is_shikigami_upgrade_panel():
            self.quit_shikigami_upgrade_panel()
            self.is_after_shikigami_upgrade = True
        # 式神御魂界面
        elif self.is_shikigami_souls_panel():
            self.processing_shikigami_souls_panel()
        # 阴阳术界面
        elif self.is_onmyoji_panel():
            self.close_onmyoji_panel()
        else:
            result, coord = self.find_skip_shikigami_cv_button()  # 跳过式神介绍
            if result:
                signal_run_list.set_current_operation.emit(self.run_id, "跳过式神介绍")
                self.click_in_circle([coord[0] - 500, coord[1] - 300], 100)

    def run_story_step_2(self):
        # 已经入战斗
        if self.is_scene_after_battling:
            # 战斗奖励
            if self.is_battle_win_prize_daruma() or self.is_battle_goods_info_panel():
                signal_run_list.set_current_scene.emit(self.run_id, "战斗奖励")
                self.skip_battle_win(random.randint(1, 3))
            # 战斗失败
            elif self.is_battle_failed_drum():
                self.processing_battle_failed()
                self.is_story_lock = True
        # 剧情场景
        elif self.is_story_scene():
            self.processing_story_scene()
        # 庭院中
        elif self.is_yard():
            signal_run_list.set_current_scene.emit(self.run_id, "庭院")
            self.souls_novice_done = False
            self.summon_novice_finish = False
            # 任务或提示大界面
            if self.is_tips_big_panel():
                self.processing_tips_big_panel()
            # 扩展语音包下载界面
            elif self.is_voice_extent_download_panel():
                self.close_voice_extent_download_panel_cancel_button()
            # 手机绑定
            elif self.is_relate_phone_panel():
                self.cancel_relate_phone_panel()
            else:
                self .processing_novice_special_in_yard()
        elif self.is_battle_ready():
            self.set_battle_ready()
        # 战斗场景
        elif self.is_battle_battling():
            signal_run_list.set_current_scene.emit(self.run_id, "战斗中")
            if self.is_battle_auto():
                self.is_scene_after_battling = True
                if self.is_battle_auto_speed_1x():
                    self.set_battle_speed()
                signal_run_list.set_current_operation.emit(self.run_id, "等待战斗结束")
            elif self.is_battle_manual():
                self.set_battle_auto()
                signal_run_list.set_current_operation.emit(self.run_id, "切换自动战斗")
        # 过场动画
        elif self.is_playing_movie():
            signal_run_list.set_current_scene.emit(self.run_id, "过场动画")
            signal_run_list.set_current_operation.emit(self.run_id, "看动画")
            self.set_playing_movie_accelerate()
        elif self.is_onmyoji_unlock_panel():
            self.close_onmyoji_unlock_panel()
        # 探索地图中
        elif self.is_explore():
            signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
            signal_run_list.set_current_operation.emit(self.run_id, "退出探索地图")
            self.quit_explore()
        else:
            result, coord = self.find_skip_shikigami_cv_button()  # 跳过式神介绍
            if result:
                signal_run_list.set_current_operation.emit(self.run_id, "跳过式神介绍")
                self.click_in_circle([coord[0] - 500, coord[1] - 300], 100)

    def run_chapter(self, chapter_stage):
        if not self.chapter.isRunning():
            self.chapter.play_input = copy.deepcopy(self.play_input)
            self.chapter.play_input.play_name = "chapter"
            self.chapter.play_input.play_name_second = "simple"
            self.chapter.play_input.counter_item = "chapter"
            self.chapter.play_input.chapter_stage = chapter_stage
            self.chapter.is_novice_mode = True
            self.chapter.start()
        else:
            pass

    def run_realm_raid(self, realm_raid_stage):
        if not self.realm_raid.isRunning():
            self.realm_raid.play_input = copy.deepcopy(self.play_input)
            self.realm_raid.play_input.play_name_second = "realm_raid_person"
            self.realm_raid.play_input.counter_item = "realm_raid_person"
            self.realm_raid.play_input.chapter_stage = str(realm_raid_stage)
            # self.realm_raid.is_novice_mode = True
            self.realm_raid.start()
        else:
            pass

    def set_default_prop(self):
        self.is_shikigami_detail_souls_set_1 = False
        self.is_shikigami_detail_souls_set_2 = False
        self.is_shikigami_detail_souls_set_3 = False
        self.is_shikigami_detail_souls_set_4 = False
        self.is_shikigami_detail_souls_set_5 = False
        self.is_shikigami_detail_souls_set_6 = False
        self.souls_novice_done = False
        self.summon_novice_finish = False
        self.is_after_shikigami_upgrade = False
        self.last_chapter = 0
        self.chapter_run_time_preset = random.randint(1200, 1800)

    def check_load_souls_in_shikigami_souls_panel(self, position: int):
        for i in range(1, 7):
            if i == position:
                if getattr(self, "is_shikigami_detail_souls_empty_selected_" + str(i))():
                    result, coord = self.find_souls_in_shikigami_panel()
                    if result:
                        self.click_in_circle([coord[0], coord[1] - 30])
                    else:
                        setattr(self, "is_shikigami_detail_souls_set_1" + str(i), True)
                elif getattr(self, "is_shikigami_detail_souls_empty_" + str(i))():
                    getattr(self, "click_shikigami_detail_souls_empty_" + str(i))()
                else:
                    setattr(self, "is_shikigami_detail_souls_set_1" + str(i), True)

    def processing_stop(self):
        while self.chapter.isRunning():
            self.chapter.stop_without_close_game()
            self.sleep_in_run(0.1)
        while self.realm_raid.isRunning():
            self.realm_raid.stop_without_close_game()
            self.sleep_in_run(0.1)
        else:
            self.stop_status = True
            self.is_finished = True

    def processing_story_scene(self):
        signal_run_list.set_current_scene.emit(self.run_id, "剧情场景")
        result, coord = self.find_battle_button_in_story_scene()  # 剧情打怪
        if result:
            signal_run_list.set_current_operation.emit(self.run_id, "剧情打怪")
            self.click_in_circle(coord)
        else:
            result, coord = self.find_seimei_vision_half_bottom()  # 晴明视界
            if result:
                signal_run_list.set_current_operation.emit(self.run_id, "点晴明视界")
                self.click_in_circle(coord)
            else:
                self.processing_novice_special_in_story_scene()

    def processing_novice_special_in_yard(self):
        result, coord = self.find_lot_button()  # 签到
        if result:
            signal_run_list.set_current_operation.emit(self.run_id, "签到")
            self.click_in_circle(coord)
        else:
            result, coord = self.find_skip_dialog_button()  # 跳过对话
            if result:
                signal_run_list.set_current_operation.emit(self.run_id, "跳过对话")
                self.click_in_circle(coord)
            else:
                result, coord = self.find_ap_button()  # 找庭院体力
                if result:
                    signal_run_list.set_current_operation.emit(self.run_id, "领体力")
                    self.click_in_circle(coord, 5)
                else:
                    self.sleep_in_run(0.1)
                    result, coord = self.find_jade_button()  # 找庭院勾玉
                    if result:
                        signal_run_list.set_current_operation.emit(self.run_id, "领勾玉")
                        self.click_in_circle(coord, 5)
                    else:
                        self.sleep_in_run(0.1)
                        self.sleep_in_run(0.1)
                        result, coord = self.find_tip_with_hand()  # 找提示手指
                        if result:
                            signal_run_list.set_current_operation.emit(self.run_id, "点提示")
                            self.click_in_circle([coord[0] - 40, coord[1] - 50], 32)
                        else:
                            self.sleep_in_run(0.1)
                            result, coord = self.find_npc_prompt_in_story_3()  # 找NPC三点符号
                            if result:
                                signal_run_list.set_current_operation.emit(self.run_id, "点NPC")
                                self.click_in_circle(coord)
                            else:
                                self.sleep_in_run(0.1)
                                result, coord = self.find_npc_prompt_in_story_2()  # 找NPC半个三点符号右边
                                if result:
                                    signal_run_list.set_current_operation.emit(self.run_id, "点NPC")
                                    self.click_in_circle(coord)
                                else:
                                    self.sleep_in_run(0.1)
                                    result, coord = self.find_npc_prompt_in_story()  # 找NPC半个三点符号左边
                                    if result:
                                        signal_run_list.set_current_operation.emit(self.run_id, "点NPC")
                                        self.click_in_circle(coord)
                                    else:
                                        self.sleep_in_run(0.1)
                                        result, coord = self.find_collection_prize_panel_common()  # 奖励
                                        if result:
                                            signal_run_list.set_current_operation.emit(self.run_id, "领取奖励")
                                            self.click_in_circle([coord[0] + 255, coord[1] - 50], 32)
                                        else:
                                            self.sleep_in_run(0.1)
                                            result, coord = self.find_story_task_finish_in_yard_1()  # 小白打勾
                                            if result:
                                                signal_run_list.set_current_operation.emit(self.run_id, "打开教学任务")
                                                self.click_in_circle(coord)
                                            else:
                                                self.sleep_in_run(0.1)
                                                result, coord = self.find_exclamation_marks_in_yard()  # 小白感叹号
                                                if result:
                                                    signal_run_list.set_current_operation.emit(self.run_id, "打开教学任务")
                                                    self.click_in_circle(coord)
                                                else:
                                                    self.sleep_in_run(0.1)
                                                    result, coord = self.find_unlock_new_chapter_tips()  # 新章节锁定提示
                                                    if result:
                                                        signal_run_list.set_current_operation.emit(self.run_id, "章节锁定，切换")
                                                        self.is_story_lock = True
                                                    else:
                                                        self.sleep_in_run(0.1)
                                                        result, coord = self.find_skip_shikigami_cv_button()  # 跳过式神介绍
                                                        if result:
                                                            signal_run_list.set_current_operation.emit(self.run_id, "跳过式神介绍")
                                                            self.click_in_circle([coord[0] - 500, coord[1] - 300], 100)
                                                        elif self.is_yard_approach():
                                                            self.close_yard_approach()
                                                        # 勾玉卡提示界面
                                                        elif self.is_jade_card_buy_panel():
                                                            self.cancel_jade_card_buy_panel()
                                                        else:
                                                            self.slide_yard_to_right()

    def processing_novice_special_in_story_scene(self):
        result, coord = self.find_skip_dialog_button()  # 跳过对话
        if result:
            signal_run_list.set_current_operation.emit(self.run_id, "跳过对话")
            self.click_in_circle(coord)
        else:
            self.sleep_in_run(0.1)
            self.sleep_in_run(0.1)
            result, coord = self.find_npc_question_mark()   # 查找问号
            if result:
                self.click_in_circle(coord)
            else:
                self.sleep_in_run(0.1)
                result, coord = self.find_npc_prompt_in_story_3()  # 找NPC三点符号
                if result:
                    signal_run_list.set_current_operation.emit(self.run_id, "点NPC")
                    self.click_in_circle(coord)
                else:
                    result, coord = self.find_npc_prompt_in_story()  # 找NPC半个三点符号
                    if result:
                        signal_run_list.set_current_operation.emit(self.run_id, "点NPC")
                        self.click_in_circle(coord)
                    else:
                        result, coord = self.find_npc_prompt_in_story_2()  # 找NPC半个三点符号右边
                        if result:
                            signal_run_list.set_current_operation.emit(self.run_id, "点NPC")
                            self.click_in_circle(coord)
                        else:
                            result, coord = self.find_tip_with_hand()  # 找提示手指
                            if result:
                                signal_run_list.set_current_operation.emit(self.run_id, "点提示")
                                self.click_in_circle([coord[0] - 40, coord[1] - 50], 32)
                            else:
                                result, coord = self.find_collection_prize_panel_common()  # 奖励
                                if result:
                                    signal_run_list.set_current_operation.emit(self.run_id, "领取奖励")
                                    self.click_in_circle([coord[0] + 255, coord[1] - 50], 32)
                                else:
                                    result, coord = self.find_skip_shikigami_cv_button()  # 跳过式神介绍
                                    if result:
                                        signal_run_list.set_current_operation.emit(self.run_id, "跳过式神介绍")
                                        self.click_in_circle([coord[0] - 500, coord[1] - 300], 100)
                                    else:
                                        self.click_empty_area_in_story()

    def processing_novice_in_battling(self):
        if self.is_battle_auto():
            if self.is_battle_auto_speed_1x():
                self.set_battle_speed()
            signal_run_list.set_current_operation.emit(self.run_id, "等待战斗结束")
        elif self.is_battle_manual():
            self.set_battle_auto()
            signal_run_list.set_current_operation.emit(self.run_id, "切换自动战斗")
        else:
            result, coord = self.find_tip_with_hand()  # 找提示手指
            if result:
                signal_run_list.set_current_operation.emit(self.run_id, "点提示")
                self.click_in_circle([coord[0] - 40, coord[1] - 40], 32)
            else:
                if self.is_has_three_ghost_fire():
                    result, coord = self.find_need_three_ghost_fire()
                    if result:
                        self.click_in_circle([coord[0], coord[1] - 30])
                    result, coord = self.find_technique_target_common()
                    if result:
                        self.click_in_circle(coord)
                elif self.is_click_to_select_technique_tips():
                    self.click_seimei_technique_1()
                elif self.is_click_to_release_technique_target_tips():
                    self.click_to_release_technique_target_dog()

                elif self.is_technique_cd_tips():
                    self.click_seimei_technique_1()
                elif self.is_shield_cd_two_second():
                    result, coord = self.find_technique_target_common()
                    if result:
                        self.click_in_circle(coord)
                elif self.is_battling_scroll_tips():
                    self.skip_battling_scroll_tips()
                else:
                    result, coord = self.find_release_technique_target_guiqing()
                    if result:
                        self.click_in_circle(coord)
                    else:
                        result, coord = self.find_technique_target_common()
                        if result:
                            self.click_in_circle(coord)

    def find_last_chapter(self):
        for i in range(28, 0, -1):
            func = getattr(self, "find_chapter_entrance_" + str(i))
            result, coord = func()
            if result:
                return i
        else:
            return False

    def find_assign_chapter(self):
        if self.product.chapter_stage == 999:
            return False
        else:
            for i in range(28, 0, -1):
                if self.product.chapter_stage == i:
                    func = getattr(self, "find_chapter_entrance_" + str(i))
                    result, coord = func()
                    return result
            else:
                return False

    def processing_tips_big_panel(self):
        result, coord = self.find_novice_task_get_prize_button()
        if result:
            self.click_in_circle(coord)
        else:
            result, coord = self.find_novice_task_accept_button()
            if result:
                self.click_in_circle(coord)
            else:
                result, coord = self.find_novice_task_daruma_prize()
                if result:
                    self.click_in_circle(coord)
                else:
                    self.close_novice_task_close_button()

    def processing_shikigami_souls_panel(self):
        signal_run_list.set_current_scene.emit(self.run_id, "式神御魂界面")
        result, coord = self.find_tip_with_hand()  # 找提示手指
        if result:
            signal_run_list.set_current_operation.emit(self.run_id, "点提示手")
            self.click_in_circle([coord[0] - 40, coord[1] - 40], 10)
        else:
            if not self.is_shikigami_detail_souls_change_position_checked():
                self.check_shikigami_detail_souls_change_position()
            elif self.is_shikigami_detail_souls_load_button():
                self.load_shikigami_detail_souls()
            elif not self.is_shikigami_detail_souls_set_1:
                self.check_load_souls_in_shikigami_souls_panel(1)
            elif not self.is_shikigami_detail_souls_set_2:
                self.check_load_souls_in_shikigami_souls_panel(2)
            elif not self.is_shikigami_detail_souls_set_3:
                self.check_load_souls_in_shikigami_souls_panel(3)
            elif not self.is_shikigami_detail_souls_set_4:
                self.check_load_souls_in_shikigami_souls_panel(4)
            elif not self.is_shikigami_detail_souls_set_5:
                self.check_load_souls_in_shikigami_souls_panel(5)
            elif not self.is_shikigami_detail_souls_set_6:
                self.check_load_souls_in_shikigami_souls_panel(6)
            else:
                self.quit_shikigami_detail_souls_panel()
                self.souls_novice_done = True
