from django.db import models
from .student import Student

class Paper_finish_time(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    Date_time = models.DateTimeField(auto_now=True)