from PySide6.QtWidgets import QMenu
from PySide6 import QtGui


# 运行列表右键菜单
class RunListContextMenuView(QMenu):
    def __init__(self):
        super(RunListContextMenuView, self).__init__()
        # 开始执行
        self.start_run_list = self.addAction("开始执行")
        # 停止执行
        self.stop_run_list = self.addAction("停止执行")
        # 计划选择菜单
        self.separator_1 = self.addSeparator()
        self.set_plan = self.addAction("选择计划")
        self.separator_2 = self.addSeparator()
        # 窗口控制菜单
        self.tile_game_window_all_desktop = self.addAction("平铺窗口")
        self.sort_game_window_all_desktop = self.addAction("排列窗口")

        self.window_manage = self.addMenu("窗口管理")
        self.set_top_window = self.window_manage.addAction("置顶")
        self.go_to_desktop_has_run_item = self.window_manage.addAction("前往")
        self.separator_3 = self.addSeparator()
        # self.sort_game_window_current_desktop = self.window_manage.addAction("排列 [当前桌面]")
        # self.sort_game_window_all_desktop = self.window_manage.addAction("排列 [所有桌面]")
        # self.tile_game_window_current_desktop = self.window_manage.addAction("平铺 [当前桌面]")
        # self.tile_game_window_all_desktop = self.window_manage.addAction("平铺 [所有桌面]")
        self.separator_4 = self.addSeparator()
        self.move_to_current_desktop = self.window_manage.addAction("移至 [当前桌面]")
        self.set_left_top_window = self.window_manage.addAction("移至左上")

        self.separator_run_and_stop = self.addSeparator()

        # 新建运行列表
        self.add_list_item = self.addAction("新建列表")
        self.del_list_item = self.addAction("删除列表")
        self.separator_del = self.addSeparator()

        self.set_env = self.addAction("绑定机器")

        # 设置账号信息
        self.set_account_info = self.addAction("绑定客户")

        # 设置运行列表运行模式
        self.set_run_mode = self.addMenu("设置模式")
        self.set_run_mode_normal = self.set_run_mode.addAction("普通 [一般情况下使用该模式]")
        self.set_run_mode_scroll = self.set_run_mode.addAction("轮换 [计划完成后会关闭机器，然后启动其他列表]")
        self.set_run_mode_manual = self.set_run_mode.addAction("手动 [解除对游戏的控制]")

        # 队伍类型
        self.set_teamup_mode = self.addMenu("队伍类型")
        self.set_teamup_mode_solo = self.set_teamup_mode.addAction("单人，单刷")
        self.set_teamup_mode_double_captain = self.set_teamup_mode.addAction("双人，队长")
        self.set_teamup_mode_double_teammate = self.set_teamup_mode.addAction("双人，队员")
        self.set_teamup_mode_free_team_captain = self.set_teamup_mode.addAction("野队，队长")
        self.set_teamup_mode_free_team_teammate = self.set_teamup_mode.addAction("野队，队员")

        # 选择队友
        self.set_teammate = self.addAction("选择队员")

        self.separator_3 = self.addSeparator()

        # 雷电模拟器控制菜单
        self.emulator_control = self.addMenu("雷电控制")
        self.launch_emulator = self.emulator_control.addAction("启动雷电")
        self.close_emulator = self.emulator_control.addAction("关闭雷电")
        self.reboot_emulator = self.emulator_control.addAction("重启雷电")
        self.launch_emulator_game = self.emulator_control.addAction("启动游戏")
        self.close_emulator_game = self.emulator_control.addAction("关闭游戏")
        self.backup_authorize = self.emulator_control.addAction("备份授权")
        self.restore_authorize = self.emulator_control.addAction("还原授权")
        self.open_backup_restore_folder = self.emulator_control.addAction("打开备份目录")

        # 沙箱控制菜单
        self.sandbox_control = self.addMenu("沙箱控制")
        self.launch_sandbox = self.sandbox_control.addAction("启动沙箱")
        self.close_sandbox = self.sandbox_control.addAction("关闭沙箱")
