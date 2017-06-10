from django.utils.html import format_html
from django.utils.timesince import timesince

from colegend.core.templatetags.core_tags import image as Image
from colegend.components.models import Component


class VisionComponent(Component):
    def get_context(self, context, vision=None, **kwargs):
        vision = vision or context.get('vision') or ''
        if vision:
            context['title'] = '{scope} vision'.format(scope=vision.get_scope_display())
            if vision.modified:
                last_update = timesince(vision.modified)
                # last_update = timesince(last_update)
                context['last_update'] = format_html('<span class="small">Updated: {} ago</span>', last_update)
            if vision.image:
                image = Image(vision.image.url, name=vision)
            else:
                image = ''
            context['image'] = image
        return context
