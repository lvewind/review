from ..Common import *


class PlaySummon(Common):
    def __init__(self, play_input: PlayInput):
        super(PlaySummon, self).__init__(play_input)
        self.normal_summon_count = 0
        self.mystery_summon_count = 0

    def run(self):
        self.normal_summon_count = 0
        self.mystery_summon_count = 0
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                if self.product.play_name_second == "summon_free":
                    self.run_free_summon()
                elif self.product.play_name_second == "summon_normal":
                    self.run_normal_summon()
                elif self.product.play_name_second == "summon_ten":
                    self.run_ten_summon()
            else:
                self .processing_stop()

    def run_free_summon(self):
        if self.is_summon_normal_confirm_button():
            self.click_summon_normal_confirm_button()
        elif self.is_summon_back_button():
            self.draw_summon()
        elif self.is_summon_room():
            if self.is_summon_free_button():
                self.click_free_summon_button()
            else:
                self.stop_flag = True
        elif self.is_yard():
            self.open_summon_room()
        elif self.is_explore():
            self.quit_explore()

    def run_normal_summon(self):
        if self.is_summon_normal_confirm_button():
            if self.normal_summon_count < self.product.preset_count:
                signal_run_list.set_current_operation.emit(self.run_id, "再次召唤")
                self.click_summon_normal_again_button()
                self.normal_summon_count += 1
            else:
                self.click_summon_normal_confirm_button()
                self.stop_flag = True
        elif self.is_summon_room():
            if self.is_summon_normal_button():
                self.click_summon_normal_button()
        elif self.is_yard():
            result, coord = self.find_summon_room_entrance()
            if result:
                self.click_in_circle(coord)
        elif self.is_explore():
            self.quit_explore()

    def run_ten_summon(self):
        if self.is_summon_share_button():
            self.skip_summon_share()
        elif self.is_summon_back_button():
            if self.is_summon_mystery_buy_amulet_panel():
                self.close_summon_mystery_buy_amulet_panel()
                self.stop_flag = True
            else:
                if self.is_summon_mystery_ten_selected():
                    if self.mystery_summon_count < self.product.preset_count:
                        self.draw_summon()
                        self.mystery_summon_count += 1
                    else:
                        self.stop_flag = True
        elif self.is_summon_room():
            if self.is_summon_mystery_button():
                self.click_summon_mystery_button()
        elif self.is_yard():
            self.open_summon_room()
        elif self.is_explore():
            self.quit_explore()

    def processing_stop(self):
        self.is_play_finished = True
        if self.is_summon_room():
            self.quit_summon_room()
        elif self.is_summon_back_button():
            self.click_summon_back_button()
        elif self.is_summon_share_button():
            self.skip_summon_share()
        elif self.is_summon_normal_confirm_button():
            self.click_summon_normal_confirm_button()
        elif self.is_yard():
            self.stop_status = True

    def draw_summon(self):
        pass
