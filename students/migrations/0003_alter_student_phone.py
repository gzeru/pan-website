# Generated by Django 4.2.1 on 2023-05-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_student_joined_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
