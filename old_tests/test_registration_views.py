# from django.test import TestCase, Client
# from django.urls import reverse
#
# class TestRegistrationViews(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.register_url = reverse('registerView')
#
#     def test_register_GET(self):
#         response = self.client.get(self.register_url)
#         #print(response)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/register.html')
