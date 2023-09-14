from django.shortcuts import render, get_object_or_404
from .models import Staff



def staff_detail(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    return render(request, 'homepage/staff_list.html', {'staff': staff})



