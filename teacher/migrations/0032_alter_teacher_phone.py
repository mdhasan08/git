# Generated by Django 4.0.1 on 2022-03-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0031_alter_teacher_fax_alter_teacher_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.PositiveBigIntegerField(max_length=14, unique=True),
        ),
    ]