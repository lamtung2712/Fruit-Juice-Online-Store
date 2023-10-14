from django.shortcuts import render, redirect
from .models import Order, Cart
from Product.models import Product

# Create your views here.
def order_list(request):
    order = Order.objects.filter(active=True)
    return render(request, 'homepage/cart.html', {'order': order})

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('orders:order_list')
    else:
        return redirect('account:login')

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





