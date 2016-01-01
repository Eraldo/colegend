from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms

from core.form_layout_fields import IconField
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
            'biography',
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
            Field('biography'),
        )
        self.helper.add_input(Submit('save', 'Save'))


class MeForm(forms.ModelForm):
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
            IconField('name', 'name'),
            IconField('gender', 'gender'),
            IconField('occupation', 'occupation'),
            IconField('birthday', 'birthday'),
            IconField('address', 'address', rows=3),
            IconField('phone', 'phone'),
            IconField('avatar', 'avatar'),
        )
        self.helper.add_input(Submit('save', 'Save'))


class BiographyForm(forms.ModelForm):
    class Meta:
        model = Legend
        fields = [
            'biography',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('biography'),
        )
        self.helper.add_input(Submit('save', 'Save', css_class='pull-right'))
        self.helper.form_show_labels = False
