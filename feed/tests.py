from django.test import TestCase, Client
from django.urls import reverse
from .models import Create

# Create your tests here.

class SecurityTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_csrf(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'csrfmiddlewaretoken')


class PerformanceTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_query_count(self):
        self.client.get(reverse('home'))
        with self.assertNumQueries(1):
            self.client.get(reverse('home'))