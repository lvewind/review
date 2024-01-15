import hiworker

from ..Common import *
from ...detect.Other import DetectMPAY_LOGIN
from ...click.Other.MPAY_LOGIN import OperateMPAY_LOGIN

from app.presenter.data import *


class PlayGameOnStart(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayGameOnStart, self).__init__(play_input)
        m_pay_login_title = "[#] [" + self.play_input.run_env.name + "] 登录 [#]"
        self.detect_MPAY_LOGIN = DetectMPAY_LOGIN()
        self.detect_MPAY_LOGIN.set_data(m_pay_login_title, im_data, coord_data)
        self.operate_MPAY_LOGIN = OperateMPAY_LOGIN()
        self.operate_MPAY_LOGIN.set_data(m_pay_login_title, coord_data)
        self.is_regional_reset = False
        self.emulator = hiworker.Emulator(play_input.app_setting.emulator_path)

    def run(self):
        self.stop_flag = False
        self.stop_status = False
        signal_run_list.set_current_scene.emit(self.run_id, "初始化")
        signal_run_list.set_current_operation.emit(self.run_id, "")
        while not self.stop_status:
            if not self.stop_flag:
                if self.play_input.run_env.env_type == 1:
                    self.processing_game_on_start_sandbox()
                elif self.play_input.run_env.env_type == 2:
                    self.processing_game_on_start_emulator()
            else:
                self.stop_status = True
            self.sleep_in_run(0.5)
        else:
            self.is_finished = True
            signal_run_list.set_current_operation.emit(self.run_id, "初始化完成")

    def processing_game_on_start_sandbox(self):
        """
        处理刚进游戏界面-沙箱
        :return:
        """
        if self.detect_MPAY_LOGIN.is_game_login_button():
            signal_run_list.set_current_scene.emit(self.run_id, "账号登录")
            signal_run_list.set_current_operation.emit(self.run_id, "切换登录")
            self.operate_MPAY_LOGIN.click_game_login_button_in_change_method()
        elif self.detect_MPAY_LOGIN.is_game_login_qrcode_success():
            signal_run_list.set_current_scene.emit(self.run_id, "扫码成功")
            signal_run_list.set_current_operation.emit(self.run_id, "等待确认")
        elif self.detect_MPAY_LOGIN.is_game_login_by_qrcode():
            signal_run_list.set_current_scene.emit(self.run_id, "扫码登录")
            if self.detect_MPAY_LOGIN.is_game_login_qrcode_exist():
                signal_run_list.set_current_operation.emit(self.run_id, "等待扫码")
            elif self.detect_MPAY_LOGIN.is_login_timeout_qrcode():
                signal_run_list.set_current_operation.emit(self.run_id, "刷新二维码")
                self.operate_MPAY_LOGIN.refresh_qrcode()
                time.sleep(3)
        elif self.detect_MPAY_LOGIN.is_game_login_by_account():
            signal_run_list.set_current_scene.emit(self.run_id, "密码登录")
            if self.play_input.account.remember_password:
                if self.detect_MPAY_LOGIN.is_game_login_not_remember_password():
                    signal_run_list.set_current_operation.emit(self.run_id, "点击免密登录")
                    self.operate_MPAY_LOGIN.remember_login_passwd()
            if self.detect_MPAY_LOGIN.is_game_login_by_email():
                signal_run_list.set_current_operation.emit(self.run_id, "等待邮箱登录")
            elif self.detect_MPAY_LOGIN.is_game_login_by_phone_number():
                if self.detect_MPAY_LOGIN.is_game_login_by_phone_number_with_identifying():
                    signal_run_list.set_current_operation.emit(self.run_id, "等待手机+验证码登录")
                else:
                    signal_run_list.set_current_operation.emit(self.run_id, "等待手机+密码登录")

        # elif self.is_game_op_animation():
        #     signal_run_list.set_current_operation.emit(self.run_id, "跳过开场动画")
        #     self.skip_game_op_animation()

        elif self.is_platform_selected_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "平台选择")
            if self.play_input.account.platform == "AOS":
                signal_run_list.set_current_operation.emit(self.run_id, "选择安卓平台")
                self.select_android()
            elif self.play_input.account.platform == "iOS":
                signal_run_list.set_current_operation.emit(self.run_id, "选择iOS平台")
                self.select_i_os()
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "无平台信息")
        else:
            self.processing_game_on_start_common()

    def processing_game_on_start_emulator(self):
        """
        处理刚进游戏界面-模拟器
        :return:
        """
        if self.emulator.is_app_m_resumed_activity_by_id(self.play_input.run_env.id, "com.netease.onmyoji") \
                or self.emulator.is_app_m_resumed_activity_by_id(self.play_input.run_env.id, "com.netease.onmyoji.bili"):
            if self.is_emulator_login_method():
                signal_run_list.set_current_scene.emit(self.run_id, "登陆界面")
                if self.is_emulator_login_method_agree_checked():
                    signal_run_list.set_current_operation.emit(self.run_id, "等待选择登录方式")
                elif self.is_emulator_login_method_agree():
                    signal_run_list.set_current_operation.emit(self.run_id, "同意隐私政策")
                    self.check_agree()
            elif self.is_emulator_login_method_phone_panel():
                signal_run_list.set_current_operation.emit(self.run_id, "等待手机登录")
            elif self.is_emulator_login_method_email_panel():
                signal_run_list.set_current_operation.emit(self.run_id, "等待邮箱登录")
            elif self.is_emulator_login_panel_bili():
                signal_run_list.set_current_operation.emit(self.run_id, "等待Bili登录")
            else:
                self.processing_game_on_start_common()

        else:
            self.emulator.run_app_by_id(self.play_input.run_env.id, "com.netease.onmyoji")
            self.emulator.run_app_by_id(self.play_input.run_env.id, "com.netease.onmyoji.bili")
            time.sleep(5)

    def processing_game_on_start_common(self):
        if self.is_game_announcement():
            signal_run_list.set_current_scene.emit(self.run_id, "游戏公告")
            signal_run_list.set_current_operation.emit(self.run_id, "关闭游戏公告")
            self.close_game_announcement()
        elif self.is_select_role_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "角色选择")
            if self.is_role_list_open():
                self.select_role()
            else:
                self.open_role_list()
        elif self.is_into_game():  # 进入游戏界面
            signal_run_list.set_current_scene.emit(self.run_id, "进入游戏")
            if self.play_input.account.change_role:
                if self.is_regional_reset:  # 游戏大区已经重设，进入游戏
                    signal_run_list.set_current_operation.emit(self.run_id, "进入游戏")
                    self.click_into_game()
                else:
                    signal_run_list.set_current_operation.emit(self.run_id, "切换角色")
                    self.click_to_change_game_regional()  # 进入角色切换界面
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "进入游戏")
                self.click_into_game()
        elif self.is_yard():
            signal_run_list.set_current_scene.emit(self.run_id, "庭院")
            if self.is_sales_promotion_close_button():
                signal_run_list.set_current_operation.emit(self.run_id, "关闭推销界面")
                self.close_sales_promotion()
            elif self.is_download_illustration_panel():
                signal_run_list.set_current_operation.emit(self.run_id, "取消插画下载")
                self.cancel_button_download_illustration()
                # signal_run_list.display_current_operation.emit(self.run_id, "勾选不再提示")
                # self.check_download_illustration_never_prompt()
            else:
                self.stop_flag = True
        elif self.is_explore():
            signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
            self.stop_flag = True
        elif self.is_battle_battling():
            signal_run_list.set_current_scene.emit(self.run_id, "战斗中")
            signal_run_list.set_current_operation.emit(self.run_id, "等待当前战斗结束")
            result, coord = self.find_tip_with_hand()  # 找提示手指
            if result:
                signal_run_list.set_current_operation.emit(self.run_id, "点提示")
                self.click_in_circle([coord[0] - 40, coord[1] - 40], 32)
            else:
                result, coord = self.find_technique_target_common()
                if result:
                    self.click_in_circle(coord)
                else:
                    pass
        elif self.is_battle_win_prize_daruma():
            signal_run_list.set_current_scene.emit(self.run_id, "战斗奖励")
            signal_run_list.set_current_operation.emit(self.run_id, "跳过战斗奖励")
            self.skip_battle_win_prize(1)
        elif self.is_battle_failed_drum():
            signal_run_list.set_current_scene.emit(self.run_id, "战斗失败")
            signal_run_list.set_current_operation.emit(self.run_id, "跳过战斗失败")
            self.skip_battle_failed(random.randint(1, 3))
        elif self.is_battle_ready():
            self.set_battle_ready()
        elif self.is_souls_stage_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "御魂界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出御魂界面")
            self.quit_souls_stage_panel()
        elif self.is_souls_zone_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "御魂界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出御魂界面")
            self.quit_souls_zone_panel_quit_button()
        elif self.is_realm_raid_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "突破界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出突破界面")
            self.close_realm_raid_panel()
        elif self.is_totem_stage_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "御灵界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出御灵界面")
            self.quit_totem_stage_panel()
        elif self.is_totem_zone_select_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "御灵界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出御灵界面")
            self.quit_totem_zone_select_panel()
        elif self.is_chapter_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "狗粮界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出狗粮界面")
            self.close_chapter_panel()
        elif self.is_chapter_zone():
            signal_run_list.set_current_scene.emit(self.run_id, "狗粮界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出狗粮界面")
            if self.is_chapter_zone_quit_confirm():
                self.confirm_quit_chapter_zone()
            else:
                self.quit_chapter_zone()
        elif self.is_daily_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "日常界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出日常界面")
            self.close_daily_panel()
        elif self.is_team_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "组队界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出组队界面")
            self.close_teamup_panel()
        elif self.is_cooperation_teamup_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "协战队伍")
            signal_run_list.set_current_operation.emit(self.run_id, "退出协战队伍")
            if self.is_cooperation_teamup_panel_confirm_quit():
                self.confirm_quit_cooperation_teamup_panel()
            self.close_cooperation_teamup_panel()
        elif self.is_evo_tower():
            signal_run_list.set_current_scene.emit(self.run_id, "觉醒界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出觉醒界面")
            self.quit_evo_tower_quit()
        elif self.is_evo_stage_panel():
            signal_run_list.set_current_scene.emit(self.run_id, "觉醒界面")
            signal_run_list.set_current_operation.emit(self.run_id, "退出觉醒界面")
            self.quit_evo_stage_panel()
        elif self.is_story_scene():
            signal_run_list.set_current_scene.emit(self.run_id, "剧情场景")
            self.stop_flag = True
        elif self.is_onmyoji_unlock_panel():
            self.close_onmyoji_unlock_panel()
        elif self.is_chat_panel():
            self.close_chat_panel()

        self.sleep_in_run()

    def select_role(self):
        signal_run_list.set_current_operation.emit(self.run_id, "选择角色")
        if self.play_input.account.login_img:
            for i in range(3):
                result, coord = self.find_in_different_template_rect(self.play_input.account.login_img, "user_login_img")
                if result:
                    self.click_in_circle(coord)
                    # self.click_in_circle([coord[0], coord[1] - 50], 20)
                    self.is_regional_reset = True
                    break
                else:
                    self.slide_role_list_to_right()
            else:
                for i in range(3):
                    result, coord = self.find_in_template_rect(self.play_input.account.login_img)
                    if result:
                        self.click_in_circle([coord[0], coord[1] - 50], 20)
                        self.is_regional_reset = True
                        break
                    else:
                        self.slide_role_list_to_left()
                else:
                    self.select_first_role()
                    self.is_regional_reset = True

        else:
            self.select_first_role()
            self.is_regional_reset = True

    # com.netease.onmyoji.bili
    # com.netease.onmyoji
