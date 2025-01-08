from django.urls import path
from .views import get_tasks, completed_tasks, create_task, home, is_done, unfinished_tasks

urlpatterns = [
    path("", home, name="home"),
    path("tasks/", get_tasks, name="get_tasks"),
    path("tasks/<int:task_id>/", get_tasks, name="get_tasks"),
    path("completed_tasks/", completed_tasks, name = "completed_tasks"),
    path("create_task/", create_task, name = "create_task"), 
    path("is_done/<int:task_id>/", is_done, name="is_done"),
    path("unfinished_tasks/", unfinished_tasks, name="unfinished_tasks")
]