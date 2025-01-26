from django.db import models
from team.models import Teams
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

class Visitors(models.Model):
    name = models.CharField(max_length=255)
    teams= models.ForeignKey(Teams, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
#we can use SET_NULL insted of CASCADE



class TodoList(models.Model):
    Visitors= models.ForeignKey(Visitors,related_name='todoLists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='todoLists', on_delete=models.CASCADE)