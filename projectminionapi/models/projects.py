from django.db import models
from projectminionapi.models.user_project import UserProject


class Project (models.model):
    """Represents a project created by user"""
    
    creator = models.ForeignKey(UserProject, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)