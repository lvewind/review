from hiworker import *


class OperateCollection(Win32Click):
    def __init__(self):
        super(OperateCollection, self).__init__()

    def click_get_all_mail_button(self):
        """
        领取所有邮件
        :return:
        """
        self.click_in_template("collection_is_collection_mail_get_all_buttin")

    def confirm_get_all_mail(self):
        """
        确认领取所有邮件
        :return:
        """
        self.click_in_template("collection_is_collection_mail_get_all_confirm_button")

    def confirm_collection_souls_bonus(self):
        """
        确认领取加成
        :return:
        """
        self.click_in_template("collection_is_collection_souls_bonus_confirm_button")

    def close_mail_panel(self):
        """
        关闭邮件界面
        :return:
        """
        self.click_in_template("collection_close_mial_panel")

    def slide_mail_list_to_bottom(self):
        """
        滑动邮件列表到底部
        :return:
        """
        self.slide_distance_with_template("collection_slide_mail_list_to_buttom", 30, -150)

    def get_lot(self):
        self.click_in_template("collection_is_lot_panel")

    def close_lot_finish(self):
        self.click_in_template("collection_close_lot_panel_finish")

    def close_lot_999_prize(self):
        self.click_in_template("collection_close_lot_999_prize")

