from django.urls import path
from . import views
from .views import index2

urlpatterns = [
    path('main2/', index2.as_view(), name='main2'),
]