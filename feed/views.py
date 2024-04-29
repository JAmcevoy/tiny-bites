from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Create, Review


# Create your views here.

class PostList(generic.ListView):
    queryset = Create.objects.all()
    template_name = "feed/index.html"


def post_detail(request, slug):
 """
 Display an individual :model:`blog.Post`.
 **Context**
 ``post``
 An instance of :model:`blog.Post`.
 **Template:**
 :template:`blog/post_detail.html`
 """
 queryset = Post.objects.filter()
 post = get_object_or_404(queryset, slug=slug)
 return render(
 request,
 "feed/post_detail.html",
 {"post": post},
 )





