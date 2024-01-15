from hiworker import *


class DetectSouls(DetectImage):
    def __init__(self):
        super(DetectSouls, self).__init__()

    def is_souls_zone_panel(self):
        """
        御魂面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_zone_select_panel")
        return result

    def is_souls_zone_panel_quit_button(self):
        """
        御魂面板关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_zone_select_panel_quit_button")
        return result

    def is_souls_zone_orochi(self):
        """
        御魂八岐大蛇面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_zone_orochi")
        return result

    def is_souls_zone_sougenbi(self):
        """
        御魂业原火面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_zone_sougenbi")
        return result

    def is_souls_zone_himiko(self):
        """
        御魂卑弥呼面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_zone_sun_fall")
        return result

    def is_souls_stage_panel(self):
        """
        御魂层数选择面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_stage_panel")
        return result

    def is_souls_stage_panel_quit_button(self):
        """
        御魂层数选择面板退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_stage_panel_button")
        return result

    def is_souls_stage_panel_orochi(self):
        """
        八岐大蛇层数选择面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_stage_panel_orochi")
        return result

    def is_souls_stage_panel_sougenbi(self):
        """
        业原火层数选择面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_stage_panel_sougenbi")
        return result

    def is_souls_stage_panel_himiko(self):
        """
        卑弥呼层数选择面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_stage_panel_himiko")
        return result

    def find_souls_orochi_stage_1(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_1", 0.9)
        return result, coord

    def find_souls_orochi_stage_2(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_2", 0.9)
        return result, coord

    def find_souls_orochi_stage_3(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_3", 0.9)
        return result, coord

    def find_souls_orochi_stage_4(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_4", 0.9)
        return result, coord

    def find_souls_orochi_stage_5(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_5", 0.9)
        return result, coord

    def find_souls_orochi_stage_6(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_6", 0.9)
        return result, coord

    def find_souls_orochi_stage_7(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_7", 0.9)
        return result, coord

    def find_souls_orochi_stage_8(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_8", 0.9)
        return result, coord

    def find_souls_orochi_stage_9(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_9", 0.9)
        return result, coord

    def find_souls_orochi_stage_10(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_10", 0.9)
        return result, coord

    def find_souls_orochi_stage_11(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_11", 0.9)
        return result, coord

    def find_souls_orochi_stage_12(self):
        """
        查找八岐大蛇层数
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_find_orochi_stage_12", 0.9)
        return result, coord

    def is_souls_orochi_stage_selected_1(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_1", 0.94)
        return result

    def is_souls_orochi_stage_selected_2(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_2", 0.94)
        return result

    def is_souls_orochi_stage_selected_3(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_3", 0.94)
        return result

    def is_souls_orochi_stage_selected_4(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_4", 0.94)
        return result

    def is_souls_orochi_stage_selected_5(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_5", 0.94)
        return result

    def is_souls_orochi_stage_selected_6(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_6", 0.94)
        return result

    def is_souls_orochi_stage_selected_7(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_7", 0.94)
        return result

    def is_souls_orochi_stage_selected_8(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_8", 0.94)
        return result

    def is_souls_orochi_stage_selected_9(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_9", 0.94)
        return result

    def is_souls_orochi_stage_selected_10(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_10", 0.94)
        return result

    def is_souls_orochi_stage_selected_11(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_11", 0.94)
        return result

    def is_souls_orochi_stage_selected_12(self):
        """
        八岐大蛇层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_orochi_stage_selected_12", 0.94)
        return result

    def is_souls_sougenbi_selected_1(self):
        """
        业原火层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_sougenbi_greedy_selected", 0.85)
        return result

    def is_souls_sougenbi_selected_2(self):
        """
        业原火层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_sougenbi_angry_selected", 0.85)
        return result

    def is_souls_sougenbi_selected_3(self):
        """
        业原火层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_sougenbi_folly_selected", 0.85)
        return result

    def is_souls_himiko_stage_selected_1(self):
        """
        卑弥呼层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_himiko_stage_selected_1", 0.97)
        return result

    def is_souls_himiko_stage_selected_2(self):
        """
        卑弥呼层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_himiko_stage_selected_2", 0.97)
        return result

    def is_souls_himiko_stage_selected_3(self):
        """
        卑弥呼层数已选中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_himiko_stage_selected_3", 0.97)
        return result

    def is_souls_teamup_button(self):
        """
        八岐大蛇组队按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_teamup_button")
        return result

    def is_souls_orochi_challenge_button(self):
        """
        八岐大蛇挑战按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_orochi_challenge_button")
        return result

    def is_souls_sougenbi_challenge_button(self):
        """
        业原火挑战那妞
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_sougenbi_challenge_button", 0.65)
        return result

    def is_souls_himiko_challenge_button(self):
        """
        卑弥呼挑战按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_himiko_challenge_button")
        return result

    def is_souls_cast_unlock(self):
        """
        御魂阵容未锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_cast_unlock")
        return result

    def is_souls_cast_lock(self):
        """
        御魂阵容已锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_cast_lock")
        return result

    def is_souls_auto_challenge_active(self):
        """
        御魂小纸人已激活
        :return:
        """
        return self.find_color_with_template_area("souls_is_souls_auto_battle", [253, 253, 253])

    def is_souls_doll_orochi_hunger(self):
        """
        八岐大蛇小纸人饿了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_doll_orochi_hunger")
        return result

    def is_souls_doll_sougenbi_hunger(self):
        """
        业原火小纸人饿了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_doll_sougenbi_hunger")
        return result

    def is_souls_doll_himiko_hunger(self):
        """
        卑弥呼小纸人饿了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("souls_is_souls_doll_himiko_hunger")
        return result
