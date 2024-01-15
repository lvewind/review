from hiworker import *


class OperateIllustratedHandbook(Win32Click):
    def __init__(self):
        super(OperateIllustratedHandbook, self).__init__()

    def close_illustrate_handbook_panel(self):
        """
        关闭绘卷界面
        :return:
        """
        self.click_in_template("illustrate_handbook_is_illustrate_handbook_panel")

    def open_illustrate_handbook_shikigami_list(self):
        """
        打开绘卷
        :return:
        """
        self.click_in_template("illustrate_handbook_is_illustrate_handbook_shikigami_entrance")

    def slide_illustrate_handbook_to_right(self):
        """
        滑动绘卷到右边
        :return:
        """
        self.slide_distance_with_template("illustrate_handbook_slide_illustrate_handbook_to_right", 200, 50)

    def close_illustrate_handbook_shikigami_list(self):
        """
        关闭式神列表
        :return:
        """
        self.click_in_template("illustrate_handbook_is_illustrate_handbook_shikigami_list_close_button")

    def open_illustrate_handbook_shikigami_scroll(self):
        """
        打开绘卷式神卷轴
        :return:
        """
        self.click_in_template("illustrate_handbook_is_illustrate_handbook_shikigami_list")

    def close_illustrate_handbook_scroll(self):
        """
        关闭绘卷卷轴
        :return:
        """
        self.click_in_template("illustrate_handbook_is_illustrate_handbook_shikigami_scroll_quit_button")

    def open_illustrate_handbook_share_method(self):
        """
        打开绘卷分享方法
        :return:
        """
        self.click_in_template("illustrate_handbook_is_illustrate_handbook_shikigami_share_button")

    def share_illustrate_handbook_to_wechat(self):
        """
        分享绘卷到微信
        :return:
        """
        self.click_in_template("illustrate_handbook_is_illustrate_handbook_shikigami_share_to_wechat")

    def close_illustrate_handbook_qrcode(self):
        """
        关闭分享二维码
        :return:
        """
        self.click_in_template("illustrate_handbook_close_illustrate_handbook_qrcode")
