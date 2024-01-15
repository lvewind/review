from hiworker import *


class OperateDuel(Win32Click):
    def __init__(self):
        super(OperateDuel, self).__init__()

    def click_daily_duel_room_battle_button(self):
        """
        进入斗技
        :return:
        """
        self.click_in_template("daily_is_daily_duel_room_battle_button")

    def quit_duel_room(self):
        """
        退出斗技房间
        :return:
        """
        self.click_in_template("daily_quit_duel_room")
