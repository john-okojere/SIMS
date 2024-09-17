from django.shortcuts import render
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Lecturer, Admin, ClinicStaff, Course, Result

# Student Views
class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['user', 'year_of_study', 'courses_registered']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['user', 'year_of_study', 'courses_registered']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

# Lecturer Views
class LecturerListView(ListView):
    model = Lecturer
    context_object_name = 'lecturers'
    template_name = 'lecturers/lecturer_list.html'

class LecturerDetailView(DetailView):
    model = Lecturer
    template_name = 'lecturers/lecturer_detail.html'

class LecturerCreateView(CreateView):
    model = Lecturer
    fields = ['user', 'department', 'courses_taught']
    template_name = 'lecturers/lecturer_form.html'
    success_url = reverse_lazy('lecturer_list')

class LecturerUpdateView(UpdateView):
    model = Lecturer
    fields = ['user', 'department', 'courses_taught']
    template_name = 'lecturers/lecturer_form.html'
    success_url = reverse_lazy('lecturer_list')

class LecturerDeleteView(DeleteView):
    model = Lecturer
    template_name = 'lecturers/lecturer_confirm_delete.html'
    success_url = reverse_lazy('lecturer_list')

# Admin Views
class AdminListView(ListView):
    model = Admin
    context_object_name = 'admins'
    template_name = 'admins/admin_list.html'

class AdminDetailView(DetailView):
    model = Admin
    context_object_name = 'clinicstaff'
    template_name = 'admins/admin_detail.html'

class AdminCreateView(CreateView):
    model = Admin
    fields = ['user']
    template_name = 'admins/admin_form.html'
    success_url = reverse_lazy('admin_list')

class AdminUpdateView(UpdateView):
    model = Admin
    fields = ['user']
    template_name = 'admins/admin_form.html'
    success_url = reverse_lazy('admin_list')

class AdminDeleteView(DeleteView):
    model = Admin
    template_name = 'admins/admin_confirm_delete.html'
    success_url = reverse_lazy('admin_list')

# Clinic Staff Views
class ClinicStaffListView(ListView):
    model = ClinicStaff
    context_object_name = 'clinicstaffs'
    template_name = 'clinic_staff/clinicstaff_list.html'

class ClinicStaffDetailView(DetailView):
    model = ClinicStaff
    template_name = 'clinic_staff/clinicstaff_detail.html'

class ClinicStaffCreateView(CreateView):
    model = ClinicStaff
    fields = ['user']
    template_name = 'clinic_staff/clinicstaff_form.html'
    success_url = reverse_lazy('clinicstaff_list')

class ClinicStaffUpdateView(UpdateView):
    model = ClinicStaff
    fields = ['user']
    template_name = 'clinic_staff/clinicstaff_form.html'
    success_url = reverse_lazy('clinicstaff_list')

class ClinicStaffDeleteView(DeleteView):
    model = ClinicStaff
    template_name = 'clinic_staff/clinicstaff_confirm_delete.html'
    success_url = reverse_lazy('clinicstaff_list')

# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

class CourseCreateView(CreateView):
    model = Course
    fields = ['course_id', 'course_name', 'credits']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['course_id', 'course_name', 'credits']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

# Result Views
class ResultListView(ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'results/result_list.html'

class ResultDetailView(DetailView):
    model = Result
    template_name = 'results/result_detail.html'

class ResultCreateView(CreateView):
    model = Result
    fields = ['student', 'course', 'grade']
    template_name = 'results/result_form.html'
    success_url = reverse_lazy('result_list')

class ResultUpdateView(UpdateView):
    model = Result
    fields = ['student', 'course', 'grade']
    template_name = 'results/result_form.html'
    success_url = reverse_lazy('result_list')

class ResultDeleteView(DeleteView):
    model = Result
    template_name = 'results/result_confirm_delete.html'
    success_url = reverse_lazy('result_list')

# Dashboard view
def dashboard(request):
    user = request.user
    is_lecturer = user.groups.filter(name='Lecturer').exists()
    is_student = user.groups.filter(name='Student').exists()
    is_admin = user.is_superuser  # Use is_superuser for admin check
    is_clinic_staff = user.groups.filter(name='ClinicStaff').exists()

    context = {
        'is_lecturer': is_lecturer,
        'is_student': is_student,
        'is_admin': is_admin,
        'is_clinic_staff': is_clinic_staff,
    }
    return render(request, 'dashboard.html', context)
import random
def generate_timetable(request):
    courses = Course.objects.all()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time_slots = [
        ("8:00 AM", "9:00 AM"),   # 1 hour
        ("9:00 AM", "11:00 AM"),  # 2 hours
        ("11:00 AM", "12:00 PM"), # 1 hour
        ("12:00 PM", "2:00 PM"),  # 2 hours
        ("2:00 PM", "3:00 PM"),   # 1 hour
        ("3:00 PM", "5:00 PM"),   # 2 hours
    ]
    
    # Sample timetable structure (you can customize this)
    timetable = {}
    
    # Example logic to generate timetable based on courses
    # Track assigned time slots to avoid overlapping
    assigned_slots = set()

    # Generate the timetable for each course
    for course in courses:
        # Randomly assign a day
        day = random.choice(days)
        
        # Ensure unique time slot selection for the day (no overlapping)
        while True:
            time_slot = random.choice(time_slots)
            if (day, time_slot) not in assigned_slots:
                assigned_slots.add((day, time_slot))
                break
        
        # Add course to the timetable
        if day not in timetable:
            timetable[day] = []
        
        timetable[day].append({
            'course_name': course.course_name,
            'time': f"{time_slot[0]} - {time_slot[1]}",
        })
    
    # Render the timetable to a template
    return render(request, 'timetable.html', {'timetable': timetable})

def lecturer_view_students(request):
    # Get the logged-in lecturer
    lecturer = Lecturer.objects.get(user=request.user)
    
    # Get all courses the lecturer is teaching
    courses_taught = lecturer.courses_taught.all()
    
    # For each course, get the list of registered students
    course_students = {}
    for course in courses_taught:
        students = course.students.all()  # This comes from the related_name in the Course model
        course_students[course] = students
    
    # Render the list to the template
    return render(request, 'dashboard/lecturer_view_students.html', {'course_students': course_students})



def lecturer_input_grades(request):
    # Get the courses the lecturer is teaching
    lecturer = Lecturer.objects.get(user=request.user)
    courses_taught = lecturer.courses_taught.all()

    # Get the registered students for each course
    course_students = {}
    for course in courses_taught:
        students = course.students.all()
        course_students[course] = students

    # Render template for inputting grades
    return render(request, 'dashboard/lecturer_input_grades.html', {'course_students': course_students})

def submit_grades(request):
    if request.method == 'POST':
        lecturer = Lecturer.objects.get(user=request.user)
        courses_taught = lecturer.courses_taught.all()

        for course in courses_taught:
            students = course.students.all()
            for student in students:
                grade_key = f"grade_{student.id}"
                if grade_key in request.POST:
                    new_grade = request.POST[grade_key]
                    result = Result.objects.get(student=student, course=course)
                    result.grade = new_grade
                    result.save()

        return redirect('lecturer_view_students')