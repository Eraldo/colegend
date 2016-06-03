from django import template
from django.template.loader import render_to_string
from django.utils import timezone

from colegend.core.templatetags.core_tags import intuitive_duration
from colegend.core.templatetags.icons import icon
from colegend.outcomes.models import Outcome

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
    context = {}
    if outcome:
        if isinstance(outcome, Outcome):
            context.update({
                'name': outcome.name,
                'description': outcome.description,
                'status': outcome.status,
                'inbox': outcome.inbox,
                'review': outcome.review,
                'date': outcome.date or '',
                'deadline': outcome.deadline or '',
                'estimate': outcome.estimate or '',
                'url': outcome.detail_url,
                'actions': [
                    {
                        'name': 'update',
                        'url': outcome.update_url,
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
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def inbox(context, inbox=None, **kwargs):
    inbox = inbox or context.get('inbox')
    if inbox:
        return icon('inbox')
    return ''


@register.simple_tag(takes_context=True)
def status(context, status=None, **kwargs):
    status = status or context.get('status')
    if status in [Outcome.OPEN, Outcome.WAITING, Outcome.CLOSED]:
        if status == Outcome.OPEN:
            return icon('open')
        elif status == Outcome.WAITING:
            return icon('waiting', classes='text-category-7')
        elif status == Outcome.CLOSED:
            return icon('closed', classes='text-category-4')
    return ''


@register.simple_tag(takes_context=True)
def review(context, review=None, **kwargs):
    review = review or context.get('review')
    symbol = ''
    review_context = {}
    if review == Outcome.DAILY:
        review_context['symbol'] = 'D'
        review_context['class'] = 'bg-category-1'
    elif review == Outcome.WEEKLY:
        review_context['symbol'] = 'W'
        review_context['class'] = 'bg-category-2'
    elif review == Outcome.MONTHLY:
        review_context['symbol'] = 'M'
        review_context['class'] = 'bg-category-3'
    elif review == Outcome.QUARTERLY:
        review_context['symbol'] = 'Q'
        review_context['class'] = 'bg-category-5'
    elif review == Outcome.YEARLY:
        review_context['symbol'] = 'Y'
        review_context['class'] = 'bg-category-6'
    elif review == Outcome.SOMETIME:
        review_context['symbol'] = 'S'
        review_context['class'] = 'bg-category-7'
    if review_context:
        review_tempalte = 'outcomes/widgets/review.html'
        symbol = render_to_string(review_tempalte, context=review_context)
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
