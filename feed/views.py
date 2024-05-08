from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Create, Comment
from .forms import PostFormCreate, CommentForm

class PostList(generic.ListView):
    queryset = Create.objects.all()
    template_name = "feed/index.html"
    paginate_by = 10


def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')

        posts = Create.objects.filter(Q(name__icontains=search_query))
        return render(request, 'feed/search_results.html', {'query': search_query, 'posts': posts})
    else:
        return render(request, 'app/search_results.html', {})


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
    if request.method == "POST":
        create_form = PostFormCreate(request.POST, request.FILES)
        if create_form.is_valid():
            new_post = create_form.save(commit=False)
            new_post.author = request.user

            new_post.slug = slugify(new_post.name)

            suffix = 1
            while Create.objects.filter(slug=new_post.slug).exists():
                new_post.slug = slugify(new_post.name) + "-" + str(suffix)
                suffix += 1
            
            new_post.save()

            return redirect("post_detail", slug=new_post.slug)
    else:
        create_form = PostFormCreate()

    return render(request, "feed/post_creation.html", {"post_form": create_form})


def edit_post(request, slug):
    post = get_object_or_404(Create, slug=slug)
    if request.method == 'POST':
        form = PostFormCreate(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostFormCreate(instance=post)
    return render(request, 'feed/edit_post.html', {'form': form, 'post': post})    
    

def my_bites(request):
    if request.user.is_authenticated:
        user_posts = Create.objects.filter(author_id=request.user.id)
        
        paginator = Paginator(user_posts, 6)
        page = request.GET.get('page')
        try:
            user_posts = paginator.page(page)
        except PageNotAnInteger:
            user_posts = paginator.page(1)
        except EmptyPage:
            user_posts = paginator.page(paginator.num_pages)
        
        return render(request, "feed/my_bites.html", {'user_posts': user_posts})
    else:
        return render(request, "account/login.html")


def to_be_approved(request):
    if request.user.is_authenticated:

        user_posts = Create.objects.filter(author=request.user)
        
        comments_pending = Comment.objects.filter(post__in=user_posts, approved=False)
        
        return render(request, "feed/to_be_approved.html", {'comments_pending': comments_pending})
    else:
        return render(request, "account/login.html")

def approve_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    comment.approved = True
    comment.save()
    
    return redirect('to_be_approved')


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Store the referring URL in the session
    request.session['referring_url'] = request.META.get('HTTP_REFERER', None)

    if request.user == comment.author or request.user.is_superuser or comment.post.author:
        post_slug = comment.post.slug
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        
        # Redirect the user back to the referring URL
        referring_url = request.session.get('referring_url', None)
        if referring_url:
            return HttpResponseRedirect(referring_url)
        else:
            return redirect('post_detail', slug=post_slug)
    else:
        messages.error(request, 'You are not authorized to delete this comment.')
        return redirect('post_detail', slug=comment.post.slug)




