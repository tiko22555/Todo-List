from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from datetime import datetime, timedelta

def home(request):
    tasks_future = Todo.objects.filter(title__in = ["Duolingo", "LeetCode"], deadline = datetime.now().date() + timedelta(days=1), done = False)

    if not tasks_future:
        Todo.objects.create(title = "Duolingo",
                            desc = "1 hour learning englsih", 
                            deadline = datetime.now().date() + timedelta(days=1))
        Todo.objects.create(title = "LeetCode",
                            desc = "Solve 2 problems", 
                            deadline = datetime.now().date() + timedelta(days=1))
    return render(request, "home.html", {})

def get_tasks(request, task_id = None):
    if not task_id:
        tasks = Todo.objects.filter(deadline = datetime.now().date(), done = False)       
        return render(request, "tasks.html", {"tasks": tasks})
    else:
        task = get_object_or_404(Todo, pk = task_id)
        return render(request, "desc.html", {"task":task})
def create_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        date_str= request.POST["date"]
        date = datetime.strptime(date_str, '%Y-%m-%d')
        Todo.objects.create(title = title, desc = desc, deadline = date)
        return redirect("home")
    return render(request, "create_task.html", {})
def completed_tasks(request):
    tasks = Todo.objects.filter(done = True).order_by("-deadline")
    return render(request, "completed_tasks.html", {"tasks": tasks})
def is_done(request, task_id):
    task = get_object_or_404(Todo, pk = task_id)
    task.done = True
    task.save()
    return redirect("get_tasks")
def unfinished_tasks(request):
    tasks = Todo.objects.filter(done = False).order_by("deadline")
    return render(request, "unfinished_tasks.html", {"tasks": tasks})



