from hiworker import *


class OperateShikigami(Win32Click):
    def __init__(self):
        super(OperateShikigami, self).__init__()

    def quit_shikigami_upgrade_panel(self):
        """
        退出式神升级面板
        :return:
        """
        self.click_in_template("shikigami_quit_shikigami_upgrade_panel")
