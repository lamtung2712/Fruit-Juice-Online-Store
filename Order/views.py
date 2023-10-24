from django.shortcuts import render, redirect
from .models import Order, Cart, CartItem
from Product.models import Product
from django.http import JsonResponse


# Create your views here.
def order_list(request):
    order = Order.objects.filter(active=True)
    return render(request, 'homepage/cart.html', {'order': order})


def add_to_cart(request, product_id):
    products = {}
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.total = cart_item.quantity * cart_item.product.price
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem(cart=cart, product=product, quantity=1)
        cart_item.total = cart_item.quantity * cart_item.product.price
        cart_item.save()

    return render(request, 'homepage/cart.html', {'cartitems': [cart_item]})
    return JsonResponse({'success': True})


def place_order(request):
    user = request.user
    cart = Cart.objects.filter(user=user, active=True)
    if cart.exists():
        # Lưu thông tin đơn hàng
        order = Order(user=user, address=request.POST['address'], cart=cart.first())
        order.save()
        cart.update(active=False)

        return redirect('your_order_success_page')
    else:
        return redirect('your_empty_cart_page')
