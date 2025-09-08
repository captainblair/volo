from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_view, name='task_list'),
    path('api/', views.tasks_api, name='tasks_api'),
    path('api/create/', views.create_task_api, name='create_task'),
    path('api/<int:task_id>/update-status/', views.update_task_status_api, name='update_task_status'),
]
