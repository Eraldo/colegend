from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag()
def article(article, classes=None):
    article_template = 'blog/widgets/article.html'
    article_context = {
        'image': article.image.get_rendition('max-1200x1200').url if article.image else '',
        'tags': article.tags.all(),
        'title': article,
        'url': article.url,
        'classes': classes or '',
        'color': article.color or article.DARK,
    }
    return render_to_string(article_template, context=article_context)
