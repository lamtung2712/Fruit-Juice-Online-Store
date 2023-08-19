from django.contrib import admin
from Customer.models import Customer
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'email', 'address')

