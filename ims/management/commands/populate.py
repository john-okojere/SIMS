import json
from django.core.management.base import BaseCommand
from users.models import CustomUser
from ims.models import Student, Lecturer, Admin, ClinicStaff, Course, Result, Timetable, Department, Level

class Command(BaseCommand):
    help = 'Load initial data from a JSON file'

    def handle(self, *args, **kwargs):
        with open('data.json') as f:  # Replace with your JSON file path
            data = json.load(f)

        # Create Departments
        departments = {}
        for dept_data in data['departments']:
            department, created = Department.objects.get_or_create(name=dept_data['name'])
            departments[dept_data['name']] = department

        # Create Admins
        for admin_data in data['admins']:
            user, created = CustomUser.objects.get_or_create(username=admin_data['username'], email=admin_data['email'])
            if created:
                user.set_password('password')
                user.is_superuser = True
                user.is_staff = True
                user.save()
            Admin.objects.get_or_create(user=user)

        # Create Clinic Staff
        for staff_data in data['clinic_staff']:
            user, created = CustomUser.objects.get_or_create(username=staff_data['username'], email=staff_data['email'])
            if created:
                user.set_password('password')
                user.save()
            ClinicStaff.objects.get_or_create(user=user)
# Create Courses
        for course_data in data['courses']:
            Course.objects.get_or_create(course_id=course_data['course_id'], course_name=course_data['course_name'], credits=course_data['credits'])

        # Create Lecturers
        for lecturer_data in data['lecturers']:
            user, created = CustomUser.objects.get_or_create(username=lecturer_data['username'], email=lecturer_data['email'])
            if created:
                user.set_password('password')
                user.save()
            department = departments[lecturer_data['department']]
            lecturer, created = Lecturer.objects.get_or_create(user=user, department=department)

            # Assign courses taught by the lecturer
            for course_id in lecturer_data['courses_taught']:
                course = Course.objects.get(course_id=course_id)
                lecturer.courses_taught.add(course)

        # Create Levels
        levels = {}
        for level_data in data['levels']:
            department = departments[level_data['department']]
            adviser = Lecturer.objects.get(user__username=level_data['adviser'])
            level, created = Level.objects.get_or_create(level=level_data['level'], department=department, adviser=adviser)
            levels[f"{level_data['level']}_{department.name}"] = level

        # Create Students
        for student_data in data['students']:
            user, created = CustomUser.objects.get_or_create(username=student_data['username'], email=student_data['email'])
            if created:
                user.set_password('password')
                user.save()
            department = departments[student_data['department']]
            dept = Department.objects.get(name= department)
            level = Level.objects.get(level = student_data['level'], department = dept)
            student, created = Student.objects.get_or_create(user=user, level=level, department=department, matric=student_data['matric'])

            # Register courses for the student
            for course_id in student_data['courses_registered']:
                course = Course.objects.get(course_id=course_id)
                student.courses_registered.add(course)

            # Add carry over courses (if any)
            for carry_course_id in student_data['carry_over']:
                carry_course = Course.objects.get(course_id=carry_course_id)
                student.carry_over.add(carry_course)

        
        # Create Results
        for result_data in data['results']:
            student = Student.objects.get(user__username=result_data['student_username'])
            course = Course.objects.get(course_id=result_data['course_id'])
            Result.objects.get_or_create(student=student, course=course, defaults={'grade': result_data['grade']})

        # Create Timetables
        for timetable_data in data['timetables']:
            course = Course.objects.get(course_id=timetable_data['course_id'])
            Timetable.objects.get_or_create(day=timetable_data['day'], course=course, time=timetable_data['time'])

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))
