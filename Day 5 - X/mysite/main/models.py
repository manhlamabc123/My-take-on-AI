from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthday = models.DateField()
    phone_number = models.CharField(max_length=10)
    regular = models.BooleanField(null=True)
    rank = models.PositiveSmallIntegerField(null=True)

# class Game(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

# class School(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Playing(models.Model):
#     member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
#     game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

# class Enrol(models.Model):
#     member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
#     school_id = models.ForeignKey(School, on_delete=models.CASCADE)
#     school_class = models.CharField(max_length=5, null=True)