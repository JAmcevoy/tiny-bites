from django.contrib.auth.models import User
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from .models import Create, Comment


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
        self.user = User.objects.create_user(
            username='testuser', password='password'
        )  # fix error by adding test user to make author
        self.create1 = Create.objects.create(
            name='Test Post 1', slug='test-post-1',
            author=self.user)  # fixed error by adding slug an author
        self.create2 = Create.objects.create(name='Another Test Post',
                                             slug='another-test-post',
                                             author=self.user)

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
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        self.create = Create.objects.create(name='Test Post',
                                            slug='test-post',
                                            author=self.user)
        self.url = reverse('post_detail', kwargs={'slug': 'test-post'})

    def test_post_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_detail.html')

    def test_post_detail_view_post_comment(self):
        user = User.objects.create_user(
            username='uniqueuser', password='testpass'
        )  # need to add a unique username as testuser has already been created in test
        self.client.login(username='uniqueuser', password='testpass')
        response = self.client.post(self.url, {'body': 'Test comment'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(body='Test comment').exists())


class PostCreationViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('post_creation')
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')

    def test_post_creation_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_creation.html')

    def test_post_creation_view_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            self.url, {
                'name': 'New Post',
                'description': 'Description',
                'ingredients': 'Ingredients',
                'instructions': 'Instructions',
            })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Create.objects.filter(name='New Post').exists())


class EditPostViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.create = Create.objects.create(name='Test Post',
                                            slug='test-post',
                                            author=self.user)
        self.url = reverse('edit_post', kwargs={'slug': 'test-post'})

    def test_edit_post_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/edit_post.html')

    def test_edit_post_view_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            self.url, {
                'name': 'Updated Post',
                'description': 'Updated description',
                'ingredients': 'Updated ingredients',
                'instructions': 'Updated instructions',
            })
        self.assertEqual(response.status_code, 302)
        self.create.refresh_from_db()
        self.assertEqual(self.create.name, 'Updated Post')


class MyBitesViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.url = reverse('my_bites')
        self.create = Create.objects.create(name='Test Post',
                                            author=self.user,
                                            slug='test-post')

    def test_my_bites_view_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/my_bites.html')

    def test_my_bites_view_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')


class ToBeApprovedViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.url = reverse('to_be_approved')
        self.create = Create.objects.create(name='Test Post',
                                            author=self.user,
                                            slug='test_post')
        self.comment = Comment.objects.create(post=self.create,
                                              body='Pending comment',
                                              approved=False,
                                              author=self.user)

    def test_to_be_approved_view_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/to_be_approved.html')

    def test_to_be_approved_view_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')


class ApproveCommentViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.url = reverse('approve_comment', kwargs={'comment_id': 1})
        self.create = Create.objects.create(name='Test Post', author=self.user)
        self.comment = Comment.objects.create(post=self.create,
                                              body='Pending comment',
                                              approved=False,
                                              author=self.user)

    def test_approve_comment_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertTrue(self.comment.approved)


class DeleteCommentViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.create = Create.objects.create(name='Test Post',
                                            author=self.user,
                                            slug='test-post')
        self.comment = Comment.objects.create(post=self.create,
                                              body='Comment to delete',
                                              author=self.user)
        self.url = reverse('delete_comment',
                           kwargs={'comment_id': self.comment.id})

    def test_delete_comment_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())


class EditCommentViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.create = Create.objects.create(name='Test Post',
                                            author=self.user,
                                            slug='test-post')
        self.comment = Comment.objects.create(post=self.create,
                                              body='Comment to edit',
                                              author=self.user)
        self.url = reverse('edit_comment',
                           kwargs={'comment_id': self.comment.id})

    def test_edit_comment_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_detail.html')
        self.assertContains(response, 'Comment to edit')

    def test_edit_comment_view_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {'body': 'Updated comment'})
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, 'Updated comment')

    def test_edit_comment_view_post_invalid(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {'body': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_detail.html')
        form = response.context['comment_form']
        self.assertTrue(form.errors)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, 'Comment to edit')


class LoginViewTestCase(TestCase):
    def test_login_view(self):
        # Test whether the login view returns the login page
        self.client = Client()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_unsuccessful(self):
        # Test login with incorrect credentials
        response = self.client.post(reverse('login'), {
            'username': 'invaliduser',
            'password': 'invalidpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertIn(
            'The username and/or password you specified are not correct.',
            response.content.decode())

    def test_login_next_url(self):
        # Test login with redirection to a next URL
        slug = 'test-post'
        next_url = reverse('post_detail', kwargs={'slug': slug})
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Log in the user and redirect to the next URL
        response = self.client.post(reverse('login'), {
            REDIRECT_FIELD_NAME: next_url,
            'username': 'testuser',
            'password': 'testpass'
        }, follow=True)

        # Check if the response is a successful redirect
        self.assertEqual(response.status_code, 200)


class ProfileViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('profile')
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')

    def test_profile_view_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/profile.html')

    def test_profile_view_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_profile_view_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            self.url, {
                'firstName': 'Updated',
                'lastName': 'Name',
                'email': 'updated@example.com',
            })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.last_name, 'Name')
        self.assertEqual(self.user.email, 'updated@example.com')


class CustomPasswordChangeView(TestCase):
    success_url = reverse_lazy('profile')
    template_name = 'feed/profile.html'  # Set the template name

    def form_valid(self, form):
        response = super().form_valid(form)

        # Update session auth hash to prevent user from being logged out
        update_session_auth_hash(self.request, self.request.user)

        # Notify user of successful password change
        messages.success(self.request, 'Password changed successfully!')

        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Incorrect Password!')
        return self.render_to_response(self.get_context_data(form=form))
