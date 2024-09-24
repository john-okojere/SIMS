from django.contrib import admin
from .models import Department, Student, Lecturer, Level, Admin as AdminUser, ClinicStaff, Course, Result, Timetable

# Admin interface for the Department model
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Admin interface for the Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'level', 'approved')
    list_filter = ('department', 'level', 'approved')
    search_fields = ('user__username', 'user__email', 'department__name')
    filter_horizontal = ('courses_registered',)


# Admin interface for the Lecturer model
@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'approved')
    list_filter = ('department', 'approved')
    search_fields = ('user__username', 'user__email', 'department__name')
    filter_horizontal = ('courses_taught',)


# Admin interface for the Level model
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('level', 'department', 'adviser')
    list_filter = ('level', 'department')
    search_fields = ('level', 'department__name', 'adviser__user__username')


# Admin interface for the AdminUser model
@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')


# Admin interface for the ClinicStaff model
@admin.register(ClinicStaff)
class ClinicStaffAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')


# Admin interface for the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'credits')
    search_fields = ('course_id', 'course_name')


# Admin interface for the Result model
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade')
    list_filter = ('course', 'grade')
    search_fields = ('student__user__username', 'course__course_name', 'grade')


# Admin interface for the Timetable model
@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('course', 'day', 'time')
    list_filter = ('day',)
    search_fields = ('course__course_name', 'day')

