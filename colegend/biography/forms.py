from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from .models import Biography

__author__ = 'Eraldo Energy'


class BiographyForm(forms.ModelForm):
    class Meta:
        model = Biography
        fields = [
            'owner',
            'text',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('owner', type="hidden"),
            Field('text'),
        )
        self.helper.add_input(Submit('save', 'Save', css_id='save-button', css_class='pull-right'))
        self.helper.form_show_labels = False
