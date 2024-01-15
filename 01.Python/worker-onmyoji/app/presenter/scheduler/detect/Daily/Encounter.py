from hiworker import *


class DetectEncounter(DetectImage):
    def __init__(self):
        super(DetectEncounter, self).__init__()

    def is_encounter_map(self):
        """
        是否在逢魔地图
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_map")
        return result

    def is_encounter_find_boss(self):
        """
        是否存在查找逢魔BOSS按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_find_boss")
        return result

    def is_encounter_use_1(self):
        """
        是否生育逢魔次数1
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_use_1")
        return result

    def is_encounter_use_2(self):
        """
        是否生育逢魔次数2
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_use_2")
        return result

    def is_encounter_use_3(self):
        """
        是否生育逢魔次数3
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_use_3")
        return result

    def is_encounter_use_4(self):
        """
        是否生育逢魔次数4
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_use_4")
        return result

    def is_encounter_use_up(self):
        """
        是否逢魔次数用尽
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_use_up")
        return result

    def is_encounter_prize_got(self):
        """
        是否出现逢魔奖励界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_prize_got")
        return result

    def is_encounter_boss_panel(self):
        """
        是否逢魔BOSS界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_panel")
        return result

    def is_encounter_boss_confirm_panel(self):
        """
        是否逢魔BOSS确认界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_confirm_panel")
        return result

    def is_encounter_boss_confirm_button(self):
        """
        是否逢魔BOSS确认按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_confirm_button")
        return result

    def is_encounter_boss_confirm_not_check(self):
        """
        是否逢魔BOSS确认未勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_confirm_not_check")
        return result

    def is_encounter_boss_confirm_checked(self):
        """
        是否逢魔BOSS确认已勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_confirm_checked")
        return result

    def is_encounter_boss_panel_time_up(self):
        """
        是否逢魔BOSS时间过期
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_panel_time_up")
        return result

    def is_encounter_boss_panel_full(self):
        """
        是否逢魔BOSS满人
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_panel_full")
        return result

    def find_encounter_boss_guilingvgeji(self):
        """
        查找鬼灵歌伎
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_guilinggeji")
        return result, coord

    def find_encounter_boss_shenqilou(self):
        """
        查找蜃气楼
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_shenqilou")
        return result, coord

    def find_encounter_boss_tuzhizhu(self):
        """
        查找土蜘蛛
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_tuzhizhu")
        return result, coord

    def find_encounter_boss_huangkulou(self):
        """
        查找荒骷髅
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_huangkulou")
        return result, coord

    def find_encounter_boss_dizhennian(self):
        """
        查找地震鲶
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_dizhennian")
        return result, coord

    def find_encounter_boss_longche(self):
        """
        查找胧车
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_longche")
        return result, coord

    def is_encounter_boss_mass_room(self):
        """
        是否逢魔BOSS集结房间
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_mass_room")
        return result

    def is_encounter_confirm_panel_checked(self):
        """
        是否确认勾选按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_confirm_panel_checked")
        return result

    def is_encounter_boss_mark_got_panel(self):
        """
        是否印记获得界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_boss_mark_got_panel")
        return result

    def is_encounter_finish_1(self):
        """
        逢魔任务完成1
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_spirit_finish_1")
        return result

    def is_encounter_finish_2(self):
        """
        逢魔任务完2
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_spirit_finish_2")
        return result

    def is_encounter_finish_3(self):
        """
        逢魔任务完3
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_spirit_finish_3")
        return result

    def is_encounter_finish_4(self):
        """
        逢魔任务完4
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_spirit_finish_4")
        return result

    def is_encounter_mail_panel(self):
        """
        是否是逢魔密信界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_mail_panel")
        return result

    def is_encounter_mail_panel_answer_1(self):
        """
        逢魔密信答案1
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_mail_panel_answer_1")
        return result

    def is_encounter_mail_panel_answer_2(self):
        """
        逢魔密信答2
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_mail_panel_answer_2")
        return result

    def is_encounter_mail_panel_answer_3(self):
        """
        逢魔密信答案3
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_mail_panel_answer_3")
        return result

    def is_encounter_mail_1(self):
        """
        是否逢魔任务1是密信
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_mail_1")
        return result

    def is_encounter_mail_2(self):
        """
        是否逢魔任务2是密信
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_mail_2")
        return result

    def is_encounter_mail_3(self):
        """
        是否逢魔任务3是密信
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_mail_3")
        return result

    def is_encounter_mail_4(self):
        """
        是否逢魔任务4是密信
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_mail_4")
        return result

    def is_encounter_box_panel(self):
        """
        是否逢魔宝箱界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_box_panel")
        return result

    def is_encounter_box_panel_button(self):
        """
        是否逢魔宝箱界面按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_box_panel_button")
        return result

    def is_encounter_box_panel_amulet(self):
        """
        是否逢魔宝箱是蓝票
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_box_panel_amulet")
        return result

    def is_encounter_box_1(self):
        """
        是否逢魔任务1是宝箱
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_box_1")
        return result

    def is_encounter_box_2(self):
        """
        是否逢魔任务2是宝箱
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_box_2")
        return result

    def is_encounter_box_3(self):
        """
        是否逢魔任务3是宝箱
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_box_3")
        return result

    def is_encounter_box_4(self):
        """
        是否逢魔任务4是宝箱
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_box_4")
        return result

    def is_encounter_task_1(self):
        """
        是否逢魔任务1是日常
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_1")
        return result

    def is_encounter_task_2(self):
        """
        是否逢魔任务2是日常
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_2")
        return result

    def is_encounter_task_3(self):
        """
        是否逢魔任务3是日常
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task_3")
        return result

    def is_encounter_task_4(self):
        """
        是否逢魔任务4是日常
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("encounter_is_encounter_task__4")
        return result
