from django.db import models


# models.py 수정을 했다? => makemigration => migrate

class Student(models.Model):
    name = models.CharField(max_length=10)
    major = models.CharField(max_length=20)
    age = models.IntegerField()
    gpa = models.FloatField()