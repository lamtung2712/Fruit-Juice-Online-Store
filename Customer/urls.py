from django.urls import path
from . import views

urlpatterns = [
    path('customer/<int:customer_id>/', views.customer_detail_view, name='customer_detail'),
    path('register/', views.register_customer, name='register_customer'),
]
