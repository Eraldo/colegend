from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class LoggedInTestMixin():
    """
    Provides an active logged in user.
    Set `user` on the TestCase to use instead of a default user.

    Accessible via `self.user`.
    Created by a user factory.
    """

    def setUp(self):
        user = UserFactory()
        self.client.login(username=user.username, password="tester")
        self.user = user
        super().setUp()


class LoggedInManagerTestMixin():
    """
    Provides an active logged in user who is also a manager.

    Accessible via `self.user`.
    Created by a user factory.
    """

    def setUp(self):
        manager = UserFactory(is_manager=True)
        self.client.login(username=manager.username, password="tester")
        self.manager = manager
        super().setUp()
