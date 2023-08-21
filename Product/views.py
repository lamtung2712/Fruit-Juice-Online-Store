from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.filter(active=True)
    return render(request, 'homepage/product_section.html', {'products': products})