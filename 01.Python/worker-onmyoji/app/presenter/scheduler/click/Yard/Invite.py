from hiworker import *


class OperateInvite(Win32Click):
    def __init__(self):
        super(OperateInvite, self).__init__()

    def accept_invite(self):
        """
        接受邀请
        :return:
        """
        self.click_in_template("invite_is_invite_accpet_button")

    def accept_invite_auto(self, coord: list):
        """
        自动接受邀请
        :param coord:
        :return:
        """
        # self.click_in_template("invite_is_invite_accpet_auto_button")
        self.click_in_circle(coord)

    def checked_confirm_auto_accept_panel(self):
        """
        勾选自动确认
        :return:
        """
        self.click_in_template("invite_is_confirm_auto_accept_panel_checked")

    def confirm_auto_accept_panel(self):
        """
        确认自动邀请
        :return:
        """
        self.click_in_template("invite_is_confirm_auto_accept_panel_button")

    def cancel_auto_accept_panel(self):
        """
        取消自动邀请
        :return:
        """
        self.click_in_template("invite_is_cancel_auto_accept_panel_button")
