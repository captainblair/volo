from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department
from users.models import CustomUser

@login_required
def department_list_view(request):
    departments = Department.objects.filter(is_active=True)
    return render(request, 'departments/list.html', {'departments': departments})

@api_view(['GET'])
@login_required
def departments_api(request):
    departments = Department.objects.filter(is_active=True)
    data = []
    for dept in departments:
        data.append({
            'id': dept.id,
            'name': dept.name,
            'description': dept.description,
            'manager': dept.manager.full_name if dept.manager else None,
            'employee_count': dept.employee_count,
            'active_tasks_count': dept.active_tasks_count,
        })
    return Response(data)

@api_view(['POST'])
@login_required
def create_department_api(request):
    if request.user.role != 'admin':
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    try:
        name = request.data.get('name')
        description = request.data.get('description', '')
        manager_id = request.data.get('manager_id')
        
        department = Department.objects.create(
            name=name,
            description=description
        )
        
        if manager_id:
            try:
                manager = CustomUser.objects.get(id=manager_id, role='manager')
                department.manager = manager
                department.save()
            except CustomUser.DoesNotExist:
                pass
        
        return Response({'message': 'Department created successfully'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
