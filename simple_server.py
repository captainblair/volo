#!/usr/bin/env python
"""
Simple Django server for Volo Africa Communication System
"""
import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application

# Configure Django settings
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='django-insecure-volo-africa-simple-key',
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ],
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        }],
        STATIC_URL='/static/',
    )

django.setup()

def home_view(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Volo Africa - Communication System</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50">
        <div class="min-h-screen flex items-center justify-center">
            <div class="max-w-md w-full bg-white rounded-lg shadow-md p-8">
                <div class="text-center">
                    <div class="mx-auto h-12 w-12 flex items-center justify-center rounded-full bg-blue-600 mb-4">
                        <svg class="h-6 w-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
                        </svg>
                    </div>
                    <h1 class="text-3xl font-bold text-gray-900 mb-2">Volo Africa</h1>
                    <p class="text-gray-600 mb-6">Departmental Communication & Task Allocation System</p>
                    
                    <div class="space-y-4">
                        <div class="bg-green-50 border border-green-200 rounded-md p-4">
                            <h3 class="text-lg font-semibold text-green-800 mb-2">✅ System Status: Running</h3>
                            <p class="text-green-700 text-sm">Django server is successfully running!</p>
                        </div>
                        
                        <div class="bg-blue-50 border border-blue-200 rounded-md p-4">
                            <h3 class="text-lg font-semibold text-blue-800 mb-2">🚀 Features Implemented</h3>
                            <ul class="text-blue-700 text-sm space-y-1">
                                <li>• User Management & Authentication</li>
                                <li>• Department Management</li>
                                <li>• Task Allocation System</li>
                                <li>• Real-time Communication</li>
                                <li>• Responsive UI with Tailwind CSS</li>
                            </ul>
                        </div>
                        
                        <div class="bg-yellow-50 border border-yellow-200 rounded-md p-4">
                            <h3 class="text-lg font-semibold text-yellow-800 mb-2">👥 Development Team</h3>
                            <p class="text-yellow-700 text-sm">Fabian Atambo & Tony Wangolo<br>Group Harambee</p>
                        </div>
                        
                        <div class="bg-purple-50 border border-purple-200 rounded-md p-4">
                            <h3 class="text-lg font-semibold text-purple-800 mb-2">🏢 Organization</h3>
                            <p class="text-purple-700 text-sm">Volo Africa<br>Contact: Anne Apiyo - 0746821567</p>
                        </div>
                    </div>
                    
                    <div class="mt-6 text-sm text-gray-500">
                        <p>Technical University of Kenya</p>
                        <p>IBL 2305 Software Development Laboratory</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('', home_view, name='home'),
]

if __name__ == '__main__':
    execute_from_command_line(['manage.py', 'runserver', '8000'])
