from django.urls import path
from . import views


urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('task_completed/<int:pk>', views.task_completed, name='task_completed'),
    path('task_uncompleted/<int:pk>', views.task_uncompleted, name='task_uncompleted'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task')
]
