from PySide6.QtCore import QObject, Signal


class RunListSignal(QObject):
    set_current_operation = Signal(int, str)
    set_current_scene = Signal(int, str)
    set_current_product = Signal(int, str)
    set_current_play_name = Signal(int)

    clear_current_product = Signal(int)
    clear_current_operation = Signal(int)
    clear_current_scene = Signal(int)

    load_table_item = Signal(dict)
    load_run_list_counter_item = Signal(int, str)
    load_run_list_item_not_save = Signal(int, str, str)
    load_table_run_time = Signal(int, int)


class RunScheduler(QObject):
    set_scheduler_start = Signal(list)
    set_scheduler_stop = Signal(list)
    set_scheduler_sleep = Signal(list, int)


class CounterRecord(QObject):
    increase_record_item_value = Signal(int, str)
    increase_record_item_value_by_record_id = Signal(str, str)


class RunEnv(QObject):
    launch_env = Signal(list, int)
    close_env = Signal(list, int)


signal_run_list = RunListSignal()
signal_scheduler = RunScheduler()
signal_counter_record = CounterRecord()
signal_run_env = RunEnv()
