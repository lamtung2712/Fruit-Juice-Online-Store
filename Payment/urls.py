from django.urls import path
from .views import checkout, payment_success

app_name = 'payment'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('payment_success/', payment_success, name='payment_success'),
    # Các đường dẫn khác của ứng dụng của bạn
]


