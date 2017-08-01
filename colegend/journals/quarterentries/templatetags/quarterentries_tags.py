# from django import template
# from django.core.urlresolvers import reverse
# from django.template.loader import render_to_string
# from django.utils import timezone
#
# from colegend.core.utils.markdown import render
# from colegend.journals.scopes import Quarter
#
# register = template.Library()
#
#
# @register.simple_tag(takes_context=True)
# def quarterentry_link(context, quarterentry=None, **kwargs):
#     quarterentry = quarterentry or context.get('quarterentry')
#     context = {
#         'name': quarterentry,
#         'url': quarterentry.get_absolute_url(),
#     }
#     context.update(kwargs)
#     template = 'quarterentries/widgets/link.html'
#     return render_to_string(template, context=context)
#
#
# @register.simple_tag(takes_context=True)
# def quarterentry_card(context, quarterentry=None, **kwargs):
#     quarterentry = quarterentry or context.get('quarterentry')
#     if quarterentry:
#         context = {
#             'id': quarterentry.id,
#             'date': quarterentry.date,
#             'dates': quarterentry.dates,
#             'quarter': quarterentry,
#             'content': render(quarterentry.content),
#             'actions': True,
#             'detail_url': quarterentry.detail_url,
#             'update_url': quarterentry.update_url,
#             'delete_url': quarterentry.delete_url,
#             'keywords': quarterentry.keywords,
#             'tags': quarterentry.tags.all(),
#         }
#     else:
#         context = context.flatten()
#         date = kwargs.get('date', context.get('date'))
#         if date:
#             quarter = Quarter(date)
#             create_url = reverse('quarterentries:create')
#             context['create_url'] = '{}?year={}&quarter={}'.format(create_url, quarter.date.year, quarter.number)
#             context['dates'] = '{0} - {1}'.format(quarter.start, quarter.end)
#             context['quarter_number'] = quarter.number
#             context['quarter'] = quarter
#     context.update(kwargs)
#     template = 'quarterentries/widgets/card.html'
#     return render_to_string(template, context=context)
#
#
# @register.simple_tag(takes_context=True)
# def quarterentry_line(context, quarterentry=None, **kwargs):
#     quarterentry = quarterentry or context.get('quarterentry')
#     today = timezone.now().date()
#     if quarterentry:
#         context = {
#             'id': quarterentry.id,
#             'date': quarterentry.date,
#             'dates': quarterentry.dates,
#             'quarter': quarterentry,
#             'actions': True,
#             'detail_url': quarterentry.detail_url,
#             'update_url': quarterentry.update_url,
#             'delete_url': quarterentry.delete_url,
#             'keywords': quarterentry.keywords,
#             'content': quarterentry.content,
#             'tags': quarterentry.tags.all(),
#             'class': 'active' if quarterentry.number == Quarter(today).number else '',
#         }
#     else:
#         context = context.flatten()
#         date = kwargs.get('date', context.get('date'))
#         if date:
#             quarter = Quarter(date)
#             create_url = reverse('quarterentries:create')
#             context['create_url'] = '{}?year={}&quarter={}'.format(create_url, date.year, quarter.number)
#             context['dates'] = '{0} - {1}'.format(quarter.start, quarter.end)
#             context['quarter_number'] = quarter.number
#             context['quarter'] = quarter
#             context['class'] = 'active' if quarter.number == Quarter(today).number else ''
#     context.update(kwargs)
#     template = 'quarterentries/widgets/item.html'
#     return render_to_string(template, context=context)
