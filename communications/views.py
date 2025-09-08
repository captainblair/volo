from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Message, Notification, ChatRoom, ChatMessage
from users.models import CustomUser

@login_required
def messages_view(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'communications/messages.html', {'messages': messages})

@login_required
def chat_view(request):
    chat_rooms = ChatRoom.objects.filter(members=request.user, is_active=True)
    return render(request, 'communications/chat.html', {'chat_rooms': chat_rooms})

@api_view(['GET'])
@login_required
def notifications_api(request):
    notifications = Notification.objects.filter(user=request.user)[:20]
    data = []
    for notification in notifications:
        data.append({
            'id': notification.id,
            'type': notification.notification_type,
            'title': notification.title,
            'message': notification.message,
            'is_read': notification.is_read,
            'created_at': notification.created_at.isoformat(),
        })
    return Response(data)

@api_view(['POST'])
@login_required
def send_message_api(request):
    try:
        recipient_id = request.data.get('recipient_id')
        subject = request.data.get('subject', '')
        content = request.data.get('content')
        
        recipient = CustomUser.objects.get(id=recipient_id)
        
        message = Message.objects.create(
            sender=request.user,
            recipient=recipient,
            subject=subject,
            content=content
        )
        
        # Create notification for recipient
        Notification.objects.create(
            user=recipient,
            notification_type='message_received',
            title=f'New message from {request.user.full_name}',
            message=f'Subject: {subject}'
        )
        
        return Response({'message': 'Message sent successfully'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@login_required
def mark_notification_read_api(request, notification_id):
    try:
        notification = get_object_or_404(Notification, id=notification_id, user=request.user)
        notification.is_read = True
        notification.read_at = timezone.now()
        notification.save()
        
        return Response({'message': 'Notification marked as read'})
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
