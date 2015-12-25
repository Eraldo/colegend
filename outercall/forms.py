from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from .models import OuterCall

__author__ = 'Eraldo Energy'


class OuterCallForm(forms.ModelForm):
    class Meta:
        model = OuterCall
        fields = [
            'owner',
            'trigger',
            'referrer',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('owner', type="hidden"),
            Field('trigger', rows=2),
            Field('referrer'),
        )
        self.helper.add_input(Submit('save', 'Save'))
