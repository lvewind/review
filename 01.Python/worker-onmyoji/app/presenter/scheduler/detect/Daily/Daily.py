from hiworker import *


class DetectDaily(DetectImage):
    def __init__(self):
        super(DetectDaily, self).__init__()

    def is_daily_panel(self):
        """
        是否是日常界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_panel")
        return result

    def is_daily_panel_close_button(self):
        """
        是否有日常界面关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_panel_close_button")
        return result

    def is_activity_panel_daily(self):
        """
        是否是活动中日常界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_panel_daily")
        return result

    def is_daily_panel_daily(self):
        return self.is_activity_panel_daily()

    def is_activity_panel_activity(self):
        """
        是否是活动中的活动界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_panel_activity")
        return result

    def is_activity_panel(self):
        """
        是否是活动界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_activity_panel")
        return result

    def is_daily_goto_button(self):
        """
        是否存在日常"前往"按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_goto_button", 0.985)
        return result

    def is_daily_encounter_entrance(self):
        """
        是否存在逢魔入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_encounter_entrance")
        return result

    def is_daily_encounter_entrance_panel(self):
        """
        是否存在逢魔入口界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_encounter_entrance_panel")
        return result

    def find_daily_boss_attack_entrance(self):
        """
        查找麒麟入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_find_daily_boss_attack_entrance")
        return result, coord

    def is_daily_boss_attack_entrance_panel(self):
        """
        是否存在麒麟入口面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_boss_attack_entrance_panel")
        return result

    def find_daily_boss_defense_entrance(self):
        """
        查找退治入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_find_daily_boss_defense_entrance")
        return result, coord

    def is_daily_boss_defense_entrance_panel(self):
        """
        是否存在退治入口界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_boss_defense_entrance_panel")
        return result

    def find_daily_netherworld_gate_entrance(self):
        """
        查找阴界之门入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_find_daily_netherworld_gate_entrance")
        return result, coord

    def is_daily_netherworld_gate_entrance_panel(self):
        """
        是否存在阴界之门入口界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_netherworld_gate_entrance_panel")
        return result, coord

    def find_daily_draft_duel_entrance(self):
        """
        查找协斗入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_find_daily_draft_duel_entrance")
        return result, coord

    def is_daily_draft_duel_entrance_panel(self):
        """
        是否存在协斗入口界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_draft_duel_entrance_panel")
        return result, coord

    # 百鬼奕
    def find_daily_royal_battle_entrance(self):
        """
        查找百鬼弈入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_find_daily_royal_battle_entrance")
        return result, coord

    def is_daily_royal_battle_entrance_panel(self):
        """
        是否存在百鬼弈入口界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_royal_battle_entrance_panel")
        return result

    def find_daily_guild_feast_entrance(self):
        """
        查找宴会入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_find_daily_guild_feast_entrance")
        return result, coord

    def is_daily_guild_feast_entrance_panel(self):
        """
        是否存在宴会入口界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_guild_feast_entrance_panel")
        return result

    def find_daily_gymnasium_entrance(self):
        """
        查找道馆入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_find_daily_gymnasium_entrance")
        return result, coord

    def is_daily_gymnasium_entrance_panel(self):
        """
        是否存在道馆入口界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_gymnasium_entrance_panel")
        return result

    def find_daily_duel_entrance(self):
        """
        查找斗技入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_find_daily_duel_entrance")
        return result, coord

    def is_daily_duel_entrance_panel(self):
        """
        是否存在斗技入口界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_daily_duel_entrance_panel")
        return result, coord
