from django.urls import path
from . import views
app_name = 'ordering'

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.delete_car_item, name='remove_cart_item'),
    ]