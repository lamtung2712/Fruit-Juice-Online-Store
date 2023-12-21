from django.urls import path
from .views import logIn, LogoutView
from .views import user_dashboard



app_name = 'authentication'

urlpatterns = [
    path('login/', logIn, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
]
