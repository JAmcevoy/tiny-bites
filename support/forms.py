from django import forms
from .models import ErrorReport

class ErrorReportForm(forms.ModelForm):
    class Meta:
        model = ErrorReport
        fields = [
            'issue', 
            'description',
            'email',
        ]