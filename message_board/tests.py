from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.
#from message_board import views

class MessageBoardTests(TestCase):

    def test_message_board_validity(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Message Board</title>')

