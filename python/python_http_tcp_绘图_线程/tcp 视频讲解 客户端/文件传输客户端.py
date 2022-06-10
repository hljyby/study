import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',8000))

# s.send('hellow'.encode('utf8'))
file_name = input('请输入想要下载的文件名：')

s.send(file_name.encode('utf8'))



with open(file_name,'wb') as file:
    while True:
        content = s.recv(1024)
        if not content:
            break
        file.write(content)

s.close()
