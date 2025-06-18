from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('accounts:home')

        print("===================")
        print("login")

        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are login successfully!")
            return redirect('accounts:home')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')
    

class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'Please login to visit home page')
            return redirect('accounts:login')
        return render(request, 'new_home.html')
    
