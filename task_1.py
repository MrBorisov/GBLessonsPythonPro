"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов
"""
import re
import csv


def get_data(my_file, element):
    """Возвращает список элементов из файла подходящих под регулярку"""
    with open(my_file, 'r', encoding='cp1251') as t_f:

        for line in t_f:
            result = re.match(element + ':', line)
            if result is not None:
                result = re.split(r':', line)
                res = " ".join(result[1].split())
        return res


def get_data_final(files):
    """Возвращает список списков с элементами из списка файлов"""
    main_data = []
    heading_list = ['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for param in heading_list:
        for text_file in files:
            if param == 'Изготовитель ОС':
                os_prod_list.append(get_data(text_file, param))
            elif param == 'Название ОС':
                os_name_list.append(get_data(text_file, param))
            elif param == 'Код продукта':
                os_code_list.append(get_data(text_file, param))
            else:
                os_type_list.append(get_data(text_file, param))
    main_data.append(heading_list)
    main_data.append(os_prod_list)
    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_type_list)
    return main_data


def write_to_csv(csv_file):
    """Пишем в файл список списков"""
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    data = get_data_final(files)
    with open(csv_file, 'w') as csv_f:
        csv_f_writer = csv.writer(csv_f)
        for row in data:
            csv_f_writer.writerow(row)


write_to_csv('csv_data.csv')
