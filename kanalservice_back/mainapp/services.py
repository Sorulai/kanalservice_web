from datetime import datetime
from mainapp.models import Order


def get_valute():
    """Возвращает валюту из файла"""
    with open('mainapp/json/valute.txt', 'r') as f:
        valute = f.read()

    return float(valute.replace(',', '.'))


def create_db_data(values):
    """
    Записывает или обновляет данные в БД
    """
    valute = get_valute()
    for list_item in values:
        Order.objects.update_or_create(
            order_id=list_item[0] if list_item[0] else None,
            order_number=list_item[1] if list_item[1] else None,
            order_cost_usd=list_item[2] if list_item[2] else None,
            order_cost_rub=round(int(list_item[2]) * valute, 2) if list_item[2] else None,
            delivery_date=datetime.strptime(list_item[3], "%d.%m.%Y") if list_item[3] else None)
