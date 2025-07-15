from django.contrib import admin
from .models import (
    CourseData, ProgrammingLanguage, Framework,
    TrainingEnquiry, CourseEnrollment, FeeInformation,
    CourseEnrollmentExtensionLog, TeacherCourseEnrollmentMapping
)


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',
    ]
admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)


class FrameworkAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'language',
    ]
admin.site.register(Framework,FrameworkAdmin)


class CourseDataAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'duration_in_weeks', 'total_fee', 'created_by', 
    ]
admin.site.register(CourseData,CourseDataAdmin)


class TrainingEnquiryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'email', 'higher_qualification','course', 'created_by','status',
    ]
    list_filter = ('gender','status')

    fieldsets = [
        (
            "Basic Details",
            {
                "fields": ["first_name", "last_name", "address", "email", "phone", "gender", "description", "higher_qualification"],
            },
        ),
        (
            "Course Details",
            {
                # "classes": ["collapse"],
                "fields": ["course", "status"],
            },
        ),
    ]
admin.site.register(TrainingEnquiry,TrainingEnquiryAdmin)


class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'student_name', 'course__name', 'course_status', 'start_date', 'end_date',
    ]

    def student_name(self, obj):
        name = obj.student.get_full_name()
        return name

    student_name.short_description = 'Stu Name'
admin.site.register(CourseEnrollment, CourseEnrollmentAdmin)


class CourseEnrollmentExtensionLogAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'enrollment', 'new_end_date',
    ]
admin.site.register(CourseEnrollmentExtensionLog, CourseEnrollmentExtensionLogAdmin)


class FeeInformationAdmin(admin.ModelAdmin):
    list_display = [
        'enrollment', 'amount_paid',
    ]
admin.site.register(FeeInformation, FeeInformationAdmin)


class TeacherCourseEnrollmentMappingAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'teacher', 'course_enrollment'
    ]
admin.site.register(TeacherCourseEnrollmentMapping, TeacherCourseEnrollmentMappingAdmin)
