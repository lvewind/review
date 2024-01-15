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
                play_name_second = self.product.play_name_second
                if play_name_second == "get_lot":
                    self.run_get_lot()
                elif play_name_second == "get_bonus":
                    self.run_get_lot()
                elif play_name_second == "get_jade":
                    self.run_get_jade()
                elif play_name_second == "get_ap":
                    self.run_get_ap()
            else:
                self.is_play_finished = False
                self.stop_status = True

    def run_get_lot(self):
        if self.is_collection_lot_finish_panel():
            self.close_lot_finish()
            self.is_play_finished = True
        elif self.is_play_finished:
            self.stop_flag = True
        elif self.is_collection_lot_panel():
            self.get_lot()
        elif self.is_yard():
            result, coord = self.find_lot_button()
            if result:
                self.click_in_circle(coord)
            else:
                self.stop_flag = True
        elif self.is_explore():
            self.quit_explore()

    def run_get_lot_999(self):
        if self.is_lot_999_prize():
            self.close_lot_999_prize()
            self.is_play_finished = True
        elif self.is_play_finished:
            self.stop_flag = True
        elif self.is_yard():
            result, coord = self.find_999_lot_button()
            if result:
                self.click_in_circle(coord)
            else:
                self.stop_flag = True
        elif self.is_explore():
            self.quit_explore()

    def run_get_bonus(self):
        result, coord = self.find_collection_prize_panel_common()
        if result:
            self.click_in_circle([coord[0] + 255, coord[1]], 50)
            self.is_play_finished = True
        elif self.is_play_finished:
            self.stop_flag = True
        else:
            if self.is_collection_souls_bonus_confirm_button():
                self.confirm_collection_souls_bonus()
            elif self.is_yard():
                result, coord = self.find_bonus_button_in_yard()
                if result:
                    self.click_in_circle(coord)
                else:
                    self.stop_flag = True
            elif self.is_explore():
                self.quit_explore()

    def run_get_jade(self):
        result, coord = self.find_collection_prize_panel_common()
        if result:
            self.click_in_circle([coord[0] + 255, coord[1]], 50)
            self.is_play_finished = True
        elif self.is_play_finished:
            self.stop_flag = True
        elif self.is_yard():
            result, coord = self.find_jade_button()
            if result:
                self.click_in_circle(coord)
            else:
                self.stop_flag = True
        elif self.is_explore():
            self.quit_explore()

    def run_get_ap(self):
        result, coord = self.find_collection_prize_panel_common()
        if result:
            self.click_in_circle([coord[0] + 255, coord[1]], 50)
            self.is_play_finished = True
        elif self.is_play_finished:
            self.stop_flag = True
        elif self.is_yard():
            result, coord = self.find_ap_button()
            if result:
                self.click_in_circle(coord)
            else:
                self.stop_flag = True
        elif self.is_explore():
            self.quit_explore()
