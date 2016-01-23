from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from .models import InnerCall

__author__ = 'Eraldo Energy'


class InnerCallForm(forms.ModelForm):
    class Meta:
        model = InnerCall
        fields = [
            'owner',
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
            Field('owner', type="hidden"),
            Field('motivation', rows=2),
            Field('change', rows=2),
            Field('drive'),
            Field('wishes', rows=2),
            Field('other', rows=2),
        )
        self.helper.add_input(Submit('save', 'Save', css_id='save-button'))
