from django.db import models
from .student import Student
from .questions import Questions


class Exam(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    question = models.ForeignKey('Questions', on_delete=models.CASCADE)
    answer_of_student = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now=True)
    
    