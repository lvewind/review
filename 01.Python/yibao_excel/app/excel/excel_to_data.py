from copy import copy

import xlwings as xw


def excel_to_list(excel_input_path: str):
    print("开始解析数据源Excel")
    source_list = []
    try:
        wb = xw.Book(excel_input_path)
        sht_count = len(wb.sheets)
        for sht_n in range(sht_count):
            empty_lines = 0
            sht = wb.sheets[sht_n]
            for row in range(5, 100):
                temp_row = []
                if empty_lines >= 10:
                    break
                name = sht.range(row, 1).value
                if name:
                    empty_lines += 1
                    temp_row.append(name)
                    for col in range(2, 40):
                        data = sht.range(row, col).value
                        if data:
                            temp_row.append(data)
                        else:
                            temp_row.append(0)
                    else:
                        source_list.append(copy(temp_row))
                else:
                    empty_lines = 0

        print("Excel数据源解析完成")
        return source_list
    except ValueError as e:
        print(e)
        return
