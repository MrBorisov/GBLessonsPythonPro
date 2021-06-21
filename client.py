"""Программа клиента, запрашивающего текущее время"""
from socket import *
from json_generator import *

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect(('localhost', 8888))  # Соединиться с сервером
msg = presence()
s.send(msg.encode('utf-8'))
data = s.recv(1000000)
print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')

print('преобразованные в dict ', response_decode(data))
s.close()
