from django.db import models

class ErrorReport(models.Model):
    issue = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)