'''
一个子线程A把一个全局的列表words进行升序的排序，另外一个D线程把这个列表进行降序的排列
'''
import threading
import time

lock = threading._RLock()
words = ['a', 'g', 'c', 'd', 'e', 'f', 'b']


def increase():
    time.sleep(1)
    global words
    for count in range(5):
        lock.acquire()  # 获取对锁的控制权
        print('A acquire')
        words = sorted(words, reverse=True)
        print('A', words)
        # time.sleep(1)
        lock.release()


def decrease():
    time.sleep(1)
    global words
    for count in range(5):
        lock.acquire()  # 获取对锁的控制权
        print('D acquire')
        words = sorted(words, reverse=False)
        print('D', words)
        # time.sleep(1)
        lock.release()


if __name__ == '__main__':
    print('The start')
    A = threading.Thread(target=increase)
    A.setDaemon(False)  # False 后台的线程
    A.start()
    D = threading.Thread(target=decrease)
    D.setDaemon(False)
    D.start()
    print('The end')
