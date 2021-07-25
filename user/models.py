from os import name
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    info = models.TextField()

    def __str__(self):
        return self.name