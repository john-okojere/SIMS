"""
URL configuration for sims project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class_based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from ims import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', views.dashboard, name='dashboard'),
    path('admins/v', views.AdminListView.as_view(), name='admin_list'),

    # Student URLs
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student-profile/', views.student_profile, name='student_profile'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('update-year-of-study/', views.update_year_of_study, name='update_year_of_study'),
    path('get-levels/<int:department_id>/', views.get_levels, name='get_levels'),
    path('approve-student/<int:student_id>/', views.approve_student, name='approve_student'),

    # Lecturer URLs
    path('lecturers/', views.LecturerListView.as_view(), name='lecturer_list'),
    path('lecturers/<int:pk>/', views.LecturerDetailView.as_view(), name='lecturer_detail'),
    path('lecturers-profile/', views.lecturer_profile, name='lecturer_profile'),
    path('lecturers/create/', views.LecturerCreateView.as_view(), name='lecturer_create'),
    path('lecturers/update/<int:pk>/', views.LecturerUpdateView.as_view(), name='lecturer_update'),
    path('lecturers/delete/<int:pk>/', views.LecturerDeleteView.as_view(), name='lecturer_delete'),
    path('update-department/', views.update_department, name='update_department'),
    path('level-adiviser/', views.level_adiviser, name='level_adiviser'),
    path('level-adiviser-students/', views.level_adiviser_students, name='level_adiviser_students'),

    # Admin URLs
    path('admins/', views.AdminListView.as_view(), name='admin_list'),
    path('admins/<int:pk>/', views.AdminDetailView.as_view(), name='admin_detail'),
    path('admins/create/', views.AdminCreateView.as_view(), name='admin_create'),
    path('admins/update/<int:pk>/', views.AdminUpdateView.as_view(), name='admin_edit'),
    path('admins/delete/<int:pk>/', views.AdminDeleteView.as_view(), name='admin_delete'),

    # Clinic Staff URLs
    path('clinicstaff/', views.ClinicStaffListView.as_view(), name='clinicstaff_list'),
    path('clinicstaff/<int:pk>/', views.ClinicStaffDetailView.as_view(), name='clinicstaff_detail'),
    path('clinicstaff/create/', views.ClinicStaffCreateView.as_view(), name='clinicstaff_create'),
    path('clinicstaff/update/<int:pk>/', views.ClinicStaffUpdateView.as_view(), name='clinicstaff_update'),
    path('clinicstaff/delete/<int:pk>/', views.ClinicStaffDeleteView.as_view(), name='clinicstaff_delete'),

    # Course URLs
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/update/<int:pk>/', views.CourseUpdateView.as_view(), name='course_update'),
    path('courses/delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),

    # Result URLs
    path('results/', views.ResultListView.as_view(), name='result_list'),
    path('results/<int:pk>/', views.ResultDetailView.as_view(), name='result_detail'),
    path('results/create/', views.ResultCreateView.as_view(), name='result_create'),
    path('results/update/<int:pk>/', views.ResultUpdateView.as_view(), name='result_update'),
    path('results/delete/<int:pk>/', views.ResultDeleteView.as_view(), name='result_delete'),

    path('generate_timetable/', views.generate_timetable, name='generate_timetable'),
    path('view_timetable/', views.view_timetable, name='view_timetable'),
    path('lecturer/students/', views.lecturer_view_students, name='lecturer_view_students'),

    # Placeholder for inputting grades
    path('lecturer/grades/', views.lecturer_input_grades, name='lecturer_input_grades'),
    path('lecturer/courses/', views.lecturer_courses_view, name='lecturer_courses'),

    path('register-courses/', views.register_courses, name='register_courses'),
    path('student/view-timetable/', views.student_view_timetable, name='student_view_timetable'),
    path('lecturer/view-timetable/', views.lecturer_view_timetable, name='lecturer_view_timetable'),
    path('submit-grades/', views.submit_grades, name='submit_grades'),

    path('create_department/', views.create_department, name='create_department'),
    path('create_level/', views.create_level, name='create_level'),
    path('create_course/', views.create_course, name='create_course'),
    path('fetch-available-advisers/', views.fetch_available_advisers, name='fetch_available_advisers'),
]
if settings.DEBUG:  # Only add this during development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
