# -*- coding: UTF-8 -*-
"""
模拟器控制模块
"""
from functools import wraps
import subprocess
import time
import psutil
import re
import copy
import os

from ..thread import Thread
from ..signal.signal import signal_hi_worker


def check_ldconsole_path(func):
    @wraps(func)
    def wrapper(self, *args, **kargs):
        if isinstance(self, Emulator):
            emulator_path = self.dnplayer_path
            # 模拟器路径不为空
            if emulator_path:
                ldconsole_path = emulator_path.strip("dnplayer.exe") + "ldconsole.exe"
                # 模拟器路径有效
                if os.path.exists(ldconsole_path):
                    # print("ldconsole_path is ok: ", ldconsole_path)
                    self.ldconsole_path = ldconsole_path
                    return func(*args, **kargs)
                else:
                    signal_hi_worker.show_info.emit("ldconsole路径无效，请重设置模拟器路径")
            else:
                signal_hi_worker.show_info.emit("dnplayer.exe为空，请设置模拟器路径")
        else:
            signal_hi_worker.show_info.emit("程序内部错误")

    return wrapper


class Emulator(Thread):
    def __init__(self, dnplayer_path: str, package_name=""):
        super(Emulator, self).__init__()
        self.dnplayer_path = dnplayer_path
        self.ldconsole_path = dnplayer_path.strip("dnplayer.exe") + "ldconsole.exe"
        self.package_name = package_name
        self.launch_ids = []
        self.launch_by_name = False
        self.launch_with_app = True

    def run(self) -> None:
        """
        以多线程方式启动模拟器
        :return:
        """
        for launch_id in self.launch_ids:
            if not self.launch_by_name:
                if not self.launch_with_app:
                    self.launch_emulator_by_id(launch_id)
                else:
                    self.launchex_emulator_by_id(launch_id)
            else:
                if not self.launch_with_app:
                    self.launch_emulator_by_name(launch_id)
                else:
                    self.launchex_emulator_by_name(launch_id)
            time.sleep(3)
        self.launch_ids = []

    def set_launch_option(self, launch_ids: list, launch_by_name=False, launch_with_app=True):
        """
        模拟器启动选项设置
        :param launch_ids: 启动列表
        :param launch_by_name: 是否通过名称启动
        :param launch_with_app: 是否再启动后执行APP
        :return:
        """
        self.launch_ids = copy.deepcopy(launch_ids)
        self.launch_by_name = launch_by_name
        self.launch_with_app = launch_with_app

    def set_dnplayer_path(self, dnplayer_path: str, package_name=None):
        """
        模拟器路径设置
        :param dnplayer_path:
        :param package_name:
        :return:
        """
        self.dnplayer_path = dnplayer_path
        self.ldconsole_path = dnplayer_path.strip("dnplayer.exe") + "ldconsole.exe"
        if package_name:
            self.package_name = package_name

    @check_ldconsole_path
    def create_emulator(self, current_create: int):
        """
        创建模拟器
        :param current_create:
        :return:
        """
        current_em_id_list = self._list_emulator(only_id=True)  # 获取模拟器ID列表
        current_em_id_list.sort(reverse=True)
        last_em_id = current_em_id_list[0]  # 获取最后一个模拟器ID
        new_em_name = "模拟器-" + str(last_em_id + current_create)  # 设置新模拟器名称
        pid = self.copy_emulator(new_em_name)  # copy模拟器，并返回pid
        if pid:
            if psutil.pid_exists(pid):
                p = psutil.Process(pid)  # 获取pid进程
                time_start = time.time()
                while p.is_running():  # 进程状态存在，尝试读取磁盘操作速度
                    try:
                        speed = p.io_counters()[3]
                        time.sleep(1)
                        time_used = time.time() - time_start
                        speed = ((int(speed) / 1024) / 1024) / time_used
                        speed = str(int(speed)) + " MB/s"
                        signal_hi_worker.refresh_disk_speed.emit(speed)
                    except psutil.NoSuchProcess:
                        print("对应PID的复制进程已结束")
                        self.modify_options_all_by_id()
                        time.sleep(1)
                        break

    def create_first_emulator(self):
        """
        创建模拟器母盘
        :return:
        """
        pid = self.add_emulator("模拟器-母盘")
        if pid:
            if psutil.pid_exists(pid):
                p = psutil.Process(pid)
                while p.is_running():
                    time.sleep(1)

    def remove_emulator(self, em_id):
        """
        删除模拟器
        :param em_id: 要删除的模拟器ID
        :return: None
        """
        pid = self.remove_emulator_by_id(int(em_id))  # 删除模拟器，并返回pid
        if pid:
            if psutil.pid_exists(pid):
                p = psutil.Process(pid)  # 获取pid进程
                while p.is_running():  # 进程状态存在，尝试读取磁盘操作速度
                    time.sleep(1)

    @check_ldconsole_path
    def close_emulator_multiple(self, em_id_list: list):
        """
        批量关闭模拟器
        :param em_id_list: 需要关闭的模拟器ID列表
        :return: None
        """
        for em_id in em_id_list:
            self.quit_emulator_by_id(em_id)

    @check_ldconsole_path
    def reboot_emulator_multiple(self, em_id_list: list):
        """
        批量重启模拟器
        :param em_id_list: 需要重启的模拟器ID列表
        :return:
        """
        for em_id in em_id_list:
            self.reboot_emulator_by_id(em_id)

    @check_ldconsole_path
    def start_emulator_game_multiple(self, em_id_list: list):
        """
        批量启动模拟器的app
        :param em_id_list: 模拟器ID列表
        :return:
        """
        for em_id in em_id_list:
            self.run_app_by_id(em_id)

    @check_ldconsole_path
    def close_emulator_game_multiple(self, em_id_list: list):
        """
        批量关闭模拟器的app
        :param em_id_list: 模拟器ID列表
        :return:
        """
        for em_id in em_id_list:
            self.kill_app_by_id(em_id, "com.tencent.tmgp.bydr3dx")

    @check_ldconsole_path
    def launch_emulator_by_name(self, emulator_name: str):
        """
        通过名称启动模拟器
        :param emulator_name: 模拟器名称
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "launch", "--name", emulator_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @check_ldconsole_path
    def launch_emulator_by_id(self, emulator_id):
        """
        通过ID启动模拟器
        :param emulator_id: 模拟器ID
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "launch", "--index", str(emulator_id)])

    @check_ldconsole_path
    def launchex_emulator_by_name(self, emulator_name: str, package_name: str):
        """
        通过名称启动模拟器并运行指定APP
        :param emulator_name: 模拟器名称
        :param package_name: APP包名
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "launchex", "--name", emulator_name, "--package_name", package_name])

    @check_ldconsole_path
    def launchex_emulator_by_id(self, emulator_id: int, package_name: str):
        """
        通过ID启动模拟器并运行指定APP
        :param emulator_id: 模拟器ID
        :param package_name: APP包名
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "launchex", "--index", str(emulator_id), "--package_name", package_name])

    @check_ldconsole_path
    def quit_emulator_by_name(self, emulator_name: str):
        """
        # 退出模拟器
        :param emulator_name: 模拟器名称
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "quit", "--name", emulator_name])

    @check_ldconsole_path
    def quit_emulator_by_id(self, emulator_id: int):
        """
        # 退出模拟器
        :param emulator_id: 模拟器ID
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "quit", "--index", str(emulator_id)])

    @check_ldconsole_path
    def quit_all_emulator(self):
        """
        # 退出所有模拟器
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "quitall"])

    @check_ldconsole_path
    def reboot_emulator_by_name(self, emulator_name: str):
        """
        # 重启模拟器
        :param emulator_name: 模拟器名称
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "reboot", "--name", emulator_name])

    @check_ldconsole_path
    def reboot_emulator_by_id(self, emulator_id: int):
        """
        # 重启模拟器
        :param emulator_id: 模拟器ID
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "reboot", "--index", str(emulator_id)])

    @check_ldconsole_path
    def backup_emulator_by_name(self, emulator_name: str, output_filepath: str):
        """
        # 备份模拟器
        :param emulator_name: 模拟器名称
        :param output_filepath: 备份路径
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "backup", "--name", emulator_name, "--file", output_filepath])

    @check_ldconsole_path
    def restore_emulator_by_name(self, emulator_name: str, input_filepath: str):
        """
        # 备份模拟器
        :param emulator_name: 模拟器名称
        :param input_filepath: 备份路径
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "restore", "--name", emulator_name, "--file", input_filepath])

    @check_ldconsole_path
    def rename_emulator_by_id(self, emulator_index: int, emulator_new_name: str):
        """
        # 更名模拟器
        :param emulator_index: 模拟器ID
        :param emulator_new_name: 新名称
        :return:
        """
        rename_emulator = subprocess.Popen([self.ldconsole_path, "rename",
                                            "--index", str(emulator_index),
                                            "--title", emulator_new_name])
        rename_emulator.wait()

    @check_ldconsole_path
    def rename_emulator_all(self):
        emulator_id_list = self._list_emulator(only_id=True)
        if emulator_id_list:
            for em_id in emulator_id_list:
                if em_id > 0:
                    em_name = "模拟器-" + str(em_id)
                    self.rename_emulator_by_id(em_id, em_name)

    @check_ldconsole_path
    def add_emulator(self, new_emulator_name):
        """
        新增单个模拟器
        :param new_emulator_name: 模拟器名称
        :return:
        """
        creating_em = subprocess.Popen([self.ldconsole_path, "add",
                                        "--name", new_emulator_name],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return creating_em.pid

    @check_ldconsole_path
    def copy_emulator(self, new_em_name: str):
        """
        复制模拟器
        :param new_em_name: 模拟器名称
        :return:
        """
        creating_em = subprocess.Popen([self.ldconsole_path, "copy",
                                        "--name", new_em_name,
                                        "--from", "0"],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return creating_em.pid

    @check_ldconsole_path
    def remove_emulator_by_name(self, emulator_name: str):
        """
         # 删除模拟器
        :param emulator_name: 模拟器名称
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "remove", "--name", emulator_name])

    @check_ldconsole_path
    def remove_emulator_by_id(self, emulator_index: int):
        """
         # 删除模拟器
        :param emulator_index: 模拟器ID
        :return:
        """
        remove_em = subprocess.Popen([self.ldconsole_path, "remove", "--index", str(emulator_index)],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return remove_em.pid

    @check_ldconsole_path
    def list_emulator(self, only_id=False):
        return self._list_emulator(only_id=only_id)

    def _list_emulator(self, only_id=False):
        """
        列出当前系统中的模拟器
        :param only_id:  是否只列出模拟器ID
        :return: 模拟器列表
        """
        emulator_list = []
        dnconsole_list2 = subprocess.Popen([self.ldconsole_path, "list2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_text, err = dnconsole_list2.communicate()
        for line in out_text.splitlines():
            out_text_sub = line.decode("GBK").split(",")
            if int(out_text_sub[0]):
                if only_id:
                    emulator_list.append(int(out_text_sub[0]))
                else:
                    emulator_list.append({"em_id": int(out_text_sub[0]), "name": out_text_sub[1], "status": int(out_text_sub[4])})
        return emulator_list

    @check_ldconsole_path
    def is_emulator_exist(self, emulator_index: int):
        """
        判断某个模拟器是否已经处在
        :param emulator_index:  模拟器ID
        :return: bool 存在返回True
        """
        dnconsole_list2 = subprocess.Popen([self.ldconsole_path, "list2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_text, err = dnconsole_list2.communicate()
        for line in out_text.splitlines():
            out_text_sub = line.decode("GBK").split(",")
            if int(out_text_sub[0]) == emulator_index:
                return True
        else:
            return False

    @check_ldconsole_path
    def get_emulator_status_by_id(self, run_id: int):
        """
        获取模拟器运行状态
        :param run_id:
        :return:
        """
        emulator_list = self._list_emulator()
        if emulator_list:
            for em_dict in emulator_list:
                if em_dict.get("id") == run_id:
                    return em_dict.get("status")
            else:
                print("failed")
                return False

    @check_ldconsole_path
    def shake_emulator_by_name(self, emulator_name):
        """
        # 模拟震动
        :param emulator_name: 模拟器名称
        :return:
        """

        subprocess.Popen([self.ldconsole_path, "action", "--name", emulator_name, "--key", "call.shake", "--value", "null"])

    @check_ldconsole_path
    def set_emulator_cpu_by_name(self, emulator_name, percentage: int):
        """
        # 设置模拟器CPU使用率
        :param emulator_name: 模拟器名称
        :param percentage: CPU百分比
        :return:
        """

        subprocess.Popen([self.ldconsole_path, "downcpu", "--name", emulator_name, "--rate", percentage])

    @check_ldconsole_path
    def get_emulator_prop_by_name(self, emulator_name: str, key: str):
        """
         # 获取模拟器属性
        :param emulator_name: 模拟器名称
        :param key: 属性名
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "getprop",
                          "--name", emulator_name,
                          "--key", key],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @check_ldconsole_path
    def get_emulator_prop_by_id(self, emulator_index: int, key: str):
        """
         # 获取模拟器属性
        :param emulator_index: 模拟器ID
        :param key: 属性名
        :return:
                """
        subprocess.Popen([self.ldconsole_path, "getprop",
                          "--index", str(emulator_index),
                          "--key", key],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @check_ldconsole_path
    def set_emulator_prop_by_name(self, emulator_name: str, key: str, value: str):
        """
        # 设置模拟器属性
        :param emulator_name:
        :param key:
        :param value:
        :return:
        """

        subprocess.Popen([self.ldconsole_path, "setprop",
                          "--name", emulator_name,
                          "--key", key,
                          "--value", value],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @check_ldconsole_path
    def push_file_by_name(self, emulator_name: str, local_filepath: str, app_filepath: str):
        """
        上传数据到模拟器
        :param emulator_name:
        :param local_filepath:
        :param app_filepath:
        :return:
        """
        creating_em = subprocess.Popen([self.ldconsole_path, "adb",
                                        "--name", emulator_name,
                                        "--command", "push " + local_filepath + " " + app_filepath],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return creating_em.pid

    @check_ldconsole_path
    def pull_file_by_name(self, emulator_name: str, local_filename: str, app_filepath: str):
        """
        从模拟器下载数据
        :param emulator_name:
        :param local_filename:
        :param app_filepath:
        :return:
        """
        pull_file = subprocess.Popen([self.ldconsole_path, "adb",
                                      "--name", emulator_name,
                                      "--command", "pull " + app_filepath + " " + local_filename],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_text, err = pull_file.communicate()
        pull_file_list = []
        for line in out_text.splitlines():  # 输出字节码按行转化为字符串列表
            out_text_sub = line.decode("GBK")
            if out_text_sub:
                pull_file_list.append(out_text_sub)
        print(pull_file_list)
        last_text = pull_file_list.pop()  # pop字符串列表末尾项
        last_text = last_text.split(" ")  # 以空格为分隔符序列化pop出来的字符串数据
        print(last_text)
        if len(last_text) > 3:  # 字符串数据列表长度大于3
            file_size = int(re.sub(r"\D", "", last_text[2]))  # 获取并提取列表索引值(只保留数字)
            print(file_size)
            return file_size
        else:
            return False

    @check_ldconsole_path
    def push_file_by_id(self, emulator_id: int, local_filepath: str, app_filepath: str):
        """
        上传数据到模拟器
        :param emulator_id:
        :param local_filepath:
        :param app_filepath:
        :return:
        """
        push_file = subprocess.Popen([self.ldconsole_path, "adb",
                                      "--index", str(emulator_id),
                                      "--command", "push " + local_filepath + " " + app_filepath],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_text, err = push_file.communicate()
        last_text = self.communicate_text_to_list(out_text)()
        if "error:" in last_text:
            return False
        else:
            # print(last_text)
            if len(last_text) > 3:  # 字符串数据列表长度大于3
                file_size = int(re.sub(r"\D", "", last_text[2]))  # 获取并提取列表索引值(只保留数字)
                print(file_size)
                return file_size
            else:
                return False

    @check_ldconsole_path
    def pull_file_by_id(self, emulator_id: int, local_filename: str, app_filepath: str):
        """
        从模拟器下载数据
        :param emulator_id:
        :param local_filename:
        :param app_filepath:
        :return:
        """
        pull_file = subprocess.Popen(
            [self.ldconsole_path, "adb", "--index", str(emulator_id), "--command", "pull " + app_filepath + " " + local_filename],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # pid = pull_file.pid
        out_text, err = pull_file.communicate()
        last_text = self.communicate_text_to_list(out_text)
        # print(last_text)
        if len(last_text) > 3:  # 字符串数据列表长度大于3
            file_size = int(re.sub(r"\D", "", last_text[2]))  # 获取并提取列表索引值(只保留数字)
            print(file_size)
            return file_size
        else:
            return False

    @staticmethod
    def communicate_text_to_list(out_text):
        """
        模拟器通信输出转换
        :param out_text:
        :return:
        """
        file_list = []
        for line in out_text.splitlines():  # 输出字节码按行转化为字符串列表
            out_text_sub = line.decode("GBK")
            if out_text_sub:
                file_list.append(out_text_sub)
        # print(pull_file_list)
        last_text = file_list.pop()  # pop字符串列表末尾项
        last_text = last_text.split(" ")  # 以空格为分隔符序列化pop出来的字符串数据
        return last_text

    @check_ldconsole_path
    def is_app_exist_by_id(self, emulator_id: int, app_name: str):
        """
        检查APP是否存在
        :param emulator_id:
        :param app_name:
        :return:
        """
        third_part_app = subprocess.Popen(
            [self.ldconsole_path, "adb", "--index", str(emulator_id),
             "--command", "shell pm list packages " + app_name],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_text, err = third_part_app.communicate()
        print(out_text)
        third_part_app = []
        for line in out_text.splitlines():  # 输出字节码按行转化为字符串列表
            out_text_sub = line.decode("GBK")
            if out_text_sub:
                out_text_sub = out_text_sub[8:len(out_text_sub)]
                print(out_text_sub)
                third_part_app.append(out_text_sub)
        if app_name in third_part_app:
            print("APP [" + app_name + "] 已安装")
            return "OK"
        elif "not found" in third_part_app:
            print("模拟器未连接")
            return "Failed"
        else:
            print("APP [" + app_name + "] 未安装")
            return "NO"

    @check_ldconsole_path
    def is_app_m_resumed_activity_by_id(self, emulator_id: int, app_name: str):
        """
        检查APP是否存在
        :param emulator_id:
        :param app_name:
        :return:
        """
        third_part_app = subprocess.Popen([self.ldconsole_path, "adb", "--index", str(emulator_id),
                                           "--command", "shell dumpsys activity activities | grep mResumedActivity"],
                                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_text, err = third_part_app.communicate()
        # print(out_text)
        for line in out_text.splitlines():  # 输出字节码按行转化为字符串列表
            out_text_sub = line.decode("GBK")
            if out_text_sub:
                if app_name in out_text_sub:  # 当前前台列表中包含有指定的app
                    # print(out_text_sub.strip())
                    return True

    @check_ldconsole_path
    def install_app_by_name(self, emulator_name: str, apk_file_name: str):
        """
        # 安装APP
        :param apk_file_name:
        :param emulator_name:
        :return:
        """

        subprocess.Popen([self.ldconsole_path, "installapp", "--name", emulator_name, "--filename", apk_file_name])

    @check_ldconsole_path
    def uninstall_app_by_name(self, emulator_name: str, apk_package_name: str):
        """
        # 卸载APP
        :param apk_package_name:
        :param emulator_name:
        :return:
        """

        subprocess.Popen([self.ldconsole_path, "uninstallapp", "--name", emulator_name, "--package_name", apk_package_name])

    @check_ldconsole_path
    def run_app_by_name(self, emulator_name: str, apk_package_name: str):
        """
        # 运行APP
        :param apk_package_name:
        :param emulator_name:
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "runapp", "--name", emulator_name, "--package_name", apk_package_name])

    @check_ldconsole_path
    def run_app_by_id(self, emulator_id: int, apk_package_name: str):
        """
        # 运行APP
        :param apk_package_name:
        :param emulator_id:
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "runapp", "--index", str(emulator_id), "--package_name", apk_package_name])

    @check_ldconsole_path
    def kill_app_by_name(self, emulator_name: str, apk_package_name: str):
        """
        # 停止模拟器运行的APP
        :param apk_package_name:
        :param emulator_name:
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "killapp", "--name", emulator_name, "--package_name", apk_package_name])

    @check_ldconsole_path
    def kill_app_by_id(self, emulator_id: int, apk_package_name: str):
        """
        # 停止模拟器运行的APP
        :param apk_package_name:
        :param emulator_id:
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "killapp", "--index", str(emulator_id), "--package_name", apk_package_name])

    @check_ldconsole_path
    def text_input(self, emulator_name, text):
        """
        # 文字输入
        :param emulator_name:
        :param text:
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "action", "--name", emulator_name, "--key", "call.input", "--value", text])

    @check_ldconsole_path
    def globalsetting_emulator(self, fps=15, audio=0, fastplay=0, cleanmode=1):
        """
        # 模拟器全局设置
        :param fps:
        :param audio:
        :param fastplay:
        :param cleanmode:
        :return:
        """

        subprocess.Popen([self.ldconsole_path, "globalsetting",
                          "--fps", str(fps),
                          "--audio", str(audio),
                          "--fastplay", str(fastplay),
                          "--cleanmode", str(cleanmode)])

    @check_ldconsole_path
    def sort_emulator(self):
        """
        # 模拟器排序
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "sortWnd"])

    @check_ldconsole_path
    def modify_resolution_by_id(self, emulator_id: int):
        """
        修正模拟器属性
        :param emulator_id:
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "modify", "--index", str(emulator_id), "--resolution", "960, 540, 160"])

    @check_ldconsole_path
    def modify_resolution_all_by_id(self):
        """
        修正模拟分辨率
        :return:
        """
        emulator_id_list = self._list_emulator(only_id=True)
        if emulator_id_list:
            for em_id in emulator_id_list:
                if em_id > 0:
                    self.modify_resolution_by_id(em_id)

    @check_ldconsole_path
    def modify_options_by_id(self, emulator_id: int):
        """
        修正模拟器属性
        :param emulator_id:
        :return:
        """
        subprocess.Popen([self.ldconsole_path, "modify", "--index", str(emulator_id),
                          "--resolution", "960, 540, 160",
                          "--cpu", "1",
                          "--memory", "3072",
                          ])

    def modify_options_all_by_id(self):
        emulator_id_list = self._list_emulator(only_id=True)
        if emulator_id_list:
            for em_id in emulator_id_list:
                if em_id > 0:
                    self.modify_options_by_id(em_id)

    @check_ldconsole_path
    def down_cpu_by_id(self, emulator_id: int):
        subprocess.Popen([self.ldconsole_path, "downcpu", "--index", str(emulator_id), "--rate", "50"])

    @check_ldconsole_path
    def down_cpu_all_by_id(self):
        emulator_id_list = self._list_emulator(only_id=True)
        if emulator_id_list:
            for em_id in emulator_id_list:
                if em_id > 0:
                    self.down_cpu_by_id(em_id)

    @check_ldconsole_path
    def adb_dumpsys_by_id(self, emulator_id: int, packages="com.tencent.tmgp.bydr3dx"):
        dumpsys_app = subprocess.Popen(
            [self.ldconsole_path, "adb", "--index", str(emulator_id), "--command", "shell dumpsys " + "meminfo" + " " + packages],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out_text, err = dumpsys_app.communicate()
        for line in out_text.splitlines():  # 输出字节码按行转化为字符串列表
            out_text_sub = line.decode("GBK")
            if out_text_sub:
                print(out_text_sub.strip())
