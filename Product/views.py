from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
