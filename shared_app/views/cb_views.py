from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Sum
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger

from shared_app.models import (
    ProgrammingLanguage, Framework, CourseData,
    TrainingEnquiry, CourseEnrollment, FeeInformation
)

from Training_Program.utility.email_functionality import send_welcome_email, send_course_assign, send_enquiry_email


class PlListView(LoginRequiredMixin, View):
    # login_url = 'accounts:login' 

    # def handle_no_permission(self):
    #     messages.error(self.request, 'You must log in to access this page.')
    #     return redirect(self.login_url)

    def handle_no_permission(self):
        messages.error(self.request, 'You must be logged in to view this page.')
        return super().handle_no_permission()

    def get(self, request):
        data = ProgrammingLanguage.objects.all().order_by('-id')

        return render(request, 'Programming-Language/list.html', {'data':data})
    


class PlAddView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self,request):
        return render(request, 'Programming-Language/add.html')
    
    def post(self, request):
        name = request.POST['name']
        description = request.POST['description']
        
        ProgrammingLanguage.objects.create(
            name = name,
            description = description
        )
        messages.success(request, "Programming Language added successfully")
        return redirect('shared-app:programming-language-list')


class PlDetailView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request, pk):
        obj = ProgrammingLanguage.objects.get(pk=pk)
        return render(request, 'Programming-Language/detail.html', {'obj':obj})
    

class PlUpdateView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request,pk):
        obj = ProgrammingLanguage.objects.get(pk=pk)
        return render(request, 'Programming-Language/update.html', {'obj':obj})

    def post(self, request, pk):
        name = request.POST["name"]
        description = request.POST["description"]
        
        obj = ProgrammingLanguage.objects.get(pk=pk)
        obj.name = name
        obj.description = description
        obj.save()
        messages.success(request, "Programming Language updated successfully")
        return redirect('shared-app:programming-language-list')


class PlDeleteView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request,pk):
        obj = ProgrammingLanguage.objects.get(pk=pk)
        return render(request, 'Programming-Language/delete.html', {'obj':obj})
    
    def post(self, request,pk):
        obj = ProgrammingLanguage.objects.get(pk=pk)
        obj.delete()
        messages.success(request, "Programming Language deleted successfully")
        return redirect('shared-app:programming-language-list')
    

class FwListView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request):
        data = Framework.objects.all().order_by('-id')
        return render(request, 'Framework/list.html', {'data':data})
    

class FwAddView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self,request):
        pl_obj = ProgrammingLanguage.objects.all()
        return render(request, 'Framework/add.html', {'pl_obj':pl_obj})
    
    def post(self,request):
        name = request.POST['name']
        description = request.POST['description']
        language = request.POST['language']

        Framework.objects.create(
            name = name,
            description = description,
            language_id = language,
        )
        messages.success(request, "Framework added successfully")
        return redirect('shared-app:framework-list')


class FwDetailView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request, pk):
        obj = Framework.objects.get(pk=pk)
        return render(request, 'Framework/detail.html', {'obj':obj})
    

class  FwUpdateView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self,  request, pk):
        pl_obj =ProgrammingLanguage.objects.all()
        obj = Framework.objects.get(pk=pk)
        return render(request, 'Framework/update.html', {'pl_obj': pl_obj, 'obj': obj})
    
    def post(self, request,pk):
        #data received
        name = request.POST["name"]
        description = request.POST["description"]
        language= request.POST["language"]
        
        obj = Framework.objects.get(pk=pk)
        obj.name = name
        obj.description = description
        obj.language_id = language
        
        obj.save()
        
        messages.success(request, "Framework updated successfully!")
        return redirect('shared-app:framework-list')


class FwDeleteView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request,pk):
        obj = Framework.objects.get(pk=pk)
        return render(request, 'Framework/delete.html', {'obj':obj})
    
    def post(self, request, pk):
        obj = Framework.objects.get(pk=pk)
        obj.delete()
        
        messages.success(request, "Framework deleted successfully!")
        return redirect('shared-app:framework-list')
       

class CdListView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request):
        data = CourseData.objects.all().order_by('-id')
        return render(request, 'Course-Data/list.html', {'data':data})
    

