from django.shortcuts import render, redirect
from .forms import ErrorReportForm
import os

def submit_error(request):
    if request.method == 'POST':
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            error_report = form.save()
            return redirect('submit_success')
    else:
        form = ErrorReportForm()
    return render(request, 'support/submit_error.html', {'form': form})

def submit_success(request):
    return render(request, 'support/submit_success.html')
