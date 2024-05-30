from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('change-password/', views.CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('post_creation/', views.post_creation, name='post_creation'),
    path('my_bites/', views.my_bites, name='my_bites'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_posts, name="delete_post"),
    path('to_be_approved/', views.to_be_approved, name='to_be_approved'),
    path('approve_comment/<int:comment_id>/', views.approve_comment, name='approve_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('search/', views.search_feature, name='search_feature'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
]
