from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Student Registration Form
class StudentRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'STUDENT'
        if commit:
            user.save()
        return user

# Lecturer/Clinic Staff Registration Form
class StaffRegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    
