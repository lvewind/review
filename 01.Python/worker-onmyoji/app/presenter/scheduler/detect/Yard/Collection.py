from hiworker import *


class DetectCollection(DetectImage):
    def __init__(self):
        super(DetectCollection, self).__init__()

    def is_collection_lot_panel(self):
        """
        签到界面
        :return:
        """
        result, coord, max_similarity = self.find_in_dynamic_scene("collection_is_lot_panel", check_t=3)
        return result

    def find_collection_prize_panel_common(self):
        """
        查找奖励界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_prize_panel_common")
        return result, coord

    def is_collection_lot_finish_panel(self):
        """
        签到完成面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_lot_panel_finish")
        return result

    def is_collection_lot_finish_panel_close_button(self):
        """
        签到完成关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_lot_finish_panel_close_button")
        return result

    def is_collection_lot_panel_qixi(self):
        """
        七夕签到
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_lot_panel_qixi")
        return result

    def is_collection_lot_panel_qixi_huaqian(self):
        """
        七夕签到
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_lot_panel_qixi_huaqian")
        return result

    def is_collection_souls_bonus_confirm_panel(self):
        """
        御魂加成领取确认界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_collection_souls_bonus_confirm_panel")
        return result

    def is_collection_souls_bonus_confirm_button(self):
        """
        御魂加成领取确认按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_collection_souls_bonus_confirm_button")
        return result

    def is_collection_mail_panel(self):
        """
        邮件界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_collection_mail_panel")
        return result

    def is_collection_mail_panel_close_button(self):
        """
        邮件界面关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_collection_mail_panel_close_button")
        return result

    def is_collection_mail_get_all_button(self):
        """
        邮件一键领取按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_collection_mail_get_all_buttin")
        return result

    def is_collection_mail_get_all_confirm_panel(self):
        """
        邮件去人一键领取界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_collection_mail_get_all_confirm_panel")
        return result

    def is_collection_mail_get_all_confirm_button(self):
        """
        邮件一键领取确认按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_is_collection_mail_get_all_confirm_button")
        return result

    def find_collection_mail_not_read(self):
        """
        查找未读邮件
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("collection_find_collection_mail_not_read")
        return result, coord

    def is_lot_999_prize(self):
        result, coord, max_similarity = self.find_in_template_rect("collection_is_lot_999_prize")
        return result
