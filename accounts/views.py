from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from shared_app.models import *

class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('accounts:home')
        
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            is_first_login = user.last_login is None

            login(request, user)

            if is_first_login:

                messages.success(request, f"Welcome {user.get_full_name()} to this portal! Now you need to explore this for your purpose and utilise it.")
            else:
                messages.info(request, f"You are successfully logged in, {user.get_full_name()}.")
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
        
        user = request.user

        user_group = ''
        if user.groups.filter(name='Admin').exists():
            user_group = 'Admin'
        elif user.groups.filter(name='HR').exists():
            user_group = 'HR'
        elif user.groups.filter(name='Student').exists():
            user_group = 'Student'
        elif user.groups.filter(name='Teacher').exists():
            user_group = 'Teacher'

        
        print("\n\n\n")

        print("user_group : ", user_group)

        pl_obj = ProgrammingLanguage.objects.count()
        fw_obj = Framework.objects.count()
        te_obj = TrainingEnquiry.objects.count()
        se_obj = CourseEnrollment.objects.count()

        print("pl_obj: ", pl_obj)
        print("fw_obj: ", fw_obj)
        print("te_obj: ", te_obj)

        return render(request, 'new_home.html', {
            'pl_obj':pl_obj, 
            'fw_obj':fw_obj, 
            'te_obj':te_obj,
            'se_obj':se_obj
            })
    