from django.contrib import admin

from django.contrib import admin
from .models import Student, Lecturer, Admin, ClinicStaff, Course, Result


# Register the Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'year_of_study')
    search_fields = ('user__username', 'year_of_study')
    filter_horizontal = ('courses_registered',)  # for many-to-many relationship

# Register the Lecturer model
@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')
    search_fields = ('user__username', 'department')
    filter_horizontal = ('courses_taught',)  # for many-to-many relationship

# Register the Admin model
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

# Register the ClinicStaff model
@admin.register(ClinicStaff)
class ClinicStaffAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

# Register the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'credits')
    search_fields = ('course_id', 'course_name')

# Register the Result model
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade')
    search_fields = ('student__user__username', 'course__course_name', 'grade')
    list_filter = ('grade',)  # to filter results by grade

