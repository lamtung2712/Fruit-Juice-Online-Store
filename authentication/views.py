from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout

class LoginClass(View):
    def get(self, request):
        return render(request, template_name='homepage/login.html')

    def post(self, request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)

        if my_user is not None:
            login(request, my_user)
            return redirect('index')  # Redirect to your desired page after successful login

        return render(request, 'homepage/login.html', {'error_message': 'Login failed - Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')  # Redirect to your desired page after logout

