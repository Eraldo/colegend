from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from .models import Legend

__author__ = 'Eraldo Energy'


class LegendForm(forms.ModelForm):
    class Meta:
        model = Legend
        fields = [
            'name',
            'gender',
            'occupation',
            'birthday',
            'address',
            'phone',
            'avatar',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),
            Field('gender'),
            Field('occupation'),
            Field('birthday'),
            Field('address', rows=3),
            Field('phone'),
            Field('avatar'),
        )
        self.helper.add_input(Submit('save', 'Save'))
