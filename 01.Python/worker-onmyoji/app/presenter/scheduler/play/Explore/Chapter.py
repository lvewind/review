from ..Common import *
from ....sender import signal_run_list


class PlayChapter(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayChapter, self).__init__(play_input)
        self.slide_to_top = True
        self.slide_to_right = True
        self.is_dog_food_list_set = False
        self.is_difficulty_selected = False
        self.chapter_stage = 0
        self.chapter_zone_slide_to_left_times = 0
        self.chapter_zone_slide_to_right_times = 0
        self.is_first_time_in_chapter_zone = True
        self.chapter_map_gift_check = False
        self.chapter_map_seal_check = False
        self.is_teammate_ready_in_zone = False
        self.is_full_dog = False
        self.can_team_up = True

    def run(self):
        self.set_run_status_default()
        self.is_full_dog = False
        self.is_first_time_in_chapter_zone = True
        self.chapter_map_gift_check = False
        self.chapter_map_seal_check = False
        self.chapter_stage = self.product.chapter_stage
        self.set_preset_count()
        while not self.stop_status:
            self.check_chat_panel()
            self.running_time = time.time() - self.start_time
            if not self.stop_flag:
                # 体力用尽，通知运行列表关闭
                if self.ap_use_up:
                    self.stop_flag = True
                # 未达到执行场数，执行狗粮
                elif self.counter < self.preset_count and not self.is_teammate_finished():
                    self.run_status.set_play_standby_status(self.run_id, True)      # 设置自身就绪状态
                    if self.run_status.get_play_standby_status(int(self.play_input.run_list.teammate_id)) or \
                            self.play_input.run_list.teamup_mode == "single_solo":    # 队友已就绪或单刷
                        if self.is_battle_failed:       # 触发战斗失败状态
                            self.processing_battle_failed_status()
                        elif self.is_scene_after_battling:  # 战斗结束
                            self.processing_after_battle()
                        else:
                            if self.is_battle_win_prize_daruma():  # 战斗奖励
                                self.skip_battle_win_prize(random.randint(1, 3))
                            elif self.is_battle_battling():   # 战斗中
                                self.processing_battling()
                            elif self.is_chapter_change_dog_food_panel():
                                self.change_dog_food()
                            elif self.is_battle_ready():    # 战斗准备
                                self.processing_battle_ready_chapter()
                            elif self.is_chapter_zone():    # 探索副本内
                                self.processing_chapter_zone()
                            elif self.is_cooperation_teamup_panel():    # 协战队伍
                                self.processing_cooperation_teamup()
                            elif self.is_chapter_panel():   # 探索入口面板
                                self.processing_chapter_panel()
                            elif self.is_seal_panel_in_explore():   # 妖气封印面板
                                self.processing_seal_panel_in_explore()
                            elif self.is_explore():         # 探索地图
                                self.processing_explore()
                            elif self.is_yard():            # 庭院
                                self.processing_yard()
                # 已达到执行场数，设置当前工作停止
                else:
                    self.stop_flag = True
            else:
                self.is_finished = True
                self.run_status.set_play_standby_status(self.run_id, False)     # 关闭自身就绪状态
                self.processing_stop()
            self.sleep_in_run()

    def processing_explore(self):
        signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
        if self.bonus_all_set:
            if self.is_bonus_panel():
                self.close_bonus_panel()
            else:
                # 获取奖励
                result, coord = self.find_collection_prize_panel_common()
                if result:
                    self.click_in_circle([coord[0] + 240, coord[1], 48])
                else:
                    # 查找奖励
                    if (not self.chapter_map_gift_check) and self.product.chapter_map_gift:
                        result, coord = self.find_prize_box_in_explore()
                        if result:
                            self.click_in_circle(coord)
                        else:
                            self.chapter_map_gift_check = True
                    # 妖气封印
                    elif (not self.chapter_map_seal_check) and self.product.chapter_map_seal:
                        result, coord = self.find_seal_in_explore()
                        if result:
                            self.click_in_circle(coord)
                        else:
                            self.chapter_map_seal_check = True
                    else:
                        # 选择层数组队
                        if self.team_position == "captain":
                            self.is_first_time_in_chapter_zone = True
                            self.chapter_zone_slide_to_right_times = 0
                            self.chapter_zone_slide_to_left_times = 0
                            if self.is_continue_invite_chapter_panel():
                                signal_run_list.set_current_operation.emit(self.run_id, "继续邀请")
                                self.confirm_continue_invite_chapter_panel()
                                self.invite_status = True
                                self.invite_time_start = time.time()
                            else:
                                signal_run_list.set_current_operation.emit(self.run_id, "查找副本")
                                self.find_and_select_stage_chapter()
                        else:
                            if self.is_confirm_auto_accept_panel():
                                if self.is_confirm_auto_accept_panel_checked():
                                    self.confirm_auto_accept_panel()
                                else:
                                    self.checked_confirm_auto_accept_panel()
                            else:
                                self.waiting_for_invite_chapter()
        else:
            if self.is_continue_invite_chapter_panel():
                self.cancel_continue_invite_chapter_panel()
            else:
                self.set_bonus(where="explore")

    def find_and_select_stage_chapter(self):
        if self.product.chapter_stage == 999:
            signal_run_list.set_current_operation.emit(self.run_id, "非剧情模式先择了剧情自动")
        else:
            result, coord = getattr(self, "find_chapter_entrance_" + str(self.chapter_stage))()
            if result:
                self.click_in_circle([coord[0], coord[1] + 30])
            else:
                current_stage = 28
                for j in range(1, 28):
                    result, coord = getattr(self, "find_chapter_entrance_" + str(j))()
                    if result:
                        current_stage = j
                        break
                if self.chapter_stage <= current_stage - 4:
                    self.slide_chapter_stage_to_top()
                elif self.chapter_stage > current_stage + 4:
                    self.slide_chapter_stage_to_bottom()

    def processing_chapter_panel(self):
        signal_run_list.set_current_scene.emit(self.run_id, "探索面板")
        self.after_boss_battle = False
        if (not self.chapter_map_gift_check) and self.product.chapter_map_gift:
            result, coord = self.find_prize_box_in_explore()
            if result:
                self.close_chapter_panel()
            else:
                self.chapter_map_gift_check = True
        elif (not self.chapter_map_seal_check) and self.product.chapter_map_seal:
            result, coord = self.find_seal_in_explore()
            if result:
                self.close_chapter_panel()
            else:
                self.chapter_map_seal_check = True
        else:
            if self.team_position == "captain":
                if self.is_difficulty_selected:
                    if self.play_input.run_list.teamup_mode == "double_captain":
                        self.teamup_chapter()
                    else:
                        signal_run_list.set_current_operation.emit(self.run_id, "开始探索")
                        self.start_chapter_panel()
                elif self.product.play_name_second == "hard":
                    if self.is_chapter_panel_hard_selected():
                        self.is_difficulty_selected = True
                    else:
                        self.select_chapter_panel_hard()
                elif self.product.play_name_second == "simple":
                    if self.is_chapter_panel_simple_selected():
                        self.is_difficulty_selected = True
                    else:
                        self.select_chapter_panel_simple()
            else:
                self.close_chapter_panel()

    def teamup_chapter(self):
        signal_run_list.set_current_operation.emit(self.run_id, "开始组队")
        self.is_first_time_in_chapter_zone = True
        if self.is_create_team_panel_chapter():
            signal_run_list.set_current_operation.emit(self.run_id, "创建队伍")
            if self.play_input.run_list.teamup_mode == "double_captain":
                if self.is_chapter_create_team_panel_only_selected():
                    self.create_team_chapter_2()
                else:
                    self.select_chapter_create_team_panel_only()
            if self.play_input.run_list.teamup_mode == "free_captain":
                if self.is_chapter_create_team_panel_any_selected():
                    self.create_team_chapter_2()
                else:
                    self.select_chapter_create_team_panel_any()
        else:
            self.teamup_chapter_panel_hard()

    def processing_chapter_zone(self):
        self.is_difficulty_selected = False
        self.chapter_map_gift_check = False
        self.chapter_map_seal_check = False
        signal_run_list.set_current_scene.emit(self.run_id, "探索副本")
        # 队长部分
        if self.play_input.run_list.teamup_mode == "single_solo" or self.play_input.run_list.teamup_mode == "double_captain" \
                or self.play_input.run_list.teamup_mode == "free_captain":
            # 刚进入探索副本, 先走两步
            if self.is_first_time_in_chapter_zone:
                for i in range(random.randint(1, 3)):
                    self.slide_chapter_dog_list_to_right()
                else:
                    self.is_first_time_in_chapter_zone = False
            # BOSS战之后
            elif self.after_boss_battle:
                if self.is_chapter_zone_quit_confirm():
                    self.confirm_quit_chapter_zone()
                else:
                    result, coord = self.find_collection_prize_panel_common()
                    if result:
                        self.click_in_circle([coord[0] + 400, coord[0]], 88)
                    else:
                        # 查找奖励纸人
                        result, coord = self.find_chapter_boss_prize_doll()
                        if result:
                            self.click_in_circle(coord)
                        else:
                            self.quit_chapter_zone()
            # 阵容锁定，自动纸人已设定
            elif self.auto_doll_set and self.cast_lock_set:
                # 队友狗粮副本中已就绪或单开
                if self.run_status.get_chapter_zone_standby_status(int(self.play_input.run_list.teammate_id)) \
                        or not self.play_input.run_list.teamup_mode == "double_captain":
                    if self.is_ap_use_up_panel():
                        if self.product.story_buy_ap:
                            if self.is_ap_use_up_buy_button_60():
                                self.click_ap_use_up_buy_button()
                            else:
                                self.ap_use_up = True
                                self.stop_flag = True
                        else:
                            self.close_ap_use_up_panel()
                            self.ap_use_up = True
                            self.stop_flag = True
                    # 自动纸人已激活， 自动找怪
                    elif self.doll_active:
                        signal_run_list.set_current_operation.emit(self.run_id, "自动找怪")
                    # 辅助找怪
                    else:
                        # 查找BOSS
                        result, coord = self.find_chapter_boss()
                        if result:
                            signal_run_list.set_current_operation.emit(self.run_id, "打BOSS")
                            self.click_in_circle(coord)
                            self.is_kick_boss = True
                        else:
                            # 查找小怪
                            result, coord = self.find_chapter_spirit()
                            if result:
                                signal_run_list.set_current_operation.emit(self.run_id, "打小怪")
                                self.is_kick_boss = False
                                self.click_in_circle(coord)
                                time.sleep(2)
                            else:
                                if self.slide_to_right:
                                    signal_run_list.set_current_operation.emit(self.run_id, "滑向右边")
                                    self.slide_chapter_zone_to_right()
                                    self.chapter_zone_slide_to_right_times += 1
                                    if self.chapter_zone_slide_to_right_times > 6:
                                        self.chapter_zone_slide_to_right_times = 0
                                        self.slide_to_right = False
                                else:
                                    signal_run_list.set_current_operation.emit(self.run_id, "滑向左边")
                                    self.slide_chapter_zone_to_left()
                                    self.chapter_zone_slide_to_left_times += 1
                                    if self.chapter_zone_slide_to_left_times > 6:
                                        self.chapter_zone_slide_to_left_times = 0
                                        self.slide_to_right = True
                else:
                    signal_run_list.set_current_operation.emit(self.run_id, "等在队友完成")

            elif self.cast_lock_set:
                self.set_auto_doll_chapter()
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "检查锁定")
                if self.product.lock_cast:  # 参数设置了锁定阵容
                    # 有满级狗粮，解除锁定
                    if self.is_full_dog:
                        if self.is_chapter_cast_unlock() or self.is_chapter_cast_unlock_novice():
                            self.cast_lock_set = True
                            self.cast_lock_up = False
                        elif self.is_chapter_cast_lock():
                            self.unlock_chapter_cast()
                        elif self.is_chapter_cast_lock_novice():
                            self.unlock_chapter_cast_novice()
                    # 无满级狗粮， 锁定
                    else:
                        if self.is_chapter_cast_lock() or self.is_chapter_cast_lock_novice():
                            self.cast_lock_set = True
                            self.cast_lock_up = True
                        elif self.is_chapter_cast_unlock():
                            self.lock_chapter_cast()
                        elif self.is_chapter_cast_unlock_novice():
                            self.lock_chapter_cast_novice()
                # 不设置锁定阵容
                else:
                    if self.is_chapter_cast_unlock() or self.is_chapter_cast_unlock_novice():
                        self.cast_lock_set = True
                        self.cast_lock_up = False
                    elif self.is_chapter_cast_lock():
                        self.unlock_chapter_cast()
                    elif self.is_chapter_cast_lock_novice():
                        self.unlock_chapter_cast_novice()
        # 队友部分
        else:
            # 阵容锁定，自动纸人已设定
            if self.auto_doll_set and self.cast_lock_set:
                result, coord = self.find_collection_prize_panel_common()
                if result:
                    signal_run_list.set_current_operation.emit(self.run_id, "BOSS奖励")
                    self.click_in_circle([coord[0] + 400, coord[0]], 88)
                else:
                    # 查找奖励纸人
                    result, coord = self.find_chapter_boss_prize_doll()
                    if result:
                        signal_run_list.set_current_operation.emit(self.run_id, "BOSS奖励小人")
                        self.click_in_circle(coord)

                signal_run_list.set_current_operation.emit(self.run_id, "等待队长选怪")
                # 设置队友狗粮副本就绪状态
                if self.play_input.run_list.teamup_mode == "double_teammate":
                    self.run_status.set_chapter_zone_standby_status(self.run_id, True)
                else:
                    self.run_status.set_chapter_zone_standby_status(self.run_id, False)
            # 设置队友自动小纸人
            if self.cast_lock_set:
                self.set_auto_doll_chapter()
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "检查锁定")
                self.run_status.set_chapter_zone_standby_status(self.run_id, False)
                if self.product.lock_cast:  # 参数设置了锁定阵容
                    # 有满级狗粮，解除锁定
                    if self.is_full_dog:
                        if self.is_chapter_cast_unlock():
                            self.cast_lock_set = True
                            self.cast_lock_up = False
                        else:
                            self.unlock_chapter_cast()
                    # 无满级狗粮， 锁定
                    else:
                        if self.is_chapter_cast_lock():
                            self.cast_lock_set = True
                            self.cast_lock_up = True
                        else:
                            self.lock_chapter_cast()
                # 不锁定阵容
                else:
                    if self.is_chapter_cast_unlock():
                        self.cast_lock_set = True
                        self.cast_lock_up = False
                    else:
                        self.unlock_chapter_cast()

    def set_auto_doll_chapter(self):
        if self.product.use_yingbing:
            if self.is_doll_auto_feed:  # 自动喂食已开启
                if self.is_chapter_doll_hunger():  # 依旧饥饿
                    self.auto_doll_set = True
                    self.doll_active = False
                else:
                    if self.is_cooperation_doll_active():
                        self.doll_active = True
                        self.auto_doll_set = True
                    else:
                        # 这里需要检测
                        self.change_cooperation_doll_active()
            else:
                if self.is_chapter_feed_doll_panel():
                    if self.is_chapter_feed_doll_panel_auto_feed_active():
                        self.is_doll_auto_feed = True

                    else:
                        self.set_chapter_feed_doll_panel_auto_feed_active()
                elif self.is_chapter_zone_doll_exist():
                    self.open_chapter_feed_doll_panel()
                else:
                    self.auto_doll_set = True
                    self.doll_active = False
        else:
            self.auto_doll_set = True
            self.doll_active = False

    # 准备界面
    def processing_battle_ready_chapter(self):
        signal_run_list.set_current_scene.emit(self.run_id, "准备场景")
        # 切换到狗粮更换界面
        if (not self.cast_lock_up) and self.is_full_dog:
            if self.is_chapter_change_dog_food_panel():  # 换狗粮界面
                pass
            else:
                self.is_dog_food_list_set = False
                self.open_chapter_change_dog_food_panel()
        else:
            if self.is_battle_ready_panel():
                signal_run_list.set_current_operation.emit(self.run_id, "开始战斗")
                self.set_battle_ready()

    # 狗粮更换界面
    def change_dog_food(self):
        if (not self.cast_lock_up) and self.is_full_dog:
            if self.is_chapter_change_dog_food_panel():  # 换狗粮界面
                signal_run_list.set_current_operation.emit(self.run_id, "换狗粮")
                if self.is_dog_food_list_set:
                    result, target_coord = False, [0, 0]
                    # 队长换狗粮
                    if self.team_position == "captain":
                        if self.product.chapter_1v3 or self.product.chapter_1v2 or not self.play_input.run_list.teamup_mode == "double_captain":
                            result, target_coord = self.find_chapter_full_dog_left_in_change_scene()
                        elif self.product.chapter_2v2:
                            result, target_coord = self.find_chapter_full_dog_all_in_change_scene()
                    else:
                        if self.product.chapter_1v2 or self.product.chapter_2v2:
                            result, target_coord = self.find_chapter_full_dog_left_in_change_scene()
                        elif self.product.chapter_0v3 or self.product.chapter_1v3:
                            result, target_coord = self.find_chapter_full_dog_all_in_change_scene()
                    if result:
                        result, source_coord = False, [0, 0]
                        if self.product.chapter_dog_food_2:
                            result, source_coord = self.find_dog_food_in_list(2)
                            if not result:
                                result, source_coord = self.find_dog_food_in_list(3)
                                if not result:
                                    result, source_coord = self.find_dog_food_in_list(4)
                        elif self.product.chapter_dog_food_3:
                            result, source_coord = self.find_dog_food_in_list(3)
                            if not result:
                                result, source_coord = self.find_dog_food_in_list(4)
                        elif self.product.chapter_dog_food_4:
                            result, source_coord = self.find_dog_food_in_list(4)
                        if result:
                            if self.is_dog_food_full_level_in_list(source_coord):
                                self.slide_chapter_dog_list_to_left()
                            else:
                                if self.product.chapter_dog_food_m:
                                    source_coord[1] -= 40
                                self.drag_a_to_b_with_point(source_coord, target_coord)
                        elif not self.is_chapter_change_dog_food_list_full_level():
                            self.slide_chapter_dog_list_to_right()
                        else:
                            self.slide_chapter_dog_list_to_left()
                    else:
                        self.set_battle_ready()
                        self.is_full_dog = False
                        self.cast_lock_set = False
                else:
                    # 切换狗粮列表
                    if self.product.chapter_dog_food_m:
                        if self.is_chapter_change_dog_food_m_list():
                            self.is_dog_food_list_set = True
                        elif self.is_chapter_change_dog_food_m_list_button():
                            self.select_chapter_change_dog_food_m_list_button()
                        else:
                            self.open_chapter_change_dog_food_type_select_panel()
                    elif self.product.chapter_dog_food_n:
                        if self.is_chapter_change_dog_food_n_list():
                            self.is_dog_food_list_set = True
                        elif self.is_chapter_change_dog_food_n_list_button():
                            self.select_chapter_change_dog_food_n_list_button()
                        else:
                            self.open_chapter_change_dog_food_type_select_panel()
            else:
                self.is_dog_food_list_set = False
                self.open_chapter_change_dog_food_panel()
        else:
            signal_run_list.set_current_operation.emit(self.run_id, "开始战斗")
            self.set_battle_ready()

    def find_dog_food_in_list(self, dog_food_star: int):
        if dog_food_star == 2:
            if self.product.chapter_dog_food_m:
                return self.find_chapter_change_dog_food_list_m_star_2()  # 查找二星狗粮
            else:
                return self.find_chapter_change_dog_food_list_n_star_2()  # 查找二星狗粮
        elif dog_food_star == 3:
            if self.product.chapter_dog_food_m:
                return self.find_chapter_change_dog_food_list_m_star_3()
            else:
                return self.find_chapter_change_dog_food_list_n_star_3()
        elif dog_food_star == 4:
            if self.product.chapter_dog_food_m:
                return self.find_chapter_change_dog_food_list_m_star_4()
            else:
                return self.find_chapter_change_dog_food_list_n_star_4()

    def is_dog_food_full_level_in_list(self, food_coord: list):
        if self.product.chapter_dog_food_m:
            result, coord = self.find_with_point_ext_area("chapter_is_be_found_dog_food_full_level",
                                                          [food_coord[0] - 40, food_coord[1] - 120], [24, 24, 24, 24])
            return result
        elif self.product.chapter_dog_food_n:
            result, coord = self.find_with_point_ext_area("chapter_is_be_found_dog_food_full_level",
                                                          [food_coord[0] - 40, food_coord[1] - 150], [24, 24, 24, 24])
            return result

    def processing_seal_panel_in_explore(self):
        self.chapter_map_gift_check = False
        self.chapter_map_seal_check = False
        self.run_status.set_play_standby_status(self.run_id, False)
        if self.is_create_team_panel_chapter():
            if self.is_chapter_create_team_panel_any_selected():
                signal_run_list.set_current_operation.emit(self.run_id, "创建队伍")
                self.create_team_chapter_2()
            else:
                self.select_chapter_create_team_panel_any()
        elif self.is_seal_panel_in_explore_challenge_button():
            self.click_seal_panel_in_explore_challenge_button()

    def waiting_for_invite_chapter(self):
        signal_run_list.set_current_operation.emit(self.run_id, "等待队长邀请")
        chapter_stage = str(self.product.chapter_stage)
        if chapter_stage == "1":
            if self.is_invite_chapter_stage_1():
                self.accept_invite_common()
        elif chapter_stage == "2":
            if self.is_invite_chapter_stage_2():
                self.accept_invite_common()
        elif chapter_stage == "3":
            if self.is_invite_chapter_stage_3():
                self.accept_invite_common()
        elif chapter_stage == "4":
            if self.is_invite_chapter_stage_4():
                self.accept_invite_common()
        elif chapter_stage == "5":
            if self.is_invite_chapter_stage_5():
                self.accept_invite_common()
        elif chapter_stage == "6":
            if self.is_invite_chapter_stage_6():
                self.accept_invite_common()
        elif chapter_stage == "7":
            if self.is_invite_chapter_stage_7():
                self.accept_invite_common()
        elif chapter_stage == "8":
            if self.is_invite_chapter_stage_8():
                self.accept_invite_common()
        elif chapter_stage == "9":
            if self.is_invite_chapter_stage_9():
                self.accept_invite_common()
        elif chapter_stage == "10":
            if self.is_invite_chapter_stage_10():
                self.accept_invite_common()
        elif chapter_stage == "11":
            if self.is_invite_chapter_stage_11():
                self.accept_invite_common()
        elif chapter_stage == "12":
            if self.is_invite_chapter_stage_12():
                self.accept_invite_common()
        elif chapter_stage == "13":
            if self.is_invite_chapter_stage_13():
                self.accept_invite_common()
        elif chapter_stage == "14":
            if self.is_invite_chapter_stage_14():
                self.accept_invite_common()
        elif chapter_stage == "15":
            if self.is_invite_chapter_stage_15():
                self.accept_invite_common()
        elif chapter_stage == "16":
            if self.is_invite_chapter_stage_16():
                self.accept_invite_common()
        elif chapter_stage == "17":
            if self.is_invite_chapter_stage_17():
                self.accept_invite_common()
        elif chapter_stage == "18":
            if self.is_invite_chapter_stage_18():
                self.accept_invite_common()
        elif chapter_stage == "19":
            if self.is_invite_chapter_stage_19():
                self.accept_invite_common()
        elif chapter_stage == "20":
            if self.is_invite_chapter_stage_20():
                self.accept_invite_common()
        elif chapter_stage == "21":
            if self.is_invite_chapter_stage_21():
                self.accept_invite_common()
        elif chapter_stage == "22":
            if self.is_invite_chapter_stage_22():
                self.accept_invite_common()
        elif chapter_stage == "23":
            if self.is_invite_chapter_stage_23():
                self.accept_invite_common()
        elif chapter_stage == "24":
            if self.is_invite_chapter_stage_24():
                self.accept_invite_common()
        elif chapter_stage == "25":
            if self.is_invite_chapter_stage_25():
                self.accept_invite_common()
        elif chapter_stage == "26":
            if self.is_invite_chapter_stage_26():
                self.accept_invite_common()
        elif chapter_stage == "27":
            if self.is_invite_chapter_stage_27():
                self.accept_invite_common()
        elif chapter_stage == "28":
            if self.is_invite_chapter_stage_28():
                self.accept_invite_common()

    def processing_after_battle(self):
        if self.is_battle_win_chapter_teamup() or self.is_battle_win_chapter():
            self.processing_battle_win_chapter()
        if self.is_battle_win_prize_daruma():  # 战斗奖励
            self.processing_battle_win_prize()
        elif self.is_battle_failed_drum():  # 失败鼓
            self.processing_battle_failed()

    def processing_battle_win_chapter(self):
        self.is_teammate_ready_in_zone = False
        self.run_status.set_chapter_zone_standby_status(self.run_id, False)
        signal_run_list.set_current_scene.emit(self.run_id, "战斗胜利")
        signal_run_list.set_current_operation.emit(self.run_id, "检查满级")
        result = False
        if self.play_input.run_list.teamup_mode == "single_solo":
            # 查找单刷满级狗粮
            result, coord = self.find_chapter_solo_full_dog()
        elif self.play_input.run_list.teamup_mode == "double_captain" or self.play_input.run_list.teamup_mode == "free_captain":
            # 查找组队队长满级狗粮
            if self.product.chapter_2v2:
                result, coord = self.find_chapter_captain_full_dog_2v2()
            elif self.product.chapter_1v3 or self.product.chapter_1v2:
                result, coord = self.find_chapter_captain_full_dog_1v3()
            elif self.product.chapter_0v0:
                pass
        elif self.play_input.run_list.teamup_mode == "double_teammate" or self.play_input.run_list.teamup_mode == "free_teammate":
            # 查找队友满级狗粮
            if self.product.chapter_2v2 or self.product.chapter_1v2:
                result, coord = self.find_chapter_teammate_full_dog_2v2()
            elif self.product.chapter_1v3 or self.product.chapter_0v3:
                result, coord = self.find_chapter_teammate_full_dog_1v3()
        if result:
            self.cast_lock_set = False
            self.is_full_dog = True
        self.skip_battle_win(random.randint(1, 3))

    def processing_battle_failed_status(self):
        if self.is_novice_mode:  # 新手模式
            if self.is_chapter_zone():
                signal_run_list.set_current_scene.emit(self.run_id, "探索副本")
                if self.is_chapter_zone_quit_confirm():
                    signal_run_list.set_current_operation.emit(self.run_id, "退出探索副本")
                    self.confirm_quit_chapter_zone()
                    time.sleep(3)
                elif self.is_ap_use_up_panel():
                    self.close_ap_use_up_panel()
                else:
                    self.quit_chapter_zone()
            elif self.is_explore():
                signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
                self.is_battle_failed = False
                self.chapter_stage = str(int(self.chapter_stage) - 1)
            elif self.is_chapter_panel():
                self.close_chapter_panel()

    def processing_stop(self):
        if self.is_chapter_panel():
            self.close_chapter_panel()
        elif self.is_explore():
            self.process_explore_after_task()
        elif self.is_chapter_zone():
            signal_run_list.set_current_scene.emit(self.run_id, "探索副本")
            if self.is_chapter_zone_quit_confirm():
                signal_run_list.set_current_operation.emit(self.run_id, "退出探索副本")
                self.confirm_quit_chapter_zone()
            elif self.is_ap_use_up_panel():
                self.close_ap_use_up_panel()
            else:
                self.quit_chapter_zone()
        elif self.is_battle_win_chapter():
            click_position = random.randint(1, 3)
            signal_run_list.set_current_operation.emit(self.run_id, "跳过胜利")
            self.skip_battle_win(click_position)
        elif self.is_battle_win_chapter_teamup():
            click_position = random.randint(1, 3)
            signal_run_list.set_current_operation.emit(self.run_id, "跳过胜利")
            self.skip_battle_win(click_position)
        elif self.is_battle_auto_invite_panel():
            self.cancel_auto_invite()
        elif self.is_battle_battling():
            self.processing_battling()
        elif self.is_yard():
            self.processing_yard()
