from django.db import models
from Customer.models import Customer
# Create your models here.

class Delivery(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField
    transport_fee = models.FloatField(default=0)
    total_pay = models.FloatField(default=0)
