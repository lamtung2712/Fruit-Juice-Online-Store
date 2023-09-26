from django.shortcuts import render, get_object_or_404
from .models import Staff
from Product.models import Product
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def staff_detail(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    return render(request, 'homepage/contact.html', {'staff': staff})


def pageView(request):
    context = {}
    product_list = Product.objects.filter(status=1).ordered_by('-created')

    # So san pham moi trang
    per_page = 10
    paginator = Paginator(product_list, per_page)

    page = request.GET.get('page')

    try:
        product_list = paginator.page(page)
    except EmptyPage:
        # Neu page khong phai la so nguyen, hien thi trang dau tien
        product_list = paginator.page(1)

    except PageNotAnInteger:
        product_list = paginator.page(paginator.num_pages)

    context.update({
        'product_list': product_list
    })
    return render(request, 'homepage/shop.html', context)



