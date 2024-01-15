from hiworker import *


class DetectBountySeals(DetectImage):
    def __init__(self):
        super(DetectBountySeals, self).__init__()

    def is_bounty_seals_invite_panel(self):
        """
        悬赏封印邀请提示界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bounty_seals_is_bounty_seals_invite_panel")
        return result

    def is_bounty_seals_invite_panel_close_button(self):
        """
        悬赏封印邀请界面关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("bounty_seals_is_bounty_seals_invite_panel_button")
        return result
