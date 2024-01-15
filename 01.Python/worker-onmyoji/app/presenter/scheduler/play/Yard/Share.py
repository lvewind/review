from ..Common import *


class PlayShare(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayShare, self).__init__(play_input)
        self.send_flower = 0
        self.receive_flower = 0
        self.flower_list_set = False
        self.friend_list_set = False
        self.friend_list_open_set = False
        self.mail_list_slide_times = 0
        self.is_flower_task_finished = False
        self.is_flower_prize_finished = False

    def run(self):
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                if self.is_illustrate_handbook_share_button():
                    if self.is_illustrate_handbook_share_qrcode():
                        self.is_play_finished = True
                    elif self.is_illustrate_handbook_qrcode_loading():
                        self.sleep_in_run()
                    elif self.is_illustrate_handbook_share_to_wechat():
                        self.share_illustrate_handbook_to_wechat()
                    else:
                        self.open_illustrate_handbook_share_method()
                elif self.is_illustrate_handbook_shikigami_list():
                    self.open_illustrate_handbook_shikigami_scroll()
                elif self.is_illustrate_handbook_panel():
                    if self.is_illustrate_handbook_shikigami_entrance():
                        self.open_illustrate_handbook_shikigami_list()
                    else:
                        self.is_play_finished = True
                elif self.is_play_finished:
                    self.stop_flag = True
                elif self.is_yard():
                    self.open_illustrated()
                elif self.is_explore():
                    self.quit_explore()
            else:
                self.is_play_finished = False
                self.stop_status = True
                self .processing_stop()
