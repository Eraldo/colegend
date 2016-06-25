from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag()
def post(post, classes=None):
    post_template = 'blog/widgets/post.html'
    post_context = {
        'image': post.image.get_rendition('max-1200x1200').url if post.image else '',
        'tags': post.tags.all(),
        'title': post,
        'url': post.url,
        'classes': classes or '',
        'color': post.color or post.DARK,
    }
    return render_to_string(post_template, context=post_context)
