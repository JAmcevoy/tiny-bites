from .models import Comment, Create
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


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