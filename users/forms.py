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
    role = forms.ChoiceField(choices=[('LECTURER', 'Lecturer'), ('CLINIC_STAFF', 'Clinic Staff')])
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user
