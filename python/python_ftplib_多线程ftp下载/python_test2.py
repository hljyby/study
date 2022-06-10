from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os
import time
import random


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n**2


if __name__ == '__main__':

    executor = ThreadPoolExecutor(max_workers=3)

    futures = []
    for i in range(11):
        print("i", i)
        time.sleep(2)
        future = executor.submit(task, i)
        futures.append(future)
    executor.shutdown(True)
    print('+++>')
    for future in futures:
        print(future.result())
