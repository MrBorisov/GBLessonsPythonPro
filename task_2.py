"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт,
автоматизирующий его заполнение данными. Для этого:

"""
import json


def write_order_to_json(items, quantitys, prices, buyers, dates):
    """пишем в json файл"""
    dict_to_json = {
        "item": items,
        "quantity": quantitys,
        "price": prices,
        "buyer": buyers,
        "date": dates
    }
    with open('orders.json', 'w') as f_n:
        json.dump(dict_to_json, f_n, sort_keys=True, indent=4)


item = ['Cisco', 'Tp-link', 'microtik']
quantity = ['1', '10', '4']
price = ['1000', '50', '100']
buyer = ['DTI', 'IP Pupkin', 'SeaLiner']
date = ['12-1-2021', '25-2-2021', '23-4-2021']
write_order_to_json(item, quantity, price, buyer, date)
