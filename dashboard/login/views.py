from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .forms import PatientLoginForm, DoctorLoginForm

def home(request):
    return render(request, 'main/home.html')
class PatientLoginView(auth_views.LoginView):
    template_name = 'patient_login.html'
    authentication_form = PatientLoginForm

class DoctorLoginView(auth_views.LoginView):
    template_name = 'doctor_login.html'
    authentication_form = DoctorLoginForm