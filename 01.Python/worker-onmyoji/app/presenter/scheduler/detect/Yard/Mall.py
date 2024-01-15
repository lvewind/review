from hiworker import *


class DetectMall(DetectImage):
    def __init__(self):
        super(DetectMall, self).__init__()

    def is_mall(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall")
        return result

    def is_mall_recommend_close_button(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_recommend_close_button")
        return result

    def is_mall_mystery(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mystery_room", 0.9)
        return result

    def is_mall_plain_souls_box(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_plain_souls_box")
        return result

    def is_mall_plain_souls_box_exchange_button(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_plain_souls_box_exchange_button")
        return result

    def is_mall_plain_souls_box_exchange_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_plain_souls_box_exchange_panel")
        return result

    def is_mall_plain_souls_box_exchange_set_top_button(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_plain_souls_box_exchange_set_top_button")
        return result

    def is_mall_plain_souls_box_sue_up(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_plain_souls_box_sue_up")
        return result

    def is_mall_general(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general", 0.9)
        return result

    def is_mall_general_honor(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_honor", 0.9)
        return result

    def find_mall_general_honor_mystery_amulet(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_honor_mystery_amulet")
        return result

    def find_mall_general_honor_mystery_amulet_exchange_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_honor_mystery_amulet_exchange_panel")
        return result

    def find_mall_general_honor_skill_daruma(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_find_mall_general_honor_skill_daruma")
        return result

    def is_mall_general_friend(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_friend", 0.9)
        return result

    def is_mall_general_friend_grade_daruma(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_friend_grade_daruma")
        return result

    def is_mall_general_friend_grade_daruma_use_up(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_friend_grade_daruma_use_up")
        return result

    def is_mall_general_friend_confirm_grade_daruma(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_friend_confirm_grade_daruma")
        return result

    def is_mall_general_medal(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_medal", 0.9)
        return result

    def is_mall_general_medal_mystery(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_medal_mystery")
        return result

    def find_mall_general_medal_skill_daruma(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_find_mall_general_medal_skill_daruma")
        return result, coord

    def find_mall_general_medal_grade_daruma(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_find_mall_general_medal_grade_daruma")
        return result

    def find_mall_general_medal_six_star_souls(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_find_mall_general_medal_six_star_souls")
        return result

    def is_mall_gift_room(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_gift_room")
        return result

    def is_mall_gift_room_skill_daruma(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_gift_room_skill_daruma")
        return result

    def is_mall_gift_room_skill_daruma_clicked(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_gift_room_skill_daruma_clicked")
        return result

    def is_mall_general_medal_confirm_button_1(self):
        result, coord, max_similarity = self.find_in_template_rect("mall_is_mall_general_medal_confirm_button_1")
        return result
