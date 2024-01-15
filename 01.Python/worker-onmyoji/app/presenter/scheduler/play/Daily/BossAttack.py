from ..Common import *


class PlayBossAttack(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayBossAttack, self).__init__(play_input)

    def run(self):
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                if self.is_daily_panel_daily():
                    if self.is_daily_boss_attack_entrance_panel():
                        self.click_daily_go_to_button()
                    else:
                        result, coord = self.find_daily_boss_attack_entrance()
                        if result:
                            self.click_in_circle(coord)
                        else:
                            self.stop_flag = True
                else:
                    self.open_daily_panel_in_yard()
