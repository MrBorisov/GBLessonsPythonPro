"""Программа клиента, запрашивающего текущее время"""
from socket import *
from json_generator import *
from sys import argv

if len(argv) == 1:
    address = 'localhost'
    port = 7777
else:
    address = argv[1]
    port = int(argv[2])
s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect((address, port))  # Соединиться с сервером
msg = presence()
s.send(msg.encode('utf-8'))
data = s.recv(1000000)
print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')

print('преобразованные в dict ', response_decode(data))
s.close()
