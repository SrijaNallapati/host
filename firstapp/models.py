from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    salary = models.FloatField()
