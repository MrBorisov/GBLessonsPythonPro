"""
скриптр сервера
"""
from socket import *
import json
from json_generator import *


def response(code, msg):
    response_msg = {
        "response": code,
        "alert": msg
    }
    return json.dumps(response_msg)


s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 8888))  # Присваивает порт 8888
s.listen(5)  # Переходит в режим ожидания запросов;
# Одновременно обслуживает не более
# 5 запросов.
while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
    print('преобразованные в dict ', response_decode(data))
    msg = response('200', 'OK')
    client.send(msg.encode('utf-8'))
    client.close()
