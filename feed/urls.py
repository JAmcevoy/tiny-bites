from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_creation/', views.post_creation, name='post_creation'),
    path('my_bites/', views.my_bites, name='my_bites'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

]