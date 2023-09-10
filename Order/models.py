from django.db import models
from Product.models import Product
from Customer.models import User

# Create your models here.
class Cart(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

