from django.db import models
from users.models import CustomUser as User

# Custom User model with roles
   

# Student model (linked to the User model)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year_of_study = models.IntegerField()
    courses_registered = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return self.user.username

# Lecturer model (linked to the User model)
class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    courses_taught = models.ManyToManyField('Course', related_name='lecturers')

    def __str__(self):
        return self.user.username

# Admin model (linked to the User model)
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Clinic Staff model (linked to the User model)
class ClinicStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Course model (holds course details)
class Course(models.Model):
    course_id = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=200)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.course_name} ({self.course_id})"

# Result model (holds student grades)
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.course_name} : {self.grade}"


class Timetable(models.Model):
    day = models.CharField(max_length=10)  # e.g., "Monday"
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course} on {self.day} at {self.time}"

