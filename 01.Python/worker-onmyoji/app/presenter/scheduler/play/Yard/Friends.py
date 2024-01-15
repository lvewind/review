from ..Common import *


class PlayFriends(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayFriends, self).__init__(play_input)
        self.friend_list_open_set = False

    def run(self):
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                if self.is_friend_panel():
                    if self.flower_list_set:
                        if self.is_friend_get_one_key_flower():
                            self.click_one_key_flower()
                        else:
                            self.is_play_finished = True
                    elif self.is_friend_panel_friend_list_flower():
                        self.flower_list_set = True
                    else:
                        self.open_friend_panel_friend_list_flower()
                elif self.is_play_finished:
                    self.stop_flag = True
                elif self.is_yard():
                    if self.is_friend_entrance():
                        self.open_friend()
                elif self.is_explore():
                    self.quit_explore()
            else:
                self.is_play_finished = True
                self.stop_status = True
        else:
            self.is_play_finished = True
