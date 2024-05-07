from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Create, Comment
from .forms import PostFormCreate, CommentForm

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


def comment_edit(request, slug, comment_id):
    """
    View to edit comments.
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)

        # Check if the current user is the author of the comment
        if comment.author != request.user:
            messages.add_message(request, messages.ERROR, 'You are not authorized to edit this comment.')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Assuming you want to mark it as unapproved after edit
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


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
    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
    return redirect('to_be_approved')


