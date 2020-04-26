from django.shortcuts import render


def task_list(request):
    task_name = "Task A"

    return render(request, 'tasks/task_list.html', {'task_name': task_name})
