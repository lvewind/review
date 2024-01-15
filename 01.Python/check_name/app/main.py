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
        self.file_input_path = ""
        self.bind_func()
        self.lineEdit_output_excel.setDisabled(True)

    def bind_func(self):
        self.pushButton_select_excel.clicked.connect(self.select_excel)
        self.pushButton_select_file.clicked.connect(self.select_name_folder)
        self.pushButton_start.clicked.connect(self.start_check)

    def select_excel(self):
        openfile_name, openfile_type = QtWidgets.QFileDialog.getOpenFileName(self, caption='选择excel数据表', filter="Excel Files (*.xls), (*.xlsx)")
        if openfile_name:
            self.lineEdit_input_excel.setText(openfile_name)
            self.excel_input_path = openfile_name
        return openfile_name

    def select_name_folder(self):
        folder_name = QtWidgets.QFileDialog.getExistingDirectory(self, caption='选择作业所在文件夹')
        if folder_name:
            self.lineEdit_input_file.setText(folder_name)
            self.file_input_path = folder_name
        return folder_name

    def start_check(self):
        if self.excel_input_path:
            if not os.path.isfile(self.excel_input_path):
                QtWidgets.QMessageBox.warning(self, "警告", "excel数据表不存在")
                return
        else:
            QtWidgets.QMessageBox.warning(self, "警告", "请先选择excel数据表")
            return

        if self.file_input_path:
            if not os.path.isdir(self.file_input_path):
                QtWidgets.QMessageBox.warning(self, "警告", "作业所在文件夹不存在")
                return
        else:
            QtWidgets.QMessageBox.warning(self, "警告", "请先选择作业所在文件夹")
            return

        Thread(target=self._check).start()

    def _check(self):
        file_name_list = os.listdir(self.file_input_path)
        print(file_name_list)
        name_list = excel_to_list(self.excel_input_path)
        print(name_list)
        output_list = []
        for name in name_list:
            temp_list = [name]
            for file_name in file_name_list:
                if name in file_name:
                    temp_list.append(file_name)
            else:
                output_list.append(temp_list)

        print(output_list)
        path, folder = os.path.split(self.file_input_path)
        print(path, folder)
        list_to_excel(output_list, folder)

