# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'g.cn'
port = 80

s.connect((host, port))

ip, port = s.getsockname()
print('本机ip 和 port {} {}'.format(ip, port))
# 本地的端口是操作系統分配的，本地的ip是路由器分配的
# 本机ip 和 port 10.64.106.222 10692

#构造一个HTTP请求
http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)
# 发送HTTP 请求给服务器
# send函数只接受bytes作为参数
# str.encode把str转换为bytes，编码是utf-8

request= http_request.encode('utf-8')
print('请求', request)
s.send(request)

# 接受服务器的响应数据
# 参数是长度，这里为1023字节
# 所以如果服务器返回的数据超过1023的部分你就得不到了
# 1023是魔法数据，随便写的
response = s.recv(1023)

print('响应', response)
# str format
print('响应的str格式', response.decode('utf-8'))

#响应行
# http头
# 空格行
#http数据 ：html文件