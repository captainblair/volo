#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volo_system.settings')
django.setup()

from django.contrib.auth import get_user_model
from departments.models import Department
from communications.models import ChatRoom, ChatMessage

User = get_user_model()

def create_sample_data():
    print("Creating sample data...")
    
    # Create departments if they don't exist
    marketing_dept, created = Department.objects.get_or_create(
        name="Marketing",
        defaults={
            'description': 'Marketing and Communications Department',
            'manager': None
        }
    )
    if created:
        print("Created Marketing department")
    
    it_dept, created = Department.objects.get_or_create(
        name="IT",
        defaults={
            'description': 'Information Technology Department',
            'manager': None
        }
    )
    if created:
        print("Created IT department")
    
    hr_dept, created = Department.objects.get_or_create(
        name="HR",
        defaults={
            'description': 'Human Resources Department',
            'manager': None
        }
    )
    if created:
        print("Created HR department")
    
    # Get or create admin user
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@volo.africa',
            'first_name': 'Admin',
            'last_name': 'User',
            'is_staff': True,
            'is_superuser': True,
            'department': it_dept
        }
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("Created admin user")
    
    # Create sample users
    users_data = [
        {'username': 'john_doe', 'first_name': 'John', 'last_name': 'Doe', 'email': 'john@volo.africa', 'department': marketing_dept},
        {'username': 'jane_smith', 'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane@volo.africa', 'department': it_dept},
        {'username': 'mike_wilson', 'first_name': 'Mike', 'last_name': 'Wilson', 'email': 'mike@volo.africa', 'department': hr_dept},
    ]
    
    created_users = []
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults=user_data
        )
        if created:
            user.set_password('password123')
            user.save()
            print(f"Created user: {user.username}")
        created_users.append(user)
    
    # Create chat rooms
    chat_rooms_data = [
        {'name': 'General Discussion', 'description': 'General company-wide discussions', 'department': marketing_dept},
        {'name': 'IT Support', 'description': 'Technical support and IT discussions', 'department': it_dept},
        {'name': 'HR Announcements', 'description': 'HR updates and announcements', 'department': hr_dept},
        {'name': 'Marketing Team', 'description': 'Marketing team coordination', 'department': marketing_dept},
    ]
    
    for room_data in chat_rooms_data:
        room, created = ChatRoom.objects.get_or_create(
            name=room_data['name'],
            defaults={
                'description': room_data['description'],
                'department': room_data['department'],
                'created_by': admin_user
            }
        )
        if created:
            # Add all users to each room
            room.members.add(admin_user, *created_users)
            print(f"Created chat room: {room.name}")
            
            # Create sample messages
            sample_messages = [
                f"Welcome to {room.name}! This is where we collaborate.",
                "Hello everyone! Looking forward to working together.",
                "Great to have this communication channel set up."
            ]
            
            for i, message_text in enumerate(sample_messages):
                user = [admin_user] + created_users
                ChatMessage.objects.get_or_create(
                    room=room,
                    user=user[i % len(user)],
                    message=message_text
                )
    
    print("Sample data creation completed!")

if __name__ == '__main__':
    create_sample_data()
