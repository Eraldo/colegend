from statuses.models import STATUSES

__author__ = 'eraldo'

"""
Tasks extension for Markdown
============================

This extension adds syntax highlighting for text lines that represent a task status.
Just type 'TODO: ' and it will add a span tag with a css class
The css class can be used to style and color the task status portion.

Example:

    'TODO: clean garage' => '<span class="label status status-todo>TODO</span> clean garage'
"""

from markdown.inlinepatterns import SimpleTextPattern
from markdown.extensions import Extension
from markdown.util import etree

# Global Vars
STATUSES
TASK_RE = r'(({})): '.format('|'.join(STATUSES))


class TaskPattern(SimpleTextPattern):
    def handleMatch(self, m):
        status = m.group(3)
        # color = STATUSES[status]
        text = m.group(3)
        el = etree.Element('span')
        el.text = text
        el.set("class", "label status status-{}".format(status.lower()))
        el.tail = ' '
        return el


class TaskExtension(Extension):
    """Adds TASK_RE extension to Markdown class."""

    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns."""
        # task_tag = SubstituteTagPattern(TASK_RE, 'span')
        # md.inlinePatterns.add('tasks', task_tag, '_begin')
        md.inlinePatterns.add('tasks', TaskPattern(TASK_RE), '_begin')


def makeExtension(configs={}):
    return TaskExtension(configs=dict(configs))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
