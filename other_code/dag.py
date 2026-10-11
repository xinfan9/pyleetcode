import threading
import time
from typing import Callable, Optional


class DagScheduler:
    def __init__(self):
        self.tasks: dict[str, Callable] = {}
        self.remain_dep: dict[str, int] = {}
        self.successors: dict[str, list[str]] = {}
        self.lock = threading.Lock()
        self.pending = 0                      # 仍在运行/待运行的任务数
        self.all_done = threading.Event()     # 全部完成时置位

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
        try:
            self.tasks[task_id]()
        finally:
            print(f"[{time.ctime()}] 任务完成 {task_id}")
            with self.lock:
                # 先登记新就绪的后继任务
                for next_task_id in self.successors[task_id]:
                    self.remain_dep[next_task_id] -= 1
                    if self.remain_dep[next_task_id] == 0:
                        self.pending += 1
                        threading.Thread(
                            target=self._run_task,
                            args=(next_task_id,),
                            daemon=True,
                        ).start()
                # 当前任务结束
                self.pending -= 1
                if self.pending == 0:
                    self.all_done.set()

    def start(self):
        with self.lock:
            start_tasks = [
                task for task, remain in self.remain_dep.items() if remain == 0
            ]
            self.pending = len(start_tasks)
            if self.pending == 0:
                self.all_done.set()
                return
            for task in start_tasks:
                threading.Thread(
                    target=self._run_task, args=(task,), daemon=True
                ).start()

    def join(self, timeout: Optional[float] = None):
        """等待所有任务执行完毕；timeout 可选，不传则一直等。"""
        self.all_done.wait(timeout)


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
    scheduler.add_task('B', B, ['A', 'C'])
    scheduler.add_task('C', C, ['A'])
    scheduler.add_task('D', D, ['A'])
    scheduler.start()
    scheduler.join()   # 等所有任务真正跑完，不再需要固定 sleep
