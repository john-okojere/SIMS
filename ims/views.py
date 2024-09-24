from django.shortcuts import render
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Lecturer, Admin, ClinicStaff, Course, Result, Department

def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()

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
    fields = ['level', 'department', 'courses_registered', 'carry_over']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['level', 'department', 'courses_registered', 'carry_over']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('level_adiviser_students')

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
    fields = ['department', 'courses_taught']
    template_name = 'lecturers/lecturer_form.html'
    success_url = reverse_lazy('lecturer_profile')

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

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Student, Level
@login_required
def approve_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    lecturer = request.user.lecturer  # Assuming the user is logged in as a Lecturer

    # Find the lecturer's level where they are the adviser
    level = get_object_or_404(Level, adviser=lecturer, department=student.department)

    if student.level.level == level.level:
        # Approve student
        student.approved = True
        student.save()
        return JsonResponse({'success': True, 'message': f'Student {student.user.username} has been approved.'})
    
    return JsonResponse({'success': False, 'message': 'Approval failed.'})

# Dashboard view
def dashboard(request):
    user = request.user
    is_lecturer = user.groups.filter(name='Lecturer').exists()
    is_student = user.groups.filter(name='Student').exists()
    is_admin = user.is_superuser  # Use is_superuser for admin check
    is_clinic_staff = user.groups.filter(name='ClinicStaff').exists()
    department = Department.objects.all()
    level = Level.objects.all()

    context = {
        'is_lecturer': is_lecturer,
        'is_student': is_student,
        'is_admin': is_admin,
        'is_clinic_staff': is_clinic_staff,
        'department':department,
        'level':level,
    }
    return render(request, 'dashboard.html', context)

import random
from django.contrib.auth.decorators import user_passes_test
from .models import Timetable

import random
from django.shortcuts import render
from .models import Course, Timetable

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

    # Clear existing timetable entries
    Timetable.objects.all().delete()

    assigned_slots = set()

    for course in courses:
        # Assign time slots based on the course's credit hours
        slots_needed = course.credits  # Number of hours the course needs per week
        
        while slots_needed > 0:
            day = random.choice(days)
            time_slot = random.choice(time_slots)
            
            # Ensure no overlapping time slots for the same day
            if (day, time_slot) not in assigned_slots:
                # Save the course to the timetable
                Timetable.objects.create(
                    day=day,
                    course=course,
                    time=f"{time_slot[0]} - {time_slot[1]}"
                )
                
                # Mark the slot as assigned to prevent overlap
                assigned_slots.add((day, time_slot))
                
                # Reduce the required number of slots by 1 (or 2, depending on the time slot length)
                slots_needed -= 1 if time_slot[0] == "8:00 AM" else 2

    return render(request, 'timetable_generated.html', {'message': 'Timetable generated and saved successfully!'})

def view_timetable(request):
    timetable_entries = Timetable.objects.all()
    lecturer = Lecturer.objects.all()
    timetable = {}

    for entry in timetable_entries:
        if entry.day not in timetable:
            timetable[entry.day] = []
        timetable[entry.day].append({
            'course': entry.course,
            'time': entry.time,
        })
    return render(request, 'timetable_view.html', {'timetable': timetable, "lecturer":lecturer})

from .forms import CourseRegistrationForm
# Course registration view
def register_courses(request):
    student = request.user.student  # Assuming that the user is logged in as a student
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_timetable')  # Redirect to timetable view after successful registration
    else:
        form = CourseRegistrationForm(instance=student)
    
    return render(request, 'students/course_registration.html', {'form': form})

# View timetable for the registered courses
def student_view_timetable(request):
    try: 
        student = request.user.student
        timetable_entries = Timetable.objects.filter(course__in=student.courses_registered.all())
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]  # List of days
        return render(request, 'students/student_timetable.html', {'timetable': timetable_entries, 'days': days})
    except:
        return redirect('/')

