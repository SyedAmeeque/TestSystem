from django.db import models
from .student import Student
from .questions import Questions
from .exam import Exam
from django.utils import timezone
from datetime import timedelta


class Paper(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    Exams = models.ManyToManyField("Exam")
    counter = models.DateTimeField(default=timezone.now)
    date_time = models.DateTimeField(auto_now=True)
    
    def time_remaining(self):
        # Calculate 30 minutes from the exact time when this method is called
        end_time = self.counter + timedelta(minutes=32)
        remaining_time = end_time - timezone.now()
        remaining_min = remaining_time.total_seconds() // 60
        return max(0, int(remaining_min))  # Ensure it does not go negativ
    