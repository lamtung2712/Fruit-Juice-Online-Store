from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ProductFilterForm



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

def product_list(request):
    products = Product.objects.all()
    form = ProductFilterForm(request.GET)

    if form.is_valid():
        if form.cleaned_data['name']:
            products = products.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data['category']:
            products = products.filter(category__icontains=form.cleaned_data['category'])
        # Áp dụng các bộ lọc khác tùy theo yêu cầu của bạn

    return render(request, 'homepage/shop.html', {'products': products, 'form': form})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    similar_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:3]
    return render(request, 'homepage/product_details.html', {'product': product, 'similar_products': similar_products})

# def your_view(request):
#     # Thực hiện tính toán giá trị đơn hàng ở đây
#     cart = get_user_cart(request.user)
#     subtotal = calculate_subtotal(cart)
#     shipping_cost = calculate_shipping_cost(cart)
#     total = subtotal + shipping_cost
#
#     context = {
#         'subtotal': subtotal,
#         'shipping_cost': shipping_cost,
#         'total': total,
#     }
#
#     return render(request, 'shop.html', context)


