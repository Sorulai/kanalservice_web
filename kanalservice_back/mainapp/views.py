from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .classes import GoogleSheet
from .models import Order
from .serializers import ListOrdersSerializer
from .services import create_db_data


class ListOrdersView(ListAPIView):
    queryset = Order.objects.all().select_related()
    serializer_class = ListOrdersSerializer

    def get(self, request, *args, **kwargs):
        gs = GoogleSheet()
        values = gs.get_data('test_list!A2:D')
        if self.get_queryset():
            Order.objects.all().delete()
        create_db_data(values)
        return super(ListOrdersView, self).get(request, *args, **kwargs)
