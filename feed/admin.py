from django.contrib import admin
from .models import Create, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Create)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'author', 'created_at')
    search_fields = ['name']
    list_filter = ('created_at', 'author')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description', 'ingredients', 'instructions')



# Register your models here.
admin.site.register(Comment)

