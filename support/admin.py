from django.contrib import admin
from .models import ErrorReport

# Register your models here.

@admin.register(ErrorReport)
class ErrorReportAdmin(admin.ModelAdmin):
    list_display = ('issue', 'email', 'description')
