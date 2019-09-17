from django.test import TestCase, Client
from django.urls import reverse
from administration.views import manage_users
from users.views import CustomUser


class TestViews(TestCase):

    def login_as_superuser(self):
        # store the password to login later
        password = 'mypassword'
        my_admin = CustomUser.objects.create_superuser('myuser', 'myemail@test.com', password)
        # c = Client()
        # You'll need to log him in before you can send requests through the client
        self.client.login(username=my_admin.username, password=password)
        return self

    def test_manage_users_view(self):
        self.login_as_superuser()  # self =
        url = reverse("manage_users")
        print("url: ",url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_manage_clubs_view(self):
        self.login_as_superuser()
        url = reverse("manage_clubs")
        # print("url: ",url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_user_view(self):
        self.login_as_superuser()  # self =
        url = reverse("create_user")
        # print("url: ",url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_club(self):
        self.login_as_superuser()  # self =
        url = reverse("create_club")
        # print("url: ",url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    # Note: Need to create a user for this to work...
    def test_edit_user_view(self):
        self.login_as_superuser()  # self =
        url = reverse("edit_user", args=['username'])
        print("edit_user_view url: ",url,"\n")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_club_view(self):
        self.login_as_superuser()  # self =
        url = reverse("edit_user", args=['club_id'])
        print("club_view url: ",url, "\n")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

