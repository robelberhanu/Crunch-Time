from django.test import TestCase
from users.models import CustomUser
from main.models import Club, Portfolio, StudentClubRelation
from users.models import CustomUser

class TestModels(TestCase):

   def test_main_Club(self):
      clubName = Club(club_name="My Club")
      # clubState = Club(is_deleted=)
      self.assertEqual(str(clubName), clubName.club_name)
      # self.assertEqual(str(clubState), clubState.is_deleted)

   def test_main_Portfolio(self):
      portName = Portfolio(portfolio_name="My Portfolio")
      self.assertEqual(str(portName), portName.portfolio_name)

   # def test_main_StudentClubRelation(self):
   #    studClubRel_userid = StudentClubRelation(CustomUser.username)
   #    studClubRel_clubid = StudentClubRelation(Club.club_name)
   #    studClubRel_portid = StudentClubRelation(Portfolio.portfolio_name)
   #    # results = studClubRel_userid+","+studClubRel_clubid+","+studClubRel_portid
   #    self.assertEqual(str(studClubRel_userid), studClubRel_userid)

   # def test_users_CustomUser(self):
   #    contactNum = CustomUser(contact_number="Contact Number")
   #    idNum = CustomUser(id_number="Id Number")
   #    self.assertEqual(str(contactNum), contactNum.contact_number)