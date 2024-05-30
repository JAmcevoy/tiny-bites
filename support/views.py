from django.shortcuts import render, redirect
from .forms import ErrorReportForm
import os


def submit_error(request):
    if request.method == 'POST':
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            error_report = form.save(commit=False)
            error_report.user = request.user  # Assign the current user to the error report
            error_report.save()
            return redirect('submit_success')
    else:
        form = ErrorReportForm()
        if request.user.is_authenticated:
            form.fields['email'].initial = request.user.email  # Pre-fill the email field with user's email
    return render(request, 'support/submit_error.html', {'form': form})


def submit_success(request):
    return render(request, 'support/submit_success.html')


