"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить
тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать
строковые представление в формат Unicode и также проверить тип и содержимое переменных.
"""

words = ('разработка', 'сокет', 'декаратор')
for el in words:
    print(type(el))

uwords = ('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
          '\u0441\u043e\u043a\u0435\u0442',
          '\u0434\u0435\u043a\u0430\u0440\u0430\u0442\u043e\u0440')

for el in uwords:
    print(type(el))

"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое
и длину соответствующих переменных.
"""

words = (b'class', b'function', b'method')
for el in words:
    print(type(el))
    print(len(el))

"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

# words = (b'attribute', b'класс', b'функция', b'type')
print('Only latin')
print('bytes can only contain ASCII literal characters.')

"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование
(используя методы encode и decode).
"""
bwords = []
words = ('разработка', 'администрирование', 'protocol', 'standard')
for el in words:
    bwords.append(el.encode('utf-8'))
print(bwords)
for el in bwords:
    print(el.decode('utf-8'))

"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
результаты из байтовового в строковый тип на кириллице.
"""
import subprocess

arg1 = ['ping', 'yandex.ru']
with subprocess.Popen(arg1, stdout=subprocess.PIPE) as subproc_ping:
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

arg2 = ['ping', 'youtube.com']
with subprocess.Popen(arg2, stdout=subprocess.PIPE) as subproc_ping:
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

"""
Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку
файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import locale

def_coding = locale.getpreferredencoding()
print(def_coding + ' кодировка файлов по умолчанию в системе')

words = ('сетевое программирование', 'сокет', 'декоратор')
with open("test.txt", "w") as f_n:
    for el in words:
        f_n.write(el + '\n')
    f_n.close()

with open("test.txt", encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')
    f_n.close()
