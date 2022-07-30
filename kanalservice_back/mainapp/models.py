from django.db import models


class Order(models.Model):
    order_id = models.IntegerField(verbose_name='ID')
    order_number = models.IntegerField(verbose_name='Номер заказа')
    order_cost_usd = models.IntegerField(verbose_name='Стоимость заказа, USD')
    order_cost_rub = models.FloatField(verbose_name='Стоимость заказа, RUB')
    delivery_date = models.DateField(verbose_name='Срок поставки')

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'
