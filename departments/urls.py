from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list_view, name='department_list'),
    path('api/', views.departments_api, name='departments_api'),
    path('api/create/', views.create_department_api, name='create_department'),
]
