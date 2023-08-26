from django.shortcuts import render
from .models import Payment

from django.shortcuts import render

# Create your views here.
def checkout(request):
    payment = Payment.objects.filter(active=True)
    return render(request, 'homepage/checkout.html', {'payment': payment})




