from django.db import models
from django.contrib.auth.models import User
from projectminionapi.models.projects import Project


class UserProject (models.model):
    """Represents all projects created by a user"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    