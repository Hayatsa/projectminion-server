"""view module for handling requests about tasks"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from projectminionapi.models import Task



class TaskView(ViewSet):
    def retrieve(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
        

    def list(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        task = Task.objects.get(user=request.auth.user)
        serializer = CreateTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(task=task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = CreateTaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'project', 'title', 'date', 'note', 'user_id')
        depth = 1


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'project', 'title', 'date', 'note']
        