from hiworker import *


class DetectShikigami(DetectImage):
    def __init__(self):
        super(DetectShikigami, self).__init__()

    def is_shikigami_panel(self):
        """
        式神录界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_panel")
        return result

    def is_shikigami_panel_quit_button(self):
        """
        式神录界面退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_panel_quit_button")
        return result

    def is_shikigami_yucheng_button(self):
        """
        式神育成按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_yucheng_button")
        return result

    def is_shikigami_yucheng_panel(self):
        """
        式神育成界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_yucheng_panel")
        return result

    def is_shikigami_yucheng_panel_quit_button(self):
        """
        式神育成界面退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_yucheng_panel_quit_button")
        return result

    def is_shikigami_yucheng_shengji(self):
        """
        升级
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_yucheng_shengji")
        return result

    def is_shikigami_yucheng_shengxing(self):
        """
        升星
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_yucheng_shengxing")
        return result

    def is_shikigami_upgrade_panel(self):
        """
        式神升级界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_upgrade_panel")
        return result

    def is_shikigami_upgrade_panel_quit_button(self):
        """
        式神升级界面退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_upgrade_panel_quit_button")
        return result

    def is_shikigami_upgrade_level_confirm_button(self):
        """
        式神升级界面确认按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_upgrade_confirm_button")
        return result

    def is_shikigami_upgrade_start_confirm_button(self):
        """
        式神升星界面退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_upgrade_start_confirm_button")
        return result

    def is_shikigami_upgrade_start_continue_button(self):
        """
        继续升级按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("shikigami_is_shikigami_upgrade_start_continue_button")
        return result
