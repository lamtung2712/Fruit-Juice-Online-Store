from django.db import models
from Product.models import Product
from Order.models import Order
# Create your models here.

class Payment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    active = models.BooleanField(default='True')

    # Trường mới để xác định trạng thái thanh toán
    is_paid = models.BooleanField(default=False)
