from django.urls import path
from django.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]
