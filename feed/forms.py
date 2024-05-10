from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Create


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Comment'
        }


class PostFormCreate(forms.ModelForm):
    class Meta:
        model = Create
        fields = (
            'name',
            'featured_image',
            'description',
            'ingredients',
            'instructions',
        )
        widgets = {
            'description': SummernoteWidget(),  # Use SummernoteWidget for rich text editing
            'ingredients': SummernoteWidget(),  # Use SummernoteWidget for rich text editing
            'instructions': SummernoteWidget(),  # Use SummernoteWidget for rich text editing
        }
