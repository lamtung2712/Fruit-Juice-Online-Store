from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    active = models.BooleanField(default='True')

    class Meta:
        verbose_name = 'Categories'

class Product(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default='True')
    currency = models.CharField(max_length=200, default='vnd')

class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    discount = models.IntegerField(default=0)
    active = models.BooleanField(default='True')


