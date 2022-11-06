from django.urls import path
from .views import index, main,get_single_task,get_all_tasks,post_task,delete_task



urlpatterns = [
    path('index/', view=index, name="index"),
    path('', view = main, name="main"),
    path('api/AllTasks', view= get_all_tasks, name="api_get_all_tasks"),
    path('api/getTask/<int:id>', view=get_single_task),
    path('api/postTask', view=post_task),
    path('api/deleteTask/<int:id>', view=delete_task),
]