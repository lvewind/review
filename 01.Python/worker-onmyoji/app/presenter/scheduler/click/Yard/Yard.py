from hiworker import *


class OperateYard(Win32Click):
    def __init__(self):
        super(OperateYard, self).__init__()

    def open_daily_panel(self):
        """
        打开日常面板
        :return:
        """
        self.click_in_template("open_daily_panel")

    def open_pets_house(self, coord):
        """
        打开宠物小屋
        :param coord:
        :return:
        """
        self.click_in_circle(coord)

    def open_explore(self):
        """
        打开探索地图
        :return:
        """
        self.click_in_template("yard_is_expolore_entrance")

    def confirm_disconnected(self):
        """
        确认掉线按钮
        :return:
        """
        self.click_in_template("yard_is_disconnected_button")

    def open_explore_left(self):
        self.click_in_template("yard_is_expolore_entrance_left")

    def open_summon_room(self):
        """
        打开召唤房间
        :return:
        """
        self.click_in_template("yard_is_summon_room_entrance")

    def open_bounty_seals(self, coord):
        """
        打开悬赏封印
        :param coord:
        :return:
        """
        self.click_in_circle(coord)

    def open_town(self, coord):
        """
        打开汀中
        :param coord:
        :return:
        """
        self.click_in_circle(coord)

    def open_illustrated(self):
        """
        打开绘卷
        :return:
        """
        self.click_in_template("yard_is_illustrated_entrance")

    def open_earthly(self):
        """
        打开现世逢魔
        :return:
        """
        self.click_in_template("yard_is_earthly_entrance")

    def open_teamup(self):
        """
        打开组队
        :return:
        """
        self.click_in_template("yard_is_teamup_entrance")

    def open_guild(self):
        """
        打开阴阳寮
        :return:
        """
        self.click_in_template("yard_is_guild_entrance")

    def open_mall_panel(self):
        """
        打开商店
        :return:
        """
        self.click_in_template("yard_is_mall_entrance")

    def open_flower_fight(self):
        """

        :return:
        """
        self.click_in_template("yard_is_flower_fight_entrance")

    def open_friend(self):
        """
        打开好友面板
        :return:
        """
        self.click_in_template("yard_is_friend_entrance")

    def open_onmyoji(self):
        """
        打开阴阳师面板
        :return:
        """
        self.click_in_template("yard_is_onmyoji_entrance")

    def open_shikigami(self):
        """
        打开式神面板
        :return:
        """
        self.click_in_template("yard_is_shikigami_entrance")

    def open_chat_channel(self):
        """
        打开聊天
        :return:
        """
        self.click_in_template("yard_is_chat_channel_entrance")

    def open_mail(self):
        """
        打开邮件
        :return:
        """
        self.click_in_template("yard_is_mail_entrance")

    def open_bonus_panel_yard(self):
        """
        打开庭院加成
        :return:
        """
        self.click_in_template("explore_open_bonus_panel_yard")

    def slide_yard_to_right(self):
        """
        庭院滑到右边
        :return:
        """
        self.slide_distance_with_template("yard_slide_yard_to_left", -300, 50)

    def slide_yard_to_left(self):
        """
        庭院滑到左边
        :return:
        """
        self.slide_distance_with_template("yard_slide_yard_to_left", 300, 50)

    def close_chat_panel(self):
        """
        关闭聊天界面
        :return:
        """
        self.click_in_template("yard_is_chat_panel")

    def close_bonus_stop_panel(self):
        """
        关闭体力耗尽提示
        :return:
        """
        self.click_in_template("yard_close_bonus_stop_panel")

    def close_ap_use_up_panel(self):
        """
        关闭体力耗尽提示
        :return:
        """
        self.click_in_template("yard_is_ap_use_up_panel_close_button")

    def click_ap_use_up_buy_button(self):
        """
        甘比体力耗尽购买提示
        :return:
        """
        self.click_in_template("yard_is_ap_use_up_buy_button_60")

    def open_bottom_menu_in_yard(self):
        """
        展开庭院菜单
        :return:
        """
        self.click_in_template("yard_is_bottom_menu_open")

    def open_bind_phone_input_panel(self):
        """
        打开手机绑定界面
        :return:
        """
        self.click_in_template("yard_is_bing_phone_panel")

    def cancel_bind_phone_input_panel(self):
        """
        取消手机绑定界面
        :return:
        """
        self.click_in_template("yard_cancel_bind_phone_input_panel")
