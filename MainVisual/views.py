from django.shortcuts import render
from django.views import View


class index2(View):
    def get(self, request):
        return render(request, 'homepage/index_2.html')

