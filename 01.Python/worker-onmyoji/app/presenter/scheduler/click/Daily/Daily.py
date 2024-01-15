from hiworker import *


class OperateDaily(Win32Click):
    def __init__(self):
        super(OperateDaily, self).__init__()

    def close_daily_panel(self):
        """
        关闭日常界面
        :return:
        """
        self.click_in_template("daily_is_daily_panel_close_button")

    def open_daily_panel(self):
        """
        打开日常界面
        :return:
        """
        self.click_in_template("yard_find_daily_panel_entrance")

    def select_daily_panel_daily(self):
        """
        选择日常界面中的日常标签
        :return:
        """
        self.click_in_template("daily_is_daily_panel_daily")

    def open_encounter_panel(self):
        """
        打开逢魔入口
        :return:
        """
        self.click_in_template("daily_is_daily_encounter_entrance")

    def click_daily_go_to_button(self):
        """
        点击"前往"按钮
        :return:
        """
        self.click_in_template("daily_is_daily_goto_button")
