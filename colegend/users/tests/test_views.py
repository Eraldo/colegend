from unittest import skip
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.http import urlencode
from users.models import User
from users.tests.test_models import UserFactory, SettingsFactory, ContactFactory, ProfileFactory
from users.views import UserUpdateView


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


class UserInactiveViewTest(TestCase):
    def test_redirect_accepted_user_to_home(self):
        user = UserFactory()
        self.client.login(username=user.username, password="tester")
        response = self.client.get(reverse('users:inactive'))
        self.assertRedirects(response, reverse("home"))

    def test_redirect_anonymous_user_to_login(self):
        response = self.client.get(reverse('users:inactive'))
        self.assertRedirects(response, reverse("account_login") + "?next=/users/inactive")

    def test_not_accepted_user_get_view(self):
        user = UserFactory(is_accepted=False)
        self.client.login(username=user.username, password="tester")
        response = self.client.get(reverse('users:inactive'))
        self.assertEquals(response.status_code, 200)


class UserRedirectViewTest(TestCase):
    def test_redirect_active_user_to_detail_page(self):
        user = UserFactory()
        self.client.login(username=user.username, password="tester")
        response = self.client.get(reverse('users:redirect'))
        self.assertRedirects(response, reverse("users:detail", kwargs={"username": user.username}))


class UserUpdateViewTest(TestCase):
    def test_get_view(self):
        user = UserFactory()
        self.client.login(username=user.username, password="tester")
        response = self.client.get(reverse('users:update'))
        self.assertEquals(response.status_code, 200)

    def test_redirect_anonymous_user_to_login_page(self):
        response = self.client.get(reverse('users:update'))
        next_parameter = "?next=/users/%7Eupdate/"  # TODO: Urlencode "?next=/users/~Update/" here instead.
        self.assertRedirects(response, reverse("account_login") + next_parameter)

    def test_update_user(self):
        user = UserFactory()
        self.client.login(username=user.username, password="tester")
        response = self.client.post(reverse('users:update'), data={"username": user.username})
        self.assertRedirects(response, reverse("users:detail", kwargs={"username": user.username}))


class SettingsUpdateViewTest(TestCase):
    def test_get_view(self):
        user = UserFactory()
        self.client.login(username=user.username, password="tester")
        response = self.client.get(reverse('users:settings'))
        self.assertEquals(response.status_code, 200)

    def test_update_settings(self):
        user = UserFactory()
        self.client.login(username=user.username, password="tester")
        data = {
            'day_start': '4',
            'language': 'EN',
        }
        response = self.client.post(reverse('users:settings'), data=data, follow=False)
        self.assertRedirects(response, reverse("users:detail", kwargs={"username": user.username}))


class UserManageListViewTests(TestCase):
    def test_get_view(self):
        manager = UserFactory(username="manager", is_manager=True)
        self.client.login(username=manager.username, password="tester")
        response = self.client.get(reverse('users:manage'))
        self.assertEquals(response.status_code, 200)


class UserManageDetailViewTests(TestCase):
    def test_get_view(self):
        user = UserFactory(is_accepted=False)
        ContactFactory(owner=user)
        ProfileFactory(owner=user)
        manager = UserFactory(username="manager", is_manager=True)
        self.client.login(username=manager.username, password="tester")
        response = self.client.get(reverse('users:manage_detail', kwargs={"username": user.username}))
        self.assertEquals(response.status_code, 200)

    def test_post(self):
        user = UserFactory(is_accepted=False)
        ContactFactory(owner=user)
        ProfileFactory(owner=user)
        manager = UserFactory(username="manager", is_manager=True)
        self.client.login(username=manager.username, password="tester")
        response = self.client.post(reverse('users:manage_detail', kwargs={"username": user.username}),
                                    data={"verify": user.pk})
        self.assertRedirects(response, reverse("users:manage"))
