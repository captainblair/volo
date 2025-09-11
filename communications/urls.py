from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.messages_view, name='messages'),
    path('chat/', views.chat_view, name='chat'),
    path('api/notifications/', views.notifications_api, name='notifications_api'),
    path('api/send-message/', views.send_message_api, name='send_message'),
    path('api/notifications/<int:notification_id>/read/', views.mark_notification_read_api, name='mark_notification_read'),
    path('api/chat-rooms/', views.chat_rooms_api, name='chat_rooms_api'),
    path('api/chat-rooms/<int:room_id>/messages/', views.chat_messages_api, name='chat_messages_api'),
    path('api/chat-rooms/<int:room_id>/send/', views.send_chat_message_api, name='send_chat_message_api'),
]
