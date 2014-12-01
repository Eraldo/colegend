from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from users.models import User


class UserViewTests(TestCase):
    def test_list_view_anonymous(self):
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 302)

    def test_list_view_authenticated(self):
        """Test the user list view with a logged in user."""
        usernew = User.objects.create_user(username="Usernew", password="usernew", is_accepted=True)
        self.client.login(username="Usernew", password="usernew")
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Usernew")
        self.assertQuerysetEqual(response.context['user_list'], ['<User: Usernew>'])

    def test_list_view_unauthenticated(self):
        """Test the user list view with a logged in user."""
        usernew = User.objects.create_user(username="Usernew", password="usernew", is_accepted=False)
        self.client.login(username="Usernew", password="usernew")
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 302)
