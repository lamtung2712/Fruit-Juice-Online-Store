from django.db import models
from Product.models import Product
from Customer.models import User

# Create your models here.
class Cart(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)

class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)