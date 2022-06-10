import socket,os


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1',8000))
server_socket.listen(128)

#接受客户端请求

client_socket,client_addr = server_socket.accept()
data = client_socket.recv(1024).decode('utf8')

# print('接收来自{}地址{}端口的数据，内容是:{}'.format(client_addr[0],client_addr[1],data))

if os.path.isfile(data):
    with open(data,'rb') as file:
        content = file.read()
        client_socket.send(content)
else:
    print('没有名字')