from django.shortcuts import render
from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-is_modified')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-is_modified')
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)
