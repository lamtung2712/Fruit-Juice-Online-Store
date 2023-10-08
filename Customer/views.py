from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerRegistrationForm

def customer_detail_view(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    return render(request, 'homepage/customer.html', {'customer': customer})


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Điều hướng đến trang sau khi đăng ký thành công (ví dụ: trang chủ)
            return redirect('home')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'Customer/customer_registration.html', {'form': form})

