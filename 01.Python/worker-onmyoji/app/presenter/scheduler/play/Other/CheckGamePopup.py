from ..Common import *


class CheckGamePopup(Common):
    def __init__(self, play_input: PlayInput):
        super(CheckGamePopup, self).__init__(play_input)

    def run(self):
        while not self.stop_flag:
            if self.is_bounty_seals_invite_panel():
                self.close_bounty_seals_panel()
            if self.is_chat_panel():
                self.close_chat_panel()
            if self.is_bonus_stop_panel():
                self.close_bonus_stop_panel()
            self.sleep_in_run(0.5)
