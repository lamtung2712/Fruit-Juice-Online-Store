from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views import View
from .forms import LoginForm
from django.contrib.auth.decorators import login_required



def logIn(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = request.POST.get('username').lower()
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)


            if user is not None:
                login(request, user)
                return redirect('index')


        else:
            print('Error:', form.errors)

    else:
        form = LoginForm()
    context.update({'form': form})
    return render(request, "homepage/login.html", context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')  # Redirect to your desired page after logout



@login_required(login_url='authentication:login')  # Update the login URL
def user_dashboard(request):
    user_info = {
        'username': request.user.username,
        # Add other user-specific information you want to display
    }

    return render(request, 'homepage/dashboard.html', {'user_info': user_info})
