from django.db import models

class ScheduleModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="Default description") 
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False) 


    def __str__(self):
        return self.title
