from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit
from django import forms
from .models import GuideRelation

__author__ = 'Eraldo Energy'


class GuideManageForm(forms.ModelForm):
    class Meta:
        model = GuideRelation
        fields = [
            'outer_call_checked',
            'inner_call_checked',
            'coLegend_checked',
            'guiding_checked',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Checklist for you and your Guidee',
                'outer_call_checked',
                'inner_call_checked',
                'coLegend_checked',
                'guiding_checked',
            )
        )
        self.helper.add_input(Submit('update', 'Update'))
