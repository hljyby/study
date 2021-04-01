import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9090))

# 0.0.0.0 代表着不管内网还是外网，只要知道我的IP地址(内网ip和外网IP)就可以访问我

server_socket.listen(128)

while True:
    client_socket, client_addr = server_socket.accept()

    data = client_socket.recv(1024).decode('utf8')

    client_socket.send('HTTP/1.1 200 OK\ncontent-type:text/html;charset=utf8\n\n'.encode('utf8'))
    # 加一段请求头charset=utf8可以使浏览器解码方式变为utf8浏览器默认解码方式为gbk
    # client_socket.send('\n'.encode('utf8'))

    path = data.splitlines()[0].split(' ')[1]  # 切出第一行

    client_socket.send('''
    
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>你好</title>
</head>
<body>
你好晚安
</body>
</html>
    '''.encode('utf8'))

    print(path)

    print(data)
