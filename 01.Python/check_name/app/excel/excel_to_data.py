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
            for row in range(5, 999):
                if empty_lines >= 10:
                    break

                name = sht.range("E" + str(row)).value
                if not name:
                    empty_lines += 1
                else:
                    empty_lines = 0
                    # signal_main_ui.refresh_text_browser.emit(str(brand) + str(name) + str(size))
                    source_list.append(name)
        print("Excel数据源解析完成")
        return source_list
    except ValueError as e:
        print(e)
        return
