# Generated by Django 4.0.1 on 2022-03-15 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='student_teacher_post',
            new_name='post',
        ),
    ]
