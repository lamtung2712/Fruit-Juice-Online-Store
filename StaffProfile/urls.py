from django.urls import path
from . import views
app_name = 'manager'

urlpatterns = [
    path('products/', views.staff_detail, name='staff_list'),
    ]