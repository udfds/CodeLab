from django.urls import path
from .views import *

urlpatterns = [
    path('task_list', task_list, name='task_list'),
    path('task_create', task_create, name='task_create'),
    path('task_edit/<int:id>', task_edit, name='task_edit'),
    path('task_delete/<int:id>', task_delete, name='task_delete')
]
