import queue


q = queue.Queue()


q.put(111)

print(q.get())  #q.get是阻塞的