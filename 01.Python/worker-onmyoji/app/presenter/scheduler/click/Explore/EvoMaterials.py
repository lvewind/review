from hiworker import *


class OperateEvoMaterials(Win32Click):
    def __init__(self):
        super(OperateEvoMaterials, self).__init__()

    def quit_evo_tower_quit(self):
        """
        退出觉醒之塔
        :return:
        """
        self.click_in_template("evo_materials_is_evo_tower_button")

    def select_evo_tower_fire(self):
        """
        选择觉醒之塔火
        :return:
        """
        self.click_in_template("evo_materials_is_evo_tower_fire")

    def select_evo_tower_wind(self):
        """
        选择觉醒之塔风
        :return:
        """
        self.click_in_template("evo_materials_is_evo_tower_wind")

    def select_evo_tower_water(self):
        """
        选择觉醒之塔水
        :return:
        """
        self.click_in_template("evo_materials_is_evo_tower_water")

    def select_evo_tower_thunder(self):
        """
        选择觉醒之塔雷
        :return:
        """
        self.click_in_template("evo_materials_is_evo_tower_thunder")

    def quit_evo_stage_panel(self):
        """
        退出觉醒层数界面
        :return:
        """
        self.click_in_template("evo_materials_is_evo_stage_panel_button")

    def select_evo_stage_panel_fire(self):
        """
        选择层数界面火
        :return:
        """
        self.click_in_template("evo_materials_is_evo_stage_panel_fire_select_button")

    def select_evo_stage_panel_wind(self):
        """
        选择层数界面风
        :return:
        """
        self.click_in_template("evo_materials_is_evo_stage_panel_wind_select_button")

    def select_evo_stage_panel_water(self):
        """
        选择层数界面水
        :return:
        """
        self.click_in_template("evo_materials_is_evo_stage_panel_water_select_button")

    def select_evo_stage_panel_thunder(self):
        """
        选择层数界面雷
        :return:
        """
        self.click_in_template("evo_materials_is_evo_stage_panel_thunder_select_button")

    def select_evo_stage(self, coord):
        """
        选择觉醒层数
        :param coord:
        :return:
        """
        self.click_in_circle(coord)

    def unlock_evo_cast(self):
        """
        取消阵容锁定
        :return:
        """
        self.click_in_template("evo_materials_is_evo_cast_lock")

    def lock_evo_cast(self):
        """
        锁定阵容
        :return:
        """
        self.click_in_template("evo_materials_is_evo_cast_unlock")

    def change_evo_auto_challenge(self):
        """
        切换自动挑战
        :return:
        """
        self.click_in_template("evo_materials_is_evo_auto_battle")

    def teamup_evo(self):
        """
        点击组队按钮
        :return:
        """
        self.click_in_template("evo_materials_is_evo_teamup_button")

    def challenge_evo(self):
        """
        挑战觉醒
        :return:
        """
        self.click_in_template("evo_materials_is_evo_challenge_button")

    def slide_up_evo_stage_list(self):
        """
        向上滑动觉醒层数列表
        :return:
        """
        self.slide_distance_with_template("evo_materials_slide_up_evo_stage_list", 30, -200)

    def slide_down_evo_stage_list(self):
        """
        向下滑动觉醒层数列表
        :return:
        """
        self.slide_distance_with_template("evo_materials_slide_down_evo_stage_list", 30, 200)

    def open_evo_feed_doll_panel(self):
        """
        打开小纸人喂食面板
        :return:
        """
        self.click_in_template("evo_materials_open_evo_feed_doll_panel")
