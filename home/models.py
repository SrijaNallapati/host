from django.db import models

# Create your models here.

# class Courses(models.Model):
#     cno = models.IntegerField()
#     cName = models.CharField(max_length=100)
#     cContent = models.CharField(max_length=200)

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

