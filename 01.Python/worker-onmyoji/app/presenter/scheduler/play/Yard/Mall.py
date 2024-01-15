from ..Common import *


class PlayMall(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayMall, self).__init__(play_input)

    def run(self):
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                if self.is_mall():
                    if self.is_mall_recommend_close_button():
                        self.close_mall_recommend()
                    else:
                        chapter_stage = self.product.chapter_stage
                        if chapter_stage == "normal_scale":
                            self.run_mall_scale()
                        elif chapter_stage == "medal_mall":
                            self.run_mall_medal()
                        elif chapter_stage == "honor_mall":
                            self.run_mall_honor()
                        elif chapter_stage == "gift_lot":
                            self.run_mall_gift_room_lot()
                else:
                    self.open_mall()
            self.sleep_in_run()
        else:
            self.run_status.set_play_standby_status(self.run_id, False)
            self.is_play_finished = True
            self.sleep_in_run()

    def run_mall_scale(self):
        if self.is_mall_mystery():
            pass
        else:
            self.open_mystery_room()

    def run_mall_medal(self):
        if self.is_mall_general():
            if self.is_mall_general_medal():
                result, coord = self.find_collection_prize_panel_common()
                if result:
                    self.click_in_circle([coord[0] + 300, coord[1]], 54)
                elif self.is_mall_general_medal_confirm_button_1():
                    self.confirm_mall_general_medal_confirm_1()
                else:
                    if self.is_mall_general_medal_mystery():
                        self.buy_general_medal_mystery()
                    else:
                        result, coord = self.find_mall_general_medal_skill_daruma()
                        if result:
                            self.click_in_circle(coord)
                        else:
                            self.stop_flag = True
            else:
                self.open_mall_general_medal()
        else:
            self.open_mall_general()

    def run_mall_honor(self):
        if self.is_mall_general():
            if self.is_mall_general_honor():
                result, coord = self.find_collection_prize_panel_common()
                if result:
                    self.click_in_circle([coord[0] + 300, coord[1]], 54)
                else:
                    pass
            else:
                self.open_mall_general_honor()
        else:
            self.open_mall_general()

    def run_mall_gift_room_lot(self):
        if self.is_mall_gift_room():
            result, coord = self.find_collection_prize_panel_common()
            if result:
                self.stop_flag = True
            elif self.is_mall_gift_room_skill_daruma_clicked():
                self.stop_flag = True
            elif self.is_mall_gift_room_skill_daruma():
                self.click_mall_gift_daruma()
            else:
                self.stop_flag = True
        else:
            self.open_mall_gift()

    def open_mall(self):
        if self.is_yard():
            self.open_mall_panel()
        elif self.is_explore():
            self.quit_explore()
