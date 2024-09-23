from django import forms
from .models import Student, Course

class CourseRegistrationForm(forms.ModelForm):
    courses_registered = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(), 
        widget=forms.CheckboxSelectMultiple,  # Allows selecting multiple courses with checkboxes
        required=True,
    )

    class Meta:
        model = Student
        fields = ['courses_registered']
