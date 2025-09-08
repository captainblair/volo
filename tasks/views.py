from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Task, TaskComment
from departments.models import Department
from users.models import CustomUser

@login_required
def task_list_view(request):
    if request.user.role == 'admin':
        tasks = Task.objects.all()
    elif request.user.role == 'manager':
        tasks = Task.objects.filter(department=request.user.department)
    else:
        tasks = Task.objects.filter(assigned_to=request.user)
    
    return render(request, 'tasks/list.html', {'tasks': tasks})

@api_view(['GET'])
@login_required
def tasks_api(request):
    if request.user.role == 'admin':
        tasks = Task.objects.all()
    elif request.user.role == 'manager':
        tasks = Task.objects.filter(department=request.user.department)
    else:
        tasks = Task.objects.filter(assigned_to=request.user)
    
    data = []
    for task in tasks:
        data.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'priority': task.priority,
            'assigned_to': task.assigned_to.full_name,
            'assigned_by': task.assigned_by.full_name,
            'department': task.department.name,
            'due_date': task.due_date.isoformat() if task.due_date else None,
            'is_overdue': task.is_overdue,
            'created_at': task.created_at.isoformat(),
        })
    return Response(data)

@api_view(['POST'])
@login_required
def create_task_api(request):
    try:
        title = request.data.get('title')
        description = request.data.get('description')
        assigned_to_id = request.data.get('assigned_to_id')
        department_id = request.data.get('department_id')
        priority = request.data.get('priority', 'medium')
        due_date = request.data.get('due_date')
        
        assigned_to = CustomUser.objects.get(id=assigned_to_id)
        department = Department.objects.get(id=department_id)
        
        # Check if user can assign tasks to this department
        if request.user.role == 'employee' and request.user.department != department:
            return Response({'error': 'Cannot assign tasks outside your department'}, 
                          status=status.HTTP_403_FORBIDDEN)
        
        task = Task.objects.create(
            title=title,
            description=description,
            assigned_to=assigned_to,
            assigned_by=request.user,
            department=department,
            priority=priority,
            due_date=due_date
        )
        
        return Response({'message': 'Task created successfully', 'task_id': task.id}, 
                       status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@login_required
def update_task_status_api(request, task_id):
    try:
        task = get_object_or_404(Task, id=task_id)
        
        # Check permissions
        if request.user != task.assigned_to and request.user.role not in ['admin', 'manager']:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        new_status = request.data.get('status')
        if new_status in dict(Task.STATUS_CHOICES):
            task.status = new_status
            if new_status == 'completed':
                task.completed_at = timezone.now()
            task.save()
            
            return Response({'message': 'Task status updated successfully'})
        else:
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
