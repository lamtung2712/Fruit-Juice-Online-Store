from django.db import models
from Product.models import Product
from Order.models import Order

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Liên kết với model Order
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.FloatField(default=0)







