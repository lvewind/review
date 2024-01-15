from ..Common import *


class PlayDuel(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayDuel, self).__init__(play_input)

    def run(self):
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                preset_count = self.product.preset_count
                if not self.approximate_count_set:
                    if self.product.approximate_count:
                        if random.randint(0, 1):
                            preset_count = preset_count + (int(preset_count / 20) + 1)
                        else:
                            preset_count = preset_count - (int(preset_count / 20) + 1)

                    else:
                        self.approximate_count_set = True
                preset_count = 100

                if self.counter < preset_count:
                    if self.is_scene_after_battling:
                        if self.is_battle_win_duel():  # 胜利
                            self .processing_battle_win_duel()
                        elif self.is_battle_failed_duel():  # 失败
                            self .processing_battle_failed_duel()
                    else:
                        if self.is_battle_battling():
                            self .processing_battling()
                        elif self.is_battle_ready():
                            self.set_battle_ready()
                        elif self.is_daily_duel_room():  # 斗技房间
                            self.click_daily_duel_room_battle_button()
                        elif self.is_activity_panel():  # 活动面板
                            if self.is_activity_panel_daily():
                                if self.is_daily_draft_duel_entrance_panel():
                                    self.click_daily_go_to_button()
                                else:
                                    result, coord = self.find_daily_duel_entrance()
                                    if result:
                                        self.click_in_circle(coord)
                                    else:
                                        self.stop_flag = True
                            else:
                                self.select_daily_panel_daily()

                        else:
                            self.open_daily_panel_in_yard()     # 打开日常界面
            else:
                if self.is_yard():
                    self.stop_status = True
                elif self.is_daily_duel_room():
                    self.quit_duel_room()
                elif self.is_battle_win_duel():  # 胜利
                    self .processing_battle_win_duel()
                elif self.is_battle_failed_duel():  # 失败
                    self .processing_battle_failed_duel()

    def processing_battle_win_duel(self):
        signal_run_list.set_current_scene.emit(self.run_id, "战斗胜利")
        while self.is_battle_win_prize():
            if random.randint(1, 3) == 1:
                self.skip_battle_win_duel_1()
            elif random.randint(1, 3) == 2:
                self.skip_battle_win_duel_1()
            elif random.randint(1, 3) == 3:
                self.skip_battle_win_duel_1()
        else:
            signal_run_list.set_current_operation.emit(self.run_id, "跳过胜利")
            self.is_scene_after_battling = False
            self.counter += 1
            self.upgrade_daily_counter()

    def processing_battle_failed_duel(self):
        signal_run_list.set_current_scene.emit(self.run_id, "战斗失败")
        if random.randint(1, 3) == 1:
            self.skip_battle_win_duel_1()
        elif random.randint(1, 3) == 2:
            self.skip_battle_win_duel_1()
        elif random.randint(1, 3) == 3:
            self.skip_battle_win_duel_1()
