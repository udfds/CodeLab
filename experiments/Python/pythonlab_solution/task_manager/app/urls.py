from django.urls import path
from .views.task_views import *
from .views.user_views import *

urlpatterns = [
    path('task_list', task_list, name='task_list'),
    path('task_create', task_create, name='task_create'),
    path('task_edit/<int:id>', task_edit, name='task_edit'),
    path('task_delete/<int:id>', task_delete, name='task_delete'),
    path('user_list', user_list, name='user_list'),
    path('user_create', user_create, name='user_create'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout')
]
