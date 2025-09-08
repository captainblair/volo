"""
URL configuration for volo_system project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),
    path('api/auth/', include('users.urls')),
    path('api/departments/', include('departments.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/communications/', include('communications.urls')),
    path('', include('users.urls')),
    path('dashboard/', include('departments.urls')),
    path('tasks/', include('tasks.urls')),
    path('communications/', include('communications.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
