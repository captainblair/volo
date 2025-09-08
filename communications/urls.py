from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.messages_view, name='messages'),
    path('chat/', views.chat_view, name='chat'),
    path('api/notifications/', views.notifications_api, name='notifications_api'),
    path('api/send-message/', views.send_message_api, name='send_message'),
    path('api/notifications/<int:notification_id>/read/', views.mark_notification_read_api, name='mark_notification_read'),
]
