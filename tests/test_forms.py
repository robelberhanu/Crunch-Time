import unittest
from django.test import SimpleTestCase, TestCase
from administration.forms import ClubCreationForm, StudentClubRelationCreationForm, EditUserForm
from main.models import Club

class TestForms(TestCase):

    # test administration forms
    # club creation
    def test_club_creation_form_valid_data(self):
        form = ClubCreationForm(
            data={
                'club_name': 'Hockey'
            }
        )
        self.assertTrue(form.is_valid())
        clubcreation = form.save()
        self.assertEqual(clubcreation.club_name, "Hockey")

    def test_club_creation_form_no_data(self):
        form = ClubCreationForm(
            data={}
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    #studentclubrelationcreationform
    def test_student_club_relation_creation_form_valid_data(self):
        attr = {'user_id': 'null', 'portfolio_id': 'null'}
        form = StudentClubRelationCreationForm(
            data=attr
        )
        self.assertFalse(form.is_valid())
        # fix the input attr to take the right values
        #print(form.errors)

    def test_student_club_relation_creation_form_no_data(self):

        form = StudentClubRelationCreationForm(
            data={}
        )
        self.assertFalse(form.is_valid())

    # clean
    # def test_clean_student_club_relation_creation_form_valid_data(self):
        # attr = {''}

    def test_edit_user_form_valid_data(self):
        attr = {'first_name': 'testFirstName', 'last_name': 'testLastName', 'email': 'test@gmail.com', 'contact_number':'0123456789'}
        form = EditUserForm(
            data=attr
        )
        self.assertTrue(form.is_valid())