from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Create, Comment
from .forms import PostFormCreate, CommentForm

class PostListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_post_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/index.html')