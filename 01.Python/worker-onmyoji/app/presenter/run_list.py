from threading import Thread

from PySide6.QtGui import QCursor

from app.presenter.data import table_setting, data_chs
from .account import AccountPresenter
from .data.image_coordinate import im_data, coord_data
from .plan import PlanPresenter
from .product import ProductPresenter
from .run_env import RunEnvPresenter
from .scheduler import RunScheduler
from .sender import signal_scheduler, signal_run_list, signal_counter_record
from ..models import *
from ..views import *
from ..views.menu import RunListContextMenuView


class RunListPresenter:

    def __init__(self):
        self.view_main = RunListView()
        self.view_set_teammate = RunListSetTeammateView()
        self.view_add = RunListAddView()
        self.view_set_env = RunListSetEnvView()
        self.view_set_env.col_setting = table_setting.sandbox_list
        self.view_set_account = RunListSetAccountView()
        self.view_set_plan = RunListSetPlanView()

        self.dialog_load_data = hiworker.DialogLoadData()
        self.dialog_info = hiworker.DialogInfo()

        self.menu = RunListContextMenuView()
        
        self._run_list = RunListModel()
        self._run_env = RunEnvModel()
        self._account = AccountModel()
        self._plan = PlanModel()
        self._counter_record = CounterRecordModel()
        self._app_setting = AppSettingModel()

        self.presenter_product = ProductPresenter()
        self.presenter_plan = PlanPresenter()
        self.presenter_account = AccountPresenter()
        self.presenter_run_env = RunEnvPresenter()

        self.last_move_to_desktop_menu_count = 0
        self.last_go_to_desktop_menu_count = 0

        self.bind_menu()
        self.bind_func_run_list()

        self.view_main.init_run_list_table_header(table_setting.run_list)
        self.view_main.init_run_count_table_header(table_setting.run_count)
        self.view_main.init_run_count_table(table_setting.run_count_row)

        self.view_add.buttonBox.accepted.connect(self.add_run_list)

        self.view_main.action_product.triggered.connect(self.presenter_product.show_main)
        self.view_main.action_plan.triggered.connect(self.presenter_plan.show_main)
        self.view_main.action_account.triggered.connect(self.presenter_account.show_main)
        self.view_main.action_run_env.triggered.connect(self.presenter_run_env.show_main)

        self.view_set_env.buttonBox.accepted.connect(self.set_env)
        self.view_set_account.buttonBox.accepted.connect(self.set_account)
        self.view_set_teammate.buttonBox.accepted.connect(self.set_teammate)
        self.view_set_plan.buttonBox.accepted.connect(self.set_plan)

        self.run_scheduler = RunScheduler()
        self.run_scheduler.start()
        signal_scheduler.set_scheduler_start.connect(self.run_scheduler.set_scheduler_start)
        self.load_table_run_list()

        signal_run_list.set_current_scene.connect(self.load_current_scene)
        signal_run_list.set_current_product.connect(self.load_current_product)
        signal_run_list.set_current_operation.connect(self.load_current_operation)

        signal_run_list.clear_current_product.connect(self.clear_current_product_name)
        signal_run_list.clear_current_scene.connect(self.clear_current_scene)
        signal_run_list.clear_current_operation.connect(self.clear_current_operation)

        signal_run_list.load_table_run_time.connect(self.load_table_run_time)
        signal_run_list.load_run_list_counter_item.connect(self.load_table_run_count_item)
        signal_counter_record.increase_record_item_value_by_record_id.connect(self._counter_record.increase_record_item_value_by_record_id)

    # 运行列表
    def bind_menu(self):
        self.menu.add_list_item.triggered.connect(self.view_add.show)
        self.menu.del_list_item.triggered.connect(self.delete_run_list)
        self.menu.set_env.triggered.connect(self.show_set_env)
        self.menu.set_account_info.triggered.connect(self.show_set_account)
        self.menu.set_teammate.triggered.connect(self.show_set_teammate)

        self.menu.start_run_list.triggered.connect(self.start_run_list)
        self.menu.stop_run_list.triggered.connect(self.stop_run_list)
        self.menu.set_run_mode_normal.triggered.connect(self.set_mode_normal)
        self.menu.set_run_mode_scroll.triggered.connect(self.set_mode_scroll)
        self.menu.set_run_mode_manual.triggered.connect(self.set_mode_manual)
        self.menu.backup_authorize.triggered.connect(self.backup_authorize)
        self.menu.restore_authorize.triggered.connect(self.restore_authorize)
        self.menu.open_backup_restore_folder.triggered.connect(self.open_backup_restore_folder)
        self.menu.launch_emulator.triggered.connect(self.launch_emulator_selected)
        self.menu.close_emulator.triggered.connect(self.close_emulator)
        self.menu.reboot_emulator.triggered.connect(self.reboot_emulator)
        self.menu.launch_emulator_game.triggered.connect(self.launch_emulator_game)
        self.menu.close_emulator_game.triggered.connect(self.close_emulator_game)
        self.menu.launch_sandbox.triggered.connect(self.launch_sandbox)
        self.menu.close_sandbox.triggered.connect(self.close_sandbox)
        self.menu.set_left_top_window.triggered.connect(self.set_left_top_window_selected)
        self.menu.move_to_current_desktop.triggered.connect(self.move_to_current_desktop_selected)

        self.menu.set_plan.triggered.connect(self.show_set_plan)

        self.menu.set_teamup_mode_solo.triggered.connect(self.set_teamup_mode_solo)
        self.menu.set_teamup_mode_double_captain.triggered.connect(self.set_teamup_mode_double_captain)
        self.menu.set_teamup_mode_double_teammate.triggered.connect(self.set_teamup_mode_double_teammate)
        self.menu.set_teamup_mode_free_team_captain.triggered.connect(self.set_teamup_mode_free_team_captain)
        self.menu.set_teamup_mode_free_team_teammate.triggered.connect(self.set_teamup_mode_free_team_teammate)

        self.menu.go_to_desktop_has_run_item.triggered.connect(self.go_to_desktop_has_run_item)
        self.menu.set_top_window.triggered.connect(self.set_top_window)
        self.menu.sort_game_window_all_desktop.triggered.connect(self.sort_game_window_all_desktop)
        self.menu.tile_game_window_all_desktop.triggered.connect(self.tile_game_window_all_desktop)
        
    def bind_func_run_list(self):
        """
        绑定信号槽函数
        :return:
        """
        self.view_main.tableWidget_run_list.clicked.connect(self.load_table_run_count)
        self.view_main.tableWidget_run_list.customContextMenuRequested.connect(self.show_menu_run_list)
        
    def show_menu_run_list(self):
        self.generate_move_to_desktop_menu()
        self.generate_go_to_desktop_menu()
        self.menu.popup(QCursor.pos())

    def show_main_window(self):
        self.view_main.show()
        Thread(target=hiworker.load_data, args=(im_data, coord_data, False)).start()

    # 加载表格数据
    def load_table_run_list(self):
        """
        加载运行列表
        :return:
        """
        data_list_to_show = []
        data_list = self._run_list.get_all_data()
        for data in data_list:
            data_to_show = {}
            env_data = self._run_env.get_name(data.get("run_env_id"))

            account_data = self._account.get_dict_by_id(data.get("account_id"))
            if account_data:
                account_data = account_data.get("name") + ',' + account_data.get("platform")
            else:
                account_data = ""
            run_mode = data_chs.run_mode.get(str(data.get("run_mode")))
            teamup_mode = data_chs.teamup_mode.get(data.get("teamup_mode"))

            teammate = ""
            teammate_run_id = data.get("teammate_id")
            if teammate_run_id:
                teammate_account_id = self._run_list.get_account_id(teammate_run_id)
                teammate_account = self._account.get_name(teammate_account_id)
                teammate_type = data_chs.teammate_type.get(str(data.get("teammate_type")), "默认")
                teammate = teammate_account + ", " + str(teammate_run_id) + ", " + str(teammate_type)

            plan_data = ""
            plan_id = data.get("plan_id")
            if plan_id:
                plan_data = self._plan.get_name(plan_id)

            run_time = data.get("run_time")
            data_to_show.update(
                {
                    "id": data.get("id"),
                    "env_name": env_data,
                    "account": account_data,
                    "run_mode": run_mode,
                    "teamup_mode": teamup_mode,
                    "teammate": teammate,
                    "plan": plan_data,
                    "run_time": run_time
                }
            )
            data_list_to_show.append(data_to_show)
        self.view_main.load_table_run_list(data_list_to_show, table_setting.run_list)

    def load_table_run_time(self, run_id: int, run_time: int):
        self.view_main.load_run_list_run_time(run_id, str(run_time), table_setting.run_list)

    def load_current_scene(self, run_id: int, text: str):
        self.view_main.load_run_list_item_not_save(run_id, text, "current_scene", table_setting.run_list)

    def load_current_product(self, run_id: int, text: str):
        self.view_main.load_run_list_item_not_save(run_id, text, "current_product", table_setting.run_list)

    def load_current_operation(self, run_id: int, text: str):
        self.view_main.load_run_list_item_not_save(run_id, text, "current_operation", table_setting.run_list)

    def load_run_list_item_not_save(self, run_id, text, col_name: str):
        row_count = self.view_main.tableWidget_run_list.rowCount()
        for row in range(row_count):  # 获取对应ID的行号
            row_id = int(self.view_main.tableWidget_run_list.item(row, 0).text())
            if int(run_id) == int(row_id):
                col_setting = table_setting.run_list.get(col_name)
                col = col_setting.get("col")
                hiworker.TableLoad.set_table_cell(self.view_main.tableWidget_run_list, text, row, col)
                break

    def load_table_run_count(self):
        run_id = hiworker.TableRead.get_current_data_id(self.view_main.tableWidget_run_list)
        if run_id:
            _run_list = self._run_list.get_dict_by_id(run_id)
            current_day = time.localtime()
            record_id = "".join([
                str(current_day.tm_year),
                str(current_day.tm_mon),
                str(current_day.tm_mday),
                str(run_id),
                str(_run_list.get("account_id"))])
            data_dict = self._counter_record.get_record_by_record_id(record_id)
            self.view_main.load_table_run_count_item(data_dict, table_setting.run_count_row)

    def load_table_run_count_item(self, run_id, row_name):
        if run_id == hiworker.TableRead.get_current_data_id(self.view_main.tableWidget_run_list):
            _run_list = self._run_list.get_dict_by_id(run_id)
            current_day = time.localtime()
            record_id = "".join([
                str(current_day.tm_year),
                str(current_day.tm_mon),
                str(current_day.tm_mday),
                str(run_id),
                str(_run_list.get("account_id"))])
            data_dict = self._counter_record.get_record_by_record_id(record_id)
            self.view_main.load_table_run_count_item(data_dict, table_setting.run_count_row)

    def display_current_product_name(self, run_id, text):
        self.load_run_list_item_not_save(run_id, text, "current_product")

    def display_current_scene(self, run_id, text):
        self.load_run_list_item_not_save(run_id, text, "current_scene")

    def display_current_operation(self, run_id, text):
        self.load_run_list_item_not_save(run_id, text, "current_operation")

    def clear_current_product_name(self, run_id):
        self.load_run_list_item_not_save(run_id, "", "current_product")

    def clear_current_scene(self, run_id):
        self.load_run_list_item_not_save(run_id, "", "current_scene")

    def clear_current_operation(self, run_id):
        self.load_run_list_item_not_save(run_id, "", "current_operation")

    # 新增运行列表
    def add_run_list(self):
        count = self.view_add.spinBoxadd_new_count.value()
        for c in range(count):
            self._run_list.add()
        self.load_table_run_list()

    # 删除运行列表
    def delete_run_list(self):
        instance_ids = self.view_main.get_selected_ids()
        if instance_ids:
            for instance_id in instance_ids:
                self._run_list.delete(instance_id)
        self.load_table_run_list()
    
    # 开始执行
    def start_run_list(self):
        run_id_list = self.view_main.get_selected_ids()
        if run_id_list:
            run_data_list = []
            for run_id in run_id_list:
                run_data = self._run_list.get_dict_by_id(run_id)
                executor_plan = self._plan.get_dict_by_id(run_data.get("plan_id"))
                teammate = self._run_list.get_dict_by_id(run_data.get("teammate_id"))
                executor_data = {
                        "run_env": self._run_env.get_dict_by_id(run_data.get("run_env_id")),
                        "account": self._account.get_dict_by_id(run_data.get("account_id")),
                        "teammate": teammate,
                        "teammate_account": self._account.get_dict_by_id(teammate.get("account_id")),
                        "plan": executor_plan,
                        "products": self._plan.get_products(run_data.get("plan_id")),
                        "app_setting": self._app_setting.get_all_options()
                    }
                # 遍历运行数据，若有空值则不加入运行数据
                for key, value in executor_data.items():
                    if not value:
                        break
                else:
                    run_data.update(executor_data)
                if run_data.get("teamup_mode") == 21:
                    teammate = executor_data.get("teammate")
                    if not (teammate.get("teamup_mode")) == 22:
                        continue
                elif run_data.get("teamup_mode") == 22:
                    teammate = executor_data.get("teammate")
                    if not (teammate.get("teamup_mode") == 21):
                        continue

                run_data_list.append(run_data)
            # 使用信号触发任务列表加载和开启状态，避免列表并发问题
            signal_scheduler.set_scheduler_start.emit(run_data_list)

    # 停止执行
    def stop_run_list(self):
        run_id_list = self.view_main.get_selected_ids()
        self.run_scheduler.set_scheduler_stop(run_id_list)

    # 设置运行环境
    def show_set_env(self):
        instance_id = self.view_main.get_selected_id()
        if instance_id:
            data = self._run_list.get_dict_by_id(instance_id)
            env_list = self._run_env.get_all_data()
            for env in env_list:
                if env.get("env_type") == 1:
                    env.update({"env_type": "沙箱"})
                elif env.get("env_type") == 2:
                    env.update({"env_type": "模拟器"})
            self.view_set_env.show_edit(data, env_list, table_setting.set_env)

    def set_env(self):
        data = self.view_set_env.data
        self._run_list.update(data)
        self.load_table_run_list()
            
    # 设置账户
    def show_set_account(self):
        instance_id = self.view_main.get_selected_id()
        if instance_id:
            data = self._run_list.get_dict_by_id(instance_id)
            account_data = self._account.get_all_data()
            self.view_set_account.show_edit(data, account_data, table_setting.account_)

    def set_account(self):
        data = self.view_set_account.data
        self._run_list.update(data)
        self.load_table_run_list()

    # 设置运行模式
    def set_mode_normal(self):
        run_list_ids = self.view_main.get_selected_ids()
        self.set_mode(run_list_ids, 1)

    def set_mode_scroll(self):
        run_list_ids = self.view_main.get_selected_ids()
        self.set_mode(run_list_ids, 2)

    def set_mode_manual(self):
        run_list_ids = self.view_main.get_selected_ids()
        self.set_mode(run_list_ids, 3)

    def set_mode(self, run_list_ids: list, mode):
        for run_list_id in run_list_ids:
            data = {"id": run_list_id, "run_mode": mode}
            self._run_list.update(data)
        self.load_table_run_list()

    # 设置组队模式
    def set_teamup_mode_solo(self):
        self.set_teamup_mode(self.view_main.get_selected_ids(), "single_solo")

    def set_teamup_mode_double_captain(self):
        self.set_teamup_mode(self.view_main.get_selected_ids(), "double_captain")

    def set_teamup_mode_double_teammate(self):
        self.set_teamup_mode(self.view_main.get_selected_ids(), "double_teammate")

    def set_teamup_mode_free_team_captain(self):
        self.set_teamup_mode(self.view_main.get_selected_ids(), "free_captain")

    def set_teamup_mode_free_team_teammate(self):
        self.set_teamup_mode(self.view_main.get_selected_ids(), "free_teammate")

    def set_teamup_mode(self, run_list_ids: list, mode):
        for run_list_id in run_list_ids:
            data = {"id": run_list_id, "teamup_mode": mode}
            self._run_list.update(data)
        self.load_table_run_list()
    
    # 设置队友
    def show_set_teammate(self):
        run_id = self.view_main.get_selected_id()
        if run_id:
            data = self._run_list.get_dict_by_id(run_id)
            data_all = self._run_list.get_all_data()
            data_to_show = []
            for d_s in data_all:
                data_to_show.append({
                    "run_id": d_s.get("id"),
                    "account_id": d_s.get("account_id"),
                    "account_name": self._account.get_name(d_s.get("account_id"))
                })
            self.view_set_teammate.show_edit(data, data_to_show, table_setting.teammate_list)

    def set_teammate(self):
        self._run_list.update(self.view_set_teammate.data)
        self.load_table_run_list()
    
    # 设置计划
    def show_set_plan(self):
        run_list_ids = self.view_main.get_selected_ids()
        run_list_data = []
        for run_list_id in run_list_ids:
            run_list_data.append(self._run_list.get_dict_by_id(run_list_id))
        plan_data = self._plan.get_all_data()
        self.view_set_plan.show_edit(run_list_data, plan_data, table_setting.run_list_set_plan)

    def set_plan(self):
        for data in self.view_set_plan.data:
            self._run_list.update(data)
        self.load_table_run_list()

    # 生成虚拟桌面菜单
    def generate_move_to_desktop_menu(self):
        desktop_count = hiworker.win32_window.get_last_desktop_count()
        if self.last_move_to_desktop_menu_count < desktop_count:
            menu_count = self.last_move_to_desktop_menu_count
            for desktop in range(menu_count + 1, desktop_count + 1):
                self.last_move_to_desktop_menu_count += 1
                self.generate_move_to_desktop_action(desktop)

    def generate_move_to_desktop_action(self, desktop):
        move_to_desktop = self.menu.window_manage.addAction("移至桌面" + str(desktop))
        move_to_desktop.triggered.connect(lambda: self.move_to_desktop_selected(desktop))

    def generate_go_to_desktop_menu(self):
        desktop_count = hiworker.win32_window.get_last_desktop_count()
        if self.last_go_to_desktop_menu_count < desktop_count:
            menu_count = self.last_go_to_desktop_menu_count
            for desktop in range(menu_count + 1, desktop_count + 1):
                self.last_go_to_desktop_menu_count += 1
                self.generate_go_to_desktop_action(desktop)

    def generate_go_to_desktop_action(self, desktop):
        go_to_desktop = self.menu.window_manage.addAction("前往桌面" + str(desktop))
        go_to_desktop.triggered.connect(lambda: hiworker.win32_window.go_to_desktop(desktop))

    # 置顶窗口
    def set_top_window(self):
        run_id_list = hiworker.TableRead.get_selected_data_ids(self.view_main.tableWidget_run_list)
        for run_id in run_id_list:
            window_title = self.get_window_title_list([run_id])[0]
            hiworker.win32_window.set_window_top(window_title)

    # 前往运行项所在的窗口
    def go_to_desktop_has_run_item(self):
        run_id = hiworker.TableRead.get_current_data_id(self.view_main.tableWidget_run_list)
        window_title = self.get_window_title_list([run_id])[0]
        hiworker.win32_window.go_to_desktop_with_window(window_title)

    # 备份安卓授权
    def backup_authorize(self):
        selected_rows = self.view_main.get_selected_ids()
        if selected_rows:
            run_id_list = []
            for row in selected_rows:
                run_id = self.view_main.tableWidget_run_list.item(row, 0).text()
                run_id_list.append(int(run_id))
            Thread(self.presenter_run_env.backup_restore.backup_app_data, args=(run_id_list,)).start()

    # 还原安卓授权数据
    def restore_authorize(self):
        selected_rows = self.view_main.get_selected_ids()
        if selected_rows:
            run_id_list = []
            for row in selected_rows:
                run_id = self.view_main.tableWidget_run_list.item(row, 0).text()
                run_id_list.append(int(run_id))
            Thread(self.presenter_run_env.backup_restore.restore_app_data, args=(run_id_list,)).start()

    def open_backup_restore_folder(self):
        pass

    def get_env_id_list_from_run_list(self, env_type: int):
        run_list_ids = self.view_main.get_selected_ids()
        env_id_list = []
        for run_list_id in run_list_ids:
            env = self._run_env.get_dict_by_id(self._run_list.get_env_id(int(run_list_id)))
            if env.get("env_type") == env_type:
                env_id = self._run_list.get_env_id(int(run_list_id))
                env_id_list.append(int(env_id))
        return env_id_list

    def launch_emulator_selected(self):
        launch_list = self.get_env_id_list_from_run_list(2)
        self.launch_emulator(launch_list)

    def launch_emulator(self, launch_list):
        self.presenter_run_env.emulator.set_launch_option(launch_list, launch_with_app=False)
        self.presenter_run_env.emulator.start()

    def close_emulator(self):
        launch_list = self.get_env_id_list_from_run_list(2)
        self.presenter_run_env.emulator.close_emulator_multiple(launch_list)

    def reboot_emulator(self):
        launch_list = self.get_env_id_list_from_run_list(2)
        self.presenter_run_env.emulator.reboot_emulator_multiple(launch_list)

    def launch_emulator_game(self):
        launch_list = self.get_env_id_list_from_run_list(2)
        self.presenter_run_env.emulator.start_emulator_game_multiple(launch_list)

    def close_emulator_game(self):
        launch_list = self.get_env_id_list_from_run_list(2)
        self.presenter_run_env.emulator.close_emulator_multiple(launch_list)

    def launch_sandbox(self):
        sandbox_id_list = self.get_env_id_list_from_run_list(1)
        self.presenter_run_env.launch_sandbox(sandbox_id_list)

    def close_sandbox(self):
        sandbox_id_list = self.get_env_id_list_from_run_list(1)
        self.presenter_run_env.close_sandbox(sandbox_id_list)

    # 游戏窗口控制
    def set_left_top_window_selected(self):
        run_id_list = self.view_main.get_selected_ids()
        window_title_list = self.get_window_title_list(run_id_list)
        hiworker.win32_window.set_window_left_top(window_title_list)

    def move_to_current_desktop_selected(self):
        run_id_list = self.view_main.get_selected_ids()
        window_title_list = self.get_window_title_list(run_id_list)
        hiworker.win32_window.move_window_to_desktop(window_title_list, 0)

    def move_to_desktop_selected(self, desktop: int):
        run_id_list = self.view_main.get_selected_ids()
        window_title_list = self.get_window_title_list(run_id_list)
        hiworker.win32_window.move_window_to_desktop(window_title_list, desktop)

    def sort_game_window_current_desktop(self):
        active_title_list = self.get_all_title_list()
        hiworker.win32_window.sort_window_on_own_desktop(active_title_list,
                                                         offset_x=self._app_setting.read_option("offset_x"),
                                                         offset_y=self._app_setting.read_option("offset_y")
                                                         )

    def sort_game_window_all_desktop(self):
        title_list = self.get_all_title_list()
        hiworker.win32_window.sort_window_on_own_desktop(title_list,
                                                         offset_x=self._app_setting.read_option("offset_x"),
                                                         offset_y=self._app_setting.read_option("offset_y")
                                                         )

    def tile_game_window_current_desktop(self):
        title_list = self.get_all_title_list()
        hiworker.win32_window.tile_window_on_own_desktop(title_list,
                                                         offset_x=self._app_setting.read_option("offset_x"),
                                                         offset_y=self._app_setting.read_option("offset_y")
                                                         )

    def tile_game_window_all_desktop(self):
        title_list = self.get_all_title_list()
        hiworker.win32_window.tile_window_on_own_desktop(title_list,
                                                         offset_x=self._app_setting.read_option("offset_x"),
                                                         offset_y=self._app_setting.read_option("offset_y")
                                                         )

    def get_all_title_list(self):
        title_list = []
        data_all = self._run_env.get_all_data()
        for data in data_all:
            if data.get("env_type") == 1:
                sandbox_title = "[#] [" + data.get("name") + "] 阴阳师-网易游戏 [#]"
                title_list.append({"title": sandbox_title, "env_type": 1})
            elif data.get("env_type") == 2:
                title_list.append({"title": data.get("name"), "env_type": 2})
        return title_list

    def get_window_title_list(self, run_id_list):
        window_title_list = []
        for run_id in run_id_list:
            env_id = self._run_list.get_env_id(run_id)
            env_type = self._run_env.get_env_type(run_id)
            env_name = self._run_env.get_name(env_id)
            if env_type == 1:
                sandbox_title = "[#] [" + env_name + "] 阴阳师-网易游戏 [#]"
                window_title_list.append(sandbox_title)
            elif env_type == 2:
                window_title_list.append(env_name)

        return window_title_list
