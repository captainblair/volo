"""
URL configuration for volo_system project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/auth/', include('users.urls')),
    path('api/departments/', include('departments.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/communications/', include('communications.urls')),
    path('', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('tasks/', include('tasks.urls')),
    path('communications/', include('communications.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
