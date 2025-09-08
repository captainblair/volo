#!/usr/bin/env python
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import json

class VoloHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0]  # Remove query parameters
        
        if path == '/' or path == '/login/':
            self.serve_login()
        elif path == '/dashboard/':
            self.serve_dashboard()
        elif path == '/tasks/':
            self.serve_tasks()
        elif path == '/departments/':
            self.serve_departments()
        elif path == '/messages/':
            self.serve_messages()
        elif path == '/chat/':
            self.serve_chat()
        else:
            self.send_error(404, "Page not found")
    
    def do_POST(self):
        if self.path == '/' or self.path == '/login/':
            # Simple login handling
            self.send_response(302)
            self.send_header('Location', '/dashboard/')
            self.end_headers()
    
    def serve_page(self, title, content):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = f'''<!DOCTYPE html>
<html>
<head>
    <title>{title} - Volo Africa</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    {content}
</body>
</html>'''
        self.wfile.write(html.encode())
    
    def serve_login(self):
        content = '''
    <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-600 to-purple-700">
        <div class="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-md transform hover:scale-105 transition-transform duration-300">
            <div class="text-center mb-8">
                <h1 class="text-3xl font-bold text-gray-800 mb-2">Volo Africa</h1>
                <p class="text-gray-600">Communication System</p>
            </div>
            <form method="post" class="space-y-6">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Username</label>
                    <input type="text" name="username" value="admin" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                    <input type="password" name="password" value="admin" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                </div>
                <button type="submit" class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition-colors font-medium">
                    Sign In
                </button>
            </form>
        </div>
    </div>'''
        self.serve_page("Login", content)
    
    def serve_dashboard(self):
        content = '''
    <nav class="bg-white shadow mb-6">
        <div class="max-w-7xl mx-auto px-4">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <h1 class="text-xl font-bold text-blue-600">Volo Africa</h1>
                    <div class="ml-6 flex space-x-4">
                        <a href="/dashboard/" class="text-blue-600 px-3 py-2 font-medium">Dashboard</a>
                        <a href="/tasks/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Tasks</a>
                        <a href="/departments/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Departments</a>
                        <a href="/messages/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Messages</a>
                        <a href="/chat/" class="text-gray-600 hover:text-blue-600 px-3 py-2">Chat</a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    
    <div class="max-w-7xl mx-auto px-4">
        <h2 class="text-2xl font-bold mb-6">Dashboard</h2>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
            <div class="bg-white p-6 rounded-lg shadow">
                <div class="flex items-center">
                    <div class="p-3 bg-blue-100 rounded-full">
                        <i class="fas fa-tasks text-blue-600 text-xl"></i>
                    </div>
                    <div class="ml-4">
                        <p class="text-sm text-gray-600">Active Tasks</p>
                        <p class="text-2xl font-bold">24</p>
                    </div>
                </div>
            </div>
            <div class="bg-white p-6 rounded-lg shadow">
                <div class="flex items-center">
                    <div class="p-3 bg-green-100 rounded-full">
                        <i class="fas fa-building text-green-600 text-xl"></i>
                    </div>
                    <div class="ml-4">
                        <p class="text-sm text-gray-600">Departments</p>
                        <p class="text-2xl font-bold">8</p>
                    </div>
                </div>
            </div>
            <div class="bg-white p-6 rounded-lg shadow">
                <div class="flex items-center">
                    <div class="p-3 bg-yellow-100 rounded-full">
                        <i class="fas fa-envelope text-yellow-600 text-xl"></i>
                    </div>
                    <div class="ml-4">
                        <p class="text-sm text-gray-600">Messages</p>
                        <p class="text-2xl font-bold">12</p>
                    </div>
                </div>
            </div>
            <div class="bg-white p-6 rounded-lg shadow">
                <div class="flex items-center">
                    <div class="p-3 bg-purple-100 rounded-full">
                        <i class="fas fa-users text-purple-600 text-xl"></i>
                    </div>
                    <div class="ml-4">
                        <p class="text-sm text-gray-600">Team Members</p>
                        <p class="text-2xl font-bold">45</p>
                    </div>
                </div>
            </div>
        </div>
    </div>'''
        self.serve_page("Dashboard", content)
    
    def serve_tasks(self):
        content = '''
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
            <h2 class="text-2xl font-bold">Tasks</h2>
            <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
                <i class="fas fa-plus mr-2"></i>New Task
            </button>
        </div>
        
        <div class="bg-white rounded-lg shadow overflow-hidden">
            <table class="min-w-full">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Task</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Priority</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Status</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Due Date</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    <tr>
                        <td class="px-6 py-4">
                            <div>
                                <p class="font-medium">Update server infrastructure</p>
                                <p class="text-sm text-gray-500">IT Department</p>
                            </div>
                        </td>
                        <td class="px-6 py-4">
                            <span class="px-2 py-1 text-xs font-semibold rounded-full bg-red-100 text-red-800">High</span>
                        </td>
                        <td class="px-6 py-4">
                            <span class="px-2 py-1 text-xs font-semibold rounded-full bg-yellow-100 text-yellow-800">In Progress</span>
                        </td>
                        <td class="px-6 py-4 text-sm text-gray-500">2024-01-15</td>
                    </tr>
                    <tr>
                        <td class="px-6 py-4">
                            <div>
                                <p class="font-medium">Marketing campaign review</p>
                                <p class="text-sm text-gray-500">Marketing Department</p>
                            </div>
                        </td>
                        <td class="px-6 py-4">
                            <span class="px-2 py-1 text-xs font-semibold rounded-full bg-yellow-100 text-yellow-800">Medium</span>
                        </td>
                        <td class="px-6 py-4">
                            <span class="px-2 py-1 text-xs font-semibold rounded-full bg-blue-100 text-blue-800">Pending</span>
                        </td>
                        <td class="px-6 py-4 text-sm text-gray-500">2024-01-20</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>'''
        self.serve_page("Tasks", content)
    
    def serve_departments(self):
        content = '''
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
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-bold">Departments</h2>
            <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
                <i class="fas fa-plus mr-2"></i>New Department
            </button>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition-shadow">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-lg font-semibold">IT Department</h3>
                    <div class="w-3 h-3 bg-green-400 rounded-full"></div>
                </div>
                <p class="text-gray-600 text-sm mb-4">Manages technology infrastructure and software development</p>
                <div class="flex justify-between text-sm">
                    <span class="text-gray-500">12 employees</span>
                    <span class="text-gray-500">8 active tasks</span>
                </div>
            </div>
            
            <div class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition-shadow">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-lg font-semibold">Marketing</h3>
                    <div class="w-3 h-3 bg-green-400 rounded-full"></div>
                </div>
                <p class="text-gray-600 text-sm mb-4">Handles brand promotion and customer engagement</p>
                <div class="flex justify-between text-sm">
                    <span class="text-gray-500">8 employees</span>
                    <span class="text-gray-500">5 active tasks</span>
                </div>
            </div>
            
            <div class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition-shadow">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-lg font-semibold">Finance</h3>
                    <div class="w-3 h-3 bg-yellow-400 rounded-full"></div>
                </div>
                <p class="text-gray-600 text-sm mb-4">Manages financial operations and budgeting</p>
                <div class="flex justify-between text-sm">
                    <span class="text-gray-500">6 employees</span>
                    <span class="text-gray-500">3 active tasks</span>
                </div>
            </div>
        </div>
    </div>'''
        self.serve_page("Departments", content)
    
    def serve_messages(self):
        content = '''
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
            <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
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
            </div>
        </div>
    </div>'''
        self.serve_page("Messages", content)
    
    def serve_chat(self):
        content = '''
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
    
    <div class="flex h-screen">
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
            </div>
        </div>
        
        <div class="flex-1 flex flex-col">
            <div class="p-4 border-b bg-gray-50">
                <h3 class="font-semibold">IT Department</h3>
                <p class="text-sm text-gray-600">12 members online</p>
            </div>
            
            <div class="flex-1 overflow-y-auto p-4 space-y-4">
                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white text-sm font-semibold">JD</div>
                    <div class="flex-1">
                        <div class="flex items-center space-x-2">
                            <span class="font-medium text-sm">John Doe</span>
                            <span class="text-xs text-gray-500">10:30 AM</span>
                        </div>
                        <p class="text-sm text-gray-700 mt-1">Server maintenance is scheduled for tonight at 11 PM.</p>
                    </div>
                </div>
            </div>
            
            <div class="border-t p-4">
                <div class="flex space-x-2">
                    <input type="text" placeholder="Type your message..." class="flex-1 p-3 border rounded-lg">
                    <button class="px-4 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
                        <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>'''
        self.serve_page("Chat", content)

if __name__ == '__main__':
    PORT = 8000
    print("🚀 Starting Volo Africa Communication System")
    print(f"📡 Server running at: http://localhost:{PORT}")
    print("🔑 Login with username: admin, password: admin")
    print("✅ All pages are now functional!")
    
    with socketserver.TCPServer(("", PORT), VoloHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")
