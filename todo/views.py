from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework import status, filters
from .serializers import TaskSerializer
from .models import Task
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def main(request):
    return render(request, "todo/main.html")


@api_view(["GET"])
def get_single_task(request, id):
    task_get = Task.objects.get(id = id)
    if  not task_get:
        return Response(status=status.HTTP_404_NOT_FOUND)
    task_get_ser = TaskSerializer(task_get)
    return Response(data=task_get_ser.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_all_tasks(request):
    tasks_get = Task.objects.all()
    if not tasks_get:
        return Response(data=[],status=status.HTTP_200_OK)
    tasks_get_ser = TaskSerializer(tasks_get, many = True)
    return Response(data=tasks_get_ser.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def post_task(request):
    task_post_ser = TaskSerializer(data=request.data)
    if task_post_ser.is_valid():
        task_post_ser.save()
        return Response(data=task_post_ser.data, status=status.HTTP_200_OK)
    return Response(data=task_post_ser.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_task(request, id):
    task_delete_get = Task.objects.get(id = id)
    if not task_delete_get:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        task_delete_get.delete()
        return Response(data=TaskSerializer(task_delete_get).data, status=status.HTTP_200_OK)