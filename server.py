"""скриптр сервера"""
from socket import *
from json_generator import *
from sys import argv


def response(code, msg_resp):
    response_msg = {
        "response": code,
        "alert": msg_resp
    }
    return json.dumps(response_msg)


if len(argv) == 1:
    address = 'localhost'
    port = 7777
else:
    address = argv[1]
    port = int(argv[2])

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((address, port))
s.listen(5)
while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
    print('преобразованные в dict ', response_decode(data))
    msg = response('200', 'OK')
    client.send(msg.encode('utf-8'))
    client.close()
