from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag()
def resource(resource, classes=None):
    resource_template = 'resources/widgets/resource.html'
    resource_context = {
        'tags': resource.tags.all(),
        'title': resource,
        'url': resource.url,
        'lead': resource.lead,
        'area_1': resource.area_1,
        'area_2': resource.area_2,
        'area_3': resource.area_3,
        'area_4': resource.area_4,
        'area_5': resource.area_5,
        'area_6': resource.area_6,
        'area_7': resource.area_7,
        'classes': classes or '',
    }
    return render_to_string(resource_template, context=resource_context)
