from hiworker import *


class DetectGuildFeast(DetectImage):
    def __init__(self):
        super(DetectGuildFeast, self).__init__()

    def is_guild_feast_room(self):
        """
        是否是宴会房间
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_is_guild_feast_room")
        return result

    def find_guild_feast_food_left(self):
        """
        查找宴会左边食物
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_find_guild_feast_food_left")
        return result

    def find_guild_feast_food_center(self):
        """
        查找宴会中间食物
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_find_guild_feast_food_center")
        return result

    def find_guild_feast_food_right(self):
        """
        查找宴会右边食物
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_find_guild_feast_food_right")
        return result

    def is_guild_feast_barrage_on(self):
        """
        弹幕是否开启
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_is_guild_feast_barrage_on")
        return result

    def is_guild_feast_barrage_off(self):
        """
        弹幕是否关闭
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_is_guild_feast_barrage_on")
        return result

    def find_guild_feast_prize(self):
        """
        查找宴会奖励
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_find_guild_feast_prize")
        return result, coord

    def is_guild_feast_dog_food_full(self):
        """
        是否宴会狗粮满级
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_is_guild_feast_dog_food_full")
        return result

    def is_guild_fireworks_button(self):
        """
        是否有烟花按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_is_guild_fireworks_button")
        return result

    def is_guild_fireworks_panel(self):
        """
        是否有烟花界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_feast_is_guild_fireworks_panel")
        return result
