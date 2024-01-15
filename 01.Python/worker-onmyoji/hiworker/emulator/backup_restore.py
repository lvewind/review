# from ...static.app_signal import *
import time
import zipfile
import os
import shutil

from .emulator import Emulator


class BackupRestore:
    def __init__(self, emulator: Emulator):
        self.emulator = emulator
        self.local_temp_path = "data/backup/tmp"
        self.local_path = "data/backup/"
        self.app_filepath = "/data/data/com.tencent.tmgp.bydr3dx"
        self.app_name = "com.tencent.tmgp.bydr3dx"
        if not os.path.exists(self.local_temp_path):
            os.makedirs(self.local_temp_path, exist_ok=True)

    def backup_app_data(self, backup_id_list: list):
        if backup_id_list:
            for backup_id in backup_id_list:
                # 设置备份zip文件名称
                zip_filename = str(backup_id) + ".zip"
                if not self.check_emulator_status(backup_id):
                    return False

                app_status = self.check_app_status(backup_id)

                if app_status == "OK":  # APP存在
                    failed_times = 0
                    print(backup_id, "正在下载数据")
                    file_size = self.emulator.pull_file_by_id(backup_id, self.local_temp_path, self.app_filepath)  # 执行ADB pull，返回备份的数据Bytes
                    if file_size and file_size / 1048576 > 4:  # adb pull 的数据大于2MB，说明pull成功
                        self.compress_file(zip_filename)  # 打包pull下来的数据
                        if app_status == "OK":
                            print(backup_id, "备份成功")
                        elif app_status == "NO":
                            print(backup_id, "备份完成，但未能检测到游戏，建议重启模拟器后运行一次游戏后重新备份")
                            self.compress_file(zip_filename)  # 打包pull下来的数据
                    else:
                        failed_times += 1
                        failed_sleep = 5
                        while failed_sleep > 0:
                            failed_message = "数据下载失败" + str(failed_times) + "次，等待" + str(failed_sleep) + "秒后重试"
                            print(backup_id, failed_message)
                            time.sleep(1)
                            failed_sleep -= 1
                elif app_status == "NO":  # APP不存在
                    print(backup_id, "备份失败，若游戏已安装，关闭对应模拟器后重试")

                elif app_status == "failed":  # ADB连接超时
                    print(backup_id, "连接超时，重启对应模拟器后重试")

    def restore_app_data(self, restore_id_list):
        if restore_id_list:
            for restore_id in restore_id_list:
                if not self.check_emulator_status(restore_id):
                    return False
                app_status = self.check_app_status(restore_id)
                failed_times = 0
                if app_status == "OK" or app_status == "NO":
                    zip_filename = str(restore_id) + ".zip"
                    if zipfile.is_zipfile(self.local_path + zip_filename):
                        # 解压数据包
                        self.decompress_file(zip_filename)
                    file_size = self.emulator.push_file_by_id(restore_id, self.local_temp_path, self.app_filepath)  # 执行ADB push，返回备份的数据Bytes
                    if file_size and file_size / 1048576 > 4:  # adb push 的数据大于2MB，说明push成功
                        # 删除临时数据
                        try:
                            shutil.rmtree(self.local_temp_path)
                        except FileNotFoundError:
                            pass
                        if app_status == "OK":
                            print(restore_id, "恢复成功")
                        elif app_status == "NO":
                            print(restore_id, "恢复成功，但游戏可能未安装，请启动一次游戏检查")

                    else:
                        if not file_size:
                            print(restore_id, "模拟器连接失败，正在重启模拟器")
                            self.emulator.reboot_emulator_by_id(restore_id)
                            time.sleep(10)
                        failed_times += 1
                        failed_sleep = 5
                        while failed_sleep > 0:
                            failed_message = "数据上传失败" + str(failed_times) + "次，等待" + str(failed_sleep) + "秒后重试"
                            print(restore_id, failed_message)
                            time.sleep(1)
                            failed_sleep -= 1
                elif app_status == "failed":
                    print(restore_id, "连接超时，重启对应模拟器后重试")
            
    def compress_file(self, zip_filename):
        zip_filename = self.local_path + zip_filename
        if os.path.isfile(self.local_temp_path):
            with zipfile.ZipFile(zip_filename, 'w') as z:
                z.write(self.local_temp_path)
        else:
            with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True, compresslevel=9) as z:
                for dir_path, dir_names, filenames in os.walk(self.local_temp_path):
                    f_path = dir_path.replace(self.local_temp_path, '')
                    f_path = f_path and f_path + os.sep or ''
                    for filename in filenames:
                        z.write(os.path.join(dir_path, filename), f_path + filename)
                print('压缩成功')
            try:
                shutil.rmtree(self.local_temp_path)
            except FileNotFoundError:
                pass
            
    def decompress_file(self, zip_filename):
        zip_filename = self.local_path + zip_filename

        if os.path.isfile(self.local_temp_path):
            with zipfile.ZipFile(zip_filename, 'w') as z:
                z.write(self.local_temp_path)
        else:
            with zipfile.ZipFile(zip_filename, 'r', compression=zipfile.ZIP_DEFLATED, allowZip64=True, compresslevel=9) as z:
                z.extractall(self.local_temp_path)
                print('解压完成')

    def check_emulator_status(self, em_id):
        launch_wait_time = 0
        while launch_wait_time <= 48:
            em_status = self.emulator.get_emulator_status_by_id(em_id)  # 获取模拟器状态
            if not em_status:
                self.emulator.launch_emulator_by_id(em_id)  # 启动模拟器
                time.sleep(1)
                launch_wait_time += 1
            else:
                return True
        else:
            return False

    def check_app_status(self, em_id):
        app_check_time = 0
        while app_check_time <= 16:
            app_check_time += 1
            app_status = self.emulator.is_app_exist_by_id(em_id, self.app_name)
            if app_status == "OK":
                return "OK"
            elif app_status == "NO":
                return "NO"
            elif app_status == "Failed":
                continue
        else:
            return False
