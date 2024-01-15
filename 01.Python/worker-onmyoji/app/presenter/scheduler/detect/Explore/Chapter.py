import random

from hiworker import *


class DetectChapter(DetectImage):
    def __init__(self):
        super(DetectChapter, self).__init__()

    def is_chapter_panel(self):
        """
        是否章节面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_panel")
        return result

    def is_chapter_panel_close_button(self):
        """
        是否章节面板关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_panel_close_button")
        return result

    def is_chapter_panel_hard_selected(self):
        """
        是否已选中章节困难难度
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_panel_hard_selected")
        return result

    def is_chapter_panel_simple_selected(self):
        """
        是否已选中章节普通难度
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_panel_simple_selected")
        return result

    def is_chapter_panel_hard_not_selected(self):
        """
        是否未选中章节困难难度
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_panel_hard_not_selected")
        return result

    def is_chapter_panel_simple_not_selected(self):
        """
        是否未选中章节普通难度
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_panel_simple_not_selected")
        return result

    def is_create_team_panel_chapter(self):
        """
        章节组队界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_create_team_panel_chapter")
        return result

    def is_chapter_zone(self):
        """
        狗粮副本内
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_zone")
        return result

    def is_chapter_zone_quit_button(self):
        """
        狗粮副本退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_zone_quit_button")
        return result

    def is_chapter_zone_quit_confirm(self):
        """
        狗粮房间退出确认按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_zone_quit_confirm")
        return result

    def is_chapter_create_team_panel_any_selected(self):
        """
        狗粮组队公开
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_create_team_panel_any_selected")
        return result

    def is_chapter_create_team_panel_friend_selected(self):
        """
        狗粮组队好友
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_create_team_panel_friend_selected")
        return result

    def is_chapter_create_team_panel_only_selected(self):
        """
        狗粮组队仅邀请
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_create_team_panel_only_selected")
        return result

    def find_chapter_boss_prize_doll(self):
        """
        狗粮查找奖励小纸人
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_boss_prize_doll")
        return result, coord

    def find_chapter_boss(self):
        """
        查找狗粮BOSS
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_boss", 0.75)
        return result, coord

    def find_chapter_spirit(self):
        """
        查找狗粮小怪
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_spirit")
        return result, coord

    def is_continue_invite_chapter_panel(self):
        """
        狗粮继续邀请
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_continue_invite_chapter_panel")
        return result

    def is_chapter_cast_unlock(self):
        """
        狗粮阵容未锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_cast_unlock")
        return result

    def is_chapter_cast_unlock_novice(self):
        """
        狗粮阵容未锁定新手模式
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_cast_unlock_novice")
        return result

    def is_chapter_cast_lock(self):
        """
        狗粮阵容已锁定
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_cast_lock")
        return result

    def is_chapter_cast_lock_novice(self):
        """
        狗粮阵容已锁定新手模式
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_cast_lock_novice")
        return result

    def find_chapter_solo_full_dog(self):
        """
        查找单刷满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_solo_full_dog", 0.65)
        return result, coord

    def find_chapter_captain_full_dog_2v2(self):
        """
        查找队长2v2满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_captain_full_dog_2v2", 0.65)
        return result, coord

    def find_chapter_captain_full_dog_1v3(self):
        """
        查找队长1v3满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_captain_full_dog_1v3", 0.65)
        return result, coord

    def find_chapter_captain_full_dog_1v2(self):
        """
        查找队长1v2满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_captain_full_dog_1v3", 0.65)
        return result, coord

    def find_chapter_teammate_full_dog_2v2(self):
        """
        查找队友2v2满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_teammate_full_dog_2v2", 0.65)
        return result, coord

    def find_chapter_teammate_full_dog_1v3(self):
        """
        查找队友1v3满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_teammate_full_dog_1v3", 0.65)
        return result, coord

    def find_chapter_teammate_full_dog_0v3(self):
        """
        查找队友0v3满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_teammate_full_dog_0v3", 0.65)
        return result, coord

    def find_chapter_teammate_full_dog_1v2(self):
        """
        查找队友1v2满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_teammate_full_dog_1v2", 0.65)
        return result, coord

    def find_chapter_full_dog_left_in_change_scene(self):
        """
        查找换狗粮场景左边满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_full_dog_left_in_change_scene")
        return result, coord

    def find_chapter_full_dog_all_in_change_scene(self):
        """
        查找换狗粮场景所有满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_full_dog_all_in_change_scene")
        return result, coord

    def is_chapter_change_dog_food_panel(self):
        """
        换狗粮界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_change_dog_food_panel")
        return result

    def is_chapter_change_dog_food_m_list(self):
        """
        换狗粮M列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_change_dog_food_m_list")
        return result

    def is_chapter_change_dog_food_m_list_button(self):
        """
        换狗粮M列表按键
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_change_dog_food_m_list_button")
        return result

    def is_chapter_change_dog_food_n_list(self):
        """
        换狗粮N列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_change_dog_food_n_list")
        return result

    def is_chapter_change_dog_food_list_full_level(self):
        """
        换狗粮列表有满级狗粮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_change_dog_food_list_full_level")
        return result

    def is_chapter_change_dog_food_n_list_button(self):
        """
        换狗粮N列表按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_change_dog_food_n_list_button")
        return result

    def find_chapter_change_dog_food_list_m_star_2(self):
        """
        在狗粮列表查找二星狗粮M
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_start_2", 0.98)
        return result, coord

    def find_chapter_change_dog_food_list_m_star_3(self):
        """
        在狗粮列表查找三星狗粮M
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_start_3", 0.98)
        return result, coord

    def find_chapter_change_dog_food_list_m_star_4(self):
        """
        在狗粮列表查找四星狗粮M
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_start_4", 0.98)
        return result, coord

    def find_chapter_change_dog_food_list_n_star_2(self):
        """
        在狗粮列表查找二星狗粮N
        :return:
        """
        result, coord, max_similarity = False, [0, 0]
        for t in range(6):
            r = random.randint(1, 12)
            match r:
                case 1:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_shi", 0.92)
                case 2:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_zhou", 0.92)
                case 3:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_qing", 0.92)
                case 4:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_huang", 0.92)
                case 5:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_hong", 0.92)
                case 6:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_lv", 0.92)
                case 7:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_san", 0.92)
                case 8:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_she", 0.92)
                case 9:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_dao", 0.92)
                case 10:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_hun", 0.92)
                case 11:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_seng", 0.92)
                case 12:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_2_deng", 0.92)
            if result:
                break
        return result, coord

    def find_chapter_change_dog_food_list_n_star_3(self):
        """
        在狗粮列表查找三星狗粮N
        :return:
        """
        result, coord, max_similarity = False, [0, 0]
        for t in range(6):
            r = random.randint(1, 12)
            match r:
                case 1:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_shi", 0.92)
                case 2:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_zhou", 0.92)
                case 3:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_qing", 0.92)
                case 4:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_huang", 0.92)
                case 5:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_hong", 0.92)
                case 6:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_lv", 0.92)
                case 7:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_san", 0.92)
                case 8:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_she", 0.92)
                case 9:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_dao", 0.92)
                case 10:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_hun", 0.92)
                case 11:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_seng", 0.92)
                case 12:
                    result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_3_deng", 0.92)
            if result:
                break
        return result, coord

    def find_chapter_change_dog_food_list_n_star_4(self):
        """
        在狗粮列表查找四星狗粮N
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_find_chapter_change_dog_food_list_n_star_4", 0.92)
        return result, coord

    def is_chapter_doll_hunger(self):
        """
        小纸人饿了
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_doll_hunger")
        return result,

    def is_chapter_feed_doll_panel(self):
        """
        小纸人喂食面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_feed_doll_panel")
        return result

    def is_chapter_feed_doll_panel_auto_feed_active(self):
        """
        小纸人自动喂食
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_feed_doll_panel_auto_feed_active")
        return result

    def is_found_spirit(self):
        """
        妖怪发现
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_found_spirit")
        return result

    def is_chapter_zone_doll_exist(self):
        """
        自动挑战
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("chapter_is_chapter_zone_doll_exist", 0.7)
        return result
