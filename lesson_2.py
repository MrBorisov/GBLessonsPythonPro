"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов
"""
import re

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = ['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']


def get_data(my_file, element):
    with open(my_file, 'r', encoding='cp1251') as t_f:

        for line in t_f:
            result = re.match(element + ':', line)
            if result != None:
                result = re.split(r':', line)
                return result[1]
                # TODO удалить пробелы и символ завершение сторки


for el in main_data:
    if el == 'Изготовитель ОС':
        os_prod_list.append(get_data('info_1.txt', el))
    elif el == 'Название ОС':
        os_name_list.append(get_data('info_1.txt', el))
    elif el == 'Код продукта':
        os_code_list.append(get_data('info_1.txt', el))
    else:
        os_type_list.append(get_data('info_1.txt', el))

print(os_prod_list, os_name_list, os_code_list, os_type_list)
