from django.db import models


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    adress = models.CharField(max_length=100)
    number = models.IntegerField()
    location = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)


def __self__(self):
    return self.name


# Create your models here.
