from django.contrib import admin
from Order.models import Order, Cart

# Register your models here.

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'cart', 'order_time',)


@admin.register(Cart)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product','user')





