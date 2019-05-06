from django.test import TestCase
from django.contrib.auth.models import User
from django.db import models
from . import models
# Create your tests here.

class TestMainModels(TestCase):

    #def setUp(self):
    #    self.club1 = Club.objects.create(
    #        club_id = "",
    #        club_name="Hockey"
    #    )

    #def test_club_is_created_succesfully(self):
    #    print(self.club1.slug)
    #    #self.assertEquals(self.club1.first(), "Hockey")

    def test_user(self):
        user = User.objects.all()
        print(user)