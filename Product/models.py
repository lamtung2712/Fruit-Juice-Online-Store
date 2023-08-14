from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200,default='')
    active = models.BooleanField(default='True')

class Product(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default='True')

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    discount = models.IntegerField(default=0)
    active = models.BooleanField(default='True')
