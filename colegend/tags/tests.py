from django.core.urlresolvers import reverse
from django.test import TestCase
import factory
from tags.forms import TagForm
from tags.models import Tag
from users.tests import UserFactory

__author__ = 'eraldo'


class TagFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tag
        django_get_or_create = ('name',)

    owner = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'Tag{0}'.format(n))
    description = "Some description."


class TagModelTests(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_create_tag(self):
        tag_new = Tag.objects.create(name="tag1", owner=self.user)
        self.assertEqual(str(tag_new), "tag1")


class TagViewTests(TestCase):

    def setUp(self):
        pass
        # TODO: refactor out user creation

    def test_tag_list_view(self):
        user = UserFactory()
        tag = TagFactory(owner=user)
        self.client.login(username=user.username, password="tester")
        url = reverse("tags:tag_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(tag, response.context['object_list'])

    def test_tag_new_view(self):
        user = UserFactory()
        # tag = TagFactory(owner=user)
        self.client.login(username=user.username, password="tester")
        url = reverse("tags:tag_new")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], TagForm)

    def test_tag_new_view_saving_a_post_request(self):
        tag_attributes = TagFactory.attributes()
        self.client.login(username=tag_attributes["owner"].username, password="tester")
        url = reverse("tags:tag_new")
        response = self.client.post(url, data=tag_attributes)
        self.assertEqual(Tag.objects.count(), 1)
        new_tag = Tag.objects.first()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_tag.name, tag_attributes["name"])

    def test_tag_show_view(self):
        user = UserFactory()
        tag = TagFactory(owner=user)
        self.client.login(username=user.username, password="tester")
        url = reverse("tags:tag_show", args=[tag.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tag, response.context['object'])

    def test_tag_edit_view(self):
        user = UserFactory()
        tag = TagFactory(owner=user)
        self.client.login(username=user.username, password="tester")
        url = reverse("tags:tag_edit", args=[tag.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], TagForm)

    def test_tag_delete_view(self):
        user = UserFactory()
        tag = TagFactory(owner=user)
        self.client.login(username=user.username, password="tester")
        url = reverse("tags:tag_delete", args=[tag.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tag, response.context['object'])
