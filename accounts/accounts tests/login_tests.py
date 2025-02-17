from django.test import Client, TestCase
from accounts.models import User

class TestLoginUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.temp = User(username="temp", password="password", email="<EMAIL>")
        self.temp.save()

    def test_page_access(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_successful_login(self):
        response = self.client.post('/', {"username": "temp", "password": "password"})
        self.assertEqual(response.status_code, 302)


    def test_failed_login(self):
        response = self.client.post('/', {"username": "wrongUsername", "password": "wrongPassword"})
        self.assertEqual(response.status_code, 200) # doesn't redirect due to incorrect password
        self.assertTemplateUsed(response, "accounts/login.html")


    def test_empty_login(self):
        response = self.client.post('/', {"username": "", "password": ""})
        self.assertEqual(response.status_code, 200) # doesn't redirect due to empty field entries
        self.assertTemplateUsed(response, 'accounts/login.html')


    def test_no_username(self):
        response = self.client.post('/', {"username": "", "password": "password"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')


    def test_no_password(self):
        response = self.client.post('/', {"username": "temp", "password": ""})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')


    def test_wrong_password(self):
        response = self.client.post('/', {"username": "temp", "password": "wrongPassword"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')


    def test_wrong_username(self):
        response = self.client.post('/', {"username": "wrongUsername", "password": "password"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')