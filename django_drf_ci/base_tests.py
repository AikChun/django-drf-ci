from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase


class BaseApiTest(TestCase):
    def setUp(self):
        superuser = User.objects.create_superuser('test', 'test@api.com', 'testpassword')
        self.factory = RequestFactory()
        self.user = superuser
        self.client.login(username=superuser.username, password='testpassword')
