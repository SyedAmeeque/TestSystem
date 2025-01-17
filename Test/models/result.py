from django.db import models
from .student import Student
# Create your models here.
class Result(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE) 
    score = models.IntegerField()
    result = models.CharField(max_length=200)
    attempted_questions = models.IntegerField()
    total_questions = models.CharField(max_length=20)
    
    def __str__(self):
        return self.result