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

class PostFormCreateTest(TestCase):

    def test_post_form_create_fields(self):
        form = PostFormCreate()
        self.assertIn('name', form.fields)
        self.assertIn('featured_image', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('ingredients', form.fields)
        self.assertIn('instructions', form.fields)

    def test_post_form_create_widgets(self):
        form = PostFormCreate()
        self.assertIsInstance(form.fields['description'].widget, SummernoteWidget)
        self.assertIsInstance(form.fields['ingredients'].widget, SummernoteWidget)
        self.assertIsInstance(form.fields['instructions'].widget, SummernoteWidget)