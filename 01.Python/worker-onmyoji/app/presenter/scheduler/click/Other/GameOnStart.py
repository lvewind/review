from hiworker import *


class OperateGameOnStart(Win32Click):
    def __init__(self):
        super(OperateGameOnStart, self).__init__()

    def skip_game_op_animation(self):
        """
        跳过开场动画
        :return:
        """
        self.click_in_template("game_on_start_skip_game_op_animation")

    def select_android(self):
        """
        选择安卓
        :return:
        """
        self.click_in_template("game_on_start_select_android")

    def select_i_os(self):
        """
        选择iOS
        :return:
        """
        self.click_in_template("game_on_select_iOS")

    def close_game_announcement(self):
        """
        关闭游戏公告
        :return:
        """
        self.click_in_template("game_on_start_close_game_announcement")

    def click_into_game(self):
        """
        点击进入游戏
        :return:
        """
        self.click_in_template("game_on_start_click_into_game")

    def click_to_change_game_regional(self):
        """
        进入服务器选择
        :return:
        """
        self.click_in_template("game_on_start_click_to_change_game_regional")

    def open_role_list(self):
        """
        展开角色列表
        :return:
        """
        self.click_in_template("game_on_start_open_role_list")

    def select_first_role(self):
        """
        选择第一个角色
        :return:
        """
        self.click_in_template("game_on_start_select_first_role")

    def slide_role_list_to_right(self):
        """
        滑动角色列表到右边
        :return:
        """
        self.slide_distance_with_template("game_on_start_slide_role_list_to_right", 150, 20)

    def slide_role_list_to_left(self):
        """
        滑动角色列表到左边
        :return:
        """
        self.slide_distance_with_template("game_on_start_slide_role_list_to_right", -150, 20)

    def check_agree(self):
        """
        勾选用户协议同意
        :return:
        """
        self.click_in_template("game_on_start_is_emulator_login_method_agree")

    def confirm_user_agreement(self):
        """
        同意用户协议
        :return:
        """
        self.click_in_template("game_on_start_is_user_agreement")

    def select_fine_quality(self):
        """
        选择高质量画面
        :return:
        """
        self.click_in_template("game_on_start_is_fine_quality")

    def skip_select_fine_quality(self):
        """
        跳过画质选择
        :return:
        """
        self.click_in_template("game_on_start_is_fine_quality_skip")

    def close_sales_promotion(self):
        """
        关闭促销界面
        :return:
        """
        self.click_in_template("game_on_start_is_sales_promotion_close_button")

    def check_download_illustration_never_prompt(self):
        """
        勾选插画不再提示
        :return:
        """
        self.click_in_template("game_on_start_is_download_illustration_panel_checked")

    def cancel_button_download_illustration(self):
        """
        取消插画下载
        :return:
        """
        self.click_in_template("game_on_start_is_download_illustration_panel_cancle_button")

    def change_video_quality_anti_alias_checked(self):
        """
        切换抗锯齿状态
        :return:
        """
        self.click_in_template("game_on_start_is_video_quality_anti_alias_checked")

    def change_video_quality_smooth_checked(self):
        """
        选择流畅画质
        :return:
        """
        self.click_in_template("game_on_start_is_video_quality_smooth_checked")

    def change_video_quality_nicety_checked(self):
        """
        选择高质量画质
        :return:
        """
        self.click_in_template("game_on_start_is_video_quality_nicety_checked")

    def change_video_quality_extreme_checked(self):
        """
        选择精细画质
        :return:
        """
        self.click_in_template("game_on_start_is_video_quality_extreme_checked")

    def close_video_quality_panel(self):
        """
        关闭画质选择界面
        :return:
        """
        self.click_in_template("game_on_start_is_video_quality_anti_alias_panel_close_button")
