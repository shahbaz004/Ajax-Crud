from django.db import models


# Create your models here.
class Student(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    roll = models.CharField("Roll No", max_length=11)
    mobile = models.CharField(max_length=13)
    program = models.CharField(max_length=10)
