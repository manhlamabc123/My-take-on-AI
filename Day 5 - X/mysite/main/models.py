from statistics import mode
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=10)
    regular = models.BooleanField(null=True)
    rank = models.IntegerField(null=True)

    def is_regular():
        pass