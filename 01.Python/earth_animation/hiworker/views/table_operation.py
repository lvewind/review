import datetime
import re
from copy import deepcopy
from operator import itemgetter

from PySide6.QtWidgets import QTableWidgetItem, QTableWidget
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QBrush, QColor


class TableLoad:

    # 初始化表格
    @classmethod
    def init_table_header(cls, table: QTableWidget, header_dict: dict, is_horizontal=True):
        """
        初始化表头
        :param table: 要初始化的表名称
        :param header_dict: 表头字典{“header_name”： , "width": ,}
        :param is_horizontal: 默认为水平表头
        :return:
        """
        if is_horizontal:
            table.setColumnCount(len(header_dict))
            table.setRowCount(0)
        else:
            table.setColumnCount(0)
            table.setRowCount(len(header_dict))
        if header_dict:
            for value in header_dict.values():
                item = QtWidgets.QTableWidgetItem()
                col = value.get("col")
                if is_horizontal:

                    table.setHorizontalHeaderItem(col, item)
                    item = table.horizontalHeaderItem(col)
                    item.setText(value.get("header_name"))
                    col_width = value.get("width")
                    if col_width:
                        table.setColumnWidth(col, col_width)
                else:
                    row = value.get("row")
                    table.setVerticalHeaderItem(row, item)
                    item = table.verticalHeaderItem(row)
                    item.setText(value.get("header_name"))
                    table.setRowHeight(row, value.get("height", 20))

    @classmethod
    def init_table_col(cls, table: QTableWidget, col_dict: dict, col=0, align="center"):
        """
        初始化列
        :param table:
        :param col_dict:
        :param col:
        :param align:
        :return:
        """
        table.setRowCount(len(col_dict))
        for value in col_dict.values():
            table.setRowHeight(value.get("height"), 18)
            cls.set_table_cell(table, value.get("header_name"), value.get("row"), col, align=align)

    @classmethod
    def init_table_row(cls, table: QTableWidget, row_text_dict: dict, row=0):
        """
        初始化行
        :param table:
        :param row_text_dict:
        :param row:
        :return:
        """
        table.setColumnCount(len(row_text_dict))
        for (key, text) in row_text_dict.items():
            cls.set_table_cell(table, str(text), row, int(key))

    # 加载表格数据
    @classmethod
    def load_table(cls, table: QTableWidget, data: list, cols_setting: dict,
                   select_first_row=False,
                   select_last_row=False,
                   order_by="", reverse=False, is_vertical=False):
        """
        将数据List加载到表格
        :param table:
        :param data:
        :param cols_setting:
        :param select_last_row:
        :param select_first_row:
        :param order_by:
        :param reverse:
        :param is_vertical:
        :return:
        """

        data_list = deepcopy(data)
        if data_list:
            if order_by:
                data_list = sorted(data_list, key=itemgetter(order_by), reverse=reverse)
            if not is_vertical:
                for row, data_dict in enumerate(data_list):  # 枚举列表，获取行数据和行号
                    row_count = table.rowCount()  # 获取表格行数
                    if row >= row_count:  # 当前数据行大于等于表格行
                        table.insertRow(row)  # 追加新行
                    if data_dict:
                        cls.load_table_row(table, data_dict, row, cols_setting)
                else:
                    # 删除多余的表格行
                    row_count = table.rowCount()
                    data_len = len(data_list)
                    del_count = row_count - data_len
                    if del_count > 0:  # 有多出的表格行
                        for n in range(1, del_count + 1):
                            table.removeRow(row_count - n)
            else:
                for col, data_dict in enumerate(data_list):  # 枚举列表，获取行数据和行号
                    col_count = table.columnCount()  # 获取表格列数
                    if col >= col_count:  # 当前数据行大于等于表格列
                        table.insertColumn(col)  # 追加新列
                    if data_dict:
                        cls.load_table_col(table, data_dict, col, cols_setting)

            if select_last_row:
                table.selectRow(table.rowCount() - 1)
            elif select_first_row:
                table.selectRow(0)
        elif is_vertical:
            table.setColumnCount(0)
        else:
            table.setRowCount(0)

    @classmethod
    def load_table_row(cls, table: QTableWidget, data_dict: dict, row, cols_setting: dict):
        """
        加载表格行数据
        :param table:
        :param data_dict: 行数据字典
        :param row: 行ID
        :param cols_setting: 列数据配置
        :return:
        """
        table.setRowHeight(row, 20)  # 设置行高, 默认20
        for col_name, value in data_dict.items():  # 显示单元格数据
            cls.load_table_item(table, data_dict, row, col_name, cols_setting)

    @classmethod
    def load_table_col(cls, table: QTableWidget, data_dict: dict, col: int, rows_setting: dict):
        """
        加载表格列数据
        :param table:
        :param data_dict: 列数据字典
        :param col: 列ID
        :param rows_setting: 行数据配置
        :return:
        """
        for row_name, value in data_dict.items():  # 显示单元格数据
            cls.load_table_item(table, data_dict, col, row_name, rows_setting, is_vertical=True)

    @classmethod
    def load_table_item(cls, table: QTableWidget, data_dict: dict, row, col_name, cols_setting: dict, is_vertical=False):
        """
        加载单元格数据
        :param table:
        :param data_dict:
        :param row:
        :param col_name:
        :param cols_setting:
        :param is_vertical:
        :return:
        """
        col_setting = cols_setting.get(col_name, None)
        if col_setting:
            if col_setting.get("use_row_number"):
                col_text = str(row + 1)
            else:
                col_text = data_dict.get(col_name)
                extend_data = col_setting.get("extend")
                if extend_data:
                    col_text = extend_data.get(str(col_text))
                elif col_setting.get("is_time"):
                    col_text = str(datetime.timedelta(seconds=int(col_text)) if col_text else "")
                elif col_setting.get("display_type") == bool:
                    col_text = "是" if col_text else ""
                elif col_setting.get("display_type") == int:
                    if not col_text:
                        col_text = "0"
            bg_color = [255, 255, 255]
            color_switch = col_setting.get("color_switch")
            if color_switch:
                color_status = 1 if data_dict.get(color_switch) else 0
                color_dict = col_setting.get("color")
                try:
                    bg_color = color_dict.get(str(color_status), [255, 0, 0])
                except AttributeError:
                    bg_color = [255, 0, 0]
            if col_setting.get("str_trim"):
                col_text = col_text[-int(col_setting.get("str_len"), 4):]
            align = col_setting.get("align", "center")
            if is_vertical:
                col = row
                column_width = col_setting.get("width")
                row = col_setting.get("row")
                cls.set_table_cell(table, col_text, row, col, bg_color=bg_color, align=align, column_width=column_width)
            else:
                col = col_setting.get("col")
                cls.set_table_cell(table, col_text, row, col, bg_color=bg_color, align=align)

    @classmethod
    def load_table_item_with_text(cls, table: QTableWidget, text, row, col_name, cols_setting: dict):
        col_setting = cols_setting.get(col_name)  # 获取列号
        if col_setting:
            col = col_setting.get("col")
            cls.set_table_cell(table, text if text else "", row, col)

    @classmethod
    def set_table_cell(cls, table: QTableWidget, text, row=0, col=0, bg_color=None, is_time=False, align="center", column_width=0):
        """
        设置单元格
        :param table:
        :param text:
        :param row:
        :param col:
        :param bg_color:
        :param is_time:
        :param align:
        :param column_width:
        :return:
        """

        if not table.item(row, col):
            table.setItem(row, col, QTableWidgetItem(""))

        if column_width:
            table.setColumnWidth(col, column_width)

        try:
            match align:
                case "center":
                    table.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                case "left":
                    table.item(row, col).setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                case "right":
                    table.item(row, col).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        except AttributeError as e:
            print(e)
        if text:
            if is_time:
                time_sec = int(text)
                table.item(row, col).setText(str(datetime.timedelta(seconds=time_sec)))
            else:
                table.item(row, col).setText(str(text))
        else:
            table.item(row, col).setText("")
        if bg_color:
            table.item(row, col).setBackground(QBrush(QColor(bg_color[0], bg_color[1], bg_color[2])))

    @staticmethod
    def sort_by_dict_key(item, key):
        return item.get(key)


