from django.urls import path
from . import views

urlpatterns = [
    path('orderline/<int:order_id>/', views.orderline_list, name='orderline_list'),
]
