from django.shortcuts import render, get_object_or_404
from .models import Staff

def staff_list(request):
    staff_list = Staff.objects.all()
    return render(request, 'homepage/staff_list.html', {'staff_list': staff_list})

def staff_detail(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    return render(request, 'homepage/staff_details.html', {'staff': staff})



