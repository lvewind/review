import sys

import win32api
import win32event
import wmi
from PySide6 import QtWidgets

from app.presenter.run_list import RunListPresenter

if __name__ == "__main__":
    w = wmi.WMI()
    cpu = w.Win32_Processor()
    cpu_id = cpu[0].ProcessorId
    cpu_id_list = ["BFEBFBFF000406F1", "178BFBFF00800F82", "178BFBFF00870F10", "BFEBFBFF000306C3", "BFEBFBFF000906E9"]
    if cpu_id in cpu_id_list:
        ERROR_ALREADY_EXISTS = 183
        sz_mutex = "HiWorker"
        h_mutex = win32event.CreateMutex(None, False, sz_mutex)
        if win32api.GetLastError() == ERROR_ALREADY_EXISTS:
            print("已运行...")
            # pass
        else:
            app = QtWidgets.QApplication(sys.argv)
            main = RunListPresenter()
            main.show_main_window()
            sys.exit(app.exec())
    else:
        print("CPU ERROR")
