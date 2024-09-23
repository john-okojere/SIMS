import json
from django.core.management.base import BaseCommand
from users.models import CustomUser
from ims.models import Student, Lecturer, Admin, ClinicStaff, Course, Result, Timetable  # Adjust import as needed

class Command(BaseCommand):
    help = 'Load initial data from a JSON file'

    def handle(self, *args, **kwargs):
        with open('data.json') as f:  # Replace with your JSON file path
            data = json.load(f)

        # Create Admins
        for admin_data in data['admins']:
            user = CustomUser.objects.create_superuser(username=admin_data['username'], email=admin_data['email'], password='password')
            Admin.objects.create(user=user)

        # Create Clinic Staff
        for staff_data in data['clinic_staff']:
            user = CustomUser.objects.create_user(username=staff_data['username'], email=staff_data['email'], password='password')
            ClinicStaff.objects.create(user=user)

        # Create Lecturers
        for lecturer_data in data['lecturers']:
            user = CustomUser.objects.create_user(username=lecturer_data['username'], email=lecturer_data['email'], password='password')
            Lecturer.objects.create(user=user, department=lecturer_data['department'])

        # Create Students
        for student_data in data['students']:
            user = CustomUser.objects.create_user(username=student_data['username'], email=student_data['email'], password='password')
            Student.objects.create(user=user, year_of_study=student_data['year_of_study'])

        # Create Courses
        for course_data in data['courses']:
            Course.objects.create(course_id=course_data['course_id'], course_name=course_data['course_name'], credits=course_data['credits'])

        # Create Results
        for result_data in data['results']:
            student = Student.objects.get(user__username=result_data['student_username'])
            course = Course.objects.get(course_id=result_data['course_id'])
            Result.objects.create(student=student, course=course, grade=result_data['grade'])

        # Create Timetable
        for timetable_data in data['timetables']:
            Timetable.objects.create(day=timetable_data['day'], course_name=timetable_data['course_name'], time=timetable_data['time'])

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))
