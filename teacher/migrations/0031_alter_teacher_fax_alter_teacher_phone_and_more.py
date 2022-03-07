# Generated by Django 4.0.1 on 2022-03-07 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_student_otp_student_user'),
        ('teacher', '0030_alter_teacher_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='fax',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(blank=True, to='student.Student'),
        ),
    ]