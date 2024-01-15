import os.path

from app.ui.main import Ui_MainWindow
from app.excel.excel_to_data import excel_to_list
from app.excel.data_to_excel import list_to_excel
from PySide6 import QtWidgets
from threading import Thread


class Kiki(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Kiki, self).__init__()
        self.setupUi(self)
        self.excel_input_path = ""
        self.bind_func()

    def bind_func(self):
        self.pushButton_select_excel.clicked.connect(self.select_excel)
        self.pushButton_start.clicked.connect(self.start_check)

    def select_excel(self):
        openfile_name, openfile_type = QtWidgets.QFileDialog.getOpenFileName(self, caption='选择excel数据表', filter="Excel Files (*.xls), (*.xlsx)")
        if openfile_name:
            self.lineEdit_input_excel.setText(openfile_name)
            self.excel_input_path = openfile_name
        return openfile_name

    def start_check(self):
        if self.excel_input_path:
            if not os.path.isfile(self.excel_input_path):
                QtWidgets.QMessageBox.warning(self, "警告", "excel数据表不存在")
                return
        else:
            QtWidgets.QMessageBox.warning(self, "警告", "请先选择excel数据表")
            return

        Thread(target=self._check).start()

    def _check(self):
        data_list = excel_to_list(self.excel_input_path)
        print(data_list)
        output = []
        for data in data_list:
            if len(data) > 3:
                for index, item in enumerate(data):
                    if item:
                        item_list = str(item).split("\n")
                        if index >= 3:
                            check_times = len(item_list)
                            if check_times == 1:
                                data[index] = "只有一次打卡记录，请查看原始数据"
                            elif check_times == 2:
                                data[index] = self.time_to_str(self.str_to_time(item_list[1]) - self.str_to_time(item_list[0]))
                            elif check_times == 4:
                                data[index] = self.time_to_str(self.str_to_time(item_list[1]) - self.str_to_time(item_list[0]) +
                                                               self.str_to_time(item_list[3]) - self.str_to_time(item_list[2]))
                            elif check_times == 6:
                                data[index] = self.time_to_str(self.str_to_time(item_list[1]) - self.str_to_time(item_list[0]) +
                                                               self.str_to_time(item_list[3]) - self.str_to_time(item_list[2]) +
                                                               self.str_to_time(item_list[5]) - self.str_to_time(item_list[4]))
                            else:
                                data[index] = "数据异常，请核对"

        print(data_list)
        list_to_excel(data_list, self.excel_input_path)

    @staticmethod
    def str_to_time(str_time: str):
        t_list = str_time.split(":")
        return int(t_list[0])*60 + int(t_list[1])

    @staticmethod
    def time_to_str(total_minutes: int):
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return str(hours)+":"+str(minutes)
