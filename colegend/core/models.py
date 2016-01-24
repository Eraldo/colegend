from annoying.fields import AutoOneToOneField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class TimeStampedBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OwnedCheckMixin(object):
    """
    Adds the ability to check ownership.
    """

    def owned_by(self, user):
        if user == self.owner:
            return True
        else:
            return False


class OwnedBase(OwnedCheckMixin, models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class SingleOwnedBase(OwnedCheckMixin, models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class AutoOwnedBase(OwnedCheckMixin, models.Model):
    owner = AutoOneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

    class Meta:
        abstract = True


class OwnedQuerySet(object):
    """
    Enable to the queryset to be filtered by owning users.
    """

    def owned_by(self, user):
        return self.filter(owner=user)


class AutoUrlsMixin(object):
    """
    A mixin that automatically adds the CRUD urls to the model.
    """

    def get_index_url(self):
        app = self._meta.app_label
        url = '{}:index'.format(app)
        return reverse(url)

    def get_list_url(self):
        app = self._meta.app_label
        url = '{}:list'.format(app)
        return reverse(url)

    def get_create_url(self):
        app = self._meta.app_label
        url = '{}:create'.format(app)
        return reverse(url)

    def get_detail_url(self):
        app = self._meta.app_label
        url = '{}:detail'.format(app)
        return reverse(url, kwargs={'pk': self.pk})

    def get_update_url(self):
        app = self._meta.app_label
        url = '{}:update'.format(app)
        return reverse(url, kwargs={'pk': self.pk})

    def get_delete_url(self):
        app = self._meta.app_label
        url = '{}:delete'.format(app)
        return reverse(url, kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return self.get_detail_url()
