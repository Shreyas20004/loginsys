from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profiles')
    contact_number = models.CharField(max_length=20)
    medical_history = models.TextField()
    # Add other patient-related fields as needed

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profiles')
    is_superuser = models.BooleanField(default=True)
    specialty = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    # Add other doctor-related fields as needed

class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default='default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)