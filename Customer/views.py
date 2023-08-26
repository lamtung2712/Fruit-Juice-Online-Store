from django.shortcuts import render
from Customer.models import Customer

# Create your views here.
def customer_list(request):
    products = Customer.objects.filter(active=True)
    return render(request, 'homepage/product_section.html', {'products': products})



