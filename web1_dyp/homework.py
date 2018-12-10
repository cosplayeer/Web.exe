#coding: utf-8

import socket

def protocol_of_url(url):
        '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'

    返回代表协议的字符串, 'http' 或者 'https'
    '''
    pass

def protocol_of_url_only(url):
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1] 
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url   #protocal value ?

    return protocal 

def protocol_of_url(url):
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1] 
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url   #protocal value ?

    i = u.find('/')
    if i == -1:
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]

    port_dict = {
        'http': 80,
        'https': 443,
    }

    port = port_dict[protocol]
    if ':' in host:
        h = host.split(':')
        port = int(h[1])
        host = h[0]

    return protocol, host, port, path