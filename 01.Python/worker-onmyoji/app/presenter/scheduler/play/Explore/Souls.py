from ..Common import *
from ....sender import signal_run_list


class PlaySouls(Common):
    def __init__(self, play_input: PlayInput):
        super(PlaySouls, self).__init__(play_input)
        self.souls_selected = False
        self.can_team_up = True

    def run(self):
        self.souls_selected = False
        self.set_run_status_default()
        # 初始化预设场数
        self.set_preset_count()
        while not self.stop_status:
            self.check_chat_panel()
            self.teamup_mode = self.play_input.run_list.teamup_mode
            if not self.stop_flag:
                # 体力用完
                if self.ap_use_up:
                    self.stop_flag = True
                # 未达到预设场数且队友未完成
                elif self.counter < self.preset_count and not self.is_teammate_finished():
                    self.run_status.set_play_standby_status(self.run_id, True)  # 设置自身就绪状态
                    if self.run_status.get_play_standby_status(int(self.play_input.run_list.teammate_id)) \
                            or self.play_input.run_list.teamup_mode == "single_solo" \
                            or self.product.play_name_second == "sougenbi":      # 队友已就绪或单刷或业原火
                        if self.is_scene_after_battling:        # 战斗结束
                            self.processing_after_battle()
                        else:
                            if self.is_battle_win_prize_daruma():  # 战斗奖励
                                self.skip_battle_win_prize(random.randint(1, 3))
                            elif self.is_battle_battling():   # 战斗中
                                self.processing_battling()
                            elif self.is_battle_ready():    # 战斗准备
                                self.processing_battle_ready()
                            elif self.is_cooperation_teamup_panel():    # 协战队伍
                                self.processing_cooperation_teamup()
                            elif self.is_team_panel():  # 组队界面
                                self.processing_teamup()
                            elif self.is_souls_stage_panel():   # 层数选择
                                self.processing_souls_stage_panel()
                            elif self.is_souls_zone_panel():   # 御魂副本选择
                                signal_run_list.set_current_scene.emit(self.run_id, "御魂")
                                signal_run_list.set_current_operation.emit(self.run_id, "选择御魂副本")
                                if self.product.play_name_second == "orochi":
                                    self.select_souls_zone_orochi()
                                elif self.product.play_name_second == "sougenbi":
                                    self.select_souls_zone_sougenbi()
                                elif self.product.play_name_second == "himiko":
                                    self.select_souls_zone_himiko()
                            elif self.is_explore():     # 探索地图
                                self.processing_explore()
                            elif self.is_yard():        # 庭院
                                self.processing_yard()
                            elif self.team_position == "captain":
                                self.processing_auto_invite_after_battle()
                    else:
                        if not self.stop_flag:
                            signal_run_list.set_current_operation.emit(self.run_id, "等待队友就绪")
                else:
                    self.stop_flag = True
            else:
                self.is_finished = True
                self.run_status.set_play_standby_status(self.run_id, False)
                self .processing_stop()
            self.sleep_in_run()

    # 探索地图
    def processing_explore(self):
        if self.team_position == "captain" or self.product.play_name_second == "sougenbi":
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
                signal_run_list.set_current_operation.emit(self.run_id, "打开御魂")
                self.open_souls()
        else:
            self.set_bonus(where="explore")

    # 层数选择界面
    def processing_souls_stage_panel(self):
        signal_run_list.set_current_scene.emit(self.run_id, "御魂界面")
        if self.stage_selected:
            # 单人单刷
            if self.play_input.run_list.teamup_mode == "single_solo" or self.product.play_name_second == "sougenbi":
                if self.auto_doll_set:
                    if self.doll_active:
                        signal_run_list.set_current_operation.emit(self.run_id, "自动挑战")
                    else:
                        signal_run_list.set_current_operation.emit(self.run_id, "开始挑战")
                        if self.product.play_name_second == "sougenbi":
                            self.challenge_sougenbi()
                        else:
                            self.challenge_orochi()
                elif self.cast_lock_set:
                    self.check_auto_doll_in_stage_panel()
                else:
                    self.check_cast_lock_in_stage_panel()
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "开始组队")
                self.teamup_souls()
        elif self.souls_selected:
            if self.product.play_name_second == "sougenbi":
                self.processing_sougenbi_stage_panel()
            elif self.product.play_name_second == "himoko":
                self.processing_himiko_stage_panel()
            elif self.product.play_name_second == "orochi":
                self.processing_orochi_stage_panel()
        else:
            if self.product.play_name_second == "orochi":
                if self.is_souls_stage_panel_orochi():
                    self.souls_selected = True
                elif self.is_souls_zone_orochi():
                    self.select_souls_zone_orochi()
                else:
                    self.select_souls_stage_panel_orochi()
            elif self.product.play_name_second == "sougenbi":
                if self.is_souls_stage_panel_sougenbi():
                    self.souls_selected = True
                elif self.is_souls_zone_sougenbi():
                    self.select_souls_zone_sougenbi()
                else:
                    self.select_souls_stage_panel_sougenbi()
            elif self.product.play_name_second == "himiko":
                if self.is_souls_stage_panel_himiko():
                    self.souls_selected = True
                elif self.is_souls_zone_himiko():
                    self.select_souls_zone_himiko()
                else:
                    self.select_souls_stage_panel_himiko()

    # 八岐大蛇层数选择
    def processing_orochi_stage_panel(self):
        result, coord = False, [0, 0]
        if self.product.play_name_second == "orochi":
            result = getattr(self, "is_souls_orochi_stage_selected_" + str(self.product.chapter_stage))()
        if result:
            self.stage_selected = True
        else:
            result, coord = getattr(self, "find_souls_orochi_stage_" + str(self.product.chapter_stage))()
            if result:
                self.select_souls_orochi_stage(coord)
            elif self.product.chapter_stage < 6:
                self.slide_down_evo_stage_list()
            else:
                self.slide_up_evo_stage_list()

    # 业原火层数选择
    def processing_sougenbi_stage_panel(self):
        result = getattr(self, "is_souls_sougenbi_selected_" + str(self.product.chapter_stage))()
        if result:
            self.stage_selected = True
        else:
            getattr(self, "select_sougenbi_" + str(self.product.chapter_stage))()

    # 日轮层数选择
    def processing_himiko_stage_panel(self):
        result = getattr(self, "is_souls_himiko_stage_selected_" + str(self.product.chapter_stage))()
        if result:
            self.stage_selected = True
        else:
            getattr(self, "select_himiko_stage_" + str(self.product.chapter_stage))()

    # 永生之海层数选择
    def processing_over_sea_stage_panel(self):
        pass

    # 探索地图队友
    def processing_explore_teammate(self):
        signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
        if self.bonus_all_set or not self.config_bonus:
            if self.is_bonus_panel():
                self.close_bonus_panel()
            elif not self.auto_accept:
                if self.product.play_name == "souls":
                    if self.is_confirm_auto_accept_panel():
                        if self.is_confirm_auto_accept_panel_checked():
                            self.confirm_auto_accept_panel()
                        else:
                            self.checked_confirm_auto_accept_panel()
                    else:
                        self.waiting_for_invite_souls()
        else:
            self.set_bonus(where="explore")

    def waiting_for_invite_souls(self):
        signal_run_list.set_current_operation.emit(self.run_id, "等待队长邀请")
        play_name_second = self.product.play_name_second
        if play_name_second == "orochi":
            if getattr(self, "is_invite_orochi_stage_" + str(self.product.chapter_stage))():
                self.accept_invite_common()
        elif play_name_second == "himiko":
            if getattr(self, "is_invite_himiko_stage_" + str(self.product.chapter_stage))():
                self.accept_invite_common()

    def processing_stop(self):
        if self.is_battle_auto_invite_panel():
            self.cancel_auto_invite()
        elif self.is_explore():
            self.process_explore_after_task()
        elif self.is_cooperation_teamup_panel():
            self.process_quit_cooperation_teamup_panel()
        elif self.is_souls_stage_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "御魂界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出御魂")
            self.quit_souls_stage_panel()
        elif self.is_team_panel():
            self.close_teamup_panel()
        elif self.is_battle_win_drum_souls():
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
            self.processing_yard()
