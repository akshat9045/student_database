from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Create your models here.
