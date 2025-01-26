from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=225)
    username = models.ManyToManyField(User)
