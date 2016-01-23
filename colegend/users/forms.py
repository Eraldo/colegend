from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms

from colegend.core.form_layout_fields import IconField

from .models import User

__author__ = 'Eraldo Energy'


class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'avatar',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            IconField('avatar', 'avatar'),
        )
        self.helper.add_input(Submit('save', 'Save', css_id='save-button'))


class LegendForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'gender',
            'birthday',
            'address',
            'phone',
            'occupation',
        ]

    def __init__(self, fields=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if fields:
            for field in self.Meta.fields:
                if field not in fields:
                    del self.fields[field]
        self.helper = FormHelper()
        self.helper.layout = Layout(
            IconField('name', 'name'),
            IconField('gender', 'gender'),
            IconField('birthday', 'birthday', placeholder="YYYY-MM-DD"),
            IconField('address', 'address', rows=3),
            IconField('phone', 'phone'),
            IconField('occupation', 'occupation'),
        )
        self.helper.add_input(Submit('save', 'Save', css_id='save-button'))
