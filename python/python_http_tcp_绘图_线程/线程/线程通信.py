import multiprocessing,queue


q = multiprocessing.Queue()

q.put(5) #限制大小为5

q.full() #是否满了

q.put('how',block=True,timeout=1)

# block=True 表示是阻塞，如果队列满了，就等待

# timeout = 1 标识超时，超过就报错

q.put_nowait('hellow') #等价于q.put('how',block=False)