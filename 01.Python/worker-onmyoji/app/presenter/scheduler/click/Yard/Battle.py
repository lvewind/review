from hiworker import *


class OperateBattle(Win32Click):
    def __init__(self):
        super(OperateBattle, self).__init__()

    def change_auto_battle(self):
        """
        切换自动战斗
        :return:
        """
        self.click_in_template("battle_is_battle_manual")

    def set_battle_ready(self):
        """
        战斗准备
        :return:
        """
        self.click_in_template("battle_is_battle_ready")

    def skip_battle_failed(self, click_position):
        """
        跳过战斗失败
        :param click_position:
        :return:
        """
        if click_position == 1:
            self.skip_battle_failed_1()
        elif click_position == 2:
            self.skip_battle_failed_2()
        elif click_position == 3:
            self.skip_battle_failed_3()
        else:
            self.skip_battle_failed_1()

    def skip_battle_failed_1(self):
        """
        跳过战斗失败1
        :return:
        """
        self.click_in_template("battle_skip_battle_failed_1")

    def skip_battle_failed_2(self):
        """
        跳过战斗失败2
        :return:
        """
        self.click_in_template("battle_skip_battle_failed_2")

    def skip_battle_failed_3(self):
        """
        跳过战斗失败3
        :return:
        """
        self.click_in_template("battle_skip_battle_failed_3")

    def skip_battle_win(self, click_position):
        """
        跳过战斗胜利
        :param click_position:
        :return:
        """
        if click_position == 1:
            self.skip_battle_win_1()
        elif click_position == 2:
            self.skip_battle_win_2()
        elif click_position == 3:
            self.skip_battle_win_3()
        else:
            self.skip_battle_win_1()

    def skip_battle_win_1(self):
        """
        跳过战斗胜利1
        :return:
        """
        self.click_in_template("battle_skip_battle_win_1")

    def skip_battle_win_2(self):
        """
        跳过战斗胜利2
        :return:
        """
        self.click_in_template("battle_skip_battle_win_2")

    def skip_battle_win_3(self):
        """
        跳过战斗胜利3
        :return:
        """
        self.click_in_template("battle_skip_battle_win_3")

    def skip_battle_win_prize(self, click_position):
        """
        领取战斗奖励
        :param click_position:
        :return:
        """
        if click_position == 1:
            self.skip_battle_win_prize_1()
        elif click_position == 2:
            self.skip_battle_win_prize_2()
        elif click_position == 3:
            self.skip_battle_win_prize_3()
        else:
            self.skip_battle_win_prize_1()

    def skip_battle_win_prize_1(self):
        """
        领取战斗奖励1
        :return:
        """
        self.click_in_template("battle_skip_battle_win_prize_1")

    def skip_battle_win_prize_2(self):
        """
        领取战斗奖励2
        :return:
        """
        self.click_in_template("battle_skip_battle_win_prize_2")

    def skip_battle_win_prize_3(self):
        """
        领取战斗奖励3
        :return:
        """
        self.click_in_template("battle_skip_battle_win_prize_3")

    def check_battle_auto_invite(self):
        """
        勾选自动邀请
        :return:
        """
        self.click_in_template("battle_is_battle_auto_invite_checked")

    def confirm_auto_invite(self):
        """
        确认自动邀请
        :return:
        """
        self.click_in_template("battle_confirm_auto_invite_button")

    def cancel_auto_invite(self):
        """
        取消自动邀请
        :return:
        """
        self.click_in_template("battle_cancel_auto_invite_button")

    def skip_battle_win_duel_1(self):
        """
        跳过斗技胜利1
        :return:
        """
        self.click_in_template("battle_is_battle_win_duel_1")

    def skip_battle_win_duel_2(self):
        """
        跳过斗技胜利2
        :return:
        """
        self.click_in_template("battle_is_battle_win_duel_2")

    def skip_battle_win_duel_3(self):
        """
        跳过斗技胜利3
        :return:
        """
        self.click_in_template("battle_is_battle_win_duel_3")

    def skip_battle_failed_duel_1(self):
        """
        跳过斗技失败1
        :return:
        """
        self.click_in_template("battle_is_battle_failed_duel_1")

    def skip_battle_failed_duel_2(self):
        """
        跳过斗技失败2
        :return:
        """
        self.click_in_template("battle_is_battle_failed_duel_2")

    def skip_battle_failed_duel_3(self):
        """
        跳过斗技失败3
        :return:
        """
        self.click_in_template("battle_is_battle_failed_duel_3")

    def set_battle_speed(self):
        """
        切换战斗动画速度
        :return:
        """
        self.click_in_template("battle_is_battle_auto_speed_1x")

    def set_battle_auto(self):
        """
        设置自动战斗
        :return:
        """
        self.click_in_template("battle_is_battle_manual")

    def confirm_continue_to_invite(self):
        """
        确认自动邀请
        :return:
        """
        self.click_in_template("battle_confirm_continue_to_invite")
