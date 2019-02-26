# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'g.cn'
port = 80

s.connect((host, port))

ip, port = s.getsockname()
print('本机ip 和 port {} {}'.format(ip, port))
# 本地的端口是操作系統分配的，本地的ip是路由器分配的

http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)

request= http_request.encode('utf-8')
print('请求', request)
s.send(request)

response = s.recv(1023)

print('响应', response)
# str format
print('响应的str格式', response.decode('utf-8'))