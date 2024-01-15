from hiworker import *


class DetectEvoMaterials(DetectImage):
    def __init__(self):
        super(DetectEvoMaterials, self).__init__()

    def is_evo_tower(self):
        """
        觉醒之塔
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_tower")
        return result

    def is_evo_tower_quit_button(self):
        """
        退出觉醒之塔按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_tower_button")
        return result

    def is_evo_tower_fire(self):
        """
        觉醒之塔火
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_tower_fire")
        return result

    def is_evo_tower_wind(self):
        """
        觉醒之塔风
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_tower_wind")
        return result

    def is_evo_tower_water(self):
        """
        觉醒之塔水
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_tower_water")
        return result

    def is_evo_tower_thunder(self):
        """
        觉醒之塔雷
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_tower_thunder")
        return result

    def is_evo_stage_panel(self):
        """
        觉醒层数选择面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_panel")
        return result

    def is_evo_stage_panel_quit_button(self):
        """
        觉醒层数选择面板退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_panel_button")
        return result

    def is_evo_stage_panel_fire(self):
        """
        觉醒层数选择面板火
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_panel_fire")
        return result

    def is_evo_stage_panel_wind(self):
        """
        觉醒层数选择面板风
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_panel_wind")
        return result

    def is_evo_stage_panel_water(self):
        """
        觉醒层数选择面板水
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_panel_water")
        return result

    def is_evo_stage_panel_thunder(self):
        """
        觉醒层数选择面板雷
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_panel_thunder")
        return result

    def find_evo_stage_1(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_1", 0.9)
        return result, coord

    def find_evo_stage_2(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_2", 0.9)
        return result, coord

    def find_evo_stage_3(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_3", 0.9)
        return result, coord

    def find_evo_stage_4(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_4", 0.9)
        return result, coord

    def find_evo_stage_5(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_5", 0.9)
        return result, coord

    def find_evo_stage_6(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_6", 0.9)
        return result, coord

    def find_evo_stage_7(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_7", 0.9)
        return result, coord

    def find_evo_stage_8(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_8", 0.9)
        return result, coord

    def find_evo_stage_9(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_9", 0.9)
        return result, coord

    def find_evo_stage_10(self):
        """
        查找觉醒层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_find_evo_stage_10", 0.9)
        return result, coord

    def is_evo_stage_selected_1(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_1", 0.98)
        return result

    def is_evo_stage_selected_2(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_2", 0.98)
        return result

    def is_evo_stage_selected_3(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_3", 0.98)
        return result

    def is_evo_stage_selected_4(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_4", 0.98)
        return result

    def is_evo_stage_selected_5(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_5", 0.98)
        return result

    def is_evo_stage_selected_6(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_6", 0.98)
        return result

    def is_evo_stage_selected_7(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_7", 0.98)
        return result

    def is_evo_stage_selected_8(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_8", 0.98)
        return result

    def is_evo_stage_selected_9(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_9", 0.98)
        return result

    def is_evo_stage_selected_10(self):
        """
        觉醒层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_stage_selected_10", 0.98)
        return result

    def is_evo_teamup_button(self):
        """
        觉醒组队按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_teamup_button")
        return result

    def is_evo_challenge_button(self):
        """
        觉醒挑战按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_challenge_button")
        return result

    def is_evo_cast_unlock(self):
        """
        觉醒阵容未锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_cast_unlock")
        return result

    def is_evo_cast_lock(self):
        """
        觉醒阵容已锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_materials_is_evo_cast_lock")
        return result

    def is_evo_auto_challenge_active(self):
        """
        觉醒自动挑战已激活
        :return:
        """
        return self.find_color_with_template_area("evo_materials_is_evo_auto_battle", [253, 253, 253])

    def is_evo_doll_fire_hunger(self):
        """
        小纸人饿了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_is_evo_doll_fire_hunger")
        return result

    def is_evo_doll_wind_hunger(self):
        """
        小纸人饿了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_is_evo_doll_wind_hunger")
        return result

    def is_evo_doll_water_hunger(self):
        """
        小纸人饿了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_is_evo_doll_water_hunger")
        return result

    def is_evo_doll_thunder_hunger(self):
        """
        小纸人饿了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_is_evo_doll_thunder_hunger")
        return result

    def is_evo_doll_hunger_common(self):
        """
        小纸人饿了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("evo_is_evo_doll_hunger_common")
        return result
