from hiworker import *


class DetectRealmRaid(DetectImage):
    def __init__(self):
        super(DetectRealmRaid, self).__init__()

    def is_realm_raid_panel(self):
        """
        突破界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_panel")
        return result

    def is_realm_raid_frog(self):
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_frog")
        return result

    def is_realm_raid_panel_close_button(self):
        """
        突破界面关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_panel_close_button")
        return result

    def is_realm_raid_panel_person(self):
        """
        个人突破界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_panel_person", 0.9)
        return result

    def is_realm_raid_panel_guild(self):
        """
        寮突破界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_panel_guild")
        return result

    def is_realm_raid_guild_not_start(self):
        """
        寮突破未开启
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_guild_not_start", 0.9)
        return result

    def is_realm_raid_refresh_button(self):
        """
        突破刷新按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_refresh_button")
        return result

    def is_realm_raid_refresh_button_frog(self):
        """
        突破刷新按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_refresh_button_frog")
        return result

    def is_realm_raid_refresh_confirm_button(self):
        """
        突破刷新确认按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_refresh_confirm_button")
        return result

    def is_realm_raid_break_0(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_0", 0.9)
        return result

    def is_realm_raid_break_1(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_1", 0.9)
        return result

    def is_realm_raid_break_2(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_2", 0.9)
        return result

    def is_realm_raid_break_3(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_3", 0.9)
        return result

    def is_realm_raid_break_4(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_4", 0.9)
        return result

    def is_realm_raid_break_5(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_5", 0.9)
        return result

    def is_realm_raid_break_6(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_6", 0.9)
        return result

    def is_realm_raid_break_7(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_7", 0.9)
        return result

    def is_realm_raid_break_8(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_8", 0.9)
        return result

    def is_realm_raid_break_1_frog(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_1_frog", 0.9)
        return result

    def is_realm_raid_break_2_frog(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_2_frog", 0.9)
        return result

    def is_realm_raid_break_3_frog(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_3_frog", 0.9)
        return result

    def is_realm_raid_break_4_frog(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_4_frog", 0.9)
        return result

    def is_realm_raid_break_5_frog(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_5_frog", 0.9)
        return result

    def is_realm_raid_break_6_frog(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_6_frog", 0.9)
        return result

    def is_realm_raid_break_7_frog(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_7_frog", 0.9)
        return result

    def is_realm_raid_break_8_frog(self):
        """
        已突破
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_break_8_frog", 0.9)
        return result

    def is_realm_raid_not_break_3(self):
        """
        为突破到3个
        :return:
        """
        return self.find_color_with_template_area("realm_raid_is_realm_raid_not_break_3", [55, 60, 90], tolerance=10)

    def is_realm_raid_not_break_6(self):
        """
        为突破到6个
        :return:
        """
        return self.find_color_with_template_area("realm_raid_is_realm_raid_not_break_6", [55, 60, 90], tolerance=10)

    def is_realm_raid_cast_lock(self):
        """
        突破阵容锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_cast_lock")
        return result

    def is_realm_raid_cast_lock_frog(self):
        """
        突破阵容锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_cast_lock_frog")
        return result

    def is_realm_raid_cast_unlock(self):
        """
        突破阵容未锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_cast_unlock")
        return result

    def is_realm_raid_cast_unlock_frog(self):
        """
        突破阵容未锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_cast_unlock_frog")
        return result

    def is_realm_raid_pass_use_up(self):
        """
        突破券用完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_pass_use_up", 0.9)
        return result

    def find_realm_raid_attack_button(self):
        """
        查找公攻击按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_realm_raid_attack_button")
        return result, coord

    def find_realm_raid_person_target(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_realm_raid_person_target")
        return result, coord

    def find_realm_raid_person_target_col_1(self):
        """
        在第1列查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_realm_raid_person_target_col_1", 0.9)
        return result, coord

    def find_realm_raid_person_target_col_2(self):
        """
        在第2列查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_realm_raid_person_target_col_2", 0.9)
        return result, coord

    def find_realm_raid_person_target_col_3(self):
        """
        在第3列查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_realm_raid_person_target_col_3", 0.9)
        return result, coord

    def find_realm_raid_person_target_row_1(self):
        """
        在第1行查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_realm_raid_person_target_row_1", 0.85)
        return result, coord

    def find_realm_raid_person_target_row_2(self):
        """
        在第2行查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_realm_raid_person_target_row_2", 0.85)
        return result, coord

    def find_realm_raid_person_target_row_3(self):
        """
        在第3行查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_realm_raid_person_target_row_3", 0.85)
        return result, coord

    def is_realm_raid_target_1(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_target_1")
        return result

    def is_realm_raid_target_2(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_target_2")
        return result

    def is_realm_raid_target_3(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_target_3")
        return result

    def is_realm_raid_target_4(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_target_4")
        return result

    def is_realm_raid_target_5(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_target_5")
        return result

    def is_realm_raid_target_6(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_target_6")
        return result

    def is_realm_raid_target_7(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_target_7")
        return result

    def is_realm_raid_target_8(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_target_8")
        return result

    def is_realm_raid_target_9(self):
        """
        查找个人突破目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_realm_raid_target_9")
        return result

    def find_guild_realm_raid_medal(self, medal_star, area):
        """
        根据星数查找目标
        :param medal_star:
        :param area:
        :return:
        """
        result, coord, max_similarity = getattr(self, "find_guild_realm_raid_medal_" + str(medal_star))(area)
        print("medal_star", medal_star)
        print("area", area)
        return result, coord

    def find_guild_realm_raid_medal_0(self, area):
        """
        查找0星寮突目标
        :param area:
        :return:
        """
        result, coord, max_similarity = self.find_in_different_template_rect("realm_raid_find_guild_realm_raid_medal_0",
                                                             "realm_raid_find_guild_realm_raid_area_" + str(area))
        return result, coord

    def find_guild_realm_raid_medal_1(self, area):
        """
        查找1星寮突目标
        :param area:
        :return:
        """
        result, coord, max_similarity = self.find_in_different_template_rect("realm_raid_find_guild_realm_raid_medal_1",
                                                             "realm_raid_find_guild_realm_raid_area_" + str(area))
        return result, coord

    def find_guild_realm_raid_medal_2(self, area):
        """
        查找2星寮突目标
        :param area:
        :return:
        """
        result, coord, max_similarity = self.find_in_different_template_rect("realm_raid_find_guild_realm_raid_medal_2",
                                                             "realm_raid_find_guild_realm_raid_area_" + str(area))
        return result, coord

    def find_guild_realm_raid_medal_3(self, area):
        """
        查找3星寮突目标
        :param area:
        :return:
        """
        result, coord, max_similarity = self.find_in_different_template_rect("realm_raid_find_guild_realm_raid_medal_3",
                                                             "realm_raid_find_guild_realm_raid_area_" + str(area))
        return result, coord

    def find_guild_realm_raid_medal_4(self, area):
        """
        查找4星寮突目标
        :param area:
        :return:
        """
        result, coord, max_similarity = self.find_in_different_template_rect("realm_raid_find_guild_realm_raid_medal_4",
                                                             "realm_raid_find_guild_realm_raid_area_" + str(area))
        return result, coord

    def find_guild_realm_raid_medal_5(self, area):
        """
        查找5星寮突目标
        :param area:
        :return:
        """
        result, coord, max_similarity = self.find_in_different_template_rect("realm_raid_find_guild_realm_raid_medal_5",
                                                             "realm_raid_find_guild_realm_raid_area_" + str(area))
        return result, coord

    def find_guild_realm_raid_target_item(self):
        """
        查找寮突目标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_guild_realm_raid_target", 0.9)
        return result, coord

    def find_guild_realm_raid_attack_button(self):
        """
        查找寮突攻击按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_guild_realm_raid_attack_button")
        return result, coord

    def find_guild_realm_raid_target_break(self):
        """
        查找寮突攻破图标
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_find_guild_realm_raid_target_break")
        return result, coord

    def is_realm_raid_guild_attack_use_up(self):
        """
        寮突次数用完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_guild_realm_raid_attack_use_up", 0.9)
        return result

    def is_realm_raid_guild_cast_lock(self):
        """
        寮突锁定阵容
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_guild_realm_cast_lock")
        return result

    def is_realm_raid_guild_cast_unlock(self):
        """
        寮突未锁定阵容
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_guild_realm_cast_unlock")
        return result

    def is_realm_raid_guild_all_break(self):
        """
        寮突完成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("realm_raid_is_guild_realm_raid_all_break")
        return result

    def is_realm_raid_guild_target_failed(self, coord):
        """
        寮突失败
        :param coord:
        :return:
        """
        result, coord, max_similarity = self.find_with_point_ext_area(template="realm_raid_is_guild_realm_raid_target_failed",
                                                      target_point=[coord[0] + 50, coord[1] - 40],
                                                      box=[50, 50, 50, 50])
        return result
