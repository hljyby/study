import threading,time

lock = threading.Lock()

def dance():
    for i in range(50):
        lock.acquire() #同步锁
        time.sleep(0.2)
        lock.release()
        print(f'跳舞{threading.current_thread().name}')

def sing():
    for i in range(50):
        time.sleep(0.2)
        print(f'唱歌{threading.current_thread().name}')


s1 = threading.Thread(target=dance,name='线程1')
s2 = threading.Thread(target=sing,name='线程2')

s1.start()
s2.start()