class CdAddView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request):
        pl_obj = ProgrammingLanguage.objects.all()
        fw_obj = Framework.objects.all()
        return render(request, 'Course-Data/add.html', {'pl_obj':pl_obj, 'fw_obj':fw_obj})
    
    def post(self, request):
        #data received
        name = request.POST["name"]
        description = request.POST["description"]
        language = request.POST.getlist("language")
        framework = request.POST.getlist("framework")
        duration_in_weeks = request.POST["duration_in_weeks"]
        total_fee = request.POST["total_fee"]
        print(request.POST)
        print('language : ', language)

        # data store/ save
        c_obj = CourseData.objects.create(
            name = name,
            description = description,
            duration_in_weeks = duration_in_weeks,
            total_fee = total_fee,
            created_by = request.user
        )

        c_obj.programming_languages.set(language)
        c_obj.frameworks.set(framework)

        messages.success(request, "Course Added successfully!")
        return redirect('shared-app:course-data-list')  
    
        
class CdDetailView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request,pk):
        obj = CourseData.objects.get(pk=pk)
        pl_obj = ProgrammingLanguage.objects.all()
        fw_obj = Framework.objects.all()
        return render (request, 'Course-Data/detail.html', {'obj':obj, 'pl_obj':pl_obj, 'fw_obj':fw_obj})
    

class  CdUpdateView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self,  request, pk):
        obj = CourseData.objects.get(pk=pk)
        pl_obj = ProgrammingLanguage.objects.all()
        fw_obj = Framework.objects.all()

        pl = obj.programming_languages.all()
        print('pl: ', pl)
        
        fw = obj.frameworks.all()
        print('fw: ', fw)
        
        return render (request, 'Course-Data/update.html', {'obj':obj, 'pl_obj':pl_obj, 'fw_obj':fw_obj})
    
    def post(self, request,pk):
        #data received
        name = request.POST["name"]
        description = request.POST["description"]
        language = request.POST.getlist("language")
        framework = request.POST.getlist("framework")
        duration_in_weeks = request.POST["duration_in_weeks"]
        total_fee = request.POST["total_fee"]

        print('\n\n')
        print("==============")
        print('request:', request.POST)
        
        obj = CourseData.objects.get(pk=pk)
        obj.name = name
        obj.description = description
        obj.duration_in_weeks = duration_in_weeks
        obj.total_fee = total_fee
        # obj.language_id = language
        obj.programming_languages.set(language)
        obj.frameworks.set(framework)
        obj.save()
        
        messages.info(request,"Course updated successfully")
        return redirect('shared-app:course-data-list')
    

class CdDeleteView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request,pk):
        obj = CourseData.objects.get(pk=pk)
        return render(request, 'Course-Data/delete.html', {'obj':obj})
    
    def post(self, request, pk):
        obj = CourseData.objects.get(pk=pk)
        obj.delete()
        
        messages.info(request,"Course deleted successfully")
        return redirect('shared-app:course-data-list')


class TeListView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request):
        gender = request.GET.get('gender')
        status = request.GET.get('status')
        data = TrainingEnquiry.objects.all().order_by('-id')

        if gender:
            data = data.filter(gender__iexact=gender)

        if status:
            data = data.filter(status__iexact=status)
        
        context = {}
        context['data'] = data
        context['selected_gender'] = gender
        context['selected_status'] = status

        return render(request, 'Training-Enquiry/list.html',context)


class TeAddView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request):
        cd_obj = CourseData.objects.all()
        return render(request, 'Training-Enquiry/add.html', {'cd_obj':cd_obj})
    
    def post(self, request):
        #data received

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        address = request.POST["address"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        gender = request.POST["gender"]
        description = request.POST["description"]
        higher_qualification = request.POST["higher_qualification"]
        course = request.POST["course"]
        status = request.POST["status"]

        print(request.POST)
       
        obj = TrainingEnquiry.objects.create(
            first_name = first_name,
            last_name = last_name,
            address = address,
            email = email,
            phone = phone,
            gender = gender,
            description = description,
            higher_qualification = higher_qualification,
            course_id = course,
            status = status, 
            created_by = request.user
        )

        send_enquiry_email(obj)       
        messages.success(request, "Trainee Added successfully!")
        return redirect('shared-app:training-enquiry-list')  
    

class TeDetailView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request, pk):
        obj = TrainingEnquiry.objects.get(pk=pk)
        return render(request, 'Training-Enquiry/detail.html', {'obj':obj})
    

