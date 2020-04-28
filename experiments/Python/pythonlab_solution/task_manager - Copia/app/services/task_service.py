from ..models import Task


def task_save(task):
    Task.objects.create(title=task.title, description=task.description,
                        expired_date=task.expired_date, priority=task.priority, user=task.user)


def task_list(user):
    return Task.objects.filter(user=user).all()


def task_get(id):
    return Task.objects.get(id=id)


def task_update(task, draft_task):
    task.title = draft_task.title
    task.description = draft_task.description
    task.expired_date = draft_task.expired_date
    task.priority = draft_task.priority
    task.save(force_update=True)


def task_delete(task):
    task.delete()

