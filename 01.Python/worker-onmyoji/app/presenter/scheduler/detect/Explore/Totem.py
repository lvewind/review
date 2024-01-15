from hiworker import *


class DetectTotem(DetectImage):
    def __init__(self):
        super(DetectTotem, self).__init__()

    def is_totem_zone_select_panel(self):
        """
        御灵选择界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_zone_select_panel")
        return result

    def is_totem_zone_select_panel_quit_button(self):
        """
        御灵选择界面退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_zone_select_panel_quit_button")
        return result

    def is_totem_stage_panel(self):
        """
        御灵层数选择界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_stage_panel")
        return result

    def is_totem_stage_panel_quit_button(self):
        """
        御灵层数选择界面退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_stage_panel_quit_button")
        return result

    ################### 未截图
    def is_totem_stage_panel_shenlong(self):
        """
        神龙层数选择界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_stage_panel_shenlong")
        return result

    def is_totem_stage_panel_baizhangzhu(self):
        """
        御灵白藏主层数选择界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_stage_panel_baizhangzhu")
        return result

    ###############

    def is_totem_stage_panel_heibao(self):
        """
        御灵黑豹层数选择界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_stage_panel_heibao")
        return result

    def is_totem_stage_panel_kongque(self):
        """
        御灵孔雀层数选择界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_stage_panel_kongque")
        return result

    def is_totem_stage_selected_1(self):
        """
        御灵层数选择
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_stage_selected_1", 0.98)
        return result

    def is_totem_stage_selected_2(self):
        """
        御灵层数选择
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_stage_selected_2", 0.98)
        return result

    def is_totem_stage_selected_3(self):
        """
        御灵层数选择
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_stage_selected_3", 0.98)
        return result

    def is_totem_challenge_button(self):
        """
        御灵挑战按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_challenge_button")
        return result

    def is_totem_cast_unlock(self):
        """
        御灵阵容未锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_cast_unlock")
        return result

    def is_totem_cast_lock(self):
        """
        御灵阵容已锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("totem_is_totem_cast_lock")
        return result

    def is_totem_auto_challenage(self):
        """
        御灵自动挑战按钮
        :return:
        """
        return self.find_color_with_template_area("totem_is_totem_auto_battle", [253, 253, 253])
