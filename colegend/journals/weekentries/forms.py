from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from colegend.tags.fields import TagsCreateFormField
from .models import WeekEntry


class WeekEntryForm(forms.ModelForm):
    class Meta:
        model = WeekEntry
        fields = [
            'journal',
            'year',
            'week',
            'focus',
            'content',
            'keywords',
            'tags',
        ]

    def __init__(self, *args, **kwargs):
        journal = kwargs.pop('journal', None)
        self.journal = journal
        owner = journal.owner
        super().__init__(*args, **kwargs)

        # Update the tags field to use the custom django-autocomplete's create field
        tags_queryset = self.fields.get('tags').queryset
        self.fields['tags'] = TagsCreateFormField(tags_queryset, required=False)

        # Check for spellchecker options
        spellchecker = journal.spellchecker

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('journal', type='hidden'),
            Field('year'),
            Field('week'),
            Field('focus', rows=3),
            Field('content', spellchecker=spellchecker, autofocus=True),
            Field('keywords'),
            Field('tags'),
        )
        self.helper.add_input(Submit('save', 'Save'))
        self.helper.include_media = False

    def clean_journal(self):
        journal = self.cleaned_data.get('journal')
        if not journal == self.journal:
            message = 'You need to be the owner.'
            self.add_error(None, message)
        return journal
