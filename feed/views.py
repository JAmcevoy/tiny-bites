from django.shortcuts import render
from django.views import generic
from .models import Create, Review


# Create your views here.

class PostList(generic.ListView):
    queryset = Create.objects.all()

