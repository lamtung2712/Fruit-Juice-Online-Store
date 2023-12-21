from django.shortcuts import render, redirect
from .models import Order, Cart, CartItem
from .models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages



# Create your views here.
def order_list(request):
    order = Order.objects.filter(active=True)
    return render(request, 'homepage/cart.html', {'order': order})



# def add_to_cart(request, product_id):
#     products = {}
#     product = Product.objects.get(pk=product_id)
#
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     try:
#         product_cartitem = CartItem.objects.get(product = product).product.id
#         cart_item = CartItem.objects.get(cart=cart, product=product)
#         cart_item.quantity += 1
#         cart_item.total = cart_item.quantity * cart_item.product.price
#         cart_item.save()
#     except CartItem.DoesNotExist:
#         cart_item = CartItem(cart=cart, product=product, quantity=1)
#         cart_item.total = cart_item.quantity * cart_item.product.price
#         cart_item.save()
#     cart_items = CartItem.objects.all()
#     return render(request, 'homepage/cart.html', {'cartitems': cart_items})
#     return JsonResponse({'success': True})



def add_to_cart(request, product_id):
    # Lấy sản phẩm từ cơ sở dữ liệu
    product = get_object_or_404(Product, pk=product_id)

    # Kiểm tra xem người dùng đã đăng nhập hay chưa
    if not request.user.is_authenticated:
        messages.warning(request, "Bạn cần đăng nhập để thêm sản phẩm vào giỏ hàng.")
        return redirect('authentication:login')

    # Lấy hoặc tạo giỏ hàng cho người dùng hiện tại
    cart, created = Cart.objects.get_or_create(user=request.user)

    try:
        # Kiểm tra xem sản phẩm đã tồn tại trong giỏ hàng chưa
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.total = cart_item.quantity * cart_item.product.price
        cart_item.save()
    except CartItem.DoesNotExist:
        # Nếu sản phẩm chưa tồn tại trong giỏ hàng, tạo mới CartItem
        cart_item = CartItem(cart=cart, product=product, quantity=1)
        cart_item.total = cart_item.quantity * cart_item.product.price
        cart_item.save()

    # Lấy danh sách tất cả các CartItem trong giỏ hàng để hiển thị trên trang giỏ hàng
    cart_items = CartItem.objects.filter(cart=cart)

    messages.success(request, f"Sản phẩm {product.title} đã được thêm vào giỏ hàng.")

    return render(request, 'homepage/cart.html', {'cartitems': cart_items})

def delete_cart_item(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)

        # Decrease quantity by 1 and delete if quantity becomes zero
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.total = cart_item.quantity * cart_item.product.price
            cart_item.save()
        else:
            cart_item.delete()

        if request.is_ajax():
            return JsonResponse({'success': True})
        else:
            # Redirect to the cart page or another appropriate page
            return HttpResponseRedirect(reverse('homepage/cart.html'))
    except CartItem.DoesNotExist:
        # Handle the case where the product is not in the cart
        if request.is_ajax():
            return JsonResponse({'success': False, 'message': 'Product not found in the cart'})
        else:
            # Redirect to the cart page or another appropriate page
            return HttpResponseRedirect(reverse('homepage/cart.html'))


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
