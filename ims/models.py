from django.db import models
from users.models import CustomUser as User

# Custom User model with roles
class Department(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name


# Lecturer model (linked to the User model)
class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses_taught = models.ManyToManyField('Course', related_name='lecturers')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

levels = (
    ('100','100'),
    ('200','200'),
    ('300','300'),
    ('400','400'),
    ('500','500')
)
class Level(models.Model):
    level = models.CharField(max_length=255, choices=levels)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    adviser = models.OneToOneField(Lecturer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.level

# Student model (linked to the User model)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    matric = models.CharField(max_length=50, blank=True, null=True)
    reg_no = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    Gaurdian_contact = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses_registered = models.ManyToManyField('Course', related_name='students')
    carry_over = models.ManyToManyField('Course', null=True, blank=True)
    
    approved = models.BooleanField(default=False)

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

