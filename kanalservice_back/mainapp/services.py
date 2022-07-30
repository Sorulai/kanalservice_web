from datetime import datetime
from mainapp.models import Order


def get_valute():
    with open('mainapp/json/valute.txt', 'r') as f:
        valute = f.read()

    return float(valute.replace(',', '.'))


def create_db_data(values):
    valute = get_valute()
    for list_item in values:
        date = datetime.strptime(list_item[3], "%d.%m.%Y")
        order_cost_rub = round(int(list_item[2]) * valute, 2)
        Order.objects.update_or_create(order_id=list_item[0], order_number=list_item[1],
                                       order_cost_usd=list_item[2], order_cost_rub=order_cost_rub, delivery_date=date)
