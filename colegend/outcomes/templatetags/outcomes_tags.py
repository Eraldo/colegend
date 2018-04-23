from django import template
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

from colegend.core.templatetags.core_tags import icon, intuitive_duration
from colegend.outcomes.forms import OutcomeStatusForm
from colegend.outcomes.models import Outcome
from colegend.scopes.models import Scope

register = template.Library()


@register.simple_tag(takes_context=True)
def outcome_link(context, outcome=None, **kwargs):
    outcome = outcome or context.get('outcome')
    context = {
        'name': outcome,
        'url': outcome.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'outcomes/widgets/link.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def outcome(context, outcome=None, **kwargs):
    outcome = outcome or context.get('outcome', {})
    request = context.get('request')
    context = {}
    if outcome:
        if isinstance(outcome, Outcome):
            context.update({
                'id': outcome.id,
                'name': outcome.name,
                'description': outcome.description,
                'status': outcome.status,
                'inbox': outcome.inbox,
                'scope': outcome.scope,
                'date': outcome.date or '',
                'deadline': outcome.deadline or '',
                'estimate': outcome.estimate or '',
                'url': outcome.detail_url,
                'status_form': OutcomeStatusForm(instance=outcome, request=request),
                'actions': [
                    {
                        'name': 'update',
                        'url': outcome.update_url,
                    },
                    {
                        'name': 'toggle inbox',
                        'post_url': '{action_url}?next={next_url}'.format(
                            action_url=reverse('outcomes:toggle_inbox', args=[outcome.id]),
                            next_url=request.path
                        ),
                        'icon': 'inbox',
                    },
                    {
                        'name': 'delete',
                        'url': outcome.delete_url,
                    },
                ],
            })
        elif isinstance(outcome, dict):
            context.update(outcome)
    context.update(kwargs)
    template = 'outcomes/widgets/card.html'
    return render_to_string(template, context=context, request=request)


@register.simple_tag(takes_context=True)
def inbox(context, inbox=None, **kwargs):
    inbox = inbox or context.get('inbox')
    if inbox:
        return icon('inbox')
    return ''


@register.simple_tag(takes_context=True)
def status(context, status=None, **kwargs):
    status = status or context.get('status')
    if status in Outcome.STATUSES:
        if status == Outcome.CURRENT:
            return icon('open')
        elif status == Outcome.WAITING:
            return icon('waiting', classes='text-category-7')
        elif status == Outcome.DONE:
            return icon('closed', classes='text-category-4')
        elif status == Outcome.CANCELED:
            return icon('canceled', classes='text-category-4')
    return ''


@register.simple_tag(takes_context=True)
def scope(context, scope=None, **kwargs):
    scope = scope or context.get('scope')
    symbol = ''
    scope_context = {}
    if scope == Scope.DAY.value:
        scope_context['symbol'] = 'D'
        scope_context['class'] = 'bg-category-1'
    elif scope == Scope.WEEK.value:
        scope_context['symbol'] = 'W'
        scope_context['class'] = 'bg-category-2'
    elif scope == Scope.MONTH.value:
        scope_context['symbol'] = 'M'
        scope_context['class'] = 'bg-category-3'
    elif scope == Scope.YEAR.value:
        scope_context['symbol'] = 'Y'
        scope_context['class'] = 'bg-category-6'
    if scope_context:
        scope_tempalte = 'outcomes/widgets/scope.html'
        symbol = render_to_string(scope_tempalte, context=scope_context)
    return symbol


@register.simple_tag(takes_context=True)
def estimate(context, estimate=None, **kwargs):
    estimate = estimate or context.get('estimate')
    if estimate:
        return render_to_string(
            'outcomes/widgets/estimate.html',
            context={'amount': intuitive_duration(estimate)})
    return ''


def get_shortened_current_date(date):
    current_year = timezone.now().year
    if date.year == current_year:
        return date.strftime('%b %-d')
    return date.strftime('%b %-d, %Y')


@register.simple_tag(takes_context=True)
def date(context, date=None, **kwargs):
    date = date or context.get('date')
    if date:
        return render_to_string(
            'outcomes/widgets/date.html',
            context={'date': get_shortened_current_date(date)})
    return ''


@register.simple_tag(takes_context=True)
def deadline(context, deadline=None, **kwargs):
    deadline = deadline or context.get('deadline')
    if deadline:
        return render_to_string(
            'outcomes/widgets/deadline.html',
            context={'deadline': get_shortened_current_date(deadline)})
    return ''
