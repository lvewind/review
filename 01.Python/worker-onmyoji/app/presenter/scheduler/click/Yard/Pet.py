from hiworker import *


class OperatePet(Win32Click):
    def __init__(self):
        super(OperatePet, self).__init__()

    def quit_pets_house(self):
        """
        退出宠物小屋
        :return:
        """
        self.click_in_template("pet_is_pets_house_quit_button")

    def open_pets_house_operation_menu(self):
        """
        打开宠物小屋操作菜单
        :return:
        """
        self.click_in_template("pet_is_pets_house_operation_open")

    def click_pets_house_dinner_button(self):
        """
        喂大餐
        :return:
        """
        self.click_in_template("pet_is_pets_house_dinner_button")

    def click_pets_house_dinner_panel_feed_button(self):
        """
        确认喂宠物
        :return:
        """
        self.click_in_template("pet_is_pets_house_dinner_panel_feed_button")

    def click_pets_house_play_panel_play_button(self):
        """
        玩耍
        :return:
        """
        self.click_in_template("pet_is_pets_house_dinner_panel_play_button")

    def close_pets_house_single_panel(self):
        """
        关闭宠物详情面板
        :return:
        """
        self.click_in_template("pet_close_pets_house_single_panel")

    def click_pets_house_play_button(self):
        self.click_in_template("pet_is_pets_house_play_button")
