from rest_framework import serializers

from .models import Order


class ListOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'order_number', 'order_cost_usd', 'order_cost_rub', 'delivery_date')
