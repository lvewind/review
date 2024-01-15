from ..Common import *


class PlayYard(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayYard, self).__init__(play_input)
        self.mail_list_slide_times = 0

    def run(self):
        self.mail_list_slide_times = 0
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                if self.is_collection_mail_get_all_confirm_panel():
                    self.confirm_get_all_mail()
                elif self.is_collection_mail_panel():
                    result, coord = self.find_collection_prize_panel_common()
                    if result:
                        self.click_in_circle([coord[0] + 255, coord[1]], 50)
                    elif self.is_collection_mail_get_all_button():
                        self.click_get_all_mail_button()
                    else:
                        result, coord = self.find_collection_mail_not_read()
                        if result:
                            self.click_in_circle(coord)
                        else:
                            if self.mail_list_slide_times <= 3:
                                self.slide_mail_list_to_bottom()
                                self.mail_list_slide_times += 1
                            else:
                                self.close_mail_panel()
                                self.is_play_finished = True
                elif self.is_play_finished:
                    self.stop_flag = True
                elif self.is_yard():
                    self.open_mail()
                elif self.is_explore():
                    self.quit_explore()
            else:
                self.is_play_finished = False
                self.stop_status = True
