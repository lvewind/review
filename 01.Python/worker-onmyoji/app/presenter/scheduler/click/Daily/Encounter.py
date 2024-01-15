from hiworker import *


class OperateEncounter(Win32Click):
    def __init__(self):
        super(OperateEncounter, self).__init__()

    def click_encounter_button_4(self):
        """
        点击逢魔4
        :return:
        """
        self.click_in_template("daily_click_encounter_button_4")

    def click_encounter_prize_got(self):
        """
        领取获得奖励
        :return:
        """
        self.click_in_template("encounter_is_encounter_prize_got")

    def click_find_encounter_boss_button(self):
        """
        点击查找逢魔Boss按钮
        :return:
        """
        self.click_in_template("encounter_click_find_encounter_boss_button")

    def click_encounter_panel_challenge_button(self):
        """
        点击集结挑战
        :return:
        """
        self.click_in_template("encounter_click_encounter_panel_challenge_button")

    def close_encounter_boss_panel(self):
        """
        关闭逢魔Boss界面
        :return:
        """
        self.click_in_template("encounter_close_encounter_boss_panel")

    def confirm_encounter_boss_mass(self):
        """
        确定集结
        :return:
        """
        self.click_in_template("encounter_confirm_encounter_boss_mass")

    def check_encounter_confirm_panel(self):
        """
        勾选勾选逢魔确认界面
        :return:
        """
        self.click_in_template("encounter_check_encounter_confirm_panel")

    def skip_encounter_boss_mark_got_panel(self):
        """
        跳过任务购买界面
        :return:
        """
        self.click_in_template("encounter_skip_encounter_boss_mark_got_panel")

    def quit_encounter_map(self):
        """
        退出逢魔地图
        :return:
        """
        self.click_in_template("encounter_quit_encounter_map")

    def check_encounter_mail_panel_answer_1(self):
        """
        选择答题问题一
        :return:
        """
        self.click_in_template("encounter_is_encounter_mail_panel_answer_1")

    def check_encounter_mail_panel_answer_2(self):
        """
        选择答题问题二
        :return:
        """
        self.click_in_template("encounter_is_encounter_mail_panel_answer_2")

    def check_encounter_mail_panel_answer_3(self):
        """
        选择答题问题三
        :return:
        """
        self.click_in_template("encounter_is_encounter_mail_panel_answer_3")

    def click_encounter_box_panel_button(self):
        """
        购买逢魔宝箱
        :return:
        """
        self.click_in_template("encounter_is_encounter_task_box_panel_button")

    def click_encounter_1(self):
        """
        点击逢魔任务一
        :return:
        """
        self.click_in_template("encounter_is_encounter_task_spirit_finish_1")

    def click_encounter_2(self):
        """
        点击逢魔任务二
        :return:
        """
        self.click_in_template("encounter_is_encounter_task_spirit_finish_2")

    def click_encounter_3(self):
        """
        点击逢魔任务三
        :return:
        """
        self.click_in_template("encounter_is_encounter_task_spirit_finish_3")

    def click_encounter_4(self):
        """
        点击逢魔任务四
        :return:
        """
        self.click_in_template("encounter_is_encounter_task_spirit_finish_4")

    def close_encounter_box_panel_1(self):
        """
        关闭逢魔任务提示框1
        :return:
        """
        self.click_in_template("encounter_close_encounter_box_panel")

    def close_encounter_box_panel_2(self):
        """
        关闭逢魔任务提示框2
        :return:
        """
        self.click_in_template("encounter_close_encounter_box_panel_2")

    def close_encounter_box_panel_3(self):
        """
        关闭逢魔任务提示框3
        :return:
        """
        self.click_in_template("encounter_close_encounter_box_panel_3")
