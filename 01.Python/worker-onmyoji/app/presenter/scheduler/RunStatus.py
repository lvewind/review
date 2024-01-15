from copy import deepcopy

from hiworker import StorageJSON


class RunStatus(StorageJSON):
    def __init__(self):
        super(RunStatus, self).__init__(filename="", json_path="")
        self.data_template = {"ready_for_teamup": False,
                              "chapter_zone_standby": False,
                              "cooperation_teamup_standby": False,
                              "is_running": False}
        self.save_to_file = False

    def add_status_item(self, run_id: int):
        """
        添加运行状态项
        :param run_id:
        :return:
        """
        new_item = {"id": run_id}
        new_item.update(deepcopy(self.data_template))
        self.add_row(new_item, save_to_file=self.save_to_file)

    def set_play_standby_status(self, run_id: int, status: bool):
        """
        设置玩法就绪状态
        :param run_id:
        :param status:
        :return:
        """
        if run_id:
            self.update_row_field(run_id, "ready_for_teamup", status, save_to_file=self.save_to_file)

    def set_chapter_zone_standby_status(self, run_id: int, status: bool):
        """
        设置狗粮副本就绪状态
        :param run_id:
        :param status:
        :return:
        """
        if run_id:
            self.update_row_field(run_id, "chapter_zone_standby", status, save_to_file=self.save_to_file)

    def set_cooperation_teamup_standby_status(self, run_id: int, status: bool):
        """
        设置组队就绪状态
        :param run_id:
        :param status:
        :return:
        """
        if run_id:
            self.update_row_field(run_id, "cooperation_teamup_standby", status, save_to_file=self.save_to_file)

    def set_run_list_is_running(self, run_id: int, status: bool):
        """
        设置运行列表就绪状态
        :param run_id:
        :param status:
        :return:
        """
        if run_id:
            self.update_row_field(run_id, "is_running", status, save_to_file=self.save_to_file)

    def get_play_standby_status(self, run_id: int):
        """
        获取玩法就绪状态
        :param run_id:
        :return:
        """
        return self.read_row_field(run_id, "ready_for_teamup")

    def get_chapter_zone_standby_status(self, run_id: int):
        """
        获取狗粮副本就绪状态
        :param run_id:
        :return:
        """
        return self.read_row_field(run_id, "chapter_zone_standby")

    def get_cooperation_teamup_standby_status(self, run_id: int):
        """
        获取组队就绪状态
        :param run_id:
        :return:
        """
        return self.read_row_field(run_id, "cooperation_teamup_standby")

    def get_run_list_is_running(self, run_id: int):
        """
        获取运行列表就绪状态
        :param run_id:
        :return:
        """
        return self.read_row_field(run_id, "is_running")


class ProductRecord(StorageJSON):
    def __init__(self):
        super(ProductRecord, self).__init__("")
        self.save_to_file = False

    def is_record_exist(self, record_id: str):
        """
        判断记录项是否存在
        :param record_id:
        :return:
        """
        data_row = self.read_row_by_record_id(record_id)
        if data_row:
            return True
        else:
            return False

    def add_record_item(self, record_id: str):
        """
        添加记录项
        :param record_id:
        :return:
        """
        self.add_row({"record_id": record_id}, save_to_file=False)

    def set_record_status(self, record_id: str, finish_status: bool):
        """
        设置记录项状态
        :param record_id:
        :param finish_status:
        :return:
        """
        data_row = self.read_row_by_record_id(record_id)
        if type(data_row) == dict:
            self.update_row_field(data_row.get("id"), "finish_status", finish_status, save_to_file=self.save_to_file)

    def get_record_finish_status(self, record_id: str):
        """
        获取记录项状态
        :param record_id:
        :return:
        """
        data_row = self.read_row_by_record_id(record_id)
        if type(data_row) == dict:
            return data_row.get("finish_status", False)


run_status = RunStatus()
task_record = ProductRecord()
