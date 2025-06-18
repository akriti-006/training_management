from django.db import models

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField(help_text='For better results please enter past date')
    address = models.TextField()
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=100)
