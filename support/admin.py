from django.contrib import admin
from .models import ErrorReport

class StepsTakenToCorrectFilter(admin.SimpleListFilter):
    title = 'Steps Taken To Correct'
    parameter_name = 'steps_taken_to_correct'

    def lookups(self, request, model_admin):
        return (
            ('null', 'Steps Not Taken'),
            ('not_null', 'Steps Taken'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'null':
            return queryset.filter(steps_taken_to_correct__isnull=True)
        elif self.value() == 'not_null':
            return queryset.exclude(steps_taken_to_correct__isnull=True)

@admin.register(ErrorReport)
class ErrorReportAdmin(admin.ModelAdmin):
    list_display = ('issue', 'email', 'description')
    search_fields = ['issue']
    list_filter = (StepsTakenToCorrectFilter,)
