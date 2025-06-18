from django.shortcuts import render, redirect
from .models import Student
from django.views import View
from django.contrib.auth import authenticate, login


class HomeStuView(View):
    def get(self, request):
        return render(request, 'stu-home.html')
    

class ListStuView(View):
    def get(self, request):
        data = Student.objects.all().order_by('-id')
        return render(request, 'stu-list.html', {'data':data})
    

class AddStuView(View):
    def get(self, request):
        return render(request, 'stu-add.html')
    
    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        gender = request.POST["gender"]
        dob = request.POST["dob"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        email = request.POST["email"]

        Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            gender = gender,
            dob = dob,
            address = address,
            phone = phone,
            email = email,
        )
        return redirect('stu-list')
    

class DetailStuView(View):
    def get(self, request, pk):
        obj = Student.objects.get(pk=pk)
        
        return render(request, 'stu-detail.html', {'obj':obj})
    

class UpdateStuView(View):
    def get(self, request,pk):
        obj = Student.objects.get(pk=pk)
        return render(request, 'stu-update.html', {'obj':obj})

    def post(self, request, pk):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        gender = request.POST["gender"]
        dob = request.POST["dob"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        email = request.POST["email"]

        obj = Student.objects.get(pk=pk)
        obj.first_name = first_name
        obj.last_name = last_name
        obj.gender = gender
        obj.dob = dob
        obj.address = address
        obj.phone = phone
        obj.email = email
        obj.save()

        return redirect('stu-list')
    
class DeleteStuView(View):
    def get(self, request,pk):
        obj = Student.objects.get(pk=pk)
        return render(request, 'stu-delete.html', {'obj':obj})
    
    def post(self, request,pk):
        obj = Student.objects.get(pk=pk)
        obj.delete()
        return redirect('stu-list')
