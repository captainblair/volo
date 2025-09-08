#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from django.template import Template, Context
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Configure minimal Django settings
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='volo-africa-key-2024',
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
                'NAME': 'volo_db.sqlite3',
            }
        },
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['templates'],
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
        STATICFILES_DIRS=['static'],
    )

django.setup()

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', 'admin')
        password = request.POST.get('password', 'admin')
        return HttpResponseRedirect('/dashboard/')
    
    return HttpResponse('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Volo Africa</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#1e40af',
                        secondary: '#64748b',
                        accent: '#f59e0b',
                    },
                    animation: {
                        'fade-in': 'fadeIn 0.5s ease-in-out',
                        'slide-up': 'slideUp 0.6s ease-out',
                        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                    }
                }
            }
        }
    </script>
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideUp {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .gradient-bg {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .glass-effect {
            backdrop-filter: blur(16px) saturate(180%);
            background-color: rgba(255, 255, 255, 0.75);
            border: 1px solid rgba(209, 213, 219, 0.3);
        }
    </style>
</head>
<body class="min-h-screen gradient-bg relative overflow-hidden">
    <!-- Animated background elements -->
    <div class="absolute inset-0 overflow-hidden">
        <div class="absolute -top-40 -right-40 w-80 h-80 bg-white opacity-10 rounded-full animate-pulse-slow"></div>
        <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-white opacity-5 rounded-full animate-pulse-slow" style="animation-delay: 1s;"></div>
        <div class="absolute top-1/2 left-1/4 w-32 h-32 bg-white opacity-10 rounded-full animate-pulse-slow" style="animation-delay: 2s;"></div>
    </div>
    
    <div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="max-w-md w-full space-y-8 animate-slide-up">
            <!-- Logo and Header -->
            <div class="text-center">
                <div class="mx-auto h-20 w-20 flex items-center justify-center rounded-full bg-white shadow-2xl mb-6 animate-fade-in">
                    <div class="h-12 w-12 flex items-center justify-center rounded-full bg-gradient-to-r from-blue-600 to-purple-600">
                        <i class="fas fa-building text-white text-2xl"></i>
                    </div>
                </div>
                <h2 class="text-4xl font-extrabold text-white mb-2 animate-fade-in">
                    Volo Africa
                </h2>
                <p class="text-xl text-blue-100 mb-2 animate-fade-in" style="animation-delay: 0.2s;">
                    Communication System
                </p>
                <p class="text-sm text-blue-200 animate-fade-in" style="animation-delay: 0.4s;">
                    Departmental Task Management & Collaboration Platform
                </p>
            </div>

            <!-- Login Form -->
            <div class="glass-effect rounded-2xl shadow-2xl p-8 animate-fade-in" style="animation-delay: 0.6s;">
                <form class="space-y-6" method="post">
                    <div class="space-y-4">
                        <div class="relative">
                            <label class="block text-sm font-medium text-gray-700 mb-2">
                                <i class="fas fa-user mr-2 text-blue-600"></i>Username
                            </label>
                            <input name="username" type="text" required 
                                   class="appearance-none relative block w-full px-4 py-3 border border-gray-300 placeholder-gray-400 text-gray-900 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 bg-white/80" 
                                   placeholder="Enter your username"
                                   value="admin">
                        </div>
                        <div class="relative">
                            <label class="block text-sm font-medium text-gray-700 mb-2">
                                <i class="fas fa-lock mr-2 text-blue-600"></i>Password
                            </label>
                            <input name="password" type="password" required 
                                   class="appearance-none relative block w-full px-4 py-3 border border-gray-300 placeholder-gray-400 text-gray-900 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 bg-white/80" 
                                   placeholder="Enter your password"
                                   value="admin">
                        </div>
                    </div>

                    <div class="flex items-center justify-between">
                        <div class="flex items-center">
                            <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded">
                            <label for="remember-me" class="ml-2 block text-sm text-gray-700">
                                Remember me
                            </label>
                        </div>
                        <div class="text-sm">
                            <a href="#" class="font-medium text-blue-600 hover:text-blue-500 transition-colors">
                                Forgot password?
                            </a>
                        </div>
                    </div>

                    <div>
                        <button type="submit" 
                                class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-xl text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-200 transform hover:scale-105 shadow-lg">
                            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                                <i class="fas fa-sign-in-alt text-blue-300 group-hover:text-blue-200 transition-colors"></i>
                            </span>
                            Sign in to Dashboard
                        </button>
                    </div>
                </form>

                <!-- Demo Credentials -->
                <div class="mt-6 p-4 bg-blue-50 rounded-xl border border-blue-200">
                    <h4 class="text-sm font-medium text-blue-800 mb-2">
                        <i class="fas fa-info-circle mr-2"></i>Demo Credentials
                    </h4>
                    <div class="text-xs text-blue-700 space-y-1">
                        <p><strong>Username:</strong> admin</p>
                        <p><strong>Password:</strong> admin</p>
                        <p class="text-blue-600 mt-2">Click "Sign in to Dashboard" to continue</p>
                    </div>
                </div>
            </div>

            <!-- Footer -->
            <div class="text-center text-blue-200 text-sm animate-fade-in" style="animation-delay: 0.8s;">
                <p>© 2024 Volo Africa | Technical University of Kenya</p>
                <p class="mt-1">Developed by Fabian Atambo & Tony Wangolo</p>
            </div>
        </div>
    </div>
    
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</body>
</html>
    ''')

def dashboard_view(request):
    return HttpResponse('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Volo Africa</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-50 min-h-screen">
    <!-- Navigation -->
    <nav class="bg-white shadow-lg border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <h1 class="text-2xl font-bold text-blue-600">Volo Africa</h1>
                    <div class="hidden md:ml-6 md:flex md:space-x-8">
                        <a href="/dashboard/" class="text-blue-600 px-3 py-2 rounded-md text-sm font-medium">
                            <i class="fas fa-tachometer-alt mr-2"></i>Dashboard
                        </a>
                        <a href="/tasks/" class="text-gray-900 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">
                            <i class="fas fa-tasks mr-2"></i>Tasks
                        </a>
                        <a href="/departments/" class="text-gray-900 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">
                            <i class="fas fa-building mr-2"></i>Departments
                        </a>
                        <a href="/messages/" class="text-gray-900 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">
                            <i class="fas fa-envelope mr-2"></i>Messages
                        </a>
                        <a href="/chat/" class="text-gray-900 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">
                            <i class="fas fa-comments mr-2"></i>Chat
                        </a>
                    </div>
                </div>
                <div class="flex items-center">
                    <span class="text-gray-700 mr-4">Welcome, Admin</span>
                    <a href="/" class="text-gray-500 hover:text-gray-700">
                        <i class="fas fa-sign-out-alt"></i>
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="py-6">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 class="text-3xl font-bold text-gray-900 mb-8">Welcome back, Admin!</h1>
            
            <!-- Stats Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                <div class="bg-white overflow-hidden shadow rounded-lg">
                    <div class="p-5">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <i class="fas fa-tasks text-2xl text-blue-600"></i>
                            </div>
                            <div class="ml-5">
                                <dt class="text-sm font-medium text-gray-500">My Tasks</dt>
                                <dd class="text-lg font-medium text-gray-900">12</dd>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white overflow-hidden shadow rounded-lg">
                    <div class="p-5">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <i class="fas fa-clock text-2xl text-yellow-600"></i>
                            </div>
                            <div class="ml-5">
                                <dt class="text-sm font-medium text-gray-500">Pending</dt>
                                <dd class="text-lg font-medium text-gray-900">5</dd>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white overflow-hidden shadow rounded-lg">
                    <div class="p-5">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <i class="fas fa-envelope text-2xl text-green-600"></i>
                            </div>
                            <div class="ml-5">
                                <dt class="text-sm font-medium text-gray-500">Messages</dt>
                                <dd class="text-lg font-medium text-gray-900">3</dd>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white overflow-hidden shadow rounded-lg">
                    <div class="p-5">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <i class="fas fa-users text-2xl text-purple-600"></i>
                            </div>
                            <div class="ml-5">
                                <dt class="text-sm font-medium text-gray-500">Team</dt>
                                <dd class="text-lg font-medium text-gray-900">8</dd>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Recent Tasks -->
            <div class="bg-white shadow rounded-lg">
                <div class="px-6 py-4 border-b border-gray-200">
                    <h3 class="text-lg font-medium text-gray-900">Recent Tasks</h3>
                </div>
                <div class="p-6">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                            <div>
                                <h4 class="text-sm font-medium text-gray-900">Update marketing materials</h4>
                                <p class="text-sm text-gray-500">Marketing Department</p>
                            </div>
                            <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full bg-yellow-100 text-yellow-800">Pending</span>
                        </div>
                        <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                            <div>
                                <h4 class="text-sm font-medium text-gray-900">Fix server issues</h4>
                                <p class="text-sm text-gray-500">IT Department</p>
                            </div>
                            <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full bg-blue-100 text-blue-800">In Progress</span>
                        </div>
                        <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                            <div>
                                <h4 class="text-sm font-medium text-gray-900">Prepare quarterly report</h4>
                                <p class="text-sm text-gray-500">Finance Department</p>
                            </div>
                            <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full bg-green-100 text-green-800">Completed</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
    ''')

def tasks_view(request):
    if request.method == 'POST':
        # Handle task creation
        return HttpResponseRedirect('/tasks/')
    
    return HttpResponse('''
<!DOCTYPE html>
<html>
<head>
    <title>Tasks - Volo Africa</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <nav class="bg-white shadow mb-6">
        <div class="max-w-7xl mx-auto px-4">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <h1 class="text-xl font-bold text-blue-600">Volo Africa</h1>
                    <div class="ml-6 flex space-x-4">
                        <a href="/dashboard/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Dashboard</a>
                        <a href="/tasks/" class="text-blue-600 px-3 py-2 font-medium">Tasks</a>
                        <a href="/departments/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Departments</a>
                        <a href="/messages/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Messages</a>
                        <a href="/chat/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Chat</a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    
    <div class="max-w-7xl mx-auto px-4">
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-bold">Task Management</h2>
            <button onclick="showCreateForm()" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
                <i class="fas fa-plus mr-2"></i>New Task
            </button>
        </div>
        
        <!-- Task List -->
        <div class="bg-white rounded-lg shadow">
            <div class="p-6">
                <div class="space-y-4">
                    <div class="border-l-4 border-red-500 bg-red-50 p-4 rounded">
                        <div class="flex justify-between items-start">
                            <div>
                                <h3 class="font-semibold text-red-800">Fix server connectivity issues</h3>
                                <p class="text-red-600 text-sm mt-1">IT Department • Assigned to: John Doe</p>
                                <p class="text-red-500 text-xs mt-2">Due: Today • Priority: High</p>
                            </div>
                            <span class="bg-red-100 text-red-800 px-2 py-1 rounded text-xs">Urgent</span>
                        </div>
                    </div>
                    
                    <div class="border-l-4 border-yellow-500 bg-yellow-50 p-4 rounded">
                        <div class="flex justify-between items-start">
                            <div>
                                <h3 class="font-semibold text-yellow-800">Update marketing materials</h3>
                                <p class="text-yellow-600 text-sm mt-1">Marketing Department • Assigned to: Jane Smith</p>
                                <p class="text-yellow-500 text-xs mt-2">Due: Tomorrow • Priority: Medium</p>
                            </div>
                            <span class="bg-yellow-100 text-yellow-800 px-2 py-1 rounded text-xs">In Progress</span>
                        </div>
                    </div>
                    
                    <div class="border-l-4 border-green-500 bg-green-50 p-4 rounded">
                        <div class="flex justify-between items-start">
                            <div>
                                <h3 class="font-semibold text-green-800">Quarterly report completed</h3>
                                <p class="text-green-600 text-sm mt-1">Finance Department • Assigned to: Mike Johnson</p>
                                <p class="text-green-500 text-xs mt-2">Completed: Yesterday</p>
                            </div>
                            <span class="bg-green-100 text-green-800 px-2 py-1 rounded text-xs">Completed</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Create Task Modal -->
    <div id="createModal" class="fixed inset-0 bg-black bg-opacity-50 hidden">
        <div class="flex items-center justify-center min-h-screen p-4">
            <div class="bg-white rounded-lg max-w-md w-full p-6">
                <h3 class="text-lg font-semibold mb-4">Create New Task</h3>
                <form method="post">
                    <div class="space-y-4">
                        <input type="text" placeholder="Task title" class="w-full p-3 border rounded">
                        <textarea placeholder="Description" class="w-full p-3 border rounded h-24"></textarea>
                        <select class="w-full p-3 border rounded">
                            <option>Select Department</option>
                            <option>IT Department</option>
                            <option>Marketing Department</option>
                            <option>Finance Department</option>
                        </select>
                        <select class="w-full p-3 border rounded">
                            <option>Priority Level</option>
                            <option>Low</option>
                            <option>Medium</option>
                            <option>High</option>
                            <option>Urgent</option>
                        </select>
                    </div>
                    <div class="flex justify-end space-x-3 mt-6">
                        <button type="button" onclick="hideCreateForm()" class="px-4 py-2 text-gray-600 border rounded hover:bg-gray-50">Cancel</button>
                        <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">Create Task</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    
    <script>
        function showCreateForm() {
            document.getElementById('createModal').classList.remove('hidden');
        }
        function hideCreateForm() {
            document.getElementById('createModal').classList.add('hidden');
        }
    </script>
</body>
</html>
    ''')

def departments_view(request):
    return HttpResponse('''
<!DOCTYPE html>
<html>
<head>
    <title>Departments - Volo Africa</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <nav class="bg-white shadow mb-6">
        <div class="max-w-7xl mx-auto px-4">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <h1 class="text-xl font-bold text-blue-600">Volo Africa</h1>
                    <div class="ml-6 flex space-x-4">
                        <a href="/dashboard/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Dashboard</a>
                        <a href="/tasks/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Tasks</a>
                        <a href="/departments/" class="text-blue-600 px-3 py-2 font-medium">Departments</a>
                        <a href="/messages/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Messages</a>
                        <a href="/chat/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Chat</a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    
    <div class="max-w-7xl mx-auto px-4">
        <h2 class="text-2xl font-bold mb-6">Department Overview</h2>
        
        <div class="grid md:grid-cols-3 gap-6">
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-center mb-4">
                    <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                        <i class="fas fa-laptop-code text-blue-600 text-xl"></i>
                    </div>
                    <div class="ml-4">
                        <h3 class="font-semibold">IT Department</h3>
                        <p class="text-gray-600 text-sm">Technology & Infrastructure</p>
                    </div>
                </div>
                <div class="space-y-2 text-sm">
                    <div class="flex justify-between">
                        <span class="text-gray-600">Manager:</span>
                        <span>John Doe</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-600">Employees:</span>
                        <span>12</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-600">Active Tasks:</span>
                        <span class="text-red-600 font-medium">8</span>
                    </div>
                </div>
            </div>
            
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-center mb-4">
                    <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
                        <i class="fas fa-bullhorn text-green-600 text-xl"></i>
                    </div>
                    <div class="ml-4">
                        <h3 class="font-semibold">Marketing Department</h3>
                        <p class="text-gray-600 text-sm">Brand & Communications</p>
                    </div>
                </div>
                <div class="space-y-2 text-sm">
                    <div class="flex justify-between">
                        <span class="text-gray-600">Manager:</span>
                        <span>Jane Smith</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-600">Employees:</span>
                        <span>8</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-600">Active Tasks:</span>
                        <span class="text-yellow-600 font-medium">5</span>
                    </div>
                </div>
            </div>
            
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-center mb-4">
                    <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
                        <i class="fas fa-chart-line text-purple-600 text-xl"></i>
                    </div>
                    <div class="ml-4">
                        <h3 class="font-semibold">Finance Department</h3>
                        <p class="text-gray-600 text-sm">Accounting & Budget</p>
                    </div>
                </div>
                <div class="space-y-2 text-sm">
                    <div class="flex justify-between">
                        <span class="text-gray-600">Manager:</span>
                        <span>Mike Johnson</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-600">Employees:</span>
                        <span>6</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-600">Active Tasks:</span>
                        <span class="text-green-600 font-medium">3</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
    ''')

def messages_view(request):
    return HttpResponse('''
<!DOCTYPE html>
<html>
<head>
    <title>Messages - Volo Africa</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <nav class="bg-white shadow mb-6">
        <div class="max-w-7xl mx-auto px-4">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <h1 class="text-xl font-bold text-blue-600">Volo Africa</h1>
                    <div class="ml-6 flex space-x-4">
                        <a href="/dashboard/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Dashboard</a>
                        <a href="/tasks/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Tasks</a>
                        <a href="/departments/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Departments</a>
                        <a href="/messages/" class="text-blue-600 px-3 py-2 font-medium">Messages</a>
                        <a href="/chat/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Chat</a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    
    <div class="max-w-7xl mx-auto px-4">
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-bold">Messages</h2>
            <button onclick="showComposeModal()" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
                <i class="fas fa-plus mr-2"></i>Compose
            </button>
        </div>
        
        <div class="bg-white rounded-lg shadow">
            <div class="divide-y">
                <div class="p-4 hover:bg-gray-50 cursor-pointer">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <div class="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center text-white font-semibold">JD</div>
                            <div>
                                <p class="font-medium">John Doe</p>
                                <p class="text-sm text-gray-600">Server maintenance update</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <p class="text-sm text-gray-500">2 hours ago</p>
                            <div class="w-2 h-2 bg-blue-500 rounded-full ml-auto"></div>
                        </div>
                    </div>
                </div>
                
                <div class="p-4 hover:bg-gray-50 cursor-pointer">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <div class="w-10 h-10 bg-green-500 rounded-full flex items-center justify-center text-white font-semibold">JS</div>
                            <div>
                                <p class="font-medium">Jane Smith</p>
                                <p class="text-sm text-gray-600">Marketing campaign approval needed</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <p class="text-sm text-gray-500">5 hours ago</p>
                        </div>
                    </div>
                </div>
                
                <div class="p-4 hover:bg-gray-50 cursor-pointer">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <div class="w-10 h-10 bg-purple-500 rounded-full flex items-center justify-center text-white font-semibold">MJ</div>
                            <div>
                                <p class="font-medium">Mike Johnson</p>
                                <p class="text-sm text-gray-600">Budget report is ready for review</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <p class="text-sm text-gray-500">1 day ago</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Compose Modal -->
    <div id="composeModal" class="fixed inset-0 bg-black bg-opacity-50 hidden">
        <div class="flex items-center justify-center min-h-screen p-4">
            <div class="bg-white rounded-lg max-w-lg w-full p-6">
                <h3 class="text-lg font-semibold mb-4">Compose Message</h3>
                <div class="space-y-4">
                    <select class="w-full p-3 border rounded">
                        <option>Select recipient...</option>
                        <option>John Doe (IT Department)</option>
                        <option>Jane Smith (Marketing)</option>
                        <option>Mike Johnson (Finance)</option>
                    </select>
                    <input type="text" placeholder="Subject" class="w-full p-3 border rounded">
                    <textarea placeholder="Type your message..." class="w-full p-3 border rounded h-32"></textarea>
                </div>
                <div class="flex justify-end space-x-3 mt-6">
                    <button onclick="hideComposeModal()" class="px-4 py-2 text-gray-600 border rounded hover:bg-gray-50">Cancel</button>
                    <button class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">Send Message</button>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        function showComposeModal() {
            document.getElementById('composeModal').classList.remove('hidden');
        }
        function hideComposeModal() {
            document.getElementById('composeModal').classList.add('hidden');
        }
    </script>
</body>
</html>
    ''')

def chat_view(request):
    return HttpResponse('''
<!DOCTYPE html>
<html>
<head>
    <title>Chat - Volo Africa</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 h-screen">
    <nav class="bg-white shadow">
        <div class="max-w-7xl mx-auto px-4">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <h1 class="text-xl font-bold text-blue-600">Volo Africa</h1>
                    <div class="ml-6 flex space-x-4">
                        <a href="/dashboard/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Dashboard</a>
                        <a href="/tasks/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Tasks</a>
                        <a href="/departments/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Departments</a>
                        <a href="/messages/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Messages</a>
                        <a href="/chat/" class="text-blue-600 px-3 py-2 font-medium">Chat</a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    
    <div class="flex h-full">
        <!-- Chat Rooms Sidebar -->
        <div class="w-1/4 bg-white border-r">
            <div class="p-4 border-b">
                <h3 class="font-semibold">Chat Rooms</h3>
            </div>
            <div class="overflow-y-auto">
                <div class="p-3 hover:bg-gray-50 cursor-pointer border-b bg-blue-50">
                    <div class="flex items-center">
                        <div class="w-3 h-3 bg-green-400 rounded-full mr-3"></div>
                        <div>
                            <p class="font-medium text-sm">IT Department</p>
                            <p class="text-xs text-gray-500">12 members</p>
                        </div>
                    </div>
                </div>
                <div class="p-3 hover:bg-gray-50 cursor-pointer border-b">
                    <div class="flex items-center">
                        <div class="w-3 h-3 bg-green-400 rounded-full mr-3"></div>
                        <div>
                            <p class="font-medium text-sm">Marketing Team</p>
                            <p class="text-xs text-gray-500">8 members</p>
                        </div>
                    </div>
                </div>
                <div class="p-3 hover:bg-gray-50 cursor-pointer border-b">
                    <div class="flex items-center">
                        <div class="w-3 h-3 bg-gray-400 rounded-full mr-3"></div>
                        <div>
                            <p class="font-medium text-sm">Finance Department</p>
                            <p class="text-xs text-gray-500">6 members</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Chat Messages Area -->
        <div class="flex-1 flex flex-col">
            <div class="p-4 border-b bg-gray-50">
                <h3 class="font-semibold">IT Department</h3>
                <p class="text-sm text-gray-600">12 members online</p>
            </div>
            
            <!-- Messages -->
            <div class="flex-1 overflow-y-auto p-4 space-y-4">
                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white text-sm font-semibold">JD</div>
                    <div class="flex-1">
                        <div class="flex items-center space-x-2">
                            <span class="font-medium text-sm">John Doe</span>
                            <span class="text-xs text-gray-500">10:30 AM</span>
                        </div>
                        <p class="text-sm text-gray-700 mt-1">Server maintenance is scheduled for tonight at 11 PM. Please save your work.</p>
                    </div>
                </div>
                
                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center text-white text-sm font-semibold">SA</div>
                    <div class="flex-1">
                        <div class="flex items-center space-x-2">
                            <span class="font-medium text-sm">Sarah Adams</span>
                            <span class="text-xs text-gray-500">10:32 AM</span>
                        </div>
                        <p class="text-sm text-gray-700 mt-1">Thanks for the heads up! How long is the expected downtime?</p>
                    </div>
                </div>
                
                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white text-sm font-semibold">JD</div>
                    <div class="flex-1">
                        <div class="flex items-center space-x-2">
                            <span class="font-medium text-sm">John Doe</span>
                            <span class="text-xs text-gray-500">10:35 AM</span>
                        </div>
                        <p class="text-sm text-gray-700 mt-1">Should be about 2 hours maximum. I'll send updates in this channel.</p>
                    </div>
                </div>
            </div>
            
            <!-- Message Input -->
            <div class="border-t p-4">
                <div class="flex space-x-2">
                    <input type="text" placeholder="Type your message..." class="flex-1 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <button class="px-4 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
                        <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
    ''')

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('tasks/', tasks_view, name='tasks'),
    path('departments/', departments_view, name='departments'),
    path('messages/', messages_view, name='messages'),
    path('chat/', chat_view, name='chat'),
]

if __name__ == '__main__':
    print("🚀 Starting Volo Africa Communication System")
    print("📡 Server will run at: http://localhost:8000")
    print("🔑 Login with username: admin, password: admin")
    
    # Setup Django
    django.setup()
    
    # Start the development server
    from django.core.management.commands.runserver import Command as RunServerCommand
    from django.core.management.base import CommandParser
    
    try:
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        
        # Simple HTTP server
        from wsgiref.simple_server import make_server
        server = make_server('127.0.0.1', 8000, application)
        print("✅ Server started successfully!")
        print("🌐 Open http://localhost:8000 in your browser")
        server.serve_forever()
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        # Fallback to basic HTTP server
        import http.server
        import socketserver
        from urllib.parse import urlparse, parse_qs
        
        class SimpleHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(login_view(None).content)
                else:
                    super().do_GET()
        
        with socketserver.TCPServer(("", 8000), SimpleHandler) as httpd:
            print("✅ Fallback server started at http://localhost:8000")
            httpd.serve_forever()
