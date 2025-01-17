from django.db import models
from .subject_category import Subject


class Questions(models.Model):
    question = models.CharField(max_length=200)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    actual_answer = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)