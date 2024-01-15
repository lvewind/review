from hiworker import *


class DetectFlowerFight(DetectImage):
    def __init__(self):
        super(DetectFlowerFight, self).__init__()

    def is_flower_fight_panel(self):
        """
        花合战界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("flower_fight_is_flower_fight_panel")
        return result

    def is_flower_fight_panel_quit_button(self):
        """
        花合战界面退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("flower_fight_is_flower_fight_panel_quit_button")
        return result

    def is_flower_fight_panel_prize_get_all_button(self):
        """
        花合战界面一键领取按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("flower_fight_is_flower_fight_panel_prize_get_all_button")
        return result

    def is_flower_fight_panel_task_get_all_button(self):
        """
        花合战界面一键领取按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("flower_fight_is_flower_fight_panel_task_get_all_button")
        return result

    def is_flower_fight_panel_prize_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("flower_fight_is_flower_fight_panel_prize_panel")
        return result

    def is_flower_fight_panel_task_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("flower_fight_is_flower_fight_panel_task_panel")
        return result

    def is_flower_fight_panel_has_prize(self):
        result, coord, max_similarity = self.find_in_template_rect("flower_fight_is_flower_fight_panel_has_prize")
        return result

    def is_flower_fight_panel_has_task(self):
        result, coord, max_similarity = self.find_in_template_rect("flower_fight_is_flower_fight_panel_has_task")
        return result

    def is_flower_fight_prize_select_button(self):
        result, coord, max_similarity = self.find_in_template_rect("flower_fight_is_flower_fight_prize_select_button")
        return result
