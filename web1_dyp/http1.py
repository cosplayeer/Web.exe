import socket

host = ''
port = 2001

s = socket.socket()

s.bind((host, port))

while True:
    s.listen(5)
    connection, address = s.accept()

    request = connection.recv(1024)
    print('ip and request, {}\n{}'.format(address, request.decode('utf-8')))

    response = b'<h1>Hello, World!</h1>'
    # response = b'HTTP/1.1 200 hao \r\n\r\n<h1>Hello World!</h1>'
    # 用 sendall 发送给客户端
    connection.sendall(response)
    # 发送完毕后, 关闭本次连接
    connection.close()


