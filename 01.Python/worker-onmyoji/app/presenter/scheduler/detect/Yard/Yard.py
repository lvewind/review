from hiworker import *


class DetectYard(DetectImage):
    def __init__(self):
        super(DetectYard, self).__init__()

    def is_yard(self):
        """
        庭院
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_yard_common")
        return result

    def is_chat_panel(self):
        """
        聊天界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_chat_panel")
        return result

    def is_disconnected(self):
        """
        网络断开
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_is_disconnected")
        return result

    def is_daily_panel_entrance(self):
        """
        日常入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_find_daily_panel_entrance")
        return result, coord

    def find_lot_button(self):
        """
        查找签到按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("yard_find_lot_button", check_t=3)
        return result, coord

    def find_999_lot_button(self):
        result, coord, max_similarity = self.find_in_dynamic_scene("yard_find_999_lot_button", check_t=3)
        return result, coord

    def find_ap_button(self):
        """
        庭院查找体力
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("yard_find_ap_button", 0.9, check_t=3)
        return result, coord

    def find_jade_button(self):
        """
        庭院查找勾玉
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("yard_find_jade_button", 0.9, check_t=3)
        return result, coord

    def find_pet_house_entrance(self):
        """
        查找宠物小屋入口
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("yard_find_pet_house_entrance", check_t=3)
        return result, coord

    def is_explore_entrance(self):
        """
        查找探索入口
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("yard_is_expolore_entrance", similarity=0.7)
        if result:
            return result

        result, coord, max_similarity = self.find_in_dynamic_scene("yard_is_expolore_entrance_anniversary", 0.7)
        if result:
            return result

    def is_explore_entrance_left(self):
        result, coord, max_similarity = self.find_in_dynamic_scene("yard_is_expolore_entrance_left", similarity=0.7)
        if result:
            return result

    def is_explore_entrance_anniversary(self):
        result, coord, max_similarity = self.find_in_template_rect("yard_is_expolore_entrance_anniversary")
        return result

    def find_summon_room_entrance(self):
        """
        查找召唤房间入口
        :return:
        """
        return self.find_in_dynamic_scene("yard_is_summon_room_entrance", similarity=0.7, check_t=3)

    def is_bottom_menu_open(self):
        """
        庭院底部菜单已打开
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_bottom_menu_open")
        return result

    def find_bounty_seals_entrance(self):
        """
        查找悬赏封印入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_bounty_seals")
        return result, coord

    def find_town_entrance(self):
        """
        查找汀中入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_town_entrance")
        return result, coord

    def is_illustrated_entrance(self):
        """
        绘卷入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_illustrated_entrance")
        return result

    def is_earthly_entrance(self):
        """
        现世逢魔入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_earthly_entrance")
        return result

    def is_teamup_entrance(self):
        """
        组队入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_teamup_entrance")
        return result

    def is_guild_entrance(self):
        """
        阴阳寮入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_guild_entrance", 0.65)
        return result

    def is_mall_entrance(self):
        """
        商店入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_mall_entrance")
        return result

    def is_flower_fight_entrance(self):
        """
        花合战入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_flower_fight_entrance")
        return result

    def is_friend_entrance(self):
        """
        好友面板入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_friend_entrance")
        return result

    def is_onmyoji_entrance(self):
        """
        阴阳师入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_onmyoji_entrance")
        return result

    def is_shikigami_entrance(self):
        """
        式神录入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_shikigami_entrance")
        return result

    def is_chat_channel_entrance(self):
        """
        聊天频道入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_chat_channel_entrance")
        return result

    def is_mail_entrance(self):
        """
        邮件入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_mail_entrance")
        return result

    def find_bonus_button_in_yard(self):
        """
        庭院查找加成
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("yard_find_souls_bonus", check_t=5)
        return result, coord

    def is_in_team_queue(self):
        """
        正在组队排队提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_in_team_queue")
        return result

    def is_ap_use_up_panel(self):
        """
        体力耗尽提示界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_ap_use_up_panel")
        return result

    def is_ap_use_up_panel_close_button(self):
        """
        体力耗尽提示界面关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_ap_use_up_panel_close_button")
        return result

    def is_ap_use_up_buy_button_60(self):
        """
        购买体力60
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_ap_use_up_buy_button_60")
        return result

    def is_bonus_button_in_yard(self):
        """
        庭院查找加成领取图标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_bonus_button_in_yard")
        return result

    def is_bind_phone_panel(self):
        """
        手机绑定界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_bing_phone_panel")
        return result

    def is_bind_phone_input_panel(self):
        """
        手机绑定界面输入框
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("yard_is_bing_phone_input_panel")
        return result

    def is_bonus_stop_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("yard_is_bonus_stop_panel")
        return result
