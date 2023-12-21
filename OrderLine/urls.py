from django.urls import path
from .views import orderline_list

app_name = 'orderline'

urlpatterns = [
    path('orderline/<int:order_id>/', orderline_list, name='orderline_list'),
    # Add other URL patterns as needed
]

