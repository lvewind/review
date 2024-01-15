from hiworker import *


class DetectDuel(DetectImage):
    def __init__(self):
        super(DetectDuel, self).__init__()

    def is_daily_duel_room(self):
        """
        是否在斗技房间
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_duel_room")
        return result

    def is_daily_duel_room_battle_button(self):
        """
        是否存在斗技战斗按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_duel_room_battle_button")
        return result

    def is_daily_duel_room_battle_button_break(self):
        """
        是否存在斗技破碎按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_duel_room_battle_button_break")
        return result
