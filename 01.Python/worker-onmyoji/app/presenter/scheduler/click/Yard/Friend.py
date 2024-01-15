from hiworker import *


class OperateFriend(Win32Click):
    def __init__(self):
        super(OperateFriend, self).__init__()

    def quit_friend_panel(self):
        """
        退出好友界面
        :return:
        """
        self.click_in_template("friend_is_friend_panel_quit_button")

    def open_friend_panel_friend(self):
        """
        打开好友界面
        :return:
        """
        self.click_in_template("friend_is_friend_panel_friend")

    def open_friend_panel_friend_list(self):
        """
        打开好友列表
        :return:
        """
        self.click_in_template("friend_is_friend_panel_friend_list_opened")

    def open_friend_panel_friend_list_flower(self):
        """
        打开好友送花列表
        :return:
        """
        self.click_in_template("friend_is_friend_panel_friend_list_flower")

    def slide_friend_list_to_bottom(self):
        """
        滑动好友列表到底部
        :return:
        """
        self.slide_distance_with_template("friend_slide_up_friend_list", 30, -200)

    def receive_or_send_flower(self, coord: list):
        """
        收送花
        :param coord:
        :return:
        """
        self.click_in_circle(coord)

    def select_friend_list_in_friend_panel(self):
        """
        选择好友列表
        :return:
        """
        self.click_in_template("friend_is_friend_panel_friend_list")

    def click_one_key_flower(self):
        self.click_in_template("friend_is_friend_get_one_key_flower")
