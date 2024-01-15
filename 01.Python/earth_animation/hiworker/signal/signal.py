from PySide6.QtCore import QObject, Signal


class SignalHiWorker(QObject):
    show_info = Signal(str)
    close_info = Signal()
    show_load_data = Signal(str)

    create_emulator = Signal(int)
    remove_emulator = Signal(list)
    launch_emulator_by_id = Signal(int)
    show_create_process = Signal(int)
    refresh_current_create_process = Signal(int)
    refresh_disk_speed = Signal(str)
    finish_create_process = Signal()
    load_emulator_list_table = Signal()

    show_remove_process = Signal(int)
    refresh_current_remove = Signal(int)
    finish_remove_process = Signal()

    launch_emulator_multiple = Signal(list)
    close_emulator_multiple = Signal(list)
    reboot_emulator_multiple = Signal(list)
    start_emulator_game_multiple = Signal(list)
    close_emulator_game_multiple = Signal(list)

    start_emulator = Signal()
    stop_emulator = Signal()
    reboot_emulator = Signal()
    start_emulator_game = Signal()

    launch_sandbox = Signal(list)
    close_sandbox = Signal(list)

    load_table_sandbox_list = Signal()

    tts_finish = Signal(str)


signal_hi_worker = SignalHiWorker()
