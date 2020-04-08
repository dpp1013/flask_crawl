# 在主线程中启动一个子线程执行readhanshu

import threading
import time
import random


def reading():
    for i in range(10):
        print('reading', i)
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    r = threading.Thread(target=reading)
    r.setDaemon(True)  # 设置线程是后台的线程，主程序执行完毕，其他线程任然可以执行
    r.start()
    r.join()    # r进程
    print('The end')
