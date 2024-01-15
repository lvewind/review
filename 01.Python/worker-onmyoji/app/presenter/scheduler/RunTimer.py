
import hiworker
import time
from ...models import RunListModel
from ..sender import signal_run_list


class RunTimer(hiworker.Thread):
    def __init__(self, run_id: int):
        self.run_id = run_id
        super(RunTimer, self).__init__()
        self.start_running_time = 0
        self.last_save_data_time = 0
        self._run_list = RunListModel()

    def run(self):
        self.stop_flag = False
        self.start_running_time = 0
        self.start_running_time = time.time()
        while not self.stop_flag:
            if self.start_running_time == 0:
                self.start_running_time = time.time()
            running_time = time.time() - self.start_running_time
            self._run_list.update({"id": self.run_id, "run_time": int(running_time)})
            signal_run_list.load_table_run_time.emit(self.run_id, running_time)

            time.sleep(1)
