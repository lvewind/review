from hiworker import *


class DetectMPAY_LOGIN(DetectImage):
    def __init__(self):
        super(DetectMPAY_LOGIN, self).__init__()
        self.correction_window = False
        self.sleep_sec = 0.3

    def is_game_login_by_qrcode(self):
        """
        二维码登录界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_by_qrcode")
        return result

    def is_login_failed_qrcode(self):
        """
        二维码登陆失败
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_login_failed_qrcode")
        return result

    def is_login_timeout_qrcode(self):
        """
        二维码超时
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_login_timeout_qrcode")
        return result

    def is_game_login_qrcode_exist(self):
        """
        二维码已存在
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_qrcode_exist")
        return result

    def is_game_login_by_account(self):
        """
        账号密码登录切换按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_by_account")
        return result

    def is_game_login_by_email(self):
        """
        邮箱登录
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_by_email")
        return result

    def is_game_login_by_phone_number(self):
        """
        手机登录
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_by_phone_number")
        return result

    def is_game_login_by_phone_number_with_identifying(self):
        """
        验证码登录
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_by_phone_number_with_identifying")
        return result

    def is_game_login_change_method(self):
        """
        登录方式切换
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_change_method")
        return result

    def is_game_login_button(self):
        """
        登录按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_button")
        return result

    def is_game_login_button_in_change_method(self):
        """
        登录按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_button_in_change_method")
        return result

    def is_game_login_remember_account(self):
        """
        记住账号
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_remember_account")
        return result

    def is_game_login_not_remember_account(self):
        """
        不记住账号
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_not_remember_account")
        return result

    def is_game_login_remember_password(self):
        """
        记住密码
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_remember_password")
        return result

    def is_game_login_not_remember_password(self):
        """
        不记住密码
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_not_remember_password")
        return result

    def is_game_login_qrcode_success(self):
        """
        二维码扫描成功
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("mpay_login_is_game_login_qrcode_success")
        return result
