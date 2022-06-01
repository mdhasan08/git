# Generated by Django 4.0.1 on 2022-03-16 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_student_slug'),
        ('teacher', '0033_alter_teacher_phone'),
        ('post', '0002_rename_student_teacher_post_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='student.student'),
        ),
        migrations.AddField(
            model_name='post',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teacher.teacher'),
        ),
    ]
