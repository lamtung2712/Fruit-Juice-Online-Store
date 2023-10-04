from django.urls import path
from .views import LoginClass

urlpatterns = [
    path('login/', LoginClass.as_view(), name='Login'),
]