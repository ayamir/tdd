from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from tddapp.views import home_page

# Create your tests here.


class HomePageTestCase(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
