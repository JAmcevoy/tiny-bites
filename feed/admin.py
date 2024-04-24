from django.contrib import admin
from .models import Post_Create, Post_Review

# Register your models here.
admin.site.register(Post_Create)
admin.site.register(Post_Review)

