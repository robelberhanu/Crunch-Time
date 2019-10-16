from django.test import TestCase, Client


class TestAdministrationViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.manage_users_url = reversed('manage_users')
        self.create_user_url = reversed('create_user')
        self.user_url = reversed('user')
        self.manage_clubs_url = reversed('manage_clubs')
        self.club_url = reversed('club')

    def test_manage_users_GET(self):
        response = self.client.get(self.manage_users_url)
        print('Manage Users Response: ',response)
    #     self.assertEqual(response.status_code, 200)

    def test_create_user_GET(self):
        response = self.client.get(self.create_user_url)
        print('Create User Response: ',response)
        # self.assertEqual(response.status_code, 200)

    def test_user_GET(self):
        response = self.client.get(self.user_url)
        print('User Response: ',response)
        # self.assertEqual(response.status_code, 200)

    def test_manage_clubs_GET(self):
        response = self.client.get(self.manage_clubs_url)
        print(response)
        # self.assertEqual(response.status_code, 200)

    def test_club_GET(self):
        response = self.client.get(self.club_url)
        print(response)
        # self.assertEqual(response.status_code, 200)