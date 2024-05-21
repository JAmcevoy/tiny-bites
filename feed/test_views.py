from django.contrib.auth.models import User
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


class SearchFeatureViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('search_feature')
        self.user = User.objects.create_user(username='testuser', password='password') # fix error by adding test user to make author
        self.create1 = Create.objects.create(name='Test Post 1', slug='test-post-1', author=self.user) # fixed error by adding slug an author
        self.create2 = Create.objects.create(name='Another Test Post', slug='another-test-post', author=self.user)

    def test_search_feature_post(self):
        response = self.client.post(self.url, {'search_query': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/search_results.html')
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Another Test Post')

    def test_search_feature_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/search_results.html')


class PostDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.create = Create.objects.create(name='Test Post', slug='test-post', author=self.user)
        self.url = reverse('post_detail', kwargs={'slug': 'test-post'})

    def test_post_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_detail.html')

    def test_post_detail_view_post_comment(self):
        user = User.objects.create_user(username='uniqueuser', password='testpass') # need to add a unique username as testuser has already been created in test
        self.client.login(username='uniqueuser', password='testpass')
        response = self.client.post(self.url, {'body': 'Test comment'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(body='Test comment').exists())


class PostCreationViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('post_creation')
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_post_creation_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_creation.html')