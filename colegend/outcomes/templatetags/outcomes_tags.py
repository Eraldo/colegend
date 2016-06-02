from django import template
from django.template.loader import render_to_string

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
                'status': outcome.get_status_display(),
                'inbox': 'inbox' if outcome.inbox else '',
                'review': outcome.get_review_display() or '',
                'date': outcome.date or '',
                'deadline': outcome.deadline or '',
                'estimate': outcome.estimate or '',
                'url': outcome.detail_url,
            })
        elif isinstance(outcome, dict):
            context.update(outcome)
    context.update(kwargs)
    template = 'outcomes/widgets/card.html'
    return render_to_string(template, context=context)

# @register.simple_tag(takes_context=True)
# def label(context, label=None, **kwargs):
#     label = label or context.get('label', {})
#     label_context = label
#     label_context.update(kwargs)
#     label_template = 'atoms/label.html'
#     return render_to_string(label_template, context=label_context)
