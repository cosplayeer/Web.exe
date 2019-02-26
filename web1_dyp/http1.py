import socket

host = ''
port = 2001

s = socket.socket()

s.bind((host, port))

# bind连接一个tuple,客户端程序要用connect, 服务器程序要用bind

while True:
    s.listen(5)
    # 当有客户端过来连接的时候，s.accept函数就会返回2个值
    # 分别是 连接 和客户 ip 地址
    connection, address = s.accept()
    print('after accept 类型', type(connection), type(address))

    request = connection.recv(1024)
    print('ip and request, {}\n{}'.format(address, request.decode('utf-8')))

    response = b'<h1>Hello, World!</h1>'
    # response = b'HTTP/1.1 200 hao \r\n\r\n<h1>Hello World!</h1>'
    # 用 sendall 发送给客户端
    connection.sendall(response)
    # 发送完毕后, 关闭本次连接
    connection.close()


