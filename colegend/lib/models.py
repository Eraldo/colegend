from annoying.fields import AutoOneToOneField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from statuses.models import Status

__author__ = 'eraldo'


class TimeStampedBase(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LoggableBase(models.Model):
    history = models.TextField(blank=True)

    class Meta:
        abstract = True

    def log(self, message):
        self.history += "[{time}] {message}\n".format(time=timezone.now(), message=message)


class TrackedBase(TimeStampedBase, LoggableBase):
    class Meta:
        abstract = True


class OwnedQueryMixin:
    def owned_by(self, user):
        return self.filter(owner=user)


class OwnedBase(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class AutoOwnedBase(models.Model):
    owner = AutoOneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

    class Meta:
        abstract = True


class StatusTrackedBase(models.Model):
    completion_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.old_status = self.status
        except Status.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        # Track status change and add completion date if closing task.
        if self.old_status.open() and self.status.closed():
            self.completion_date = timezone.now()
        super().save(*args, **kwargs)
        self.old_status = self.status


class AutoUrlMixin():

    def _get_auto_url(self, operation, pk=None):
        namespace = self._meta.app_label
        prefix = self._meta.model_name
        alias = '{}:{}_{}'.format(namespace, prefix, operation)
        args=[]
        if pk:
            args.append(pk)
        return reverse(alias, args=args)

    def get_list_url(self):
        return self._get_auto_url("list")

    def get_new_url(self):
        return self._get_auto_url("new")

    def get_show_url(self):
        return self._get_auto_url("show", pk=self.pk)

    def get_edit_url(self):
        return self._get_auto_url("edit", pk=self.pk)

    def get_delete_url(self):
        return self._get_auto_url("delete", pk=self.pk)

    def get_absolute_url(self):
        return self.get_show_url()


class ValidateModelMixin(object):

    """Make :meth:`save` call :meth:`full_clean`.

    .. warning:
        This should be the left-most mixin/super-class of a model.

    Do you think Django models ``save`` method will validate all fields
    (i.e. call ``full_clean``) before saving or any time at all? Wrong!

    I discovered this awful truth when I couldn't understand why
    a model object with an email field (without `blank=True`) could be
    saved with an empty string as email address.

    More info:

    * "Why doesn't django's model.save() call full clean?"
        http://stackoverflow.com/questions/4441539/
    * "Model docs imply that ModelForm will call Model.full_clean(),
        but it won't."
        https://code.djangoproject.com/ticket/13100

    """

    def save(self, *args, **kwargs):
        """Call :meth:`full_clean` before saving."""
        self.full_clean()
        super(ValidateModelMixin, self).save(*args, **kwargs)
