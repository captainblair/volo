#!/usr/bin/env python
import os
import sys

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volo_system.settings')

try:
    import django
    print(f"Django version: {django.get_version()}")
    
    django.setup()
    print("Django setup successful")
    
    # Test imports
    from users.models import CustomUser
    print("Users app imported successfully")
    
    from departments.models import Department
    print("Departments app imported successfully")
    
    from tasks.models import Task
    print("Tasks app imported successfully")
    
    from communications.models import Message
    print("Communications app imported successfully")
    
    print("All imports successful!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
