from hiworker import *


class DetectTeam(DetectImage):
    def __init__(self):
        super(DetectTeam, self).__init__()

    def is_team_panel(self):
        """
        组队界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("team_is_teamup_panel", similarity=0.7)
        return result

    def is_team_panel_quit_button(self):
        """
        组队界面关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_quit_button")
        return result

    def is_team_panel_seal(self):
        """
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_seal")
        return result

    def is_team_panel_seal_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_seal_selected")
        return result

    def is_team_panel_exp(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_exp")
        return result

    def is_team_panel_exp_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_exp_selected")
        return result

    def is_team_panel_coin(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_coin")
        return result

    def is_team_panel_coin_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_coin_selected")
        return result

    def is_team_panel_nen(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_nen")
        return result

    def is_team_panel_nen_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_nen_selected")
        return result

    def is_team_panel_kraken(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_kraken")
        return result

    def is_team_panel_kraken_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_kraken_selected")
        return result

    def is_team_panel_refresh_button(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_refresh_button")
        return result

    def is_team_panel_auto_macth_button(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_panel_auto_macth_button")
        return result

    def is_team_seal_tiaotiaogege(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_tiaotiaogege")
        return result

    def is_team_seal_tiaotiaogege_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_tiaotiaogege_selected")
        return result

    def is_team_seal_jiaotu(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_jiaotu")
        return result

    def is_team_seal_jiaotu_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_jisotu_selected")
        return result

    def is_team_seal_gunv(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_gunv")
        return result

    def is_team_seal_gunv_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_gunv_selected")
        return result

    def is_team_seal_egui(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_egui")
        return result

    def is_team_seal_egui_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_egui_selected")
        return result

    def is_team_seal_erkounv(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_erkounv")
        return result

    def is_team_seal_erkounv_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_erkounv_selected")
        return result

    def is_team_seal_haifangzhu(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_haifangzhu")
        return result

    def is_team_seal_haifangzhu_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_haifangzhu_selected")
        return result

    def is_team_seal_guishihei(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_guishihei")
        return result

    def is_team_seal_guishihei_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_guishihei_selected")
        return result

    def is_team_seal_xiaosongwan(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_xiaosongwan")
        return result

    def is_team_seal_xiaosongwan_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_xiaosongwan_selected")
        return result

    def is_team_seal_rihefang(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_rihefang")
        return result

    def is_team_seal_rihefang_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_team_seal_rihefang_selected")
        return result

    def is_create_team_button(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_create_team_button")
        return result

    def is_create_team_button_2(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_create_team_button_2")
        return result

    def is_create_team_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_create_team_panel")
        return result

    def is_create_team_panel_any_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_create_team_panel_any_selected")
        return result

    def is_create_team_panel_friend_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_create_team_panel_friend_selected")
        return result

    def is_create_team_panel_only_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_create_team_panel_only_selected")
        return result

    def is_cooperation_teamup_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_panel", similarity=0.7)
        return result

    def is_cooperation_teamup_panel_quit_button(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_panel_quit_button")
        return result

    def is_cooperation_teamup_panel_confirm_quit(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_panel_confirm_quit")
        return result

    def is_cooperation_teamup_panel_invite_button(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_panel_invite_button")
        return result

    def is_cooperation_teamup_friend_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_friend_panel")
        return result

    def is_cooperation_teamup_friend_panel_invite_button(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_friend_panel_invite_button")
        return result

    def is_cooperation_teamup_friend_panel_cancel_button(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_friend_panel_cancel_button")
        return result

    def is_cooperation_teamup_friend_panel_friend(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_friend_panel_friend", 0.95)
        return result

    def is_cooperation_teamup_friend_panel_friend_chapter(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_friend_panel_friend_chapter", 0.95)
        return result

    def is_cooperation_teamup_friend_panel_recent(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_friend_panel_recent", 0.95)
        return result

    def is_cooperation_teamup_friend_panel_cross(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_friend_panel_cross", 0.95)
        return result

    def is_cooperation_teamup_friend_panel_guild(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_friend_panel_guild", 0.95)
        return result

    def is_cooperation_teamup_challenge_button_gray(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_challenge_button_gray", 0.98)
        return result

    def is_cooperation_teamup_challenge_button_yellow(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_challenge_button_yellow", 0.98)
        return result

    def is_cooperation_teamup_challenge_button_gray_longche(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_challenge_button_gray_longche", 0.98)
        return result

    def is_cooperation_teamup_challenge_button_yellow_longche(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teamup_challenge_button_yellow_longche", 0.98)
        return result

    def is_cooperation_teammate_selected(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_teammate_selected")
        return result

    def is_cooperation_cast_lock_up(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_cast_lock_up")
        return result

    def is_cooperation_cast_lock_up_longche(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_cast_lock_up_longche")
        return result

    def is_cooperation_cast_not_lock_up(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_cast_not_lock_up")
        return result

    def is_cooperation_cast_not_lock_up_longche(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_cast_not_lock_up_longche")
        return result

    def is_cooperation_doll_active(self):
        return self.find_color_with_template_area("team_is_cooperation_doll_active", [253, 253, 253])

    def is_cooperation_doll_active_longche(self):
        return self.find_color_with_template_area("team_is_cooperation_doll_active_longche", [253, 253, 253])

    def is_cooperation_hunger(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_cooperation_hunger")
        return result

    def is_feed_doll_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_feed_doll_panel")
        return result

    def is_feed_doll_panel_auto_feed_active(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_feed_doll_panel_auto_feed_active", 0.85)
        return result

    def is_bonus_button_in_cooperation_teamup(self):
        result, coord, max_similarity = self.find_in_template_rect("team_is_bonus_button_in_cooperation_teamup")
        return result
