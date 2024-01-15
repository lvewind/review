from hiworker import *


class DetectBattle(DetectImage):
    def __init__(self):
        super(DetectBattle, self).__init__()

    def is_battle_battling(self):
        """
        正在战斗中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battling", 0.85)
        return result

    def is_battle_ready(self):
        """
        战斗准备
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_ready", 0.9)
        return result

    def is_battle_ready_panel(self):
        """
        战斗准备
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_ready_panel")
        return result

    def is_battle_manual(self):
        """
        手动战斗
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_manual", 0.9)
        return result

    def is_battle_auto_speed_1x(self):
        """
        战斗一倍速
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_auto_speed_1x", 0.8)
        return result

    def is_battle_auto(self):
        """
        自动战斗
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_auto", 0.8)
        return result

    def is_battle_win_prize(self):
        """
        战斗胜利奖励
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_prize")
        return result

    def is_battle_win_prize_captain(self):
        """
        队长战斗胜利奖励
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_prize_captain")
        return result

    def is_battle_win_prize_daruma(self):
        """
        战斗胜利达摩奖励
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_prize_drum")
        return result

    def is_battle_win_drum(self):
        """
        战斗胜利鼓
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_drum")
        return result

    def is_battle_win_chapter(self):
        """
        狗粮副本战斗胜利
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_chapter")
        return result

    def is_battle_win_chapter_teamup(self):
        """
        狗粮副本战斗胜利
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_chapter_teamup")
        return result

    def is_battle_win_chapter_solo(self):
        """
        单刷狗粮战斗胜利
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_chapter_solo")
        return result

    def is_battle_win_drum_souls(self):
        """
        御魂战斗胜利
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_drum")
        return result

    def is_battle_win_drum_evo(self):
        """
        觉醒战斗胜利
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_drum_evo")
        return result

    def is_battle_failed_drum(self):
        """
        战斗失败
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_failed_drum")
        return result

    def is_battle_failed_continue_to_invite(self):
        """
        战斗失败继续邀请
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_failed_continue_to_invite")
        return result

    def is_battle_auto_invite_panel(self):
        """
        自动邀请提示
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_auto_invite_panel")
        return result

    def is_battle_auto_invite_checked(self):
        """
        确认自动邀请复选框
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_auto_invite_checked")
        return result

    def is_battle_win_duel(self):
        """
        斗技战斗胜利
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_win_duel")
        return result

    def is_battle_failed_duel(self):
        """
        斗技战斗失败
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_failed_duel")
        return result

    def is_battle_goods_info_panel(self):
        """
        战利品信息提示界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("battle_is_battle_goods_info_panel", 0.95)
        return result
