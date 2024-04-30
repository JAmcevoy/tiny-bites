from django.contrib import admin
from .models import Create, Review, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Create)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'author', 'created_at')
    search_fields = ['name']
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description', 'ingredients', 'instructions')



# Register your models here.
admin.site.register(Review)
admin.site.register(Comment)

