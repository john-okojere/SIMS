# Generated by Django 4.2.15 on 2024-09-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0004_remove_timetable_course_name_timetable_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
