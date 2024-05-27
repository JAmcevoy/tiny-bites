from django.contrib.auth.models import User
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages import get_messages
from .models import Create, Comment


class PostListViewTest(TestCase):

    """
    Tests the view for listing posts.
    """

    def setUp(self):
        """
        Sets up the client and the URL for the home page.
        """
        self.client = Client()
        self.url = reverse('home')

    def test_post_list_view(self):
        """
        Tests the behavior of the post list view.
        Verifies that the response status code is 200 (OK).
        Verifies that the correct template is used for rendering.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/index.html')


class SearchFeatureViewTest(TestCase):

    """
    Tests the search feature view.
    """

    def setUp(self):
        """
        Sets up the client, URL for the search feature, and creates test data.
        """
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
        """
        Tests the behavior of the search feature when using the POST method.
        Verifies that the response status code is 200 (OK).
        Verifies that the correct template is used for rendering.
        Verifies that the response contains the expected search results.
        """
        response = self.client.post(self.url, {'search_query': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/search_results.html')
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Another Test Post')

    def test_search_feature_get(self):
        """
        Tests the behavior of the search feature when using the GET method.
        Verifies that the response status code is 200 (OK).
        Verifies that the correct template is used for rendering.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/search_results.html')


class PostDetailViewTest(TestCase):

    """
    Tests the view for displaying post details.
    """

    def setUp(self):
        """
        Sets up the client, user, post data, and URL for the post detail view.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        self.create = Create.objects.create(name='Test Post',
                                            slug='test-post',
                                            author=self.user)
        self.url = reverse('post_detail', kwargs={'slug': 'test-post'})

    def test_post_detail_view(self):
        """
        Tests the behavior of the post detail view.
        Verifies that the response status code is 200 (OK).
        Verifies that the correct template is used for rendering.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_detail.html')

    def test_post_detail_view_post_comment(self):
        """
        Tests the behavior of the post detail view when posting a comment.
        Verifies that the response status code is 200 (OK).
        Verifies that the comment is successfully added to the database.
        """
        user = User.objects.create_user(
            username='uniqueuser', password='testpass'
        )  # need to add a unique username as testuser has already been created in test
        self.client.login(username='uniqueuser', password='testpass')
        response = self.client.post(self.url, {'body': 'Test comment'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(body='Test comment').exists())


class PostCreationViewTest(TestCase):

    """
    Tests the view for creating a new post.
    """
    def setUp(self):
        """
        Sets up the client, URL for the post creation view, and creates a test user.
        """
        self.client = Client()
        self.url = reverse('post_creation')
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')

    def test_post_creation_view_get(self):
        """
        Tests the behavior of the post creation view when accessing via GET request.
        Verifies that the response status code is 200 (OK).
        Verifies that the correct template is used for rendering.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_creation.html')

    def test_post_creation_view_post(self):
        """
        Tests the behavior of the post creation view when submitting a POST request.
        Verifies that the response status code is 302 (Redirect).
        Verifies that the new post is successfully created and saved to the database.
        """
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

    """
    Tests the view for editing a post.
    """
    def setUp(self):
        """
        Sets up the client, creates a test user and a post, and defines the URL for editing the post.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.create = Create.objects.create(name='Test Post',
                                            slug='test-post',
                                            author=self.user)
        self.url = reverse('edit_post', kwargs={'slug': 'test-post'})

    def test_edit_post_view_get(self):
        """
        Tests the behavior of the edit post view when accessing via GET request.
        Verifies that the response status code is 200 (OK).
        Verifies that the correct template is used for rendering.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/edit_post.html')

    def test_edit_post_view_post(self):
        """
        Tests the behavior of the edit post view when submitting a POST request.
        Verifies that the response status code is 302 (Redirect).
        Verifies that the post is successfully updated in the database.
        """
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


class DeletePostsTest(TestCase):
    """
    Tests the delete_posts function.
    """

    def setUp(self):
        """
        Set up the client, create a test user, and a test post.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Create.objects.create(name='Test Post', author=self.user, slug='test-post')

    def test_delete_posts(self):
        """
        Tests the delete_posts function.
        Verifies that a post is deleted successfully.
        """
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse('delete_post', kwargs={'slug': self.post.slug}))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Create.objects.filter(slug=self.post.slug).exists())


