from hiworker import *


class OperateMPAY_LOGIN(Win32Click):
    def __init__(self):
        super(OperateMPAY_LOGIN, self).__init__()
        self.correction_window = False

    def click_game_login_button_in_change_method(self):
        """
        切换登录方式
        :return:
        """
        self.click_in_template("mpay_login_is_game_login_button_in_change_method")

    def change_login_method_to_qrcode(self):
        """
        选择二维码登录
        :return:
        """
        self.click_in_template("mpay_login_is_game_login_by_account")

    def change_login_method_to_account(self):
        """
        选择账号密码登录
        :return:
        """
        self.click_in_template("mpay_login_is_game_login_by_qrcode")

    def change_login_method_to_account_with_email(self):
        """
        选择邮箱登录
        :return:
        """
        self.click_in_template("mpay_login_is_game_login_by_qrcode_with_email")

    def change_login_method_to_account_with_phone_number(self):
        """
        选择手机号码登录
        :return:
        """
        self.click_in_template("mpay_login_is_game_login_by_qrcode_with_phone_number")

    def change_login_method_to_account_with_phone_number_password(self):
        """
        选择手机号码密码登录
        :return:
        """
        self.click_in_template("mpay_login_is_game_login_by_qrcode_with_phone_number_password")

    def change_login_method_to_account_with_phone_number_identifying(self):
        """
        选择手机验证码登录
        :return:
        """
        self.click_in_template("mpay_login_is_game_login_by_qrcode_with_phone_number_identifying")

    def remember_login_account(self):
        """
        记住账号
        :return:
        """
        self.click_in_template("mpay_login_remember_login_account")

    def remember_login_passwd(self):
        """
        记住密码
        :return:
        """
        self.click_in_template("mpay_login_remember_login_passwrd")

    def cancel_remember_login_account(self):
        """
        取消记住账号
        :return:
        """
        self.click_in_template("mpay_login_cancle_remember_login_account")

    def cancel_remember_login_passwd(self):
        """
        取消记住密码
        :return:
        """
        self.click_in_template("mpay_login_cancle_remember_login_passwrd")

    def refresh_qrcode(self):
        """
        刷新二维码
        :return:
        """
        self.click_in_template("mpay_login_refresh_qrcode")
