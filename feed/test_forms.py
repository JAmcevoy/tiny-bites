from django.test import TestCase
from django_summernote.widgets import SummernoteWidget
from .forms import CommentForm, PostFormCreate
from .models import Comment, Create

class CommentFormTest(TestCase):

    def test_comment_form_fields(self):
        form = CommentForm()
        self.assertIn('body', form.fields)
        self.assertEqual(form.fields['body'].label, 'Comment')