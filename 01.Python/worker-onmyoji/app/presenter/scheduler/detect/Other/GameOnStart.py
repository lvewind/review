from hiworker import *


class DetectGameOnStart(DetectImage):
    def __init__(self):
        super(DetectGameOnStart, self).__init__()
        self.detect_sleep_sec = 0.2

    def is_game_op_animation(self):
        """
        开场动画
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_game_op_animation")
        return result

    def is_platform_selected_panel(self):
        """
        平台选择界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_platform_selected_panel")
        return result

    def is_game_announcement(self):
        """
        游戏公告
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_game_announcement")
        return result

    def is_into_game(self):
        """
        进入游戏按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_into_game")
        return result

    def is_select_role_panel(self):
        """
        角色选择界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_select_role_panel")
        return result

    def is_role_list_open(self):
        """
        角色列表已展开
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_role_list_open")
        return result

    def is_user_agreement(self):
        """
        用户协议界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_user_agreement")
        return result

    def is_fine_quality(self):
        """
        画质选择接麦你
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_fine_quality")
        return result

    def is_sales_promotion_close_button(self):
        """
        促销关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_sales_promotion_close_button")
        return result

    def is_download_illustration_panel(self):
        """
        插画下载界面
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("game_on_start_is_download_illustration_panel", check_t=5)
        return result

    def is_download_illustration_panel_not_checked(self):
        """
        插画下载界面复选框未选择
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_download_illustration_panel_not_checked")
        return result

    def is_download_illustration_panel_checked(self):
        """
        插画下载界面复选框已选择
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_download_illustration_panel_checked")
        return result

    def is_download_illustration_panel_cancel_button(self):
        """
        插画下载取消按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_download_illustration_panel_cancle_button")
        return result

    def is_emulator_login_method(self):
        """
        模拟器登录
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method")
        return result

    def is_emulator_login_method_phone(self):
        """
        模拟器手机登录
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_phone")
        return result

    def is_emulator_login_method_email(self):
        """
        模拟器邮箱登录
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_email")
        return result

    def is_emulator_login_method_phone_panel(self):
        """
        模拟器手机登陆界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_phone_panel")
        return result

    def is_emulator_login_method_phone_panel_input(self):
        """
        模拟器手机登录路输入框
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_phone_panel_input")
        return result

    def is_emulator_login_method_email_panel(self):
        """
        模拟器邮箱登录界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_email_panel")
        return result

    def is_emulator_login_method_email_panel_input(self):
        """
        模拟器邮箱登录输入框
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_email_panel_input")
        return result

    def is_emulator_login_method_weibo(self):
        """
        模拟器微博登录
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_weibo")
        return result

    def is_emulator_login_method_quick(self):
        """
        模拟器快速登录
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_quick")
        return result

    def is_emulator_login_method_agree(self):
        """
        模拟器登录同意
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_agree")
        return result

    def is_emulator_login_method_agree_checked(self):
        """
        模拟器登录同意复选框已勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_method_agree_checked")
        return result

    def is_emulator_login_panel_bili(self):
        """
        模拟器bili登录
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_panel_bili")
        return result

    def is_emulator_login_panel_bili_login_button(self):
        """
        模拟器bili登录按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_emulator_login_panel_bili_login_button")
        return result

    def is_video_quality_anti_alias_panel(self):
        """
        抗锯齿设置界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_anti_alias_panel")
        return result

    def is_video_quality_anti_alias_panel_close_button(self):
        """
        关闭抗锯齿设置界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_anti_alias_panel_close_button")
        return result

    def is_video_quality_anti_alias_panel_next_button(self):
        """
        画质设置下一步按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_anti_alias_panel_next_button")
        return result

    def is_video_quality_anti_alias_checked(self):
        """
        抗锯齿已勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_anti_alias_checked")
        return result

    def is_video_quality_anti_alias_not_checked(self):
        """
        抗锯齿未勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_anti_alias_not_checked")
        return result

    def is_video_quality_panel(self):
        """
        画质设置界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_panel")
        return result

    def is_video_quality_smooth_not_checked(self):
        """
        流畅画质未勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_smooth_not_checked")
        return result

    def is_video_quality_smooth_checked(self):
        """
        流畅画质已勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_smooth_checked")
        return result

    def is_video_quality_nicety_not_checked(self):
        """
        高质量画质未勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_nicety_not_checked")
        return result

    def is_video_quality_nicety_checked(self):
        """
        高质量画质已勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_nicety_checked")
        return result

    def is_video_quality_extreme_not_checked(self):
        """
        精细画质未勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_extreme_not_checked")
        return result

    def is_video_quality_extreme_checked(self):
        """
        精细画质已勾选
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("game_on_start_is_video_quality_extreme_checked")
        return result
