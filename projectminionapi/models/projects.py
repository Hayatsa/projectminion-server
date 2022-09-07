from django.db import models
from django.contrib.auth.models import User


class Project (models.Model):
    """Represents a project created by user"""
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    users = models.ManyToManyField(User, related_name="projects")