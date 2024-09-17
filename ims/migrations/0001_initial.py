# Generated by Django 5.1.1 on 2024-09-13 21:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10, unique=True)),
                ('course_name', models.CharField(max_length=200)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_study', models.IntegerField()),
                ('courses_registered', models.ManyToManyField(related_name='students', to='ims.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.student')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('lecturer', 'Lecturer'), ('clinic', 'Clinic Staff')], default='student', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='user_role',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ims.userrole'),
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('courses_taught', models.ManyToManyField(related_name='lecturers', to='ims.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ims.userrole')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ims.userrole')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ims.userrole')),
            ],
        ),
    ]
