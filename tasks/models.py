from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """
    Model representing a task in the task management system.

    Attributes:
        title (str): The title of the task.
        description (str): A detailed description of the task.
        status (str): The current status of the task (either 'pending' or 'completed').
        assigned_to (User, optional): The user to whom the task is assigned. Can be null or blank.
        created_at (datetime): The timestamp when the task was created.
        updated_at (datetime): The timestamp when the task was last updated.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title