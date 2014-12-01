from django.core.urlresolvers import reverse
from django.test import TestCase
from tags.forms import TagForm
from tags.models import Tag
from tags.tests.test_models import TagFactory
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class LoggedInTestMixin():

    def setUp(self):
        user = UserFactory()
        self.client.login(username=user.username, password="tester")
        self.user = user


class TagListViewTest(LoggedInTestMixin, TestCase):

    def test_tag_list_view(self):
        tag = TagFactory(owner=self.user)
        url = reverse("tags:tag_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(tag, response.context['object_list'])


class TagNewViewTest(LoggedInTestMixin, TestCase):

    def test_tag_new_view(self):
        url = reverse("tags:tag_new")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], TagForm)

    def test_tag_new_view_saving_a_post_request(self):
        tag_attributes = TagFactory.attributes()
        tag_attributes["owner"] = self.user
        url = reverse("tags:tag_new")
        response = self.client.post(url, data=tag_attributes)

        self.assertEqual(Tag.objects.count(), 1)
        new_tag = Tag.objects.first()
        self.assertEqual(new_tag.name, tag_attributes["name"])
        self.assertRedirects(response, reverse("tags:tag_list"))


class TagShowViewTest(LoggedInTestMixin, TestCase):

    def test_tag_show_view(self):
        tag = TagFactory(owner=self.user)
        url = reverse("tags:tag_show", args=[tag.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tag, response.context['object'])


class TagEditViewTest(LoggedInTestMixin, TestCase):

    def test_tag_edit_view(self):
        tag = TagFactory(owner=self.user)
        url = reverse("tags:tag_edit", args=[tag.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], TagForm)


class TagDeleteViewTest(LoggedInTestMixin, TestCase):

    def test_tag_delete_view(self):
        tag = TagFactory(owner=self.user)
        url = reverse("tags:tag_delete", args=[tag.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tag, response.context['object'])
