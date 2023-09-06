from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(default='', max_length=100)
    phone_number = models.CharField(default='', max_length=100)
    email = models.CharField(default='', max_length=100)
    password = models.CharField(default='', max_length=100)
    address = models.TextField(default='')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


    
