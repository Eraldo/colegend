from urllib.request import Request

from django.test import TestCase

from users.tests.factories import UserFactory
from .views import PrologueView


class PrologueViewTests(TestCase):
    """
    Unit test case for testing the `PrologueView`.
    """

    def setUp(self):
        # Attach the view to be tested to this class
        view = PrologueView()
        self.view = view
        # Generate a fake request
        view.request = Request

    def test_get_client_ip(self):
        self.view.request.META = {'HTTP_X_FORWARDED_FOR': '89.204.139.76'}
        request = self.view.request
        self.assertEqual(self.view.get_client_ip(request), '89.204.139.76')

    def test_get_client_country(self):
        self.view.request.META = {'HTTP_X_FORWARDED_FOR': '89.204.139.76'}
        self.assertEqual(self.view.get_client_country(), 'Germany')

    def test_get_client_country__with_unknown_ip(self):
        self.view.request.META = {'HTTP_X_FORWARDED_FOR': '10.0.0.1'}
        self.assertEqual(self.view.get_client_country(), '')

    def test_get_prologue_country__from_countinous(self):
        user = UserFactory()
        self.view.request.user = user
        user.continuous.prologue_country = 'Germany'
        self.assertEqual(self.view.get_prologue_country(), 'Germany')

    def test_get_prologue_country__from_ip(self):
        self.view.request.META = {'HTTP_X_FORWARDED_FOR': '89.204.139.76'}
        user = UserFactory()
        self.view.request.user = user
        self.assertEqual(self.view.get_prologue_country(), 'Germany')
        # Check if the country has been saved to the continious path.
        self.assertEqual(user.continuous.prologue_country, 'Germany')

    def test_get_time_of_day(self):
        # TODO: Write tests
        pass

    def test_post(self):
        # TODO: Write tests
        pass
