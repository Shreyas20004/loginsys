from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Add other patient-related fields

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_superuser = models.BooleanField(default=True)  # Doctor is a superuser
    # Add other doctor-related fields



class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default='default.jpg') 

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  