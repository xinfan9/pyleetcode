import threading
import time
from typing import Callable


class DagScheduler:
    def __init__(self):
        self.tasks: dict[str, Callable] = {}
        self.remain_dep: dict[str, int] = {}
        self.successors: dict[str, list[str]] = {}
        self.lock = threading.Lock()

    def add_task(self, task_id: str, func: Callable, deps: list[str]):
        self.tasks[task_id] = func
        self.remain_dep[task_id] = len(deps)
        if task_id not in self.successors:
            self.successors[task_id] = []
        for dep_id in deps:
            if dep_id not in self.successors:
                self.successors[dep_id] = []
            self.successors[dep_id].append(task_id)

    def _run_task(self, task_id: str):
        print(f"[{time.ctime()}] 任务开始 {task_id}")
        self.tasks[task_id]()
        print(f"[{time.ctime()}] 任务完成 {task_id}")

        with self.lock:
            for next_task_id in self.successors[task_id]:
                self.remain_dep[next_task_id] -= 1
                if self.remain_dep[next_task_id] == 0:
                    # `daemon=True` 表示把该线程设为守护线程，核心作用是：主线程退出时，程序不会等待这个线程，直接结束进程，同时把它强制终止。
                    t = threading.Thread(target = self._run_task, args = (next_task_id,), daemon = True)
                    t.start()

    def start(self):
        start_tasks = [task for task, remain_dep in self.remain_dep.items() if remain_dep == 0]
        for task in start_tasks:
            t = threading.Thread(target = self._run_task, args = (task,), daemon = True)
            t.start()



if __name__ == '__main__':
    def A():
        time.sleep(1)
    def B():
        time.sleep(2)
    def C():
        time.sleep(3)
    def D():
        time.sleep(1.5)

    scheduler = DagScheduler()
    scheduler.add_task('A', A, [])
    scheduler.add_task('B', B, ['A','C'])
    scheduler.add_task('C', C, ['A'])
    scheduler.add_task('D', D, ['A'])
    scheduler.start()
    time.sleep(10)





