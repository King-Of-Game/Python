import time
import threading

_lock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, thread_id, thread_name, exec_count, time_interval, whether_lock):
        threading.Thread.__init__(self)
        self.thread_id = thread_id  # 自定义线程ID
        self.thread_name = thread_name  # 自定义线程名字
        self.exec_count = exec_count  # 线程执行次数
        self.time_interval = time_interval  # 线程执行前后的间隔
        self.whether_lock = whether_lock  # 是否加锁

    def run(self) -> None:
        print('# %s start...' % self.thread_name)
        if self.whether_lock:
            _lock.acquire()
            be_called(self.thread_name, self.time_interval, self.exec_count)
            _lock.release()
        else:
            be_called(self.thread_name, self.time_interval, self.exec_count)
        print('# %s end...' % self.thread_name)


def be_called(thread_name, time_interval, count):
    while count:
        time.sleep(time_interval)
        print('%s: %s' % (thread_name, time.ctime(time.time())))
        count -= 1


if __name__ == '__main__':
    thread_list = []
    thread1 = MyThread(thread_id=1, thread_name='thread1', exec_count=3, time_interval=1, whether_lock=True)
    thread2 = MyThread(thread_id=2, thread_name='thread2', exec_count=3, time_interval=2, whether_lock=True)

    thread1.start()
    thread2.start()

    thread_list.append(thread1)
    thread_list.append(thread2)

    for thread in thread_list:
        thread.join()

    print('主线程退出！')
