from urllib.parse import urlparse, parse_qs
from markdown import markdown
from mdx_linkify.mdx_linkify import LinkifyExtension

__author__ = 'eraldo'


def set_target_blank(attrs, new=False):
    attrs['target'] = '_blank'
    return attrs


def embed_youtube(attrs, new=False):
    url = attrs['href']
    p = urlparse(url)
    if p.netloc in ['www.youtube.com']:
        youtube_id = parse_qs(p.query).get('v', [''])[0]
        embed = parse_qs(p.query).get('embed', [''])[0]
        html = """
            <iframe class="embed-responsive-item" src="//www.youtube.com/embed/{}"
                frameborder="0" allowfullscreen>
            </iframe>
            """.format(youtube_id)
        if embed:  # make it responsive
            html = """
                <div class="embed-responsive embed-responsive-16by9">
                    {}
                </div>
                """.format(html)
        attrs['_text'] = html
    return attrs


def markup(text, *args, **kwargs):
    return markdown(text, *args, safe_mode=True,
                    extensions=['nl2br', 'sane_lists', 'extra',
                                LinkifyExtension(
                                    configs={"linkify_callbacks": [set_target_blank, embed_youtube]}
                                )],
                    **kwargs)
