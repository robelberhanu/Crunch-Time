from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.mainMessageBoard_url = reverse('mainMessageBoardView')
        self.messages_url = reverse('Messages')
        self.sendmessage_url = reverse('SendMessage')