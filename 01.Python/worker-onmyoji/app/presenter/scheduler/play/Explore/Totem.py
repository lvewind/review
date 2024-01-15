from ..Common import *
from ....sender import signal_run_list


class PlayTotem(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayTotem, self).__init__(play_input)
        self.totem_selected = False

    def run(self):
        self.totem_selected = False
        self.set_run_status_default()
        self.set_preset_count()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:

                if self.counter < self.preset_count:
                    if self.is_scene_after_battling:
                        self.processing_after_battle()
                    else:
                        if self.is_battle_win_prize_daruma():  # 战斗奖励
                            self.skip_battle_win_prize(random.randint(1, 3))
                        elif self.is_battle_battling():
                            self.processing_battling()
                        elif self.is_battle_ready():
                            self.processing_battle_ready()
                        elif self.is_totem_stage_panel():
                            self.processing_totem_stage_panel()
                        elif self.is_totem_zone_select_panel():
                            self.processing_totem_zone_select_panel()
                        elif self.is_explore():
                            self.processing_explore()
                        elif self.is_yard():
                            self.processing_yard()
                else:
                    self.stop_flag = True
            else:
                self.is_finished = True
                self.processing_stop()
            self.sleep_in_run()

    def processing_totem_zone_select_panel(self):
        signal_run_list.set_current_scene.emit(self.run_id, "御灵之境")
        signal_run_list.set_current_operation.emit(self.run_id, "选择御灵")
        week_day = time.localtime(time.time())[6] + 1
        if week_day == 6 or week_day == 7:
            if self.product.play_name_second == "an_shen_long":
                self.select_totem_zone_panel_shenlong()
            elif self.product.play_name_second == "an_bai_zang_zhu":
                self.select_totem_zone_panel_baizhangzhu()
            elif self.product.play_name_second == "an_hei_bao":
                self.select_totem_zone_panel_heibao()
            elif self.product.play_name_second == "an_kong_que":
                self.select_totem_zone_panel_kongque()
        elif week_day == 5:
            self.select_totem_zone_panel_kongque()
        elif week_day == 4:
            self.select_totem_zone_panel_heibao()
        elif week_day == 3:
            self.select_totem_zone_panel_baizhangzhu()
        elif week_day == 2:
            self.select_totem_zone_panel_shenlong()
        else:
            self.stop_flag = True
            self.is_finished = True

    def processing_totem_stage_panel(self):
        signal_run_list.set_current_scene.emit(self.run_id, "御灵层数")
        if self.auto_doll_set:
            self.challenge_totem()
        elif self.cast_lock_set:
            self.check_auto_doll_in_stage_panel()
        elif self.stage_selected:
            self.check_cast_lock_in_stage_panel()
        elif self.totem_selected:
            result = getattr(self, "is_totem_stage_selected_" + str(self.product.chapter_stage))()
            if result:
                self.stage_selected = True
            else:
                getattr(self, "select_totem_stage_" + str(self.product.chapter_stage))()

        else:
            week_day = time.localtime(time.time())[6] + 1
            if week_day == 6 or week_day == 7:
                if self.product.play_name_second == "an_shen_long":
                    self.select_totem_zone_panel_shenlong()
                    self.totem_selected = True
                elif self.product.play_name_second == "an_bai_zang_zhu":
                    self.select_totem_zone_panel_baizhangzhu()
                    self.totem_selected = True
                elif self.product.play_name_second == "an_hei_bao":
                    self.select_totem_zone_panel_heibao()
                    self.totem_selected = True
                elif self.product.play_name_second == "an_kong_que":
                    self.select_totem_zone_panel_kongque()
                    self.totem_selected = True
            elif week_day == 5:
                self.totem_selected = True
            elif week_day == 4:
                self.totem_selected = True
            elif week_day == 3:
                self.totem_selected = True
            elif week_day == 2:
                self.totem_selected = True

    def processing_explore(self):
        signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
        if self.bonus_all_set or not self.config_bonus:
            if self.is_bonus_panel():
                self.close_bonus_panel()
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "打开御灵")
                self.open_totem()
        else:
            self.set_bonus(where="explore")

    def processing_stop(self):
        if self.is_totem_stage_panel():
            signal_run_list.set_current_operation.emit(self.run_id, "退出层数选择")
            self.quit_totem_stage_panel()
        elif self.is_battle_win_prize_daruma():
            self.process_battle_win_prize_daruma()
        elif self.is_battle_failed_drum():
            self.process_battle_failed_drum()
        elif self.is_battle_battling():
            self.processing_battling()
        elif self.is_explore():
            self.process_explore_after_task()
        elif self.is_yard():
            self.processing_yard()
