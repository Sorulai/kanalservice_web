from rest_framework.response import Response
from rest_framework.views import APIView

from .google import get_google_add
from .models import Order
from .serializers import ListOrdersSerializer
from .services import create_db_data


class ListOrdersView(APIView):
    """Контроллер, который отдает на фронт данные с заказами и их общей стоимостью"""
    def get(self, request, format=None):
        orders = Order.objects.all().select_related()
        values = get_google_add('test_list!A2:D')
        if orders:
            Order.objects.all().delete()
        create_db_data(values)
        serializer = ListOrdersSerializer(orders.first())
        return Response(serializer.data)

