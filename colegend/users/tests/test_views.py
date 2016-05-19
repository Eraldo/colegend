from django.test import RequestFactory

from test_plus.test import TestCase

from ..views import (
    LegendUpdateView
)


class BaseUserTestCase(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()


class TestLegendUpdateView(BaseUserTestCase):
    def setUp(self):
        # call BaseUserTestCase.setUp()
        super(TestLegendUpdateView, self).setUp()
        # Instantiate the view directly. Never do this outside a test!
        self.view = LegendUpdateView()
        # Generate a fake request
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        self.view.request = request
