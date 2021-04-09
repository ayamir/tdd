from django.test import TestCase


class SmokeTestCase(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)


# Create your tests here.
