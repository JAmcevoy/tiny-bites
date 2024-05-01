from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from .models import Create, Review, Comment
from .forms import CommentForm, PostFormCreate


# Create your views here.

class PostList(generic.ListView):
    queryset = Create.objects.all()
    template_name = "feed/index.html"
    paginate_by = 10


def post_detail(request, slug):
    queryset = Create.objects.filter()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "feed/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def post_creation(request):
    if request.method == 'POST':
        form = PostFormCreate(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            
            # Generate unique slug
            new_post.slug = slugify(new_post.name)
            
            # Handle duplicate slugs
            suffix = 1
            while Create.objects.filter(slug=new_post.slug).exists():
                new_post.slug = slugify(new_post.name) + '-' + str(suffix)
                suffix += 1
            
            new_post.save()

            return redirect('post_detail', slug=new_post.slug)
    else:
        form = PostFormCreate()
    return render(request, 'feed/post_creation.html', {'form': form})