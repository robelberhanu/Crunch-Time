# from django.test import SimpleTestCase, Client
# from django.urls import reverse, resolve
# from administration.views import manage_users, create_user, manage_clubs, club, user, edit_user
#
#
# class TestAdministrationUrls(SimpleTestCase):
#
#     def setUp(self):
#         self.client = Client(
#
#         )
#
#     def test_manage_user_url(self):
#         url = reverse('manage_users')
#         print(resolve(url).func)
#         self.assertEqual(resolve(url).func, manage_users)
#
#     def test_create_user_url(self):
#         url = reverse('create_user')
#         # print(resolve(url))
#         self.assertEqual(resolve(url).func, create_user)
#
#     def test_user_url(self):
#         testId = 12
#         url = reverse('user', args=['user_id'])
#         # print('Arguments: ',resolve(url))
#         self.assertEqual(resolve(url).func, user)
#
#     def test_manage_clubs_url(self):
#         url = reverse('manage_clubs')
#         # print(resolve(url))
#         self.assertEqual(resolve(url).url_name, 'manage_clubs')
#         self.assertEqual(resolve(url).func, manage_clubs)
#
#     def test_clubs_url(self):
#         url = reverse('club', args=['club_id'])
#         # print(resolve(url))
#         self.assertEqual(resolve(url).func, club)
#
#     def test_edit_user_url(self):
#         url = reverse('edit_user', args=['user_id'])
#         # print('Arguments: ',resolve(url))
#         self.assertEqual(resolve(url).func, edit_user)
