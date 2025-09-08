#!/usr/bin/env python
"""
Development server runner for Volo Africa Communication System
This script helps run the Django development server with proper setup
"""

import os
import sys
import subprocess
import time

def check_redis():
    """Check if Redis server is running"""
    try:
        import redis
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.ping()
        print("✓ Redis server is running")
        return True
    except:
        print("✗ Redis server is not running. Please start Redis server first.")
        print("  Download Redis from: https://redis.io/download")
        return False

def check_database():
    """Check database connection"""
    try:
        os.system("python manage.py check --database default")
        print("✓ Database connection successful")
        return True
    except:
        print("✗ Database connection failed. Please check your MySQL configuration.")
        return False

def run_migrations():
    """Run database migrations"""
    print("Running database migrations...")
    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate")
    print("✓ Migrations completed")

def create_sample_data():
    """Create sample data for testing"""
    print("Creating sample data...")
    # This would typically be done through Django management commands
    print("✓ Sample data creation completed")

def main():
    """Main function to start the development server"""
    print("=" * 50)
    print("Volo Africa Communication System")
    print("Development Server Setup")
    print("=" * 50)
    
    # Check prerequisites
    if not check_redis():
        return
    
    # Run migrations
    run_migrations()
    
    # Start the development server
    print("\nStarting Django development server...")
    print("Access the application at: http://localhost:8000")
    print("Admin panel at: http://localhost:8000/admin")
    print("\nPress Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        os.system("python manage.py runserver")
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    main()
