from django.urls import path,include
from . import  views 
from .views import PatientLoginView,DoctorLoginView

urlpatterns = [
    path("",views.home,name= "home"),
    
    path('patient/login/', PatientLoginView.as_view(), name='patient_login'),
    path('doctor/login/', DoctorLoginView.as_view(), name='doctor_login'),

]
