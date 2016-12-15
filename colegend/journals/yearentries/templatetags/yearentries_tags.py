from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils import timezone

from colegend.core.utils.markdown import render
from colegend.journals.scopes import Year

register = template.Library()


@register.simple_tag(takes_context=True)
def yearentry_link(context, yearentry=None, **kwargs):
    yearentry = yearentry or context.get('yearentry')
    context = {
        'name': yearentry,
        'url': yearentry.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'yearentries/widgets/link.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def yearentry_card(context, yearentry=None, **kwargs):
    yearentry = yearentry or context.get('yearentry')
    if yearentry:
        context = {
            'id': yearentry.id,
            'date': yearentry.date,
            'dates': yearentry.dates,
            'year': yearentry,
            'content': render(yearentry.content),
            'actions': True,
            'detail_url': yearentry.detail_url,
            'update_url': yearentry.update_url,
            'delete_url': yearentry.delete_url,
            'keywords': yearentry.keywords,
            'tags': yearentry.tags.all(),
        }
    else:
        date = kwargs.get('date', context.get('date'))
        if date:
            year = Year(date)
            create_url = reverse('yearentries:create')
            context['create_url'] = '{}?year={}'.format(create_url, year.number)
            context['dates'] = '{0} - {1}'.format(year.start, year.end)
            context['year_number'] = year.number
            context['year'] = year
    context.update(kwargs)
    template = 'yearentries/widgets/card.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def yearentry_line(context, yearentry=None, **kwargs):
    yearentry = yearentry or context.get('yearentry')
    today = timezone.now().date()
    if yearentry:
        context = {
            'id': yearentry.id,
            'date': yearentry.date,
            'dates': yearentry.dates,
            'year': yearentry,
            'actions': True,
            'detail_url': yearentry.detail_url,
            'update_url': yearentry.update_url,
            'delete_url': yearentry.delete_url,
            'keywords': yearentry.keywords,
            'content': yearentry.content,
            'tags': yearentry.tags.all(),
            'class': 'active' if yearentry.year == today.year else '',
        }
    else:
        date = kwargs.get('date', context.get('date'))
        if date:
            year = Year(date)
            create_url = reverse('yearentries:create')
            context['create_url'] = '{}?year={}'.format(create_url, year.number)
            context['dates'] = '{0} - {1}'.format(year.start, year.end)
            context['year_number'] = year.number
            context['year'] = year
            context['class'] = 'active' if year.number == today.year else ''
    context.update(kwargs)
    template = 'yearentries/widgets/item.html'
    return render_to_string(template, context=context)
