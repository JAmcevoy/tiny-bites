from django.db import models

class ErrorReport(models.Model):
    issue = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    steps_taken_to_correct = models.TextField(default=None, blank=True, null=True)
