from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms

from .models import Profile

__author__ = 'Eraldo Energy'


class BiographyForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'biography',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('biography'),
        )
        self.helper.add_input(Submit('save', 'Save', css_id='save-button', css_class='pull-right'))
        self.helper.form_show_labels = False
