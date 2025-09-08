from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_departments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def employee_count(self):
        return self.customuser_set.count()

    @property
    def active_tasks_count(self):
        return self.tasks.filter(status__in=['pending', 'in_progress']).count()

    class Meta:
        db_table = 'departments'
        ordering = ['name']
