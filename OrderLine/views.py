from django.shortcuts import render
from .models import OrderLine

def orderline_list(request, order_id):
    orderlines = OrderLine.objects.filter(order_id=order_id)
    context = {'orderlines': orderlines}
    return render(request, 'orderline_list.html', context)

