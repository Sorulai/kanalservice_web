from django.contrib import admin

# Register your models here.
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk','order_id', 'order_number', 'order_cost_usd', 'order_cost_rub', 'delivery_date')
    search_fields = ['order_number', ]
    date_hierarchy = 'delivery_date'
