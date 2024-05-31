from django.db import models
from django.contrib.auth.models import User

class ErrorReport(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    issue = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    steps_taken_to_correct = models.TextField(default=None, blank=True, null=True)
    handled_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'is_superuser': True})