from ..Common import *


class PlayBountySeals(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayBountySeals, self).__init__(play_input)

    def run(self):
        while not self.stop_flag:
            if self.is_bounty_seals_invite_panel():
                self.close_bounty_seals_panel()
