from django.test import SimpleTestCase
from registration.views import register
from django.urls import resolve, reverse

class TestRegistrationUrls(SimpleTestCase):

    def test_register_url(self):
        url = reverse('registerView');
        # print(resolve(url))
        self.assertEqual(resolve(url).func, register)
