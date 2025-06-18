from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'gender', 'dob', 'email'
    ]

admin.site.register(Student,StudentAdmin)
