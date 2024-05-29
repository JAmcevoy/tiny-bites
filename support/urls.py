from django.urls import path
from . import views

urlpatterns = [
    path('submit_error/', views.submit_error, name='submit_error'),
    path('submit_success/', views.submit_success, name='submit_success'),
]
