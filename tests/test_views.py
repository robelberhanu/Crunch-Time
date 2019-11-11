from django.test import TestCase, Client
from django.urls import reverse
from administration.views import manage_users
from users.views import user_profile_view
from users.models import CustomUser
from message_board.views import messageBoard

class TestViews(TestCase):

    def login_as_superuser(self):
        # store the password to login later
        password = 'mypassword'
        my_admin = CustomUser.objects.create_superuser('myuser', 'myemail@test.com', password)
        # You'll need to log him in before you can send requests through the client
        self.client.login(username=my_admin.username, password=password)
        return self

    def test_manage_users_view(self):
        self.login_as_superuser()  # self =
        url = reverse("manage_users")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'administration/manage_users.html')

    def test_manage_clubs_view(self):
        self.login_as_superuser()
        url = reverse("manage_clubs")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'administration/manage_clubs.html')

    def test_create_user_view(self):
        self.login_as_superuser()  # self =
        url = reverse("create_user")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'administration/create_user.html')

    def test_create_club(self):
        self.login_as_superuser()  # self =
        url = reverse("create_club")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'administration/create_club.html')

    # # Note: Need to create a user for this to work...
    def test_edit_user_view(self):
        self.login_as_superuser()  # self =
        url = reverse("edit_user", args=['username'])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        self.assertTemplateNotUsed(resp, 'administration/edit_user.html')

    def test_club_view(self):
        self.login_as_superuser()  # self =
        url = reverse("edit_user", args=['club_id'])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
        self.assertTemplateNotUsed(resp, 'administration/club.hhtml')
