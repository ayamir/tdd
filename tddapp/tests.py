from django.urls import resolve
from django.test import TestCase
from tddapp.views import home_page

# Create your tests here.


class HomePageTestCase(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
