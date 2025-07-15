from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from Training_Program.utility.common_model import CommonModel


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

STATUS_CHOICE = (
    ('Enquiry', 'Enquiry'),
    ('In Progress', 'In Progress'),
    ('Started', 'Started'),
    ('Completed', 'Completed'),
    ('Dropped', 'Dropped'),
)

COURSE_STATUS_CHOICE = (
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('On Hold', 'On Hold'),
)

class ProgrammingLanguage(CommonModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Framework(CommonModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, related_name='frameworks')

    def __str__(self):
        return self.name


class CourseData(CommonModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_in_weeks = models.PositiveSmallIntegerField()
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    programming_languages = models.ManyToManyField(ProgrammingLanguage, blank=True)
    frameworks = models.ManyToManyField(Framework, blank=True)

    def clean(self):
        self.name = self.name.lower()
        self.description = self.description.lower()

    def __str__(self):
        return self.name


class TrainingEnquiry(CommonModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    description = models.TextField(blank=True, null=True)
    higher_qualification = models.CharField(max_length=20)
    course = models.ForeignKey(CourseData, on_delete=models.CASCADE, related_name='courses' )
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def get_full_name(self):
        return self.first_name + ' ' +self.last_name

    def __str__(self):
        return self.first_name


class CourseEnrollment(CommonModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    course = models.ForeignKey(CourseData, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    course_status = models.CharField(max_length=20, choices=COURSE_STATUS_CHOICE)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date must be after start date.")

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"


class CourseEnrollmentExtensionLog(CommonModel):
    enrollment = models.ForeignKey(CourseEnrollment, on_delete=models.CASCADE)
    new_end_date = models.DateField()
    remark = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class FeeInformation(CommonModel):
    enrollment = models.ForeignKey(CourseEnrollment, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.enrollment.student} paid {self.amount_paid}"


class TeacherCourseEnrollmentMapping(CommonModel):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher")
    course_enrollment = models.ForeignKey(CourseEnrollment, on_delete=models.CASCADE)

