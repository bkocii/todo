from django.shortcuts import render, redirect, get_object_or_404
from . models import Task
# Create your views here.


def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('home')


# todo : the argument 'pk' has to match url int:'pk'
def task_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def task_uncompleted(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        edited_task = request.POST['task']
        task.task = edited_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task
        }
        return render(request, 'edit_task.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


