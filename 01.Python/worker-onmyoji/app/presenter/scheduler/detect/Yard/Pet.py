from hiworker import *


class DetectPet(DetectImage):
    def __init__(self):
        super(DetectPet, self).__init__()

    def is_pets_house(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house")
        return result

    def is_pets_house_quit_button(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_quit_button")
        return result

    def is_pets_house_operation_menu_close(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_operation_close")
        return result

    def is_pets_house_operation_menu_open(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_operation_open")
        return result

    def is_pets_house_dinner_button(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_dinner_button")
        return result

    def is_pets_house_dinner_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_dinner_panel")
        return result

    def is_pets_house_dinner_panel_feed_button(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_dinner_panel_feed_button")
        return result

    def is_pets_house_dinner_eating(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_dinner_eating")
        return result

    def is_pets_house_dinner_not_hungry(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_dinner_not_hungry")
        return result

    def is_pets_house_play_button(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_play_button")
        return result

    def is_pets_house_play_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_play_panel")
        return result

    def is_pets_house_play_panel_play_button(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_dinner_panel_play_button")
        return result

    def is_pets_house_play_panel_playing(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_playing")
        return result

    def is_pets_house_play_happy(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_play_happy")
        return result

    def is_pets_house_single_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("pet_is_pets_house_single_panel")
        return result
