from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login




class LoginClass(View):
    def get(self, request):
        return render(request, template_name='authentication/login.html')

    def post(self, request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_user = authenticate(username = user_name, password = pass_word)
        if my_user is None:
            return HttpResponse('Login failed/User does not exist')

        login(request, my_user)
        return render(request, 'authentication/successfully.html')

