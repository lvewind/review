import xlwings as xw
import os


def list_to_excel(data_list: list, excel_name: str):
    print(data_list)
    save_name = os.path.join(os.getcwd(), excel_name + ".xlsx")
    try:
        wb = xw.Book(save_name)
    except FileNotFoundError:
        wb = xw.Book()
    last_sht = wb.sheets[-1]
    if last_sht.name == "Sheet1":
        sht = wb.sheets["Sheet1"]
        # sht.name = product_name
    else:
        # wb.sheets.add(name=product_name, after=last_sht.name)
        sht = wb.sheets.active
    sht.range(1, 1).row_height = 24
    sht.range(1, 1).column_width = 20
    sht.range(1, 2).column_width = 64
    sht.range(1, 3).column_width = 40
    sht.range(1, 4).column_width = 15
    sht.range(1, 5).column_width = 15
    sht.range(1, 6).column_width = 40

    sht.range(1, 1).value = "姓名"
    sht.range(1, 2).value = "作业文件"

    for index, name_item in enumerate(data_list):
        if name_item:
            n = index + 2
            sht.range(n, 1).row_height = 20
            sht.range(n, 1).api.NumberFormat = "0"
            if len(name_item) <= 1:
                sht.range(n, 1).value = name_item[0]
                sht.range(n, 1).color = (255, 0, 0)
            else:
                for sub_index, item in enumerate(name_item):
                    sht.range(n, sub_index + 1).value = item
                    sht.range(n, sub_index + 1).color = (255, 255, 255)
                    sht.range(n, sub_index + 1).api.Borders(7).LineStyle = 1
                    sht.range(n, sub_index + 1).api.Borders(8).LineStyle = 1
                    sht.range(n, sub_index + 1).api.Borders(9).LineStyle = 1
                    sht.range(n, sub_index + 1).api.Borders(10).LineStyle = 1
                    sht.range(n, sub_index + 1).api.Borders(11).LineStyle = 1
                    sht.range(n, sub_index + 1).api.Borders(12).LineStyle = 1

    active_window = wb.app.api.ActiveWindow
    active_window.FreezePanes = False
    active_window.SplitRow = 1
    active_window.FreezePanes = True
    wb.save(save_name)
