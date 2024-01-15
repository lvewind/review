from hiworker import *


class DetectFriend(DetectImage):
    def __init__(self):
        super(DetectFriend, self).__init__()

    def is_friend_panel(self):
        """
        好友面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel")
        return result

    def is_friend_panel_quit_button(self):
        """
        好友面板退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel_quit_button")
        return result

    def is_friend_panel_friend(self):
        """
        好友面板好友列表按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel_friend")
        return result

    def is_friend_panel_friend_list(self):
        """
        好友面板好友列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel_friend_list", 0.985)
        return result

    def is_friend_panel_friend_list_opened(self):
        """
        好友面板好友列表为展开状态
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel_friend_list_opened", 0.9)
        return result

    def is_friend_panel_friend_list_flower(self):
        """
        好友送花列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel_friend_list_flower")
        return result

    def find_friend_panel_friend_list_flower_send_1(self):
        """
        送花
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel_friend_list_flower_send_1")
        return result

    def find_friend_panel_friend_list_flower_send_2(self):
        """
        送花
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel_friend_list_flower_send_2")
        return result

    def find_friend_panel_friend_list_flower_receive_1(self):
        """
        收花
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel_friend_list_flower_receive_1")
        return result

    def find_friend_panel_friend_list_flower_receive_2(self):
        """
        收花
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_panel_friend_list_flower_receive_2")
        return result

    def is_friend_get_one_key_flower(self):
        result, coord, max_similarity = self.find_in_template_rect("friend_is_friend_get_one_key_flower")
