from django import template
from django.template.loader import render_to_string
from django.utils import timezone

from colegend.core.utils.markdown import render

register = template.Library()


@register.simple_tag(takes_context=True)
def journal_link(context, journal=None):
    if not journal:
        journal = context.get('journal')
    context = {
        'name': journal,
        'url': journal.get_absolute_url(),
    }
    template = 'journals/widgets/link.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def journalentry_card(context, journalentry=None, **kwargs):
    journalentry = journalentry or context.get('entry')
    if journalentry:
        context = {
            'id': journalentry.id,
            'date': journalentry.start,
            'weekday': journalentry.start.strftime('%a'),
            'weekday_number': journalentry.start.isoweekday(),
            'locations': '',
            'content': render(journalentry.content),
            'actions': True,
            # 'detail_url': journalentry.detail_url,
            'detail_url': '#detail',
            # 'update_url': journalentry.update_url,
            'update_url': '#update',
            # 'delete_url': journalentry.delete_url,
            'delete_url': '#delete',
            'keywords': journalentry.keywords,
            'tags': journalentry.tags.all(),
        }
    else:
        context = context.flatten()
        date = kwargs.get('date', context.get('date'))
        if date:
            # create_url = reverse('dayentries:create')
            create_url = '#create'
            context['create_url'] = '{}?date={}'.format(create_url, date)
            context['weekday'] = date.strftime('%a')
            context['weekday_number'] = date.isoweekday()
    context.update(kwargs)
    template = 'journals/widgets/entry_card.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def journalentry_line(context, journalentry=None, **kwargs):
    journalentry = journalentry or context.get('entry')
    today = timezone.now().date()
    if journalentry:
        context = {
            'id': journalentry.id,
            'date': journalentry.start,
            'weekday': journalentry.start.strftime('%a'),
            'weekday_number': journalentry.start.isoweekday(),
            'locations': journalentry.locations,
            'actions': True,
            # 'detail_url': journalentry.detail_url,
            'detail_url': '#detail',
            # 'update_url': journalentry.update_url,
            'update_url': '#update',
            # 'delete_url': journalentry.delete_url,
            'delete_url': '#delete',
            'keywords': journalentry.keywords,
            'content': journalentry.content,
            'tags': journalentry.tags.all(),
            'class': 'active' if journalentry.start == today else '',
        }
    else:
        context = context.flatten()
        date = kwargs.get('date', context.get('date'))
        if date:
            # create_url = reverse('dayentries:create')
            create_url = '#create'
            context['create_url'] = '{}?date={}'.format(create_url, date)
            context['weekday'] = date.strftime('%a')
            context['weekday_number'] = date.isoweekday()
            context['class'] = 'active' if date == today else ''
    context.update(kwargs)
    template = 'journals/widgets/entry_item.html'
    return render_to_string(template, context=context)
