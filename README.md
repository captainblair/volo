# Volo Africa - Departmental Communication and Task Allocation System

A comprehensive web application built with Django and modern frontend technologies to solve communication and task allocation challenges between departments.

## Features

- **User Management**: Role-based authentication (Admin, Manager, Employee)
- **Department Management**: Create and manage organizational departments
- **Task Allocation**: Smart task assignment with priority levels and due dates
- **Real-time Communication**: WebSocket-powered chat and notifications
- **Responsive Design**: Modern UI with Tailwind CSS
- **API Integration**: RESTful APIs for all functionality

## Technology Stack

- **Backend**: Django 4.2, Django REST Framework
- **Database**: MySQL
- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Real-time**: Django Channels, WebSockets, Redis
- **Authentication**: Django's built-in authentication system

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd volo
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**
   - Create MySQL database named `volo_system`
   - Update `.env` file with your database credentials

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start Redis server** (for WebSocket support)
   ```bash
   redis-server
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the application**: http://localhost:8000
2. **Login** with your credentials
3. **Dashboard**: View overview of tasks, departments, and notifications
4. **Tasks**: Create, assign, and manage tasks across departments
5. **Departments**: Manage organizational structure
6. **Messages**: Send direct messages to team members
7. **Chat**: Real-time group communication

## API Endpoints

- `/api/auth/` - Authentication endpoints
- `/api/departments/` - Department management
- `/api/tasks/` - Task operations
- `/api/communications/` - Messages and notifications

## Project Structure

```
volo/
├── volo_system/          # Main Django project
├── users/                # User management app
├── departments/          # Department management app
├── tasks/                # Task allocation app
├── communications/       # Chat and messaging app
├── templates/            # HTML templates
├── static/               # CSS, JS, images
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Team

- **Fabian Atambo** - SCCI/01226/2022
- **Tony Wangolo** - SCNI/01228/2023

## Organization

**Volo Africa** - Improving organizational communication and productivity

## Contact

**Anne Apiyo** - 0746821567

## License

This project is developed as part of IBL 2305 Software Development Laboratory at The Technical University of Kenya.