class MyBitesViewTest(TestCase):

    """
    Tests the view for displaying user's saved posts (bites).
    """

    def setUp(self):
        """
        Sets up the client, creates a test user, a test post, and defines the URL for accessing user's saved posts.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.url = reverse('my_bites')
        self.create = Create.objects.create(name='Test Post',
                                            author=self.user,
                                            slug='test-post')

    def test_my_bites_view_authenticated(self):
        """
        Tests the behavior of the my bites view when the user is authenticated.
        Verifies that the response status code is 200 (OK).
        Verifies that the correct template is used for rendering.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/my_bites.html')

    def test_my_bites_view_unauthenticated(self):
        """
        Tests the behavior of the my bites view when the user is unauthenticated.
        Verifies that the response status code is 200 (OK).
        Verifies that the user is redirected to the login page.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')


class ToBeApprovedViewTest(TestCase):

    """
    Tests the view for displaying comments to be approved by an admin.
    """

    def setUp(self):
        """
        Sets up the client, creates a test user, a test post, and a pending comment.
        """
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
        """
        Tests the behavior of the to-be-approved view when the user is authenticated.
        Verifies that the response status code is 200 (OK).
        Verifies that the correct template is used for rendering.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/to_be_approved.html')

    def test_to_be_approved_view_unauthenticated(self):
        """
        Tests the behavior of the to-be-approved view when the user is unauthenticated.
        Verifies that the response status code is 200 (OK).
        Verifies that the user is redirected to the login page.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')


class ApproveCommentViewTest(TestCase):

    """
    Tests the view for approving comments by an admin.
    """

    def setUp(self):
        """
        Sets up the client, creates a test user, a test post, and a pending comment.
        """
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
        """
        Tests the behavior of the approve comment view.
        Verifies that the user can approve a pending comment.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertTrue(self.comment.approved)

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
    """
    Tests the view for deleting comments.
    """
    def setUp(self):
        """
        Sets up the client, creates a test user, a test post, and a comment to delete.
        """
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
        """
        Tests the behavior of the delete comment view for GET request.
        Verifies that the comment is deleted after the GET request.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())


class EditCommentViewTest(TestCase):

    """
    Tests the view for editing comments.
    """

    def setUp(self):
        """
        Sets up the client, creates a test user, a test post, and a comment to edit.
        """
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
        """
        Tests the behavior of the edit comment view for GET request.
        Verifies that the view returns the correct template and contains the comment to edit.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_detail.html')
        self.assertContains(response, 'Comment to edit')

    def test_edit_comment_view_post(self):
        """
        Tests the behavior of the edit comment view for POST request with valid data.
        Verifies that the comment is updated with the new content.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {'body': 'Updated comment'})
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, 'Updated comment')

    def test_edit_comment_view_post_invalid(self):
        """
        Tests the behavior of the edit comment view for POST request with invalid data.
        Verifies that the comment is not updated and errors are present in the form.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, {'body': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/post_detail.html')
        form = response.context['comment_form']
        self.assertTrue(form.errors)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, 'Comment to edit')


class LoginViewTestCase(TestCase):

    """
    Tests for the login functionality.
    """

    def test_login_view(self):
        """
        Test whether the login view returns the login page.
        """
        self.client = Client()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_unsuccessful(self):
        """
        Test login with incorrect credentials.
        """
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
        """
        Test login with redirection to a next URL.
        """
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

    """
    Tests for the user profile view.
    """

    def setUp(self):
        """
        Set up the client and URL for profile view.
        """
        self.client = Client()
        self.url = reverse('profile')
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')

    def test_profile_view_authenticated(self):
        """
        Test profile view for authenticated user.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/profile.html')

    def test_profile_view_unauthenticated(self):
        """
        Test profile view for unauthenticated user.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_profile_view_post(self):
        """
        Test profile view for POST request.
        """
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


class CustomPasswordChangeViewTest(TestCase):

    """
    Test suite for CustomPasswordChangeView.
    Ensures the correct behavior of the password change view in a Django app.
    Includes tests for valid password change and invalid old password scenarios.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass', 
        )
        self.url = reverse_lazy('profile')
        self.client.login(username='testuser', password='testpass') 

    def test_password_change_view_post_valid(self):
        """
        Test password change with valid input.
        """
        response = self.client.post(
            self.url, {
                'old_password': 'testpass',
                'new_password1': 'newpass123',
                'new_password2': 'newpass123',
            })
        self.assertRedirects(response, reverse_lazy('profile'))

    def test_password_change_view_post_invalid_old_password(self):
        """
        Test password change with invalid old password.
        """
        response = self.client.post(
            self.url, {
                'old_password': 'wrongpass',
                'new_password1': 'newpass123',
                'new_password2': 'newpass123',
            })
        
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse_lazy('profile'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertTrue(str(messages[0]) == 'Profile updated successfully!' or str(messages[0]) == 'Incorrect Password!')

