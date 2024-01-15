from hiworker import *


class OperateOnmyoji(Win32Click):
    def __init__(self):
        super(OperateOnmyoji, self).__init__()

    def close_onmyoji_panel(self):
        """
        关闭阴阳师面板
        :return:
        """
        self.click_in_template("yard_close_onmyoji_panel")
