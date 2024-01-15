import time

import xlwings as xw
import os


def list_to_excel(data_list: list, excel_name: str):
    print(data_list)
    save_name = os.path.join(os.getcwd(), excel_name.rstrip(".xlsx") + str(int(time.time())) + ".xlsx")
    print(save_name)
    try:
        wb = xw.Book(excel_name)
    except FileNotFoundError:
        wb = xw.Book()
    # sht = wb.sheets[0]
    sht = wb.sheets.active

    for index, data_item in enumerate(data_list):
        if data_item:
            n = index + 5
            for sub_index, data in enumerate(data_item):
                sht.range(n, sub_index + 1).api.NumberFormat = "@"
                sht.range(n, sub_index + 1).value = str(data)

    # active_window = wb.app.api.ActiveWindow
    # active_window.FreezePanes = False
    # active_window.SplitRow = 1
    # active_window.FreezePanes = True
    wb.save(save_name)

