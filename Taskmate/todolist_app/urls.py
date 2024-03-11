from django.urls import path,include
from todolist_app import views

urlpatterns=[
    path('', views.TodoList, name='TodoList'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('pending_task/<task_id>', views.pending_task, name='pending_task'),
    path('completed_task/<task_id>', views.completed_task, name='completed_task'),
]