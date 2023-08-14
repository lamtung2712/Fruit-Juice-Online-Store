from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    user_name = models.CharField(default='',max_length=100)
    phone_number = models.TextField
    email = models.CharField(default='',max_length=100)
    password = models.CharField(default='',max_length=100)
    address = models.CharField(default='',max_length=200)

class Customer(AbstractUser):
    customer_name = models.CharField(default='', max_length=100)
    phone_number = models.TextField
    email = models.CharField(default='', max_length=100)
    password = models.CharField(default='', max_length=100)
    address = models.CharField(default='', max_length=200)


    
