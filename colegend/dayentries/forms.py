from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from .models import DayEntry


class DayEntryForm(forms.ModelForm):
    class Meta:
        model = DayEntry
        fields = [
            'journal',
            'date',
            'locations',
            'content',
            'keywords',
            'tags',
        ]

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('journal', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('journal', type='hidden'),
            Field('date'),
            Field('locations'),
            Field('content'),
            Field('keywords'),
            Field('tags'),
        )
        self.helper.add_input(Submit('save', 'Save'))
