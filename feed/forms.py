from .models import Comment, Create, Review
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

class PostFormReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'name',
            'featured_image',
            'name_of_chef',
            'description',
        )