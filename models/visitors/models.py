from django.db import models
from team.models import Teams

# Create your models here.
class Visitors(models.Model):
    name : models.CharField(max_length=255) # type: ignore
    teams: models.ForeignKey(Teams, related_name='clients', on_delete=models.CASCADE) # type: ignore
#we can use SET_NULLinsted of CASCADE
