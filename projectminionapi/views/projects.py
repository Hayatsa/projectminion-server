"""view module for handling requests about projects"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from projectminionapi.models import Project
from projectminionapi.models.task import Task




class ProjectView(ViewSet):
    def retrieve(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
        

    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    
    def create(self, request):
        creator = request.auth.user
        serializer = CreateProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=creator)
        project = Project.objects.get(pk=serializer.data["id"])
        response_serializer = ProjectSerializer(project)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = CreateProjectSerializer(project, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # @action(methods=['post'], detail=True)
    # def signup(self, request, pk):
    #     user = request.auth.user
    #     project = Project.objects.get(pk=pk)
    #     project.users.add(user)
    #     return Response({'message': 'User added'}, status=status.HTTP_201_CREATED)
    

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'project', 'title', 'date', 'note')
    
class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Project
        fields = ('id', 'creator', 'title', 'description', 'date', 'users', 'tasks')
        

class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'date')


# if projects:
#             for id in projects:
#                 user_projects = User.objects.get(pk=id)
#                 project.projects.add(user_projects)
        