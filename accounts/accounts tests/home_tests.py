from django.test import Client, TestCase
from accounts.models import User

class TestDataPage(TestCase):
    def setUp(self):
        self.client = Client()