from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms

from core.form_layout_fields import IconField
from .models import Legend

__author__ = 'Eraldo Energy'


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Legend
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
        model = Legend
        fields = [
            'name',
            'gender',
            'occupation',
            'birthday',
            'address',
            'phone',
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
            IconField('occupation', 'occupation'),
            IconField('birthday', 'birthday', placeholder="YYYY-MM-DD"),
            IconField('address', 'address', rows=3),
            IconField('phone', 'phone'),
        )
        self.helper.add_input(Submit('save', 'Save', css_id='save-button'))


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
        self.helper.add_input(Submit('save', 'Save', css_id='save-button', css_class='pull-right'))
        self.helper.form_show_labels = False
