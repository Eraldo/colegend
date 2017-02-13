from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from colegend.outcomes.fields import OutcomeCreateFormField
from colegend.tags.fields import TagsCreateFormField
from .models import QuarterEntry


class QuarterEntryForm(forms.ModelForm):
    class Meta:
        model = QuarterEntry
        fields = [
            'journal',
            'year',
            'quarter',
            'outcome_1',
            'outcome_2',
            'outcome_3',
            'outcome_4',
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

        # Update the outcomes field to use the custom django-autocomplete's create field
        outcome_queryset = self.fields.get('outcome_1').queryset
        self.fields['outcome_1'] = OutcomeCreateFormField(outcome_queryset, required=False)
        self.fields['outcome_2'] = OutcomeCreateFormField(outcome_queryset, required=False)
        self.fields['outcome_3'] = OutcomeCreateFormField(outcome_queryset, required=False)
        self.fields['outcome_4'] = OutcomeCreateFormField(outcome_queryset, required=False)

        # Check for spellchecker options
        spellchecker = journal.spellchecker

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('journal', type='hidden'),
            Field('year'),
            Field('quarter'),
            Field('outcome_1'),
            Field('outcome_2'),
            Field('outcome_3'),
            Field('outcome_4'),
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

    def clean(self):
        outcome_1 = self.cleaned_data.get('outcome_1')
        outcome_2 = self.cleaned_data.get('outcome_2')
        outcome_3 = self.cleaned_data.get('outcome_3')
        outcome_4 = self.cleaned_data.get('outcome_4')
        outcomes = [outcome_1, outcome_2, outcome_3, outcome_4]
        outcomes = [outcome for outcome in outcomes if outcome]
        if len(outcomes) != len(set(outcomes)):
            message = 'Please chose an ontcome only once.'
            self.add_error(None, message)
        return super().clean()
