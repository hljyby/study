import multiprocessing, time, os, random


def worker(msg):
    t_start = time.time()
    print('%s开始执行，进程号为%d ' % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, '执行完毕耗时%0.2f ' % (t_stop - t_start))


if __name__ == '__main__':
    po = multiprocessing.Pool(3)
    for i in range(0, 10):
        po.apply_async(worker, (i,))

    print('-------你好---------')

    po.close()
    # 关闭进程池，关闭后po不再接受新的请求
    po.join()
    # 等待po 中所有子进程执行完毕，必须放在close之后
    #让主线程等待子线程
    print('-------end---------')
