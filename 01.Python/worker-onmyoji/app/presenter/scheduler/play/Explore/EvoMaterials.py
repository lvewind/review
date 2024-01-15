from ..Common import *
from ....sender import signal_run_list


class PlayEvoMaterials(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayEvoMaterials, self).__init__(play_input)
        self.evo_selected = False
        self.can_team_up = True

    def run(self):
        self.set_run_status_default()
        self.evo_selected = False
        self.set_preset_count()
        while not self.stop_status:
            self.check_chat_panel()
            self.teamup_mode = self.play_input.run_list.teamup_mode
            if not self.stop_flag:
                # 体力用完
                if self.ap_use_up:
                    self.stop_flag = True
                # 未达到场数
                elif self.counter < self.preset_count and not self.is_teammate_finished():
                    self.run_status.set_play_standby_status(self.run_id, True)  # 设置自身就绪状态
                    if self.run_status.get_play_standby_status(int(self.play_input.run_list.teammate_id)) \
                            or self.play_input.run_list.teamup_mode == "single_solo":  # 队友已就绪或单刷
                        if self.is_scene_after_battling:
                            self.processing_after_battle()
                        else:
                            if self.is_battle_win_prize_daruma():  # 战斗奖励
                                self.skip_battle_win_prize(random.randint(1, 3))
                            elif self.is_battle_battling():       # 战斗中
                                self.processing_battling()
                            elif self.is_battle_ready():        # 战斗准备
                                self.processing_battle_ready()
                            elif self.is_cooperation_teamup_panel():  # 协战队伍
                                self .processing_cooperation_teamup()
                            elif self.is_team_panel():          # 组队界面
                                self .processing_teamup()
                            elif self.is_evo_stage_panel():     # 层数选择
                                self .processing_evo_stage_panel()
                            elif self.is_evo_tower():           # 觉醒之塔
                                self .processing_evo_tower()
                            elif self.is_explore():             # 探索地图
                                self.processing_explore()
                            elif self.is_yard():                # 庭院中
                                self.processing_yard()
                            elif self.team_position == "captain":
                                self.processing_auto_invite_after_battle()
                    else:
                        signal_run_list.set_current_operation.emit(self.run_id, "等待队友就绪")
                else:
                    self.stop_flag = True
            else:
                self.is_finished = True
                self.run_status.set_play_standby_status(self.run_id, False)
                self .processing_stop()
            self.sleep_in_run()

    def processing_evo_stage_panel(self):
        signal_run_list.set_current_scene.emit(self.run_id, "觉醒材料")
        if self.stage_selected:
            # 单人单刷
            if self.play_input.run_list.teamup_mode == "single_solo":
                if self.auto_doll_set:
                    if self.doll_active:
                        signal_run_list.set_current_operation.emit(self.run_id, "自动挑战")
                    else:
                        signal_run_list.set_current_operation.emit(self.run_id, "开始挑战")
                        self.challenge_evo()
                elif self.cast_lock_set:
                    self.check_auto_doll_in_stage_panel()
                else:
                    self.check_cast_lock_in_stage_panel()
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "开始组队")
                self.teamup_evo()
        elif self.evo_selected:
            # 选择觉醒材料层数
            result, coord = False, [0, 0]
            result = getattr(self, "is_evo_stage_selected_" + str(self.product.chapter_stage))()
            if result:
                self.stage_selected = True
            else:
                if self.product.play_name == "evo_materials":
                    result, coord = getattr(self, "find_evo_stage_" + str(self.product.chapter_stage))()
                if result:
                    self.select_evo_stage(coord)
                elif self.product.chapter_stage < 6:
                    self.slide_down_evo_stage_list()
                else:
                    self.slide_up_evo_stage_list()

        else:
            self.find_and_select_evo_in_stage_panel()

    def find_and_select_evo_in_stage_panel(self):
        if self.product.play_name_second == "fire":
            if self.is_evo_stage_panel_fire():
                self.evo_selected = True
            else:
                self.select_evo_stage_panel_fire()
        elif self.product.play_name_second == "wind":
            if self.is_evo_stage_panel_wind():
                self.evo_selected = True
            else:
                self.select_evo_stage_panel_wind()
        elif self.product.play_name_second == "water":
            if self.is_evo_stage_panel_water():
                self.evo_selected = True
            else:
                self.select_evo_stage_panel_water()
        elif self.product.play_name_second == "thunder":
            if self.is_evo_stage_panel_thunder():
                self.evo_selected = True
            else:
                self.select_evo_stage_panel_thunder()

    def processing_evo_tower(self):
        signal_run_list.set_current_scene.emit(self.run_id, "觉醒之塔")
        signal_run_list.set_current_operation.emit(self.run_id, "选择麒麟")
        if self.product.play_name_second == "fire":
            self.select_evo_tower_fire()
        elif self.product.play_name_second == "wind":
            self.select_evo_tower_wind()
        elif self.product.play_name_second == "water":
            self.select_evo_tower_water()
        elif self.product.play_name_second == "thunder":
            self.select_evo_tower_thunder()

    # 探索地图
    def processing_explore(self):
        if self.team_position == "captain":
            self.processing_explore_captain()
        else:
            self.processing_explore_teammate()

    # 探索地图队长
    def processing_explore_captain(self):
        signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
        if self.bonus_all_set or not self.config_bonus:
            if self.is_bonus_panel():
                self.close_bonus_panel()
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "打开觉醒之塔")
                self.open_evo()
        else:
            self.set_bonus(where="explore")

    # 探索地图队友
    def processing_explore_teammate(self):
        signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
        if self.bonus_all_set or not self.config_bonus:
            if self.is_bonus_panel():
                self.close_bonus_panel()
            else:
                if not self.auto_accept:
                    if self.is_confirm_auto_accept_panel():
                        if self.is_confirm_auto_accept_panel_checked():
                            self.confirm_auto_accept_panel()
                        else:
                            self.checked_confirm_auto_accept_panel()
                    else:
                        self.waiting_for_invite_evo()
        else:
            self.set_bonus(where="explore")

    def waiting_for_invite_evo(self):
        signal_run_list.set_current_operation.emit(self.run_id, "等待队长邀请")
        play_name_second = self.product.play_name_second
        if play_name_second == "fire":
            if getattr(self, "is_invite_evo_fire_stage_" + str(self.product.chapter_stage))():
                self.accept_invite_common()

        elif play_name_second == "wind":
            if getattr(self, "is_invite_evo_wind_stage_" + str(self.product.chapter_stage))():
                self.accept_invite_common()

        elif play_name_second == "water":
            if getattr(self, "is_invite_evo_water_stage_" + str(self.product.chapter_stage))():
                self.accept_invite_common()

        elif play_name_second == "thunder":
            if getattr(self, "is_invite_evo_thunder_stage_" + str(self.product.chapter_stage))():
                self.accept_invite_common()

    def processing_stop(self):
        if self.is_battle_auto_invite_panel():
            self.cancel_auto_invite()
        elif self.is_explore():
            signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
            if self.is_continue_invite_chapter_panel():
                self.cancel_continue_invite_chapter_panel()
            elif not self.bonus_off_total and self.config_bonus:
                self.set_bonus(set_on=False)
            else:
                if self.is_bonus_panel():
                    self.close_bonus_panel()
                else:
                    signal_run_list.set_current_operation.emit(self.run_id, " ")
                    run_status.set_play_standby_status(self.run_id, False)
                    self.is_play_finished = self.stop_status = True
                    self.stop_flag = False
        elif self.is_cooperation_teamup_panel():
            if self.is_cooperation_teamup_panel_confirm_quit():
                self.confirm_quit_cooperation_teamup_panel()
                time.sleep(1.2)
            else:
                self.close_cooperation_teamup_panel()
        elif self.is_evo_stage_panel():
            signal_run_list.set_current_operation.emit(self.run_id, "退出层数选择")
            self.quit_evo_stage_panel()
        elif self.is_evo_tower():
            signal_run_list.set_current_operation.emit(self.run_id, "退出觉醒之塔")
            self.quit_evo_tower_quit()
        elif self.is_battle_win_drum_evo():
            click_position = random.randint(1, 3)
            signal_run_list.set_current_operation.emit(self.run_id, "跳过胜利")
            self.skip_battle_win(click_position)
        elif self.is_battle_win_prize_daruma():
            self.process_battle_win_prize_daruma()
        elif self.is_battle_failed_drum():
            self.process_battle_failed_drum()
        elif self.is_battle_battling():
            self.processing_battling()
        elif self.is_yard():
            signal_run_list.set_current_scene.emit(self.run_id, "庭院")
            signal_run_list.set_current_operation.emit(self.run_id, "进入探索地图")
            self.processing_yard()
