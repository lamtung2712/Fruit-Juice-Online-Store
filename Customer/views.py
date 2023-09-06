from django.shortcuts import render
from .models import Customer

def customer_detail_view(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    return render(request, 'homepage/customer.html', {'customer': customer})



