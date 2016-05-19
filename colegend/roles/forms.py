from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from .models import Role


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = [
            'name',
            'nickname',
            'item',
            'icon',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),
            Field('nickname'),
            Field('item'),
            Field('icon'),
            Field('description'),
        )
        self.helper.add_input(Submit('save', 'Save'))
