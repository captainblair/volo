#!/usr/bin/env python3
"""
Quick HTTP server for Volo Africa Communication System demo
"""
import http.server
import socketserver
import webbrowser
from urllib.parse import urlparse, parse_qs

class VoloHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volo Africa - Communication System</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <!-- Header -->
        <div class="text-center mb-12">
            <div class="mx-auto h-16 w-16 flex items-center justify-center rounded-full bg-blue-600 mb-4">
                <i class="fas fa-building text-white text-2xl"></i>
            </div>
            <h1 class="text-4xl font-bold text-gray-900 mb-2">Volo Africa</h1>
            <p class="text-xl text-gray-600">Departmental Communication & Task Allocation System</p>
        </div>

        <!-- Status Card -->
        <div class="max-w-4xl mx-auto">
            <div class="bg-white rounded-lg shadow-lg p-8 mb-8">
                <div class="flex items-center justify-center mb-6">
                    <div class="bg-green-100 rounded-full p-3">
                        <i class="fas fa-check-circle text-green-600 text-3xl"></i>
                    </div>
                </div>
                <h2 class="text-2xl font-bold text-center text-gray-900 mb-4">System Successfully Built!</h2>
                <p class="text-center text-gray-600 mb-8">Your complete full-stack communication system is ready.</p>
            </div>

            <!-- Features Grid -->
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
                <div class="bg-white rounded-lg shadow p-6">
                    <div class="flex items-center mb-4">
                        <i class="fas fa-users text-blue-600 text-2xl mr-3"></i>
                        <h3 class="text-lg font-semibold">User Management</h3>
                    </div>
                    <p class="text-gray-600">Role-based authentication with Admin, Manager, and Employee roles</p>
                </div>

                <div class="bg-white rounded-lg shadow p-6">
                    <div class="flex items-center mb-4">
                        <i class="fas fa-building text-green-600 text-2xl mr-3"></i>
                        <h3 class="text-lg font-semibold">Department Management</h3>
                    </div>
                    <p class="text-gray-600">Create and manage organizational departments with assigned managers</p>
                </div>

                <div class="bg-white rounded-lg shadow p-6">
                    <div class="flex items-center mb-4">
                        <i class="fas fa-tasks text-purple-600 text-2xl mr-3"></i>
                        <h3 class="text-lg font-semibold">Task Allocation</h3>
                    </div>
                    <p class="text-gray-600">Smart task assignment with priority levels and due date tracking</p>
                </div>

                <div class="bg-white rounded-lg shadow p-6">
                    <div class="flex items-center mb-4">
                        <i class="fas fa-comments text-orange-600 text-2xl mr-3"></i>
                        <h3 class="text-lg font-semibold">Real-time Chat</h3>
                    </div>
                    <p class="text-gray-600">WebSocket-powered group chat and direct messaging</p>
                </div>

                <div class="bg-white rounded-lg shadow p-6">
                    <div class="flex items-center mb-4">
                        <i class="fas fa-bell text-red-600 text-2xl mr-3"></i>
                        <h3 class="text-lg font-semibold">Notifications</h3>
                    </div>
                    <p class="text-gray-600">Real-time notifications for task updates and messages</p>
                </div>

                <div class="bg-white rounded-lg shadow p-6">
                    <div class="flex items-center mb-4">
                        <i class="fas fa-mobile-alt text-indigo-600 text-2xl mr-3"></i>
                        <h3 class="text-lg font-semibold">Responsive Design</h3>
                    </div>
                    <p class="text-gray-600">Modern UI with Tailwind CSS, works on all devices</p>
                </div>
            </div>

            <!-- Technical Details -->
            <div class="bg-white rounded-lg shadow-lg p-8 mb-8">
                <h2 class="text-2xl font-bold text-gray-900 mb-6">Technical Implementation</h2>
                <div class="grid md:grid-cols-2 gap-8">
                    <div>
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">Backend Technologies</h3>
                        <ul class="space-y-2 text-gray-600">
                            <li><i class="fas fa-check text-green-500 mr-2"></i>Django 4.2 Framework</li>
                            <li><i class="fas fa-check text-green-500 mr-2"></i>Django REST Framework</li>
                            <li><i class="fas fa-check text-green-500 mr-2"></i>SQLite/MySQL Database</li>
                            <li><i class="fas fa-check text-green-500 mr-2"></i>WebSocket Support</li>
                            <li><i class="fas fa-check text-green-500 mr-2"></i>Custom User Model</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold text-gray-900 mb-3">Frontend Technologies</h3>
                        <ul class="space-y-2 text-gray-600">
                            <li><i class="fas fa-check text-green-500 mr-2"></i>HTML5 & Modern CSS</li>
                            <li><i class="fas fa-check text-green-500 mr-2"></i>Tailwind CSS Framework</li>
                            <li><i class="fas fa-check text-green-500 mr-2"></i>Alpine.js for Interactivity</li>
                            <li><i class="fas fa-check text-green-500 mr-2"></i>Responsive Design</li>
                            <li><i class="fas fa-check text-green-500 mr-2"></i>Font Awesome Icons</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Project Info -->
            <div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg shadow-lg p-8 text-white">
                <div class="text-center">
                    <h2 class="text-2xl font-bold mb-4">Project Information</h2>
                    <div class="grid md:grid-cols-3 gap-6">
                        <div>
                            <h3 class="font-semibold mb-2">Development Team</h3>
                            <p>Fabian Atambo - SCCI/01226/2022</p>
                            <p>Tony Wangolo - SCNI/01228/2023</p>
                            <p class="text-blue-200">Group Harambee</p>
                        </div>
                        <div>
                            <h3 class="font-semibold mb-2">Organization</h3>
                            <p>Volo Africa</p>
                            <p>Contact: Anne Apiyo</p>
                            <p class="text-blue-200">Phone: 0746821567</p>
                        </div>
                        <div>
                            <h3 class="font-semibold mb-2">Academic</h3>
                            <p>Technical University of Kenya</p>
                            <p>IBL 2305 Software Development</p>
                            <p class="text-blue-200">Laboratory Practical</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Next Steps -->
            <div class="bg-yellow-50 border border-yellow-200 rounded-lg p-6 mt-8">
                <h3 class="text-lg font-semibold text-yellow-800 mb-3">
                    <i class="fas fa-lightbulb mr-2"></i>Next Steps to Run Full System
                </h3>
                <ol class="list-decimal list-inside space-y-2 text-yellow-700">
                    <li>Install dependencies: <code class="bg-yellow-100 px-2 py-1 rounded">pip install -r requirements.txt</code></li>
                    <li>Run migrations: <code class="bg-yellow-100 px-2 py-1 rounded">python manage.py migrate</code></li>
                    <li>Create superuser: <code class="bg-yellow-100 px-2 py-1 rounded">python manage.py createsuperuser</code></li>
                    <li>Start server: <code class="bg-yellow-100 px-2 py-1 rounded">python manage.py runserver</code></li>
                </ol>
            </div>
        </div>
    </div>
</body>
</html>
            """
            self.wfile.write(html_content.encode())
        else:
            super().do_GET()

PORT = 8000
Handler = VoloHandler

print(f"🚀 Starting Volo Africa Communication System Demo")
print(f"📡 Server running at: http://localhost:{PORT}")
print(f"🌐 Open your browser and visit the URL above")
print(f"⏹️  Press Ctrl+C to stop the server")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped")
        httpd.shutdown()
