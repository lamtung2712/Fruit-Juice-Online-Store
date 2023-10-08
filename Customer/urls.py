from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.customer_detail_view, name='customer_detail_view'),
    path('register/', views.register_customer, name='register_customer'),
]
