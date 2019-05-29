from django.test import SimpleTestCase
from message_board.views import messageBoard, Messages, ManageClubs, ManageUsers, CustomiseUsers, SendMessage, CustomiseClubs
from django.urls import reverse, resolve

# MainMessages,

class TestMessageBoardUrls(SimpleTestCase):

    def test_messageBoard_url_resolves(self):
       url = reverse('messageBoardView')
       # print(resolve(url))
       self.assertEquals(resolve(url).func, messageBoard)

    def test_Messages_url_resolves(self):
       url = reverse('Messages')
       # print(resolve(url))
       self.assertEquals(resolve(url).func, Messages)

    # def test_MainMessages_url_resolves(self):
    #     url = reverse('MainMessageBoard')
    #     # print(resolve(url))
    #     self.assertEquals(resolve(url).func, MainMessages)

    def test_ManageUsers_url_resolves(self):
       url = reverse('ManageUsers')
       # print(resolve(url))
       self.assertEquals(resolve(url).func, ManageUsers)

    def test_ManageClubs_url_resolves(self):
       url = reverse('ManageClubs')
       # print(resolve(url))
       self.assertEquals(resolve(url).func, ManageClubs)

    def test_CustomiseUsers_url_resolves(self):
       url = reverse('CustomiseUsers')
       # print(resolve(url))
       self.assertEquals(resolve(url).func, CustomiseUsers)

    def test_SendMessage_url_resolves(self):
       url = reverse('SendMessage')
       # print(resolve(url))
       self.assertEquals(resolve(url).func, SendMessage)

    def test_CustomiseClubs_url_resolves(self):
       url = reverse('CustomiseClub')
       # print(resolve(url))
       self.assertEquals(resolve(url).func, CustomiseClubs)