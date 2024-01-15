from typing import List

import hiworker
from .RunTimer import RunTimer
from .play import *
from ..sender import signal_run_list
from ...models import CounterRecordModel


class PlanExecutor(hiworker.Thread):
    def __init__(self, plan_executor_data: dict):
        """
        套路调度线程
        :param plan_executor_data: 运行数据
        """
        super(PlanExecutor, self).__init__()
        self.play_input = PlayInput(plan_executor_data)
        self.run_id = self.play_input.run_list.id

        self.window_title = "[#] [" + self.play_input.run_env.name + "] 阴阳师-网易游戏 [#]"
        self.MPAY_LOGIN_title = "[#] [" + self.play_input.run_env.name + "] 登录 [#]"

        self.running_timer = RunTimer(self.run_id)  # 初始化时间记录
        self.need_init = True
        self.sleep_mode_on = False
        self.restart_interval = 0

        self.task_on_start = PlayGameOnStart(self.play_input)
        self.check_game_popup = CheckGamePopup(self.play_input)

        self.tasks: List[Common] = []
        self.load_task()
        self.init_tasks_record()
        self._counter_record = CounterRecordModel()

        self.sandboxie = hiworker.SandBox(self.play_input.app_setting.sandbox_path, self.play_input.app_setting.onmyoji_pc_path)
        self.sandboxie.set_handle_option(offset_x=self.play_input.app_setting.offset_x,
                                         offset_y=self.play_input.app_setting.offset_y)

    def run(self):
        self.stop_flag = False
        self.need_init = True
        self.restart_interval = 0
        self.running_timer.start()
        signal_run_list.clear_current_product.emit(self.run_id)
        signal_run_list.clear_current_operation.emit(self.run_id)
        signal_run_list.clear_current_scene.emit(self.run_id)
        # 计划运行中
        while not self.stop_flag:
            # 运行环境启动检测
            self.sandboxie.launch_sandbox(self.play_input.run_env.name, self.window_title)
            # 初始化
            if self.need_init:
                if self.task_on_start.is_finished:
                    self.need_init = False
                elif not self.task_on_start.stop_status:
                    self.task_on_start.start()
            # 初始化已完成
            else:
                # 启动悬赏封印检测
                if not self.check_game_popup.isRunning():
                    self.check_game_popup.start()
                # 执行任务
                self.run_task()
            time.sleep(0.5)
        # 计划已停止
        else:
            # 关闭所有子线程，清空单个玩法工人记录，处理运行环境的关闭留存
            while not self.check_all_tasks_stop():
                time.sleep(0.5)
            signal_run_list.set_current_operation.emit(self.run_id, "")
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.window_title, "当前计划已完成: ", self.play_input.plan.name)

    def run_task(self):
        if len(self.tasks) > 0:
            for index, task in enumerate(self.tasks):
                current_task_record_id, current_teammate_task_record_id = self.generate_task_record_id(task.product.id)
                # 检查是否是组队模式
                if task.play_input.run_list.teamup_mode in ["double_captain", "double_teammate"] and task.can_team_up:
                    # 检查组队模式下队友的任务记录状态
                    if task_record.get_record_finish_status(current_teammate_task_record_id):
                        # 队友已完成的时候，自己也同步完成
                        task_record.set_record_status(current_task_record_id, True)
                        task.stop()
                # 检查自己任务状态
                if task.stop_status or task.is_finished:
                    task_record.set_record_status(current_task_record_id, True)
                    if not task.isRunning():
                        self.tasks.pop(index)
                        break
                    else:
                        task.stop()

                elif not task.isRunning() and not task.stop_flag:
                    task.start()
                    break
        else:
            self.stop_flag = True

    def check_all_tasks_stop(self):
        if self.task_on_start.isRunning():
            self.task_on_start.stop()
            return False
        elif self.check_game_popup.isRunning():
            self.check_game_popup.stop()
            return False
        elif self.running_timer.isRunning():
            self.running_timer.stop()
            return False
        else:
            for task in self.tasks:
                if task.isRunning():
                    task.stop()
                    return False
            else:
                return True

    def load_task(self):
        for product in self.play_input.products:
            self.play_input.current_product = product
            match product.play_name:
                case "souls":
                    self.tasks.append(PlaySouls(self.play_input))
                case "evo_materials":
                    self.tasks.append(PlayEvoMaterials(self.play_input))
                case "chapter":
                    self.tasks.append(PlayChapter(self.play_input))
                case "totem":
                    self.tasks.append(PlayTotem(self.play_input))
                case "realm_raid":
                    self.tasks.append(PlayRealmRaid(self.play_input))
                case "yard":
                    self.tasks.append(PlayYard(self.play_input))
                case "summon":
                    self.tasks.append(PlaySummon(self.play_input))
                case "pet":
                    self.tasks.append(PlayPet(self.play_input))
                case "mall":
                    self.tasks.append(PlayMall(self.play_input))
                case "daily":
                    match product.play_name_second:
                        case "encounter":
                            pass
                        case "gymnasium":
                            pass
                        case "duel":
                            pass
                        case "draft_duel":
                            pass
                        case "royal_battle":
                            pass
                        case "boss_attack":
                            pass
                        case "boss_defense":
                            pass
                        case "netherworld_gate":
                            pass
                        case "guild_feast":
                            pass
                case "guild":
                    match product.play_name_second:
                        case "guild_contribute":
                            pass
                        case "guild_daily":
                            pass
                        case "guild_mall":
                            pass
                case "guild_realm":
                    match product.play_name_second:
                        case "guild_realm_card_setting":
                            pass
                        case "guild_realm_card_synthesis":
                            pass
                        case "guild_realm_foster":
                            pass
                        case "guild_realm_cultivate":
                            pass
                        case "guild_realm_collection":
                            pass

                case "shikigami":
                    self.tasks.append(PlayShikigami(self.play_input))
                case "area_boss":
                    self.tasks.append(PlayAreaBoss(self.play_input))
                case "real_orochi":
                    pass
                case "demon_parade":
                    self.tasks.append(PlayDemonParade(self.play_input))
                case "side_bet":
                    pass
                case "story":
                    self.tasks.append(PlayStory(self.play_input))

    def init_tasks_record(self):
        for index, task in enumerate(self.tasks):
            current_task_record_id, current_teammate_task_record_id = self.generate_task_record_id(task.product.id)
            # 队友已完成的时候，自己也同步完成
            task_record.set_record_status(current_task_record_id, False)

    def generate_task_record_id(self, product_id: int):
        """
        生成任务记录id
        :param product_id:
        :return:
        """
        current_day = time.localtime()
        task_record_id = "".join([
            str(current_day.tm_year),
            str(current_day.tm_mon),
            str(current_day.tm_mday),
            str(self.run_id),
            str(self.play_input.account.id),
            str(product_id)])
        teammate_task_record_id = "".join([
            str(current_day.tm_year),
            str(current_day.tm_mon),
            str(current_day.tm_mday),
            str(self.play_input.teammate.id),
            str(self.play_input.teammate_account.id),
            str(product_id)])

        if not task_record.is_record_exist(task_record_id):  # 执行记录项不存在, 新增记录项
            task_record.add_record_item(task_record_id)

        return task_record_id, teammate_task_record_id

    def generate_counter_record(self):
        current_day = time.localtime()
        record_id = "".join([
            str(current_day.tm_year),
            str(current_day.tm_mon),
            str(current_day.tm_mday),
            str(self.play_input.run_list.id),
            str(self.play_input.account.id)])
        if not self._counter_record.get_record_by_record_id(record_id):
            self._counter_record.add({"record_id": record_id})
