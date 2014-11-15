from markdown import markdown
from mdx_linkify.mdx_linkify import LinkifyExtension

__author__ = 'eraldo'


def set_target_blank(attrs, new=False):
    attrs['target'] = '_blank'
    return attrs


def markup(text, *args, **kwargs):
    return markdown(text, *args, safe_mode=True,
                    extensions=['nl2br', 'sane_lists', 'extra',
                                LinkifyExtension(
                                    configs={"linkify_callbacks": [set_target_blank]}
                                )],
                    **kwargs)
