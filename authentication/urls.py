from django.urls import path
from .views import LoginClass, LogoutView

urlpatterns = [
    path('login/', LoginClass.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Add other URL patterns as needed
]
