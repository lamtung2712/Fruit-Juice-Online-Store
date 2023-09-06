from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(default='', max_length=100)
    phone_number = models.CharField(default='', max_length=100)
    email = models.CharField(default='', max_length=100)
    password = models.CharField(default='', max_length=100)

