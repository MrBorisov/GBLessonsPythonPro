"""
Задание на закрепление знаний по модулю yaml. Написать скрипт,
автоматизирующий сохранение данных в файле YAML-формата. Для этого:
"""
import yaml

dict_to_write = {
    '1': ['firs', 'second'],
    '2': 55,
    '3': {
        '2€': 'www',
        '3€': 'ddd',
        '4€': 'fff'
    }
}

with open('file.yaml', 'w') as y_f:
    yaml.dump(dict_to_write, y_f, allow_unicode=True)
y_f.close()
with open('file.yaml') as y_f:
    print(y_f.read())
y_f.close()
