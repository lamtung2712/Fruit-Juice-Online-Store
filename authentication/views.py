from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login




class LoginClass(View):
    def get(self, request):
        return render(request, template_name='authentication/login.html')

    def post(self, request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is not None:
            login(request, my_user)
            return redirect('index')

        return HttpResponse('Login failed - User does not exist')
