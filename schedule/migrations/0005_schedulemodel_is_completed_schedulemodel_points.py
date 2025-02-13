# Generated by Django 4.0 on 2024-11-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_schedulemodel_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulemodel',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedulemodel',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