# View timetable for the registered courses
def lecturer_view_timetable(request):
    lecturer = request.user.lecturer
    timetable_entries = Timetable.objects.filter(course__in=lecturer.courses_taught.all())
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]  # List of days
    return render(request, 'students/student_timetable.html', {'timetable': timetable_entries, 'days': days})


def student_profile(request):
    student = Student.objects.get(user=request.user) # Assuming the user is authenticated as a student
    courses = student.courses_registered.all()  # Get the registered courses
    return render(request, 'students/student_detail.html', {'student': student, 'courses': courses})

def lecturer_profile(request):
    lecturer = request.user.lecturer  # Get the lecturer's profile
    courses_taught = lecturer.courses_taught.all()
    # Render the lecturer's profile page
    return render(request, 'lecturers/lecturer_profile.html', {
        'lecturer': lecturer,
        'courses_taught': courses_taught
    })

from django.http import JsonResponse

def update_year_of_study(request):
    if request.method == 'POST':
        year_of_study = request.POST.get('level')
        department_val = request.POST.get('department')
        department = Department.objects.get(id=department_val)
        level = Level.objects.get(id=year_of_study, department=department)
        if year_of_study:
            student = Student.objects.create(user=request.user, level = level, department = department)
            student.save()
            return JsonResponse({'success': True, 'message': 'Year of study updated successfully!'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid input. Please enter a valid year.'})

    return render(request, 'update_year_of_study.html')

from django.http import JsonResponse
from .models import Level

def get_levels(request, department_id):
    levels = Level.objects.filter(department_id=department_id).values('id', 'level')
    return JsonResponse({'levels': list(levels)})

def level_adiviser(request):
    level = Level.objects.get(adviser = request.user.lecturer)
    students = Student.objects.filter(department = level.department, level=level, approved= False)
    context = {
        'levels':level,
        'students':students
    }
    return render(request, 'lecturers/level_adviser.html', context)

def level_adiviser_students(request):
    level = Level.objects.get(adviser = request.user.lecturer)
    students = Student.objects.filter(department = level.department, level=level, approved= True)
    context = {
        'levels':level,
        'students':students
    }
    return render(request, 'lecturers/level_adviser_student.html', context)



def update_department(request):
    if request.method == 'POST':
        department_val = request.POST.get('department')
        department = Department.objects.get(id=department_val)
        if department:
            lecturer = Lecturer.objects.create(user=request.user, department = department)
            lecturer.save()
            return JsonResponse({'success': True, 'message': 'Department updated successfully!'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid input. Please enter a valid department.'})

    return render(request, 'update_department.html')


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
    # Assume this view is for a specific lecturer
    lecturer = request.user.lecturer

    # Get all courses taught by the lecturer
    courses = lecturer.courses_taught.all()

    # Prepare a dictionary to map courses to their students and current grades
    course_students = {}

    for course in courses:
        students = course.students.all()  # All students registered for this course
        student_grades = []

        for student in students:
            # Find the result for this student and course, or set it as None
            result = Result.objects.filter(student=student, course=course).first()
            student_grades.append({
                'student': student,
                'grade': result.grade if result else "Not graded"
            })
        course_students[course] = student_grades
    return render(request, 'dashboard/lecturer_input_grades.html', {'course_students': course_students})

def submit_grades(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        student_id = request.POST.get('student_id')
        new_grade = request.POST.get('new_grade')

        # Retrieve the course and student objects
        course = Course.objects.get(id=course_id)
        student = Student.objects.get(id=student_id)

        # Update or create the result
        result, created = Result.objects.get_or_create(student=student, course=course)
        result.grade = new_grade
        result.save()

        # Redirect back to the input grades page
        return redirect('lecturer_input_grades')

def lecturer_courses_view(request):
    lecturer = request.user.lecturer  # Get the lecturer from the logged-in user
    courses_taught = lecturer.courses_taught.all()  # Get all courses assigned to the lecturer

    context = {
        'lecturer': lecturer,
        'courses_taught': courses_taught,
    }

    return render(request, 'lecturers/lecturer_courses.html', context)