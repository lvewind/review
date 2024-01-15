import datetime
import time
from typing import List, Union

import hiworker
from .PlanExecutor import PlanExecutor
from ..sender import signal_run_list, signal_run_env


class SchedulerInput:
    def __init__(self, scheduler_data: dict):
        self.id = 0
        self.thread: Union[hiworker.Thread, None] = None
        self.start_flag = False
        self.start_time = 0
        self.sleep = False
        self.sleep_point = 0
        self.restart_interval = 0
        self.close_env = False
        self.run_mode = ""
        self.run_env_id = 0
        self.scroll_count = 0
        self.scroll_time = 0
        self.teamup_mode = 0
        self.teammate = {}
        self.timing_start = 0

        self.run_env = {}
        self.account = {}
        self.teammate = {}
        self.teammate_account = {}
        self.plan = {}
        self.products = []
        self.app_setting = {}

        self.plan_executor_data = {}

        self.set_data(scheduler_data)

    def set_data(self, scheduler_data: dict):
        for key, value in scheduler_data.items():
            setattr(self, key, value)

        self.close_env = self.plan.get("close_env")
        self.timing_start = self.plan.get("timing_start")
        self.scroll_count = self.app_setting.get("scroll_count")
        self.scroll_time = self.app_setting.get("scroll_time") * 60

        self.plan_executor_data = scheduler_data

    def set_start(self):
        self.start_flag = True
        self.sleep = False
        self.sleep_point = 0

    def set_stop(self):
        self.start_flag = False

    def set_sleep(self, restart_interval: int):
        self.sleep = True
        self.sleep_point = time.time()
        self.restart_interval = restart_interval


