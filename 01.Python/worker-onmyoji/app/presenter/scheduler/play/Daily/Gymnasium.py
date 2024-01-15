from ..Common import *


class PlayGymnasium(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayGymnasium, self).__init__(play_input)

    def run(self):
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                if self.is_daily_panel_daily():
                    pass
                else:
                    self.open_daily_panel_in_yard()