class TableRead:

    @classmethod
    def filter_not_number_input(cls, input_data: str):
        """
        过滤输入的非数字数据
        :param input_data:
        :return:
        """
        data_number = re.sub(r"\D", "", input_data)
        if not data_number == "":
            return int(data_number)
        else:
            return 0

    @classmethod
    def get_selected_rows(cls, table: QTableWidget):
        """
        获取当前表格被选中的rows
        :param table: 当前表格
        :return:
        """
        selected_rows = []
        rows = table.rowCount()
        for row in range(rows):
            if table.item(row, 0) and table.item(row, 0).isSelected():
                selected_rows.append(row)
        return selected_rows

    @classmethod
    def get_selected_rows_item_data(cls, table: QTableWidget, col):
        """
        获取当前表格被选中的rows
        :param table: 当前表格
        :param col: 数据列
        :return:
        """
        rows_data = []
        rows = table.rowCount()
        for row in range(rows):
            if table.item(row, col) and table.item(row, col).isSelected():
                rows_data.append(table.item(row, col).text())
        return rows_data

    @classmethod
    def get_all_rows(cls, table: QTableWidget):
        return list(range(table.rowCount()))

    @classmethod
    def get_current_data_id(cls, current_table: QTableWidget, id_col=0):
        """
        # 获取当前表格选中row的ID
        :param current_table: 当前表格
        :param id_col: 默认ID所在列
        :return:
        """
        current_id = cls.get_current_row_item_data(current_table, id_col)
        if current_id:
            return int(current_id)
        return 0

    @classmethod
    def get_selected_data_ids(cls, table: QTableWidget, id_col=0):
        """
        获取当前表格被选中的rows的id字段
        :param table:
        :param id_col: 默认ID所在列
        :return:
        """
        selected_data_id = []
        rows = table.rowCount()
        for row in range(rows):
            if table.item(row, id_col) and table.item(row, id_col).isSelected():
                selected_data_id.append(int(cls.get_cell_data(table, row, id_col)))
        return selected_data_id

    @classmethod
    def get_all_data_ids(cls, table: QTableWidget):
        """
        获取当前表格被选中的rows的id字段
        :param table:
        :return:
        """
        all_data_id = []
        rows = table.rowCount()
        for row in range(rows):
            all_data_id.append(int(cls.get_cell_data(table, row, 0)))
        return all_data_id

    @classmethod
    def get_item_text_with_col_name(cls, table: QTableWidget, row, col_name: str, cols_setting: dict):
        """
        通过表头名称获取数据
        :param table:
        :param row: 行ID
        :param col_name: 表头名称
        :param cols_setting: 表格参数
        :return:
        """
        col_setting = cols_setting.get(col_name)
        col = col_setting.get("col")
        if col:
            return cls.get_cell_data(table, row, col)

    @classmethod
    def get_current_row_item_data(cls, current_table: QTableWidget, col: int):
        current_row = current_table.currentRow()
        if current_row < 0:
            return False
        return cls.get_cell_data(current_table, current_row, col)

    @classmethod
    def get_cell_data(cls, current_table: QTableWidget, row: int, col: int):
        if not current_table.item(row, col):
            return False
        return current_table.item(row, col).text()

    @classmethod
    def get_current_row_number(cls, table: QTableWidget):
        """
        获取当前表格被选中的rows
        :param table: 当前表格
        :return:
        """
        return table.currentRow()

    @classmethod
    def get_rows_item_data(cls, table: QTableWidget, rows: list, col):
        """
        获取当前表格被选中的rows
        :param rows: 行号列表
        :param table: 当前表格
        :param col: 数据列
        :return:
        """
        rows_data = []
        for row in rows:
            if table.item(row, col) and table.item(row, col).isSelected():
                rows_data.append(table.item(row, col).text())
        return rows_data

    @classmethod
    def get_row_item_data(cls, table: QTableWidget, row, col):
        """
        获取当前表格被选中的row的字段
        :param row: 行号
        :param table: 当前表格
        :param col: 数据列
        :return:
        """
        return table.item(row, col).text()
