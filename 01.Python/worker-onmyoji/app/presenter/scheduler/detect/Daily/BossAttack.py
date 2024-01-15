from hiworker import *


class DetectBossAttack(DetectImage):
    def __init__(self):
        super(DetectBossAttack, self).__init__()

    def is_boss_attack_invite(self):
        """
        是否存在麒麟邀请
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("daily_is_boss_attack_invite")
        return result
