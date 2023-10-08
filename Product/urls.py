from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('products/', views.product_list, name='products_list'),
    path('product_details/<str:product_id>/', views.product_detail, name='product_detail'),

]
