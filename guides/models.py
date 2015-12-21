from allauth.account.signals import user_signed_up
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from django_slack import slack_message
from core.models import AutoOwnedBase, TimeStampedBase


class GuideRelationQuerySet(models.QuerySet):
    def searching(self):
        return self.filter(guide__isnull=True)

    def active(self):
        return self.filter(done=False, guide__isnull=False)

    def passive(self):
        return self.filter(done=True)


class GuideRelation(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the relation between a user and his guide.
    """
    # TODO: make sure that guide and guidee are never the same user.

    guide = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='guidee_relations',
        null=True)
    outer_call_checked = models.BooleanField(
        verbose_name=_("Talked about Outer Call"),
        default=False)
    inner_call_checked = models.BooleanField(
        verbose_name=_("Talked about Inner Call"),
        default=False)
    coLegend_checked = models.BooleanField(
        verbose_name=_("Answered any questions about coLegend"),
        default=False)
    guiding_checked = models.BooleanField(
        verbose_name=_("Talked about becoming a Guide"),
        default=False)
    done = models.BooleanField(
        verbose_name=_("Guiding process is done"),
        default=False)

    objects = GuideRelationQuerySet.as_manager()

    def __str__(self):
        return "Guide relation: {} - {}".format(self.owner, self.guide)

    def get_absolute_url(self):
        return reverse('guides:detail', kwargs={'owner': self.owner.username})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # Check if the guide did all tasks with his guidee.
        if not self.done:
            connected = self.owner.connected
            if all(
                [self.guide, self.outer_call_checked, self.inner_call_checked,
                 self.coLegend_checked, self.guiding_checked]):
                self.done = True
                connected.guide = True
                connected.save()
        super().save(force_insert, force_update, using, update_fields)


@receiver(user_signed_up)
def start_guiding_process(request, user, **kwargs):
    # Create a new guide relation
    relation = user.guiderelation
    # Notify potential guides
    username = user.username
    url = reverse('guides:list')
    message = "{} is looking for a guide: {}".format(username, url)
    slack_message('slack/message.slack', {'message': '@channel: {}'.format(message), 'channel': 'cloudguide'})
