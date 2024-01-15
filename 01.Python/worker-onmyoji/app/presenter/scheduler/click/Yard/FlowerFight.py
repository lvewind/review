from hiworker import *


class OperateFlowerFight(Win32Click):
    def __init__(self):
        super(OperateFlowerFight, self).__init__()

    def quit_flower_fight(self):
        """
        退出
        :return:
        """
        self.click_in_template("flower_fight_is_flower_fight_panel_quit_button")

    def get_flower_fight_all_prize(self):
        """
        全部领取
        :return:
        """
        self.click_in_template("flower_fight_is_flower_fight_panel_get_all_prize")

    def get_flower_fight_all_task(self):
        """
        全部领取
        :return:
        """
        self.click_in_template("flower_fight_is_flower_fight_panel_get_all_task")

    def click_flower_fight_prize_select_button(self):
        self.click_in_template("flower_fight_is_flower_fight_prize_select_button")

    def select_flower_fight_task_panel(self):
        self.click_in_template("flower_fight_select_flower_fight_task_panel")

    def select_flower_fight_prize_panel(self):
        self.click_in_template("flower_fight_select_flower_fight_prize_panel")
