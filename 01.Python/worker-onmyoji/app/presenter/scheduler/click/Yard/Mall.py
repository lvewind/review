from hiworker import *


class OperateMall(Win32Click):
    def __init__(self):
        super(OperateMall, self).__init__()

    def open_mystery_room(self):
        """
        打开秘卷屋
        :return:
        """
        self.click_in_template("mall_is_mystery_room")

    def exchange_plain_souls_box(self):
        """
        打开朴素礼盒
        :return:
        """
        self.click_in_template("mall_is_plain_souls_box_exchange_button")

    def set_top_exchange_plain_souls_box(self):
        """
        拉满朴素礼盒
        :return:
        """
        self.click_in_template("mall_is_plain_souls_box_exchange_set_top_button")

    def confirm_exchange_plain_souls_box(self):
        """
        确认兑换朴素礼盒
        :return:
        """
        self.click_in_template("mall_confirm_exchange_plain_souls_box")

    def open_mall_general(self):
        """
        打开杂货铺
        :return:
        """
        self.click_in_template("mall_is_mall_general")

    def open_mall_general_honor(self):
        """
        打开荣誉商店
        :return:
        """
        self.click_in_template("mall_is_mall_general_honor")

    def open_mall_general_friend(self):
        """
        打开友情点商店
        :return:
        """
        self.click_in_template("mall_is_mall_general_friend")

    def open_mall_general_medal(self):
        """
        打开勋章商店
        :return:
        """
        self.click_in_template("mall_is_mall_general_medal")

    def open_mall_gift(self):
        """
        打开礼包屋
        :return:
        """
        self.click_in_template("mall_is_mall_gift_room")

    def click_mall_gift_daruma(self):
        """
        点击礼包屋达摩
        :return:
        """
        self.click_in_template("mall_is_mall_gift_room_skill_daruma")

    def close_mall_recommend(self):
        """
        关闭商店推荐
        :return:
        """
        self.click_in_template("mall_is_mall_recommend_close_button")

    def buy_general_medal_mystery(self):
        """
        勋章购买蓝票
        :return:
        """
        self.click_in_template("mall_is_mall_general_medal_mystery")

    def confirm_mall_general_medal_confirm_1(self):
        """
        确认勋章购买蓝票
        :return:
        """
        self.click_in_template("mall_confirm_mall_general_medal_confirm_1")
