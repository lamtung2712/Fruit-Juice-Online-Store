from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Order.models import Cart


# Create your views here.
def product_list(request):
    context = {}
    products = Product.objects.filter(active=True)

    per_page = 1
    paginator = Paginator(products, per_page)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)

    except EmptyPage:
        # Neu page khong phai la so nguyen, hien thi trang dau tien
        products = paginator.page(1)

    except PageNotAnInteger:
        products = paginator.page(paginator.num_pages)

    context.update({
        'products': products
    })

    return render(request, 'homepage/shop.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'homepage/product_details.html', {'product': product})


def your_view(request):
    # Thực hiện tính toán giá trị đơn hàng ở đây
    cart = get_user_cart(request.user)
    subtotal = calculate_subtotal(cart)
    shipping_cost = calculate_shipping_cost(cart)
    total = subtotal + shipping_cost

    context = {
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'total': total,
    }

    return render(request, 'shop.html', context)
