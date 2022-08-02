from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Order(models.Model):
    """Модель заказов"""
    order_id = models.IntegerField(verbose_name='ID', **NULLABLE)
    order_number = models.IntegerField(verbose_name='Номер заказа', **NULLABLE)
    order_cost_usd = models.IntegerField(verbose_name='Стоимость заказа, USD', **NULLABLE)
    order_cost_rub = models.FloatField(verbose_name='Стоимость заказа, RUB', **NULLABLE)
    delivery_date = models.DateField(verbose_name='Срок поставки', **NULLABLE)

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'