class  TeUpdateView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request, pk):
        cd_obj = CourseData.objects.all()
        obj = TrainingEnquiry.objects.get(pk=pk)
        return render(request, 'Training-Enquiry/update.html', {'cd_obj':cd_obj, 'obj':obj})
    
    def post(self, request, pk):
        #data received
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        address = request.POST["address"]
        description = request.POST["description"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        gender = request.POST["gender"]
        higher_qualification = request.POST["higher_qualification"]
        course = request.POST["course"]
        status = request.POST["status"]
        
        print(request.POST)
       
        # data store/ save
        obj = TrainingEnquiry.objects.get(pk=pk)
        obj.first_name = first_name
        obj.last_name = last_name
        obj.address = address
        obj.email = email
        obj.phone = phone
        obj.gender = gender
        obj.description = description
        obj.higher_qualification = higher_qualification
        obj.course_id = course
        obj.status = status
               
        obj.save()     

        messages.success(request, "Trainee updated successfully!")
        return redirect('shared-app:training-enquiry-list') 
    

class TeDeleteView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request,pk):
        obj = TrainingEnquiry.objects.get(pk=pk)
        return render(request, 'Training-Enquiry/delete.html', {'obj':obj})
    
    def post(self, request, pk):
        obj = TrainingEnquiry.objects.get(pk=pk)
        obj.delete()
        
        messages.success(request, "Trainee deleted successfully!")
        return redirect('shared-app:training-enquiry-list')


class TeStartView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request, pk):
        obj = TrainingEnquiry.objects.get(pk=pk)
        return render(request, 'Training-Enquiry/start.html', {'obj':obj})
    
    def post(self, request, pk):
        obj = TrainingEnquiry.objects.get(pk=pk)

        # collect all the possible data
        course_start_date = request.POST.get('course_start_date')
        fee_amount = request.POST.get('fee_amount')
        password = request.POST.get('password', '12345')
        first_name = obj.first_name
        last_name = obj.last_name
        email = obj.email

        # Step-1 update status in TrainingEnquiry model
        obj.status = 'In Progress'
        obj.save()

        # Step-2 create User model object
        if user_obj := User.objects.filter(username=email).first():
            # user already exist
            platform_msg = "Course assigned to the user as this is already exist."
            email_msg = f"Hi {obj.first_name} {obj.last_name}, New course is assigned to your account."
        else:
            # new user
            platform_msg = "Course started successfully!."
            email_msg = f"Hi {obj.first_name} {obj.last_name}, Your account is created for course : {obj.course.name}."

            # create user object
            user_obj = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = email,
                password = password,
                is_active = True
            )

            send_welcome_email(obj, password, course_start_date, course_start_date)
        
        # Step-3 create CourseEnrollment obj
        course_duration = obj.course.duration_in_weeks
        print("course duration : ", course_duration)
        course_enroll_obj = CourseEnrollment(
            student=user_obj,
            course=obj.course,
            start_date = course_start_date,
            end_date = course_start_date,
            created_by = request.user
            )
        course_enroll_obj.save()

        send_course_assign(obj, course_start_date, course_start_date)
        
        # Step-4 Add FeeInformation
        fee_info_obj = FeeInformation(
            enrollment=course_enroll_obj,
            amount_paid=fee_amount,
            created_by = request.user
            )
        fee_info_obj.save()

        # send_mail('mail',email_msg, settings.EMAIL_HOST_USER,[obj.email])
        messages.success(request, platform_msg)

        return redirect('shared-app:training-enquiry-list') 
    

class SeListView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request):
        data = CourseEnrollment.objects.all().order_by('-id')

        data1 = []
        

        for i in data:
            result = {}
            result['id'] = i.id
            result['full_name'] = i.student.get_full_name()
            result['course_name'] = i.course.name
            total_fee = i.course.total_fee
            if i.feeinformation_set.all():
                paid = int(i.feeinformation_set.aggregate(total=Sum('amount_paid'))['total'])  
            else:
                paid = 0
            result['total_fee'] = total_fee
            result['paid_fee'] = paid
            result['pending'] = total_fee - paid
            result['start_date'] = i.start_date
            result['end_date'] = i.end_date

            data1.append(result)
        
        print('data1 : ', data1)


        return render(request, 'Student-Enrollment/list.html', {'data':data})
    

class SeDetailView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request, pk):
        obj = CourseEnrollment.objects.get(pk=pk)
        return render(request, 'Student-Enrollment/detail.html', {'obj':obj})
    

class SeUpdateView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()
    
    def get(self, request, pk):
        te_obj = TrainingEnquiry.objects.all()
        obj = CourseEnrollment.objects.get(pk=pk)
        return render(request, 'Student-Enrollment/update.html', {'obj':obj, 'te_obj':te_obj})
    
    def post(self ,request, pk):
    
        student = request.POST['student']
        course = request.POSt['course']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        obj = CourseEnrollment.objects.get(pk=pk)
        obj.student = student
        obj.course = course
        obj.start_date = start_date
        obj.end_date = end_date
        obj.save()

        messages.success(request, "Course entrollment updated successfully!")
        return redirect('shared-app:course-enrollment-list')
        