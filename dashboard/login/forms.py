from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Profile

from django import forms


class PatientLoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        if not self.user_cache.is_patient:
            raise forms.ValidationError("You are not a patient.")
        return cleaned_data

class DoctorLoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        if not self.user_cache.is_doctor:
            raise forms.ValidationError("You are not a doctor.")
        return cleaned_data
    
class UpdateUserForm(forms.ModelForm):
    password = None 
    class Meta:
        model = User
        fields = ['username', 'email',]
        exclude = ['password1','password2',]

class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = Profile
        fields = [ 'profile_pic' ]