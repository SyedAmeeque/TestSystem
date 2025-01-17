from django.db import models

# Create your models here.
class Subject(models.Model):
    Subject = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.Subject