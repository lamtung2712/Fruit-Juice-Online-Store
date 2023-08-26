from django.shortcuts import render
from .models import Order


# Create your views here.
def order_list(request):
    order = Order.objects.filter(active=True)
    return render(request, 'homepage/cart.html', {'order': order})





