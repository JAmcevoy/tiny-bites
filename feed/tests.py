from django.test import TestCase, Client
from django.urls import reverse
from .models import Create

class SecurityTest(TestCase):
    """
    Tests related to security features of the application.
    """

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_csrf(self):
        """
        Ensure that the CSRF token is included in the response.
        """
        response = self.client.get(self.url)
        self.assertContains(response, 'csrfmiddlewaretoken')


class PerformanceTest(TestCase):
    """
    Tests related to the performance of the application.
    """

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_query_count(self):
        """
        Ensure that the number of database queries does not exceed expected limit.
        """
        self.client.get(reverse('home'))
        with self.assertNumQueries(1):
            self.client.get(reverse('home'))
