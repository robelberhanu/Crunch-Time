from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from message_board import views
from . import models

class DatabaseTests(TestCase):

    def test_user(self):
        user = User.objects.first()
        self.assertEqual(user, None)



