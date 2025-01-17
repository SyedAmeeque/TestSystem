from django.db import models
from .subject_category import Subject

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=50) 
    email = models.EmailField()
    batch = models.CharField(max_length=10)
    course = models.ForeignKey('Subject', on_delete=models.CASCADE, default=1)
    password = models.CharField(max_length=500)
    
    def __str__(self):
        return self.fullname