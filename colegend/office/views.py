from itertools import zip_longest

from rest_framework import viewsets
from django.utils.translation import ugettext_lazy as _

from colegend.experience.models import add_experience
from colegend.scopes.models import get_scope_by_name, DAY, WEEK, MONTH
from .serializers import FocusSerializer
from .models import Focus


class FocusViewSet(viewsets.ModelViewSet):
    queryset = Focus.objects.all()
    serializer_class = FocusSerializer
    filter_fields = ['scope', 'start']

    def get_queryset(self):
        user = self.request.user
        return user.focuses.all()

    def filter_queryset(self, queryset):
        scope = self.request.query_params.get('scope')
        start = self.request.query_params.get('start')
        if scope and start and scope != DAY:
            # Update start to match correct scope start date.
            start = get_scope_by_name(scope)(start).start
            params = self.request.query_params
            params._mutable = True
            params['start'] = str(start)
            params._mutable = False
        return super().filter_queryset(queryset)

    def perform_create(self, serializer):
        self.perform_update(serializer)
        # Add experience.
        user = serializer.instance.owner
        add_experience(user, 'office', 1)

    def perform_update(self, serializer, reason=''):
        # Gathering data for notification
        reason = serializer.validated_data['reason']

        # Pre-safe
        old_outcomes = serializer.instance.outcomes if serializer.instance else []

        # Applying changes
        focus = serializer.save(owner=self.request.user)

        # Post-safe
        new_outcomes = serializer.instance.outcomes

        # Sending message to group
        notify_partners(focus, reason, old_outcomes, new_outcomes)


def notify_partners(focus, reason, old_outcomes, new_outcomes):
    # Notifying group partner(s) about focus creation/update.

    # Stop if there there was an update without outcome changes.
    if reason and old_outcomes == new_outcomes:
        return

    owner = focus.owner
    action = _('updated') if reason else _('set')
    subject = '{user} {action} {possessive_pronoun} {scope} focus: ({scope_display})'.format(
        user=owner,
        action=action,
        possessive_pronoun=owner.get_pronoun(kind='possessive adjective'),
        scope=focus.scope,
        scope_display=focus.get_scope(),
    )
    message = subject + '\n\n'
    for index, [old_outcome, new_outcome] in enumerate(zip_longest(old_outcomes, new_outcomes)):
        if old_outcome != new_outcome:
            title = 'Outcome {0}'.format(index + 1)
            if reason:
                message += '{title}: {old} => {new}\n'.format(title=title, old=old_outcome, new=new_outcome)
            else:
                message += '{title}: {new}\n'.format(title=title, new=new_outcome)
    if reason:
        message += '\nUpdate Reason:\n{reason}'.format(reason=reason)

    # Notifying group partners
    group = None
    if focus.scope == DAY:
        group = owner.duo
    elif focus.scope == WEEK:
        group = owner.clan
    elif focus.scope == MONTH:
        group = owner.tribe
    if group:
        group.notify_partners(owner, subject, message)
