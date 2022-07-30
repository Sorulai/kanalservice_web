from django.urls import path

from .views import ListOrdersView

app_name = 'mainapp'
urlpatterns = [
    path('list-orders/', ListOrdersView.as_view())
]
