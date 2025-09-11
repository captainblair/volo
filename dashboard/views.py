from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count, Q
from tasks.models import Task
from communications.models import Message, ChatMessage
from departments.models import Department
from users.models import CustomUser
from django.utils import timezone
from datetime import timedelta

@login_required
def dashboard_view(request):
    """Dashboard view with real data"""
    user = request.user
    
    # Get user's tasks
    if user.role == 'admin':
        user_tasks = Task.objects.all()
    elif user.role == 'manager':
        user_tasks = Task.objects.filter(department=user.department)
    else:
        user_tasks = Task.objects.filter(assigned_to=user)
    
    # Calculate stats
    active_tasks = user_tasks.filter(status__in=['pending', 'in_progress']).count()
    completed_tasks = user_tasks.filter(status='completed').count()
    
    # Get unread messages
    unread_messages = Message.objects.filter(recipient=user, is_read=False).count()
    
    # Get team members count
    if user.department:
        team_members = CustomUser.objects.filter(department=user.department).count()
    else:
        team_members = CustomUser.objects.count()
    
    # Get recent tasks
    recent_tasks = user_tasks.order_by('-created_at')[:3]
    
    # Get recent messages
    recent_messages = Message.objects.filter(recipient=user).order_by('-created_at')[:2]
    
    # Get recent activity (last 24 hours)
    yesterday = timezone.now() - timedelta(days=1)
    recent_completed_tasks = Task.objects.filter(
        completed_at__gte=yesterday,
        department=user.department if user.department else None
    ).order_by('-completed_at')[:4]
    
    context = {
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks,
        'unread_messages': unread_messages,
        'team_members': team_members,
        'recent_tasks': recent_tasks,
        'recent_messages': recent_messages,
        'recent_completed_tasks': recent_completed_tasks,
    }
    
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def dashboard_stats_api(request):
    """API endpoint for dashboard statistics"""
    user = request.user
    
    # Get user's tasks based on role
    if user.role == 'admin':
        user_tasks = Task.objects.all()
        all_tasks = Task.objects.all()
    elif user.role == 'manager':
        user_tasks = Task.objects.filter(department=user.department)
        all_tasks = Task.objects.filter(department=user.department)
    else:
        user_tasks = Task.objects.filter(assigned_to=user)
        all_tasks = user_tasks
    
    # Calculate comprehensive stats
    stats = {
        'active_tasks': user_tasks.filter(status__in=['pending', 'in_progress']).count(),
        'unread_messages': Message.objects.filter(recipient=user, is_read=False).count(),
        'pending_approvals': user_tasks.filter(status='pending').count(),
        'team_performance': 85,  # This could be calculated based on completion rates
        'new_messages_today': Message.objects.filter(
            recipient=user, 
            created_at__date=timezone.now().date()
        ).count(),
        'urgent_approvals': user_tasks.filter(status='pending', priority='high').count(),
        'task_completion_rate': _calculate_completion_rate(all_tasks),
        'total_tasks': all_tasks.count(),
        'completed_tasks': all_tasks.filter(status='completed').count(),
        'in_progress_tasks': all_tasks.filter(status='in_progress').count(),
        'overdue_tasks': all_tasks.filter(
            due_date__lt=timezone.now().date(),
            status__in=['pending', 'in_progress']
        ).count(),
    }
    
    return JsonResponse(stats)

def _calculate_completion_rate(tasks):
    """Calculate task completion rate percentage"""
    total = tasks.count()
    if total == 0:
        return 0
    completed = tasks.filter(status='completed').count()
    return round((completed / total) * 100)
