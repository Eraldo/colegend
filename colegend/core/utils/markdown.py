from django.utils.safestring import mark_safe
import markdown
import bleach


def render(text):
    html = markdown.markdown(
        text,
        extensions=['extra',
                    # 'codehilite',
                    # markdown.mdx.tables.TableExtension(),
                    # markdown.mdx.linker.LinkerExtension({
                    #     '__default__':  'wagtailmarkdown.mdx.linkers.page',
                    #     'page:':        'wagtailmarkdown.mdx.linkers.page',
                    #     'image:':       'wagtailmarkdown.mdx.linkers.image',
                    #     'doc:':         'wagtailmarkdown.mdx.linkers.document',
                    # })
                    ],
        extension_configs={
            # 'codehilite': [
            #     ('guess_lang', False),
            # ]
        },
        output_format='html5')
    return mark_safe(bleach.clean(
        html,
        tags=[
            'p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'tt', 'pre',
            'em', 'strong', 'ul', 'li', 'dl', 'dd', 'dt', 'code', 'img', 'a',
            'table', 'tr', 'th', 'td', 'tbody', 'caption', 'colgroup', 'thead',
            'tfoot', 'blockquote', 'ol', '<hr>', ],
        attributes={
            '*': ['class', 'style', 'id', ],
            'a': ['href', 'target', 'rel', ],
            'img': ['src', 'alt', ],
            'tr': ['rowspan', 'colspan', ],
            'td': ['rowspan', 'colspan', 'align', ],
        },
        styles=[
            'color', 'background-color', 'font-family', 'font-weight', 'font-size',
            'width', 'height', 'text-align',
            'border', 'border-top', 'border-bottom', 'border-left', 'border-right',
            'padding', 'padding-top', 'padding-bottom', 'padding-left', 'padding-right',
            'margin', 'margin-top', 'margin-bottom', 'margin-left', 'margin-right',
        ]
    ))
