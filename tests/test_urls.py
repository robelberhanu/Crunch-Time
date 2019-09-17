from django.urls import reverse, resolve
from django.test import SimpleTestCase

from users.views import user_profile_view

from user_message_board.views import MainMessages  # Might cause issues...
import user_message_board

from message_board.views import messageBoard, SendMessage
import message_board.views

from administration.views import user, club, create_user, create_club, edit_user, manage_users, manage_clubs


class TestUrls(SimpleTestCase):
    # -------------------
    # users
    def test_user_profile_url(self):
        # print('\n Hello World xD \n')
        url = reverse('user_profile')
        self.assertEquals(resolve(url).func, user_profile_view)

    # ------------------
    # user message board
    def test_main_message_board_url(self):  # mainMessageBoardView
        url = reverse('mainMessageBoardView')
        # print('Hello World xD')
        self.assertEquals(resolve(url).func, MainMessages)

    def test_main_message_url(self):  # mainMessageBoardView
        url = reverse('UserMessage')
        # print('Hello World xD')
        self.assertEquals(resolve(url).func, user_message_board.views.Messages)

    # -------------------
    # Admin Message Board - i.e. message_board
    def test_admin_message_board_url(self):
       url = reverse('Messages')
       self.assertEquals(resolve(url).func, message_board.views.Messages)

    def test_admin_message_url(self):
       url = reverse('messageBoardView')
       # print(resolve(url))
       self.assertEquals(resolve(url).func, messageBoard)

    def test_send_message_url(self):
        url = reverse('SendMessage')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, SendMessage)

    # -------------------
    # Administration
    def test_manage_users_url(self):
        url = reverse('manage_users')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, manage_users)

    def test_manage_clubs_url(self):
        url = reverse('manage_clubs')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, manage_clubs)

    def test_create_user_url(self):
        url = reverse('create_user')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, create_user)

    def test_create_club_url(self):
        url = reverse('create_club')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, create_club)

    def test_user_url(self):
        url = reverse('user', args=['username'])
        self.assertEqual(resolve(url).func, user)

    def test_club_url(self):
        url = reverse('club', args=['club_id'])
        self.assertEqual(resolve(url).func, club)

    def test_edit_user_url(self):
        url = reverse('edit_user', args=['username'])
        self.assertEqual(resolve(url).func, edit_user)