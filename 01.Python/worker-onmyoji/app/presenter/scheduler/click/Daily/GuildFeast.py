from hiworker import *


class OperateGuildFeast(Win32Click):
    def __init__(self):
        super(OperateGuildFeast, self).__init__()

    def click_change_dog_food_button(self):
        """
        点击更换狗粮按钮
        :return:
        """
        self.click_in_template("guild_feast_click_change_dog_food_button")
