from django.shortcuts import render, redirect
from .forms import ErrorReportForm


def submit_error(request):
    """
    Handles the error report form submission.

    If the request method is POST and the form is valid, saves the error report
    with the user's email if logged in, then redirects to submit success page.
    If the request method is GET, initializes the form with the user's email
    if logged in.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponse object
    """
    if request.method == 'POST':
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            error_report = form.save(commit=False)
            if request.user.is_authenticated:
                error_report.user = request.user
            error_report.save()
            return redirect('submit_success')
    else:
        form = ErrorReportForm(
            initial={'email': request.user.email}
            if request.user.is_authenticated else None
        )
    return render(request, 'support/submit_error.html', {'form': form})


def submit_success(request):
    """
    Renders the submit success page.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponse object
    """
    return render(request, 'support/submit_success.html')