class RunScheduler(hiworker.Thread):
    def __init__(self):
        super(RunScheduler, self).__init__()

        self.scheduler_normal: List[SchedulerInput] = []  # 初始化普通模式列表
        self.scheduler_scroll: List[SchedulerInput] = []  # 初始化滚号模式列表

    def run(self):
        while not self.stop_status:
            stop_day = (2025, 12, 31, 0, 0, 0, 0, 0, 0)
            if time.time() < time.mktime(stop_day):
                self.process_scheduler_normal()
                self.process_scheduler_scroll()
                time.sleep(0.5)
            else:
                time.sleep(1)
                hiworker.signal_hi_worker.show_info.emit("此版本已过期, 请获取新版本")

    # 装载线程数据
    def load_scheduler_list(self, run_list_data: list):
        """
        装载调度列表
        :return:
        """
        for run_item in run_list_data:  # 遍历运行数据
            if run_item.get("run_mode", 0) == 1:  # 加入普通任务列表
                for normal_item in self.scheduler_normal:
                    # 项目已存在，更新执行数据
                    if normal_item.id == run_item.get("id"):
                        normal_item.set_data(run_item)
                        break
                else:
                    self.scheduler_normal.append(SchedulerInput(run_item))
            elif run_item.get("run_mode", 0) == 2:  # 加入滚号任务列表
                for scroll_item in self.scheduler_scroll:
                    if scroll_item.id == run_item.get("id"):
                        scroll_item.set_data(run_item)
                        break
                else:
                    self.scheduler_scroll.append(SchedulerInput(run_item))

    # 轮询控制线程状态
    def process_scheduler_normal(self):
        """
        处理普通任务
        :return:
        """
        # 遍历普通任务列表
        for index, scheduler_item in enumerate(self.scheduler_normal):  # 遍历任务列表项
            # 项目处于普通模式
            if scheduler_item.run_mode == 1:
                # 激活状态
                if scheduler_item.start_flag and not scheduler_item.sleep:
                    # 任务项线程为空，添加线程
                    if not scheduler_item.thread:
                        scheduler_item.thread = PlanExecutor(scheduler_item.plan_executor_data)
                        if not scheduler_item.timing_start:
                            scheduler_item.thread.start()
                        else:
                            scheduler_item.sleep = True
                            current_day = time.localtime()
                            scheduler_item.sleep_point = current_day.tm_hour * 3600 + current_day.tm_min * 60 + current_day.tm_sec
                            scheduler_item.restart_interval = scheduler_item.timing_start + (86400 - scheduler_item.sleep_point)
                    # 任务自己完成时，设置调度状态为False，避免重复开启
                    elif scheduler_item.thread.stop_flag:
                        if not scheduler_item.timing_start:
                            scheduler_item.start_flag = False
                        else:
                            scheduler_item.sleep = True
                            current_day = time.localtime()
                            scheduler_item.sleep_point = current_day.tm_hour * 3600 + current_day.tm_min * 60 + current_day.tm_sec
                            scheduler_item.restart_interval = scheduler_item.timing_start + (86400 - scheduler_item.sleep_point)
                    elif scheduler_item.thread.restart_interval:
                        scheduler_item.sleep = True
                        scheduler_item.restart_interval = scheduler_item.thread.restart_interval
                        scheduler_item.sleep_point = time.time()
                # 睡眠状态
                elif scheduler_item.start_flag and scheduler_item.sleep:
                    self.stop_item_scheduler_normal(scheduler_item)  # 停止运行项
                    # 达到恢复时间
                    if time.time() - scheduler_item.sleep_point > scheduler_item.restart_interval:
                        scheduler_item.sleep = False  # 停止睡眠状态
                        scheduler_item.sleep_point = 0  # 清空睡眠时间点
                        scheduler_item.thread.stop_flag = False
                        scheduler_item.thread.start()
                    # 未达到恢复时间
                    else:
                        restart_time = scheduler_item.restart_interval - int(time.time() - scheduler_item.sleep_point)
                        signal_run_list.set_current_operation.emit("等待自动恢复 [" + str(datetime.timedelta(seconds=restart_time)) + "]", scheduler_item.id)
                # 停止状态
                elif not scheduler_item.start_flag:
                    if self.remove_item_scheduler_normal(index, scheduler_item):
                        break
            # 项目处于其他模式
            else:
                if self.remove_item_scheduler_normal(index, scheduler_item):
                    break

    def process_scheduler_scroll(self):
        """
        处理滚号任务
        :return:
        """
        # 遍历滚号任务列表
        for index, scheduler_item in enumerate(self.scheduler_scroll):
            # 开始处理需要移除的选项
            # 滚号模式
            if scheduler_item.run_mode == 2:  # 运行项为滚号模式
                # 任务项在滚号范围内, 且处于开启状态
                if index < scheduler_item.scroll_count:
                    # 活动状态
                    if scheduler_item.start_flag and not scheduler_item.sleep:
                        # 线程不存在，创建新线程
                        if not scheduler_item.thread:
                            scheduler_item.thread = PlanExecutor(scheduler_item.plan_executor_data)
                            scheduler_item.start_time = time.time()
                            scheduler_item.sleep = False
                            scheduler_item.sleep_point = 0
                            scheduler_item.thread.start()
                        # 运行项线程已创建
                        elif scheduler_item.thread:
                            # 设置任务休眠
                            if int(time.time() - scheduler_item.start_time) > scheduler_item.scroll_time or scheduler_item.thread.stop_flag:
                                scheduler_item.sleep = True
                    # 休眠状态
                    elif scheduler_item.start_flag and scheduler_item.sleep:
                        # 停止睡眠
                        if time.time() - scheduler_item.sleep_point > scheduler_item.restart_interval:
                            scheduler_item.sleep = False
                            scheduler_item.sleep_point = 0
                            scheduler_item.thread.stop_flag = False
                            scheduler_item.start_time = time.time()
                            scheduler_item.thread.start()
                        # 睡眠中
                        else:
                            self.stop_item_scheduler_scroll(index, scheduler_item, move_to_last=True)
                            signal_run_list.set_current_operation.emit("线程已休眠")
                            break
                    # 停止状态
                    elif not scheduler_item.start_flag:  # 任务项start_flag为True
                        if self.remove_item_scheduler_scroll(index, scheduler_item):
                            break
                # 在滚号数之外
                elif index >= scheduler_item.scroll_count:
                    if scheduler_item.start_flag:
                        signal_run_list.set_current_operation.emit("排队中...", int(scheduler_item.id))
                    elif self.remove_item_scheduler_scroll(index, scheduler_item):
                        break
            # 其他模式
            else:
                self.remove_item_scheduler_scroll(index, scheduler_item)
                break

    # 设置线程状态
    def set_scheduler_start(self, run_data_list: list):
        self.load_scheduler_list(run_data_list)
        for run_data in run_data_list:
            # 在普通列表查找运行项
            for scheduler_item in self.scheduler_normal:
                if scheduler_item.id == run_data.get("id"):
                    scheduler_item.set_start()
                    break
            for scheduler_item in self.scheduler_scroll:
                if scheduler_item.id == run_data.get("id"):
                    scheduler_item.set_start()
                    break

    def set_scheduler_stop(self, run_list_ids: list):
        # 在普通列表查找运行项
        for run_id in run_list_ids:
            # 在普通列表查找运行项
            for scheduler_item in self.scheduler_normal:
                if scheduler_item.id == run_id:
                    scheduler_item.set_stop()
                    break
            for scheduler_item in self.scheduler_scroll:
                if scheduler_item.id == run_id:
                    scheduler_item.set_stop()
                    break

    def set_scheduler_sleep(self, run_data_list: list, restart_interval: int):
        # 在普通列表查找运行项
        for run_data in run_data_list:
            # 在普通列表查找运行项
            for scheduler_item in self.scheduler_normal:
                if scheduler_item.id == run_data.get("id"):
                    scheduler_item.set_sleep(restart_interval)
                    break
            for scheduler_item in self.scheduler_scroll:
                if scheduler_item.id == run_data.get("id"):
                    scheduler_item.set_sleep(restart_interval)
                    break

    # 停止线程
    @staticmethod
    def stop_item_scheduler_normal(scheduler_item: SchedulerInput):
        if scheduler_item.thread is not None:  # 运行项线程存在
            if scheduler_item.thread.isRunning():  # 未删除的线程正在运行
                scheduler_item.thread.stop()  # 执行停止
            else:  # 运行项线程已经关闭
                scheduler_item.thread = None  # 删除线程
            time.sleep(0.1)
            return False
        else:
            if scheduler_item.close_env:
                signal_run_env.close_env.emit([scheduler_item.id], scheduler_item.run_env_id)
            return True

    def stop_item_scheduler_scroll(self, index: int, scheduler_item: SchedulerInput, move_to_last=False):
        if scheduler_item.thread is not None:  # 运行项线程存在
            # 线程正在运行
            if scheduler_item.thread.isRunning():
                scheduler_item.thread.stop()
            else:
                # 未删除的线程已经关闭
                scheduler_item.thread = None  # 删除线程
            time.sleep(0.1)
            return False
        else:
            # 关闭游戏
            if scheduler_item.close_env:
                signal_run_env.close_env.emit([scheduler_item.id], scheduler_item.run_env_id)
            scheduler_item.start_time = 0  # 重置任务项开始时间
            scheduler_pop_item = self.scheduler_scroll.pop(index)  # 从列表删除并返回任务项
            if move_to_last:
                self.scheduler_scroll.append(scheduler_pop_item)  # 将返回的任务项重新追加到列表末尾
            return True

    # 移除线程项
    def remove_item_scheduler_normal(self, index: int, scheduler_item: SchedulerInput):
        """
        移除普通任务项
        :param scheduler_item:
        :param index:
        :return:
        """
        if self.stop_item_scheduler_normal(scheduler_item):
            del self.scheduler_normal[index]  # 移除运行项
            return True

    def remove_item_scheduler_scroll(self, index: int, scheduler_item: SchedulerInput):
        """
        移除滚号任务项
        :param index:
        :param scheduler_item:
        :return:
        """
        if self.stop_item_scheduler_scroll(index, scheduler_item):
            del self.scheduler_scroll[index]  # 移除运行项
            return True
