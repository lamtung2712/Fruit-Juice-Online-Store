from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm

def checkout(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            # Xử lý thông tin thanh toán và lưu vào database
            card_number = form.cleaned_data['card_number']
            expiration_date = form.cleaned_data['expiration_date']
            cvv = form.cleaned_data['cvv']

            # Lưu thông tin thanh toán vào database
            Payment.objects.create(card_number=card_number, expiration_date=expiration_date, cvv=cvv, is_paid=True)

            # Cập nhật trạng thái thanh toán cho đơn hàng (ví dụ)
            # order = ...  # Lấy đơn hàng tương ứng
            # order.is_paid = True
            # order.save()

            return redirect('payment_success')  # Chuyển hướng đến trang thanh toán thành công
    else:
        form = PaymentForm()

    return render(request, 'homepage/checkout.html', {'form': form})

def payment_success(request):
    return render(request, 'payment_success.html')







