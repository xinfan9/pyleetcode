import threading

state, max_num = 1, 10
cond = threading.Condition()

def print_num(parity: int):            # parity: 1=奇数线程, 0=偶数线程
    global state
    while state <= max_num:
        with cond:
            while state % 2 != parity:
                # `cond.wait()` 是条件变量的「等待」操作，作用一句话：**把锁交出去、让出 CPU、阻塞当前线程，直到别的线程调用 `notify()`/`notify_all()` 把它唤醒，唤醒后重新抢回锁再继续往下走。**
                # **永远是把 `wait()` 放进 `while` 循环里**：`wait()` 只是 "被叫醒 + 抢到锁" 的记号，不是 "条件成立" 的保证；`while` 就是醒来后再亲眼看一眼条件到底成不成立。
                cond.wait()
            if state <= max_num:
                print(state, end=' ')
                state += 1
            cond.notify_all()
if __name__ == '__main__':
    t1 = threading.Thread(target=print_num, args=(1,))
    t2 = threading.Thread(target=print_num, args=(0,))
    t1.start(); t2.start()
    t1.join(); t2.join()
