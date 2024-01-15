from ..Common import *


class PlayPet(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayPet, self).__init__(play_input)
        self.feed_pet_done = False
        self.play_pet_done = False

    def run(self):
        self.feed_pet_done = False
        self.play_pet_done = False
        self.is_play_finished = False
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                if self.product.play_name_second == "play":
                    self.run_play_pet()
                elif self.product.play_name_second == "feed":
                    self.run_feed_pet()
                elif self.product.play_name_second == "all":
                    self.run_feed_and_play_pet()
            else:
                self.stop_status = True
                self.is_play_finished = True

    def run_play_pet(self):
        if self.play_pet_done:
            if self.is_pets_house():
                self.quit_pets_house()
            elif self.is_yard():
                self.stop_flag = True
        elif self.is_pets_house_play_panel():
            if self.is_pets_house_play_happy():
                self.play_pet_done = True
            else:
                self.click_pets_house_play_panel_play_button()

        elif self.is_pets_house():
            if self.is_pets_house_operation_menu_open():
                if self.is_pets_house_play_button():
                    self.click_pets_house_play_button()
            else:
                self.open_pets_house_operation_menu()
        elif self.is_yard():
            result, coord = self.find_pet_house_entrance()
            if result:
                self.click_in_circle(coord)
        elif self.is_explore():
            self.quit_explore()

    def run_feed_pet(self):
        if self.feed_pet_done:
            if self.is_pets_house():
                self.quit_pets_house()
            elif self.is_yard():
                self.stop_flag = True
        elif self.is_pets_house_dinner_panel():
            if self.is_pets_house_dinner_not_hungry():
                self.feed_pet_done = True
            else:
                self.click_pets_house_dinner_panel_feed_button()
        elif self.is_pets_house():
            if self.is_pets_house_operation_menu_open():
                if self.is_pets_house_dinner_button():
                    self.click_pets_house_dinner_button()
            else:
                self.open_pets_house_operation_menu()
        elif self.is_yard():
            result, coord = self.find_pet_house_entrance()
            if result:
                self.click_in_circle(coord)
        elif self.is_explore():
            self.quit_explore()

    def run_feed_and_play_pet(self):
        if self.is_pets_house_play_panel():
            if self.is_pets_house_play_happy():
                self.play_pet_done = True
            else:
                self.click_pets_house_play_panel_play_button()
        elif self.is_pets_house_dinner_panel():
            if self.is_pets_house_dinner_not_hungry():
                self.feed_pet_done = True
            else:
                self.click_pets_house_dinner_panel_feed_button()
        elif self.feed_pet_done and self.play_pet_done:
            if self.is_pets_house():
                self.quit_pets_house()
            elif self.is_yard():
                self.stop_flag = True
        elif self.is_pets_house():
            if not self.feed_pet_done:
                if self.is_pets_house_operation_menu_open():
                    if self.is_pets_house_dinner_button():
                        self.click_pets_house_dinner_button()
                else:
                    self.open_pets_house_operation_menu()
            elif not self.play_pet_done:
                if self.is_pets_house_operation_menu_open():
                    if self.is_pets_house_dinner_button():
                        self.click_pets_house_dinner_button()
                else:
                    self.open_pets_house_operation_menu()
            else:
                self.is_play_finished = True
        elif self.is_yard():
            result, coord = self.find_pet_house_entrance()
            if result:
                self.click_in_circle(coord)
        elif self.is_explore():
            self.quit_explore()
