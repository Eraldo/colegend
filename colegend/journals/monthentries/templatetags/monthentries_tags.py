from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils import timezone

from colegend.core.utils.markdown import render

register = template.Library()


@register.simple_tag(takes_context=True)
def monthentry_link(context, monthentry=None, **kwargs):
    monthentry = monthentry or context.get('monthentry')
    context = {
        'name': monthentry,
        'url': monthentry.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'monthentries/widgets/link.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def monthentry_card(context, monthentry=None, **kwargs):
    monthentry = monthentry or context.get('monthentry')
    if monthentry:
        context = {
            'id': monthentry.id,
            'date': monthentry.date,
            'dates': monthentry.dates,
            'month': monthentry,
            'content': render(monthentry.content),
            'actions': True,
            'detail_url': monthentry.detail_url,
            'update_url': monthentry.update_url,
            'delete_url': monthentry.delete_url,
            'keywords': monthentry.keywords,
            'tags': monthentry.tags.all(),
        }
    else:
        date = kwargs.get('date', context.get('date'))
        if date:
            create_url = reverse('monthentries:create')
            month_number = date.month
            context['create_url'] = '{}?year={}&month={}'.format(create_url, date.year, month_number)
            context['dates'] = context.get('dates')
            context['month_number'] = month_number
            context['month'] = '{}-W{}'.format(date.year, month_number)
    context.update(kwargs)
    template = 'monthentries/widgets/card.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def monthentry_line(context, monthentry=None, **kwargs):
    monthentry = monthentry or context.get('monthentry')
    today = timezone.now().date()
    if monthentry:
        context = {
            'id': monthentry.id,
            'date': monthentry.date,
            'dates': monthentry.dates,
            'month': monthentry,
            'actions': True,
            'detail_url': monthentry.detail_url,
            'update_url': monthentry.update_url,
            'delete_url': monthentry.delete_url,
            'keywords': monthentry.keywords,
            'content': monthentry.content,
            'tags': monthentry.tags.all(),
            'class': 'active' if monthentry.date == today else '',
        }
    else:
        date = kwargs.get('date', context.get('date'))
        if date:
            create_url = reverse('monthentries:create')
            month_number = date.month
            context['create_url'] = '{}?year={}&month={}'.format(create_url, date.year, month_number)
            context['dates'] = context.get('dates')
            context['month_number'] = month_number
            context['month'] = '{}-M{} {}'.format(date.year, month_number, date.strftime("%b"))
            context['class'] = 'active' if date == today else ''
    context.update(kwargs)
    template = 'monthentries/widgets/item.html'
    return render_to_string(template, context=context)