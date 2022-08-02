from django.db.models import Sum
from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Серилизатор модели заказа"""
    class Meta:
        model = Order
        fields = ('order_id', 'order_number', 'order_cost_usd', 'order_cost_rub', 'delivery_date')


class ListOrdersSerializer(serializers.ModelSerializer):
    """Серилизатор, который отдает все заказы, а так же общую стоимость заказов в $"""
    orders = serializers.SerializerMethodField()
    total_usd = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('orders', 'total_usd')

    def get_orders(self, instance):
        orders = Order.objects.all().select_related()
        order_serializer = OrderSerializer(orders, many=True)
        return order_serializer.data

    def get_total_usd(self, instance):
        res = Order.objects.all().aggregate(Sum('order_cost_usd'))
        return res.get('order_cost_usd__sum')
