from django.core.urlresolvers import reverse
from django.db import models

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


class TrackedBase(TimeStampedBase, LoggableBase):
    class Meta:
        abstract = True


class AutoUrlMixin():

    def _get_auto_url(self, operation, pk=None):
        namespace = self._meta.app_label
        prefix = self._meta.module_name
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
