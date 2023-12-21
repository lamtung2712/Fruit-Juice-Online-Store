from django.shortcuts import render
from .models import OrderLine

def calculate_total(orderline):
    return orderline.quantity * orderline.price

def orderline_list(request, order_id):
    orderlines = OrderLine.objects.filter(order_id=order_id)

    # Calculate total for each order line in the views
    for orderline in orderlines:
        orderline.total = calculate_total(orderline)

    context = {'orderlines': orderlines}
    return render(request, 'orderline_list.html', context)

