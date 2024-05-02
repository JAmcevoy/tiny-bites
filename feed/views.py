from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from .models import Create, Review
from .forms import PostFormCreate, PostFormReview, CommentForm

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
        create_form = PostFormCreate(request.POST, request.FILES)
        if create_form.is_valid():
            new_post = create_form.save(commit=False)
            new_post.author = request.user

            new_post.slug = slugify(new_post.name)

            suffix = 1
            while Create.objects.filter(slug=new_post.slug).exists():
                new_post.slug = slugify(new_post.name) + '-' + str(suffix)
                suffix += 1
            
            new_post.save()

            return redirect('post_detail', slug=new_post.slug)
    else:
        create_form = PostFormCreate()

    return render(request, 'feed/post_creation.html', {'post_form': create_form})

# def review_creation(request):
#     if request.method == 'POST':
#         review_form = ReviewForm(request.POST)
#         if review_form.is_valid():
#             new_review = review_form.save(commit=False)
#             new_review.author = request.user

#             new_review.slug = slugify(new_review.name)

#             suffix = 1
#             while Review.objects.filter(slug=new_review.slug).exists():
#                 new_review.slug = slugify(new_review.name) + '-' + str(suffix)
#                 suffix += 1
            
#             new_review.save()

#             return redirect('post_detail', slug=new_review.slug)
#     else:
#         review_form = ReviewForm()

#     return render(request, 'feed/post_creation.html', {'review_form': review_form})

