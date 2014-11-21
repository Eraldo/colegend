from markdown import Extension
from markdown.postprocessors import Postprocessor

__author__ = 'eraldo'

"""
Replacement extension for Markdown
==================================

This extension replaces parts of the output.

Example:

    '<table>' => '<table class="table">'
"""

REPLACEMENTS = {
    '<table>': '<table class="table table-hover">',
}


class ReplacePostprocessor(Postprocessor):
    def run(self, text):
        for key, value in REPLACEMENTS.items():
            text = text.replace(key, value)
        return text


class ReplacementExtension(Extension):
    """Adds string replacement to Markdown class."""

    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns."""
        # task_tag = SubstituteTagPattern(TASK_RE, 'span')
        # md.inlinePatterns.add('tasks', task_tag, '_begin')
        md.postprocessors.add('replacement', ReplacePostprocessor(md), '_end')


def makeExtension(configs={}):
    return ReplacementExtension(configs=dict(configs))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
