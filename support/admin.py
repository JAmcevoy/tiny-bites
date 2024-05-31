from django.contrib import admin
from .models import ErrorReport

@admin.register(ErrorReport)
class ErrorReportAdmin(admin.ModelAdmin):
    list_display = ('issue', 'email', 'description', 'status', 'submitted_at', 'handled_by')
    list_filter = ('status', 'submitted_at')
    search_fields = ('issue', 'email', 'description')

    def save_model(self, request, obj, form, change):
        if change: 
            obj.handled_by = request.user
        obj.save()