from django.shortcuts import render, redirect
from .forms import ErrorReportForm
import os

def submit_error(request):
    if request.method == 'POST':
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            error_report = form.save()

            # Save to /docs/errors as a text file
            error_dir = os.path.join(os.path.dirname(__file__), '../support/errors')
            os.makedirs(error_dir, exist_ok=True)
            file_path = os.path.join(error_dir, f'error_{error_report.id}.txt')
            
            with open(file_path, 'w') as file:
                file.write(f"Title: {error_report.issue}\n")
                file.write(f"Email: {error_report.email}\n")
                file.write(f"Description:\n{error_report.description}\n")
                file.write(f"Submitted at: {error_report.submitted_at}\n")

            return redirect('submit_success')
    else:
        form = ErrorReportForm()
    return render(request, 'support/submit_error.html', {'form': form})

def submit_success(request):
    return render(request, 'support/submit_success.html')
