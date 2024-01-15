"""
线程扩展
"""
from PySide6.QtCore import QThread
from PySide6.QtCore import QMutex


class Thread(QThread):
    def __init__(self):
        super(Thread, self).__init__()
        self.stop_flag = False
        self.stop_status = False
        self.suspend = False
        self.close_env = True

    def stop(self):
        """
        停止线程
        :return:
        """
        self.stop_flag = True

    def suspend_on(self):
        self.suspend = True

    def suspend_off(self):
        self.suspend = False


class ThreadLock(QMutex):
    def __init__(self):
        super(ThreadLock, self).__init__()
