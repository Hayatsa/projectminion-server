from django.db import models
from projectminionapi.models.projects import Project


class Task (models.model):
    """Represents a task for a project"""
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date = models.DateField(auto_now=False, auto_now_add=False)
    note = models.CharField(max_length=200)