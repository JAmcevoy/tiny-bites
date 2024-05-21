from django.test import TestCase
from django_summernote.widgets import SummernoteWidget
from .forms import CommentForm, PostFormCreate
from .models import Comment, Create

class CommentFormTest(TestCase):

    def test_comment_form_fields(self):
        form = CommentForm()
        self.assertIn('body', form.fields)
        self.assertEqual(form.fields['body'].label, 'Comment')

    def test_comment_form_valid_data(self):
        form = CommentForm(data={'body': 'Test comment'})
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_data(self):
        form = CommentForm(data={'body': ''})
        self.assertFalse(form.is_valid())