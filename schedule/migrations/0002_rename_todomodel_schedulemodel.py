# Generated by Django 4.0 on 2024-11-18 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoModel',
            new_name='ScheduleModel',
        ),
    ]
