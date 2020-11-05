# -*- coding：utf-8 -*-

import multiprocessing,time,os
# from multiprocessing  import Queue
# 进程间通信 用这个Queue
# q = Queue()
# p1 = multiprocessing.Process(target=dance, args=(q,))
# 进程不共享全局变量，所以需要把q 传到里面去，而进程不需要

def dance(n):
    print(os.getpid())

    for a in range(n):
        time.sleep(0.5)
        print('appp  {}'.format(a))

def sing(m):
    print(os.getpid())

    for b in range(m):
        time.sleep(0.5)
        print('apppssss  {}'.format(b))
if __name__ == '__main__':

    print(os.getpid())
    #创建了两个进程
    p1 = multiprocessing.Process(target=dance,args=(100,))
    p2 = multiprocessing.Process(target=sing,args=(100,))

    p1.start()
    p2.start()
