from hiworker import *


class DetectIllustratedHandbook(DetectImage):
    def __init__(self):
        super(DetectIllustratedHandbook, self).__init__()

    def is_illustrate_handbook_panel(self):
        """
        绘卷界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_panel")
        return result

    def is_illustrate_handbook_panel_close_button(self):
        """
        绘卷界面关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_panel_close_button")
        return result

    def is_illustrate_handbook_shikigami_entrance(self):
        """
        绘卷式神列表入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_shikigami_entrance")
        return result

    def is_illustrate_handbook_shikigami_list(self):
        """
        绘卷式神界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_shikigami_list")
        return result

    def is_illustrate_handbook_shikigami_list_close_button(self):
        """
        关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_shikigami_list_close_button")
        return result

    def is_illustrate_handbook_share_button(self):
        """
        分享按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_shikigami_share_button")
        return result

    def is_illustrate_handbook_share_to_wechat(self):
        """
        分享到微信按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_shikigami_share_to_wechat")
        return result

    def is_illustrate_handbook_share_qrcode(self):
        """
        分享二维码
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_shikigami_share_qrcode")
        return result

    def is_illustrate_handbook_scroll_quit_button(self):
        """
        退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_shikigami_scroll_quit_button")
        return result

    def is_illustrate_handbook_qrcode_loading(self):
        """
        二维码加载界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("illustrate_handbook_is_illustrate_handbook_shikigami_qrcode_loadingn")
        return result
