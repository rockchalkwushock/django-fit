from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    age = models.IntegerField()
    avatar = models.ImageField()
    date_of_birth = models.CharField(max_length=30)
    distance_unit = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    height = models.IntegerField()
    height_unit = models.CharField(max_length=10)
    timezone = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    weight = models.IntegerField()
    weight_unit = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.username} {self.age}'
