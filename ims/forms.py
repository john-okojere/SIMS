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

from django import forms
from .models import Department, Level, Course

# Form for creating a new department
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

# Form for creating a new level
class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['level', 'department', 'adviser']

# Form for creating a new course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'credits']
