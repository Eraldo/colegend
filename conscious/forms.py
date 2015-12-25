from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from .models import OuterCall, InnerCall

__author__ = 'Eraldo Energy'


class OuterCallForm(forms.ModelForm):
    class Meta:
        model = OuterCall
        fields = [
            'trigger',
            'referrer',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('trigger', rows=2),
            Field('referrer'),
        )
        self.helper.add_input(Submit('save', 'Save'))


class InnerCallForm(forms.ModelForm):
    class Meta:
        model = InnerCall
        fields = [
            'motivation',
            'change',
            'drive',
            'wishes',
            'other',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('motivation', rows=2),
            Field('change', rows=2),
            Field('drive'),
            Field('wishes', rows=2),
            Field('other', rows=2),
        )
        self.helper.add_input(Submit('save', 'Save'))
