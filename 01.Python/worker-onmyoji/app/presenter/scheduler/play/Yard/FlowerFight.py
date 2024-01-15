from ..Common import *


class PlayFlowerFight(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayFlowerFight, self).__init__(play_input)
        self.is_flower_task_finished = False
        self.is_flower_prize_finished = False

    def run(self):
        self.is_flower_task_finished = False
        self.is_flower_prize_finished = False
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                result, coord = self.find_collection_prize_panel_common()
                if result:
                    self.click_in_circle([coord[0] + 255, coord[1]], 50)
                elif self.is_flower_fight_prize_select_button():
                    self.click_flower_fight_prize_select_button()
                elif self.is_flower_fight_panel():
                    if not self.is_flower_task_finished:
                        if self.is_flower_fight_panel_task_panel():
                            if self.is_flower_fight_panel_task_get_all_button():
                                self.get_flower_fight_all_task()
                            else:
                                self.is_flower_task_finished = True
                        else:
                            self.select_flower_fight_task_panel()
                    elif not self.is_flower_prize_finished:
                        if self.is_flower_fight_panel_prize_panel():
                            if self.is_flower_fight_panel_prize_get_all_button():
                                self.get_flower_fight_all_prize()
                            else:
                                self.is_flower_prize_finished = True
                        else:
                            self.select_flower_fight_prize_panel()
                    else:
                        self.quit_flower_fight()
                        self.is_play_finished = True
                elif self.is_play_finished:
                    self.stop_flag = True
                elif self.is_yard():
                    if self.is_flower_fight_entrance():
                        self.open_flower_fight()
                elif self.is_explore():
                    self.quit_explore()
            else:
                self.is_play_finished = False
                self.stop_status = True
