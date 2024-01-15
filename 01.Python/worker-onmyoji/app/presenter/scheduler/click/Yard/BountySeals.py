from hiworker import *


class OperateBountySeals(Win32Click):
    def __init__(self):
        super(OperateBountySeals, self).__init__()

    def close_bounty_seals_panel(self):
        """
        关闭悬赏封印界面
        :return:
        """
        self.click_in_template("bounty_seals_is_bounty_seals_invite_panel_button")
