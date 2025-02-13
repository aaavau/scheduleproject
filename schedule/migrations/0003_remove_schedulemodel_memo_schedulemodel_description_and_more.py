# Generated by Django 4.0 on 2024-11-20 03:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_rename_todomodel_schedulemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulemodel',
            name='memo',
        ),
        migrations.AddField(
            model_name='schedulemodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedulemodel',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='schedulemodel',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='schedulemodel',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
