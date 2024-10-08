import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.views import PasswordChangeView

from .models import Create, Comment
from .forms import PostFormCreate, CommentForm


class PostList(generic.ListView):
    """
    Displays a list of posts with pagination.
    """
    queryset = Create.objects.all()
    template_name = "feed/index.html"
    paginate_by = 10
    ordering = ['-created_at']


def search_feature(request):
    """
    Handles the search functionality for posts.
    """
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        posts = Create.objects.filter(Q(name__icontains=search_query))
        return render(
            request, 'feed/search_results.html', 
            {'query': search_query, 'posts': posts}
        )
    else:
        return render(request, 'feed/search_results.html', {})


def post_detail(request, slug):
    """
    Displays the details of a specific post along with its comments.
    """
    queryset = Create.objects.filter()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    commented_forms = [
        (comment, CommentForm(instance=comment)) for comment in comments
    ]

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
            return redirect('post_detail', slug=post.slug)

    comment_form = CommentForm()

    return render(
        request,
        "feed/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "commented_forms": commented_forms,
        },
    )


@login_required
def post_creation(request):
    """
    Handles the creation of a new post.
    Generates a unique slug for each post and displays appropriate messages 
    based on the form submission result.
    """
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

            messages.success(
                request, 'Your post has been created successfully!'
            )
            return redirect("post_detail", slug=new_post.slug)
        else:
            messages.error(
                request, 'There was an error with your submission. '
                'Please check the form and try again.'
            )
    else:
        create_form = PostFormCreate()

    return render(request, "feed/post_creation.html", {"post_form": create_form})


@login_required
def edit_post(request, slug):
    """
    Handles the editing of an existing post.
    """
    post = get_object_or_404(Create, slug=slug)

    if request.user != post.author:
        messages.error(request, 'You do not have permission to edit this post.')
        return redirect('home')

    if request.method == 'POST':
        form = PostFormCreate(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your bite has been updated successfully.')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostFormCreate(instance=post)

    return render(request, 'feed/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_posts(request, slug):
    """
    Handles the deletion of an existing post.
    """
    post = get_object_or_404(Create, slug=slug)

    if request.user == post.author or request.user.is_superuser:
        post.delete()
        messages.success(request, 'Your bite was deleted successfully.')
        return redirect('my_bites')
    else:
        messages.error(request, 'There has been an error. Try again later.')
        return redirect('my_bites')


def my_bites(request):
    """
    Displays the posts created by the logged-in user with pagination.
    """
    if request.user.is_authenticated:
        user_posts = Create.objects.filter(
            author_id=request.user.id
        ).order_by('created_at')

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
        return redirect('login')


def to_be_approved(request):
    """
    Displays the comments that are pending approval by the logged-in user.
    """
    if request.user.is_authenticated:
        user_posts = Create.objects.filter(author=request.user)
        comments_pending = Comment.objects.filter(
            post__in=user_posts, approved=False
        )
        return render(
            request, "feed/to_be_approved.html", 
            {'comments_pending': comments_pending}
        )
    else:
        return redirect('login')


@login_required
def approve_comment(request, comment_id):
    """
    Approves a comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.approved = True
    comment.save()
    return redirect('to_be_approved')


@login_required
def delete_comment(request, comment_id):
    """
    Deletes a comment. Redirects to the referring URL if available,
    otherwise redirects to the post detail page.
    Only the owner of the comment or superuser can delete the comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    request.session['referring_url'] = request.META.get('HTTP_REFERER', None)
    default_url = reverse('post_detail', kwargs={'slug': comment.post.slug})

    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return referring_url(request, default_url)
    else:
        messages.error(request, 'You do not have permission to delete this comment.')
        return redirect(default_url)


@login_required
def edit_comment(request, comment_id):
    """
    Edits a comment and sets its approval status to False.
    Renders the post detail template with the necessary context.
    Only the owner of the comment can edit it.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.author:
        messages.error(request, 'You do not have permission to edit this comment.')
        return redirect('post_detail', slug=comment.post.slug)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment updated!')
            return redirect('post_detail', slug=comment.post.slug)
    else:
        comment_form = CommentForm(instance=comment, initial={'body': comment.body})

    post = comment.post
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    commented_forms = [
        (comment, CommentForm(instance=comment)) for comment in comments
    ]

    return render(request, 'feed/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
        'commented_forms': commented_forms,
        'comment': comment
    })


def referring_url(request, default_url):
    """
    Redirects to the referring URL or a default URL if the referring URL is not
    available.
    """
    referring_url = request.session.get('referring_url', None)
    if referring_url:
        return HttpResponseRedirect(referring_url)
    else:
        return HttpResponseRedirect(default_url)


def login_view(request):
    """
    Handles user login. Redirects to the 'next' URL if specified.
    """
    next_url = request.GET.get('next')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            messages.error(
                request, "The username and/or password you specified are "
                "not correct."
            )
            return render(request, "account/login.html", {'next': next_url})
    else:
        return render(request, "account/login.html", {'next': next_url})


@login_required
def profile(request):
    """
    Displays and updates the user's profile.
    Only accessible to authenticated users.
    """
    user = request.user

    if request.method == 'POST':
        first_name = request.POST.get('firstName', '').strip()
        last_name = request.POST.get('lastName', '').strip()
        email = request.POST.get('email', '').strip()

        # Update the user object
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(request, 'feed/profile.html', {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    })


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.request.user)
        messages.success(self.request, 'Password changed successfully!')
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, 'Your old password was entered incorrectly.'
        )
        return HttpResponseRedirect(reverse_lazy('profile'))
