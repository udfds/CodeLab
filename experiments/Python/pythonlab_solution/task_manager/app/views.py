from django.shortcuts import render, redirect
from .forms import TaskForm
from .entities.task import Task
from .services import task_service


def task_list(request):
    tasks = task_service.task_list()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            title = task_form.cleaned_data['title']
            description = task_form.cleaned_data['description']
            expired_date = task_form.cleaned_data['expired_date']
            priority = task_form.cleaned_data['priority']

            new_task = Task(title=title, description=description, expired_date=expired_date, priority=priority)
            task_service.task_save(new_task)
            return redirect('task_list')
    else:
        task_form = TaskForm()

    return render(request, 'tasks/task_create.html', {'task_form': task_form})


def task_edit(request, id):
    task = task_service.task_get(id)
    task_form = TaskForm(request.POST or None, instance=task)
    if task_form.is_valid():
        title = task_form.cleaned_data['title']
        description = task_form.cleaned_data['description']
        expired_date = task_form.cleaned_data['expired_date']
        priority = task_form.cleaned_data['priority']

        draft_task = Task(title=title, description=description, expired_date=expired_date, priority=priority)
        task_service.task_update(task, draft_task)
        return redirect('task_list')
    return render(request, 'tasks/task_edit.html', {'task_form': task_form})


def task_delete(request, id):
    task = task_service.task_get(id)
    if request.method == 'POST':
        task_service.task_delete(task)
        return redirect('task_list')
    return render(request, 'tasks/task_delete.html', {'task': task})